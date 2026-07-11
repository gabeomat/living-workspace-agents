# Pulse Design System — the locked layout + the log format

The layout is FIXED (it's part of the product — every user's pulse has the same editorial bones).
The identity is PULLED: business name, accent colors, and vocabulary come from the profile. Do not
redesign this page per-user or per-day; inject their values into this system.

---

## The file

- One self-contained HTML file: `pulse/pulse-YYYY-MM-DD.html`. Opens beautifully when double-clicked
  from Finder. All CSS inline; all JS inline; Chart.js via CDN
  (`https://cdn.jsdelivr.net/npm/chart.js`) is the only external asset. System-font fallbacks so the
  page never breaks offline.
- Keep the **last 7** daily files; delete older ones. History lives in the log, not in stale HTML.
- In Cowork, push the same content to the pinned artifact (stable id `daily-pulse`) via
  update-in-place so the sidebar copy is always today's. The HTML file is still written — it's the
  copy that works everywhere.

## Typography & palette (defaults — accent is pulled)

- **Display serif** for the masthead, section heads, and big numbers' labels: `Playfair Display`
  (Google Fonts), fallback `ui-serif, Georgia`.
- **Body sans:** `Inter`, fallback system sans. Body line-height 1.6.
- **Mono for every number** in stat pills and deltas: `IBM Plex Mono`, fallback `ui-monospace`.
- Base palette (CSS `:root` vars): `--paper: #faf9f6` (page), `--card: #f2efe9` (pills/cards),
  `--ink: #1b1d1e` (text), `--rule: #26282a` (heavy rules), `--muted: #6b6f73`,
  `--good: #2d7a4f`, `--warn: #b07a1a`, `--bad: #9b2c2c`.
- `--accent` and optional `--accent-2` come from the profile. Default accent if none:
  `#3d5a80`. The accent carries the masthead kicker, The One Thing action pill, sparkline strokes,
  and rank-1 priority — used sparingly, so it reads as *their* mark, not decoration.

## The page, top to bottom

1. **Masthead** — thin top strip in small all-caps sans: left = `<BUSINESS NAME> · DAILY PULSE ·
   NO. <run count from log>` in `--accent`; right = full date. Below: the day's title in the display
   serif (~3rem) — a 3–6 word editorial headline for the day ("Quiet night, loud calendar."), not a
   label. Bottom border `2px solid var(--rule)`.
2. **The One Thing** — the inverted block, immediately under the masthead, impossible to scroll
   past: full-width band, `--ink` background, `--paper` text. Inside: all-caps kicker ("THE ONE
   THING · TODAY"), the single move in display serif (~1.8rem), one lighter line of *why this and
   not the obvious alternative*, then a small pill in `--accent` labeled **FIRST MOVE** followed by
   the 30-minute action. If today's call is "let it run," the pill reads **HOLD** in `--muted` at
   the same visual weight — a confident no-action day, never a vague one.
3. **Stat strip (Money)** — one pill per profiled metric, in a responsive grid. Each pill: `--card`
   background, 3px left border in `--accent`, small all-caps label, big mono number, a sparkline
   beneath (from log history — see rules), and a mono delta line vs. the previous logged reading
   with ▲ ▼ → colored `--good`/`--bad`/`--muted` **by the metric's `direction`** (down can be good).
   Under each pill in tiny muted text: the source + freshness tag ("stripe · live", "csv · Jul 8",
   "your last update · Jul 5").
4. **What Came In** — short prose + a compact list of overnight arrivals (new subscribers, orders,
   replies) with counts. "Quiet night" is a fine section when true.
5. **Today at a Glance** — the calendar: first event, count, the biggest free block, any crunch
   flagged in `--warn`. Paste-mode or off states per `source-map.md`.
6. **Tasks & Goals** — the weekly goal quoted, then what's due/stalling from their task file, then —
   when it exists — one honest line on drift between the goal and the visible activity.
7. **Top 3 Today** — three ranked cards (grid, stacks on mobile): rank number in display serif,
   headline, one-sentence rationale, and a small tag pill — at least one **PROTECTS REVENUE** and
   one **GROWS REVENUE** when both apply. Card 1's left border is `--accent`; 2 and 3 are `--rule`
   and `--muted`.
8. **Footer** — three small columns: data freshness summary (each source's tag), the date of the
   latest focus note, and links (yesterday's pulse file, their task file, `pulse/pulse-log.md`).
   Then the loop line, styled as a quiet prompt: *"What's your focus today? Reply and I'll log it."*

## Sparkline rules (honesty in charts)

- Sparklines draw **only from logged rows**. 1 reading = no line, show "day 1". 2–4 readings = dot
  markers, caption "Nth reading". 5+ = line.
- **Never label a span "last 7 days" unless 7 daily readings exist.** Caption the truth: "8 readings
  · Jun 30 – Jul 11". Plot actual dates — never assume even spacing.
- Chart.js sizing (prevents the runaway-canvas bug — required pattern): every canvas lives inside a
  relative-positioned wrapper div with a fixed height (~48px) and `overflow: hidden`; the canvas is
  absolutely positioned to fill it. Chart options: `responsive: true, maintainAspectRatio: false,
  resizeDelay: 100, animation: false`, legends/tooltips/axes off. Never put a fixed height on the
  canvas element itself.

## Editorial copy rules

- 300–500 words of prose total across the page. A briefing, not a report.
- Direct and honest; numbers and dates, not vague summaries. One pull-quote allowed for the day's
  biggest flag, left-bordered in `--accent`.
- The user's vocabulary throughout (members/clients/customers/jobs — from the profile).

---

## `pulse/pulse-log.md` — the rolling log (the memory)

One markdown table, one row appended per run. This file is why trends exist even for paste-based
metrics — and it is the only place history lives.

```
| date | metric values… | sources… | focus_note |
```

- **Header row is written at onboarding** with one value column + one source-tag column per profiled
  metric (e.g. `mrr`, `mrr_src`). Adding a metric later appends new columns; old rows leave them
  blank. Retired metrics keep their columns — never rewrite history.
- Values are raw numbers (no formatting); source tags are short (`live`, `csv:2026-07-08`,
  `asked`, `carried`).
- `focus_note` holds the user's one-liner from the loop question (Mode 2 appends it to today's row).
- Delta and trend math reads this table deterministically. If the table and a fresh source disagree
  about yesterday, trust the log for yesterday and the source for today — and never edit old rows.
