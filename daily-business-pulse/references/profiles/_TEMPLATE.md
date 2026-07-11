# Pulse Profile — <Your Business Name>

> This is a SCAFFOLD. It is never used as real data — the `<angle-bracket>` prompts are instructions, not values.
> The agent builds a real copy of this WITH you on first run (onboarding). To fill it in by hand instead: copy this
> file to `<your-business>.md` (no leading underscore) and replace every `<...>`. Delete any line you don't use.

## Metrics (3–5 numbers that tell you your business is healthy)

> One block per metric. `source_type` is one of: `connector` | `file-drop` | `workspace-file` | `ask-me`.
> The onboarding probes each source with ONE real read before saving it here — if it can't be read today,
> it can't be trusted tomorrow at 7am.

- **Metric 1:** <name, e.g. "MRR" or "weekly sales">
  - source_type: <connector | file-drop | workspace-file | ask-me>
  - source: <exact connector tool + read pattern | file pattern in pulse/data/ | path to the workspace file + where the number lives in it | "asked in chat">
  - unit: <$ | count | %>
  - direction: <up-is-good | down-is-good>
- **Metric 2:** <...>
- **Metric 3:** <...>
- **Metric 4 (optional):** <...>
- **Metric 5 (optional):** <...>

## Tasks & goals
- **Task/goal file:** <path to the file the pulse reads (READ-ONLY) | "pulse created goals.md for me">
- **Where the weekly goal lives in it:** <heading or convention, e.g. "the '🎯 This Week' section">

## Calendar
- **Source:** <calendar connector name | "I'll paste my day when asked" | "off">

## What came in (the overnight section)
- **Signals to check:** <e.g. "new subscribers (email connector)", "new orders (payments)", "new members (community export)" — or "derive from my metrics" | "off">

## Language & brand
- **My people are called:** <members | clients | customers | jobs>
- **Business name:** <name>
- **Accent colors:** <1–2 hex codes, or "pull from my brand file at <path>" | "use the default">
- **Brand/voice skill or file:** <name/path | "none">

## Rhythm
- **Run time:** <e.g. 7:00 AM> — **Timezone:** <e.g. America/Anchorage>
- **Scheduled task:** <"created YYYY-MM-DD" | "manual — I say 'run my pulse'">
- **Sections off:** <any of the six spine sections you've disabled | "none">

## Notes
- <anything the pulse should always remember — busy seasons, numbers that spike on weekends, a metric that lags by a day, etc.>
