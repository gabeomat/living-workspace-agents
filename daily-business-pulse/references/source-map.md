# Source Map — where numbers come from, and what happens when they don't

Every profiled metric resolves through exactly one of four source types, each with a defined
fallback. The discipline in this file is what makes the pulse trustworthy: **a number without a
source tag doesn't ship, and a missing number is a finding, not a blank.**

---

## The four source types

### 1. `connector` — an MCP tool reads it live
Payments (Stripe, PayPal, Square), email platforms (MailerLite, Kit, Mailchimp), communities,
CRMs, calendars — whatever the user has connected.
- The profile records the **exact tool and read pattern** discovered during the onboarding probe
  (e.g. "list_resources with resource_type: group, read metadata.subscriber_count") — never a vague
  "check the email platform." Wrappers rename things; the probe found the real shape once so the
  daily run doesn't rediscover it.
- **Freshness tag:** `live`.
- **On failure** (auth expired, tool gone, shape changed): report it plainly in the pulse
  ("Stripe read failed — MRR unavailable today; yesterday's logged value was $X"), fall back to the
  last logged value **labeled as carried-forward**, and flag the fix (usually re-auth) in the pulse
  footer. Never guess. If it fails 3 runs straight, suggest downgrading the source in the profile.

### 2. `file-drop` — the user drops exports into `pulse/data/`
For anything they can download but not connect: community member CSVs, platform analytics exports,
bank statements.
- The pulse reads the **newest file matching the metric's pattern** (recorded in the profile, e.g.
  `members-*.csv → row count`). Parse mechanically; don't re-interpret a format that parsed before.
- **Freshness tag:** `as of <file date>` — always show how old the export is.
- **On no new file:** use the last logged value labeled carried-forward, and note gently which
  export is due ("member count is 9 days old — drop a fresh export when convenient"). Nag exactly
  once per pulse, never per metric.

### 3. `workspace-file` — a file the user already keeps
A tracker spreadsheet, a log their other agents maintain (e.g. money-manager's books), a notes file
with a known convention.
- The profile records the path and where in the file the number lives. Read-only, always.
- **Freshness tag:** the file's own date/latest entry date, stated.
- **On missing/moved file or unparseable value:** report it, carry forward with the label, suggest
  a profile fix in the footer.

### 4. `ask-me` — the user tells the pulse
Zero infrastructure, fully legitimate. The number lives in the user's head or in an app with no
export worth the trouble.
- The pulse renders the metric with its last logged value **labeled "your last update — <date>"**
  and includes one collected ask at the end of the briefing: "Quick updates when you have them:
  bookings? cash collected?" Answers get logged (Mode 2 handles the append).
- Never block the pulse waiting for answers. Stale-by-choice is the user's right; the label keeps
  it honest.

---

## The degradation ladder

When a source breaks or was never available, each metric slides DOWN this ladder, one rung at a
time, always with the user's knowledge:

**connector → file-drop → workspace-file → ask-me → (section shrinks to "not tracked yet")**

The bottom rung is still honest: a metric with no source renders as *"not tracked yet — say 'add a
metric' and tell me where it lives (or just tell me the number each morning)."* One line, no guilt,
no fake zero.

## The probe discipline (applies at onboarding AND whenever a source is added)

A source is only saved to the profile after **one successful real read** that the user confirmed
("Stripe says $4,210 — is that the number you mean?"). Presence-checks lie: a connector can be
installed, authed, and still return nothing usable. The probe is one cheap read; do it every time a
source enters or changes rungs.

## Calendar specifics

- Connector: read today's events (and tomorrow morning's, if the run is late in the day). Surface:
  count, first event, last event, the biggest free block, and any conflict/back-to-back crunch.
- Paste-mode: the section renders a one-line invitation ("paste your day and I'll read it into the
  briefing") — if the user pastes, treat it as today's schedule; if not, the section stays one line.
- Off: the section doesn't render at all (profile `Sections off`).

## "What Came In" specifics

This section answers *"did anything happen since yesterday?"* — new subscribers, orders, members,
replies, bookings. Prefer deriving it from the same sources already profiled (delta vs. yesterday's
log row costs nothing). Only profile extra signals here if the user asked for them. If nothing came
in, say "quiet night" — a true zero is information, and it only counts as zero when a real source
said so.
