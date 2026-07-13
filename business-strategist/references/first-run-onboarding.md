# First-Run Onboarding — build the source map

Run this once, when no real profile exists in `references/profiles/`. The goal: leave this single
conversation with a saved source map, the `strategy/` folder created, and **the user's first
question answered or their first review run** — whichever brought them here. First run to first
advice in one sitting.

Tone: a sharp advisor's first day — they walk in having already skimmed the files. **Scan first,
ask second.** Never interrogate the user about things the workspace can already tell you; detect,
then confirm.

---

## Step 1 — Scan the workspace (before asking anything)

Look for what's already being written, especially by other Library agents. Auto-detect candidates:

| If you find | Likely source for |
|-------------|-------------------|
| `pulse/pulse-log.md` (daily-business-pulse) | Money, Audience & Marketing, Goals (focus notes) |
| A lead ledger under `leads/` (lead-manager) | Leads & Sales |
| A pipeline + deal files under `sales/` (sales-call-copilot) | Leads & Sales |
| Books / P&L spreadsheet (money-manager or hand-kept) | Money |
| A goals/tasks file (`TASKS.md`, `goals.md`, or similar) | Goals & Execution |
| Client folders, churn/retention trackers, testimonials | Clients & Delivery |
| Content folders (blog drafts, social output, video scripts) | Audience & Marketing |
| Any tracker/spreadsheet with dated business numbers | Wherever it fits |

Also read `CLAUDE.md`/the Brain for business shape, offers, and stated goals — that context makes
every later answer sharper.

## Step 2 — Confirm the map with the user (5 minutes, not 20)

Present what was found, domain by domain: *"For money, I found your books at `<path>` — is that
the source of truth? Anything I missed?"* For each of the five domains (money, leads & sales,
clients & delivery, audience & marketing, goals & execution):

- **Found + confirmed** → goes in the profile with its exact path/read pattern.
- **Found but wrong/stale** → user points at the right source.
- **Nothing found** → one question: *"Do you track this anywhere — a file, a spreadsheet, an
  export you could drop in?"* If genuinely untracked, record the domain as `not tracked` — that is
  a legitimate answer, and it becomes standing advice, not a blocker.

## Step 3 — Probe every source, one real read, right now

Non-negotiable (presence-checks lie). For each confirmed source, do one real read and show the
user something true from it: *"Your ledger has 113 people, newest entry Jul 8 — that the one?"*
A source that can't produce a value now is recorded as `not tracked` or repointed — never saved
on faith.

## Step 4 — Goals & cadence

- **Goals:** if a goals file was found, confirm it (READ-ONLY — say so out loud; it builds trust).
  If none, ask for the current top 1–3 goals in conversation and record them in the profile —
  the first review needs *something* to score against next time.
- **Cadence:** *"How often do you want the full review — quarterly is the default; some run it
  monthly."* Record it. Offer a scheduled task only AFTER the first review has run (they should
  see one before committing to a rhythm). **The scheduled prompt must be a thin loader** — "read
  the business-strategist SKILL.md and run Mode 2" — never a pasted copy of instructions.
- **Language:** *"What do you call the people you serve — members, clients, customers?"* Business
  name from the Brain if present; otherwise ask.

## Step 5 — Save and go

1. **Create the workspace:** `strategy/` and `strategy/reviews/`.
2. **Write the real profile** to `references/profiles/<their-business>.md` — read the source map
   back to them in a few sentences, not a wall of markdown.
3. **Run what they came for, immediately:**
   - They arrived with a question → Mode 1, right now, on the fresh map.
   - They arrived saying "run my review" (or with no specific ask) → Mode 2. The first review is
     the baseline: comparisons and goal-scoring sections honestly say "first review — baseline
     set; scoring starts next time" instead of faking a history.
4. **Close with what happens next:** *"Ask me anything strategic whenever — I read before I
   answer. Say 'run my review' at `<cadence>`, or I can schedule it. And every source you add —
   or every Library agent you start running — makes me smarter."*

## Failure handling

- **Thin or empty workspace:** run the interview standalone — goals from conversation, every
  domain `not tracked`. The first output is still real: honest advice on their question plus a
  ranked "start tracking these first" list. Never a wall.
- **User wants to skip the probes:** don't. One read per source is seconds, and an unverified map
  produces confidently wrong reviews — say exactly that, then probe.
- **Overwhelming workspace (hundreds of candidate files):** map the best source per domain, note
  runners-up in the profile's Notes. The map can grow in Mode 3; it doesn't need to be complete to
  be useful.
