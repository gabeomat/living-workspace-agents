# Debrief, Deal Files, and the Pipeline — the memory spec

This file defines the `sales/` workspace, what gets extracted from a transcript, and the cost discipline that keeps the whole system cheap.

## The workspace

Created at onboarding, at the user's workspace root (or where they prefer):

```
sales/
├── inbox/                      ← drop transcripts here (any format: .vtt, .txt, .md, pasted)
├── processed.log               ← append-only; a transcript listed here is NEVER read again
├── pipeline.md                 ← the living "who's waiting on what" board
├── deals/
│   └── <person-or-company>.md  ← one deal file per prospect: the distilled memory
├── scorecards/
│   └── YYYY-MM-DD-<person>.md  ← debrief + rubric scores per call
├── followups/
│   └── YYYY-MM-DD-<person>.md  ← drafted follow-ups (approval copies)
├── proposals/
│   └── YYYY-MM-DD-<person>.md  ← drafted proposals
└── playbook/
    ├── objections.md           ← every objection heard, verbatim, categorized, + what worked
    └── buyer-language.md       ← striking prospect phrases: pains, goals, praise — raw copy ore
```

## The read-once discipline (non-negotiable)

A transcript enters `sales/inbox/`, gets extracted **once** (cheap tier), and is logged in `processed.log`. From then on, every mode — briefs, proposals, pipeline checks, coaching trends — reads the **distilled files** (deal file, scorecards, playbook), never the raw transcript. A 90-minute transcript might be 25k tokens; its deal-file distillation is a few hundred. That ratio, honored on every call, is why this agent stays cheap at any volume. Keep the raw file (audit trail; the user may want to check a quote) — just never re-read it.

## What extraction captures (Mode 1, cheap tier)

From each transcript, capture — verbatim where marked, with rough timestamps:

1. **Header facts:** date, participants + roles, call type (discovery / follow-up / close / other), duration.
2. **Their goals & pains** — *verbatim.* What they want, what it's costing them, why now. These exact words later power the proposal and the follow-up.
3. **Numbers mentioned** — budgets, team size, revenue, timelines. Verbatim, with who said them.
4. **Objections & hesitations** — verbatim, plus how the seller responded (summarized) and whether it resolved.
5. **Questions the prospect asked** — buying signals live here.
6. **Commitments — both directions:** what the seller promised (and by when), what the prospect promised (and by when). Dates explicit or marked "no date set."
7. **How it ended** — the agreed next step, or the fog, quoted.
8. **Rubric raw material:** approximate talk split; the price-delivery moment (quote the seller's exact wording); the ask (quoted, or "no ask made"); any confidence-leak phrasings (quoted).
9. **Striking phrases** — anything the prospect said that names a pain or a desire memorably. → `playbook/buyer-language.md`.

Rules: **invent nothing; guess nothing.** Unclear audio/garbled text is marked `[unclear]`, not reconstructed. Speaker attribution follows the transcript's labels; if labels are missing, say so and attribute only what context makes certain.

## The deal file (`deals/<person>.md`)

One file per prospect — the distilled memory every other mode reads. Sections:

- **Who** — name, company/context, how they found the user, offer they're routed to.
- **Status** — one line: `active — proposal sent 2026-07-10, their move` / `won` / `lost (reason)` / `gone quiet since <date>`.
- **Story so far** — 3–6 bullets, newest first, one per touchpoint (calls, notable emails), each dated.
- **Their words** — the standing verbatim bank: goals, pains, numbers, memorable phrases (dated). Append per call; never rewrite history.
- **Open loops** — what we owe them / what they owe us, with dates.
- **Objection map** — objections raised so far and current state (resolved / open / recurring).

Update per call by **appending**, not rewriting — a deal file is a ledger, not an essay. If it grows past ~2 pages, compress the oldest "story" bullets, never "Their words."

## The pipeline (`pipeline.md`)

One table, updated mechanically (inline, no subagent) after every debrief and whenever the user reports an outcome:

```markdown
| Deal | Stage | Whose move | What's owed | Due / promised | Last touch | Notes |
|------|-------|-----------|-------------|----------------|------------|-------|
```

- **Stage:** `new → in conversation → proposal out → deciding → won / lost / gone quiet`.
- **Whose move** is the column that matters — the whole point is that nothing waits invisibly. The user's own overdue promises get flagged as loudly as the prospect's silence.
- `gone quiet` = no response past the profile's [[Follow-Up Window]]; a pipeline check suggests the nudge.
- Won/lost rows move to a `## Closed` section at the bottom with a one-line reason — that's the raw material for win/loss trends (Mode 5) later.

## The playbook files

- **`objections.md`** — grouped by theme (price, timing, trust, fit, authority…). Each entry: the objection verbatim + date + deal, what the seller answered, whether it landed. Over time, the best-performing answer rises to the top of each theme — the user's own sales playbook, written by their real calls.
- **`buyer-language.md`** — dated verbatim phrases, tagged pain/goal/praise. This is copy ore for the user's marketing (ads, landing pages, emails) — with the standing rule: **strip names and identifying details before anything public.** If sibling content agents are installed (blog, landing page, social), point them here.
