#!/usr/bin/env python3
"""Lead Ledger scoring — deterministic, stdlib-only, zero tokens.

Usage:
    python3 scripts/score_leads.py [path/to/leads/]   (default: ./leads/)

Reads leads/ledger.csv, dedupes by email, scores every row, assigns a segment,
rewrites the ledger in place (backup kept), flags name-only duplicate candidates
to leads/needs-review.md, and prints a summary with the current top prospects.

Weights can be overridden via leads/weights.json (same keys as DEFAULTS below,
include only what changes). See references/scoring-method.md for the rationale.
"""

import csv
import json
import shutil
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

DEFAULTS = {
    "source_points": {
        "event_attended": 25,
        "past_customer": 25,
        "community": 20,
        "manual_add": 15,
        "event_registered": 10,
        "email_list": 5,
    },
    "signal_points": {
        "purchased": 30,
        "asked_question": 20,
        "replied": 15,
        "personal_share": 15,
        "posted": 12,
        "requested_info": 12,
        "referred": 12,
        "attended": 10,
        "joined": 5,
        "registered": 5,
    },
    "multi_source": {"2": 1.15, "3+": 1.3},
    "recency": {"30": 1.0, "90": 0.85, "180": 0.65, "older": 0.4},
    "batch_floor": 30,       # minimum score to enter a batch
    "cooldown_days": 14,     # minimum days between personal touches
}

EXCLUDED_STATUSES = {"not_interested", "unsubscribed"}
WARM_SIGNALS = {"replied", "asked_question", "personal_share", "purchased"}


def load_weights(leads_dir: Path) -> dict:
    weights = json.loads(json.dumps(DEFAULTS))  # deep copy
    override_path = leads_dir / "weights.json"
    if override_path.exists():
        overrides = json.loads(override_path.read_text())
        for key, value in overrides.items():
            if isinstance(value, dict) and isinstance(weights.get(key), dict):
                weights[key].update(value)
            else:
                weights[key] = value
    return weights


def parse_date(value: str):
    value = (value or "").strip()
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def parse_signals(raw: str):
    """signals field: 'YYYY-MM-DD|type|note' items separated by ';'."""
    signals = []
    for item in (raw or "").split(";"):
        item = item.strip()
        if not item:
            continue
        parts = item.split("|", 2)
        signals.append({
            "date": parse_date(parts[0]) if parts else None,
            "type": parts[1].strip() if len(parts) > 1 else "",
            "note": parts[2].strip() if len(parts) > 2 else "",
        })
    return signals


def source_token_points(token: str, pts: dict) -> int:
    token = token.strip().lower()
    if not token:
        return 0
    if token.startswith("event_"):
        # event_2026-06-13 → attended unless explicitly marked registered-only
        return pts["event_registered"] if token.endswith("_registered") else pts["event_attended"]
    return pts.get(token, 0)


def recency_factor(row, signals, weights) -> float:
    dates = [d for d in [parse_date(row.get("last_activity", ""))] if d]
    dates += [s["date"] for s in signals if s["date"]]
    if not dates:
        return weights["recency"]["older"]
    days = (date.today() - max(dates)).days
    if days <= 30:
        return weights["recency"]["30"]
    if days <= 90:
        return weights["recency"]["90"]
    if days <= 180:
        return weights["recency"]["180"]
    return weights["recency"]["older"]


def score_row(row, weights):
    signals = parse_signals(row.get("signals", ""))
    sources = [s for s in (row.get("sources", "") or "").split(";") if s.strip()]

    points = sum(source_token_points(t, weights["source_points"]) for t in sources)
    points += sum(weights["signal_points"].get(s["type"], 0) for s in signals)

    if len(sources) >= 3:
        points *= weights["multi_source"]["3+"]
    elif len(sources) == 2:
        points *= weights["multi_source"]["2"]

    points *= recency_factor(row, signals, weights)
    return round(points, 1), signals, sources


def assign_segment(row, signals, sources) -> str:
    status = (row.get("status", "") or "").strip().lower()
    if status in EXCLUDED_STATUSES:
        return "excluded"
    if status == "customer":
        return "customer"
    attended = any(
        t.strip().lower().startswith("event_") and not t.strip().lower().endswith("_registered")
        for t in sources
    )
    warm = (
        attended
        or "community" in [t.strip().lower() for t in sources]
        or "past_customer" in [t.strip().lower() for t in sources]
        or any(s["type"] in WARM_SIGNALS for s in signals)
    )
    if warm:
        return "warm"
    if signals:
        return "engaged"
    return "cold"


def batch_eligible(row, weights) -> bool:
    if row["segment"] in ("excluded", "cold"):
        return False
    if not parse_signals(row.get("signals", "")):
        return False
    if float(row["score"]) < weights["batch_floor"]:
        return False
    touched = parse_date(row.get("last_touch", ""))
    if touched and (date.today() - touched).days < weights["cooldown_days"]:
        return False
    return True


def dedupe(rows):
    """Merge exact-email duplicates; return merged rows + name-only flag pairs."""
    by_email, no_email, flagged = {}, [], []

    def merge_field(a, b, sep=";"):
        items = [x.strip() for x in (a or "").split(sep) if x.strip()]
        for x in (b or "").split(sep):
            x = x.strip()
            if x and x not in items:
                items.append(x)
        return sep.join(items)

    for row in rows:
        email = (row.get("email", "") or "").strip().lower()
        if not email:
            no_email.append(row)
            continue
        if email in by_email:
            kept = by_email[email]
            for field in ("sources", "handles", "signals", "interests"):
                kept[field] = merge_field(kept.get(field, ""), row.get(field, ""))
            for field, pick in (("first_seen", min), ("last_activity", max), ("last_touch", max)):
                dates = [d for d in (kept.get(field, ""), row.get(field, "")) if d]
                kept[field] = pick(dates) if dates else ""
            kept["notes"] = merge_field(kept.get("notes", ""), row.get("notes", ""), sep=" / ")
        else:
            by_email[email] = row

    merged = list(by_email.values()) + no_email

    names = defaultdict(list)
    for row in merged:
        key = (row.get("name", "") or "").strip().lower()
        if key:
            names[key].append(row)
    for name_key, group in names.items():
        emails = {(r.get("email", "") or "").strip().lower() for r in group}
        if len(group) > 1 and len(emails - {""}) != 1:
            flagged.append(group)  # same name, different/missing emails → human call

    return merged, flagged


def main():
    leads_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("leads")
    ledger_path = leads_dir / "ledger.csv"
    if not ledger_path.exists():
        sys.exit(f"No ledger at {ledger_path} — run onboarding / ingest first.")

    weights = load_weights(leads_dir)
    with ledger_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = [dict(r) for r in reader]

    rows, flagged = dedupe(rows)

    for row in rows:
        score, signals, sources = score_row(row, weights)
        row["score"] = str(score)
        row["segment"] = assign_segment(row, signals, sources)

    rows.sort(key=lambda r: float(r["score"]), reverse=True)

    shutil.copy(ledger_path, ledger_path.with_suffix(".csv.bak"))
    for col in ("score", "segment"):
        if col not in fieldnames:
            fieldnames.append(col)
    with ledger_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    if flagged:
        lines = ["# Needs review — possible duplicates (NOT auto-merged)", ""]
        for group in flagged:
            lines.append(f"## {group[0].get('name', '?')}")
            for r in group:
                lines.append(
                    f"- id `{r.get('id','?')}` · email `{r.get('email','') or '(none)'}` ·"
                    f" sources: {r.get('sources','')} · confirm same person before merging"
                )
            lines.append("")
        (leads_dir / "needs-review.md").write_text("\n".join(lines), encoding="utf-8")

    counts = defaultdict(int)
    for row in rows:
        counts[row["segment"]] += 1
    eligible = [r for r in rows if batch_eligible(r, weights)]

    print(f"Ledger: {len(rows)} people | " + " · ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    print(f"Batch-eligible now: {len(eligible)}"
          + (f" | ⚠ {len(flagged)} possible duplicate(s) → needs-review.md" if flagged else ""))
    print("\nTop prospects:")
    for row in eligible[:15]:
        touched = row.get("last_touch", "") or "never touched"
        print(f"  {row['score']:>6}  {row.get('name','?'):<28} {row['segment']:<8} "
              f"→ {row.get('offer_fit','') or '-':<7} last touch: {touched}")


if __name__ == "__main__":
    main()
