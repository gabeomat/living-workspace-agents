# First-Run Onboarding — "what tells you your business is healthy?"

Run this once, when no real profile exists in `references/profiles/`. The goal: leave this single
conversation with a saved profile, a working `pulse/` folder, **Pulse #1 already rendered**, and
(if they want it) the daily schedule set. First run to first pulse in one sitting — that's the wow.

Tone: a sharp chief of staff on day one. Curious, efficient, zero jargon. Never ask for something
you can read from their Brain — check `CLAUDE.md`/workspace context first and confirm instead of
interrogating ("Looks like you run a membership community — is member count one of your health
numbers?").

---

## The interview (6 beats, ~10 minutes)

### 1. The numbers
Ask: **"What 3–5 numbers tell you your business is healthy? Not everything you *could* track —
the ones that, if you saw them every morning, you'd know where you stand."**

If they struggle, offer by business shape (never push all of these):
- Membership/community: MRR, member count, churn/cancellations this month
- Client services: booked calls, active clients, cash collected this month
- E-commerce: orders, revenue, refund count
- Audience-first: list size, new subscribers, content published

For **each** metric, ask: **"Where does that number live?"** and classify it:

| They say | source_type |
|----------|-------------|
| "It's in Stripe / my email platform / my community / my CRM" (and a connector exists) | `connector` |
| "I can download an export/CSV" | `file-drop` (they'll drop it in `pulse/data/`) |
| "It's in a file/spreadsheet I keep in this workspace" | `workspace-file` |
| "I just know it / I check the app on my phone" | `ask-me` |

### 2. Probe every source — one real read, right now
This is non-negotiable. For each `connector` and `workspace-file` source, **do one real read during
onboarding** and show them the value: "Stripe says $4,210 this month — is that the number you mean?"
- A source that can't produce a value now gets **downgraded one rung on the ladder** (see
  `source-map.md`) with their agreement — never saved on faith.
- For `file-drop`, have them drop one real export in `pulse/data/` now and parse it once.
- For `ask-me`, capture today's value in conversation — it becomes log row #1.

### 3. Tasks & goals
Ask where their to-dos and weekly goal live. If they have a file, record the path and read it once
(READ-ONLY — say so out loud; it builds trust). If they have nothing, offer to create a simple
`goals.md` next to `pulse/` with a "This Week" section and today's brain-dump seeded from
conversation — that file is theirs to edit; the pulse only ever reads it.

### 4. Calendar
Ask if they use Google Calendar (or any calendar with a connector). If yes, connect and **probe with
one real read** — show them today's first event as confirmation. If no connector is available, offer
paste-mode ("each morning the pulse will show a calendar slot — paste your day or ignore it") or turn
the section off. Their call.

### 5. Language & brand
- "What do you call the people you serve — members, clients, customers?" (Sets the vocabulary for
  every section.)
- Pull business name + accent colors from their brand file/skill/Brain if one exists; otherwise ask
  for a color or use the default palette. One accent is enough.

### 6. Rhythm
- "What time should this be waiting for you, and what timezone?"
- If scheduled tasks are available, offer to create the daily task now. **The scheduled prompt must
  be a thin loader** — "Read the daily-business-pulse SKILL.md and run Mode 1" — never a pasted copy
  of the instructions (copies drift, then lie).
- If not available, tell them the ritual: "say *run my pulse* with your coffee."

---

## Then, in order (same conversation)

1. **Create the workspace:** `pulse/`, `pulse/data/`, and `pulse/pulse-log.md` with the header row
   (format in `pulse-design-system.md`).
2. **Write their real profile** to `references/profiles/<their-business>.md` from the interview —
   read it back to them in three sentences, not a wall of markdown.
3. **Generate Pulse #1 immediately** (Mode 1). Today's values become log row #1. Be honest on the
   first-pulse dashboard: sparklines need history, so say "day 1 — trends start forming this week"
   rather than drawing a one-point line.
4. **Pin it** as the `daily-pulse` artifact where supported; either way, hand them the HTML file link.
5. **Ask the loop question** ("What's your focus today?") and log the answer — so tomorrow's One
   Thing is already personal.
6. **Close with what happens next:** "Tomorrow at <time>, this is waiting for you. Drop any exports
   in `pulse/data/` whenever — I read the newest. Say *add a metric* or *change my pulse time*
   anytime."

## Failure handling
- **They can't name any metrics:** start with ONE (usually money in the door). A one-metric pulse
  that runs beats a five-metric pulse that never ships. Note in the profile that expansion is welcome.
- **Every source is `ask-me`:** fine — say so positively. The log still builds their trend history
  from day one; that's the quiet superpower.
- **No Brain / empty workspace:** run the interview standalone and suggest (don't require) creating
  a `CLAUDE.md` so future pulses understand the business behind the numbers.
