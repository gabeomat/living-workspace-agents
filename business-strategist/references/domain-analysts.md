# Domain Analysts — who reads what, and the evidence contract

The Strategist never reads the whole workspace itself. It dispatches one **inexpensive analyst
agent per domain**, each with a narrow brief: read ONLY your mapped sources, return structured
evidence, invent nothing. The frontier model's job is judgment on top of that evidence — not
re-reading files. This split is what keeps a whole-business review cheap enough to run quarterly
(or a pricing question cheap enough to ask on a Tuesday).

---

## The five domains

Every business maps onto these five. A domain with no sources in the profile is **skipped by the
analysts and reported by the synthesis** as "not tracked yet" — with a concrete start-tracking
recommendation, never a guess.

### 1. Money
*Is the business making money, and where is it going?*
- **Typical sources:** money-manager books/P&L, bookkeeping spreadsheet, payment-platform exports, the revenue rows of a pulse log.
- **Looks for:** revenue trend, margin trend, expense creep, concentration risk (one client/channel carrying everything), cash pattern.

### 2. Leads & Sales
*Is new business coming in, and is it converting?*
- **Typical sources:** lead-manager ledger, sales-call-copilot pipeline + deal files, CRM exports, an opportunities spreadsheet.
- **Looks for:** lead flow trend, pipeline health (what's stuck, what's waiting on whom), close rate, time-to-close, where deals die.

### 3. Clients & Delivery
*Are the people who pay staying, succeeding, and saying so?*
- **Typical sources:** client files/notes, churn or cancellation tracker, retention/community data, testimonials folder.
- **Looks for:** churn/retention trend, at-risk signals, delivery load vs. capacity, proof being generated (or not).

### 4. Audience & Marketing
*Is the business getting found, and is the audience growing?*
- **Typical sources:** email-list metrics (pulse log rows or platform exports), content output (blog/social/video folders), ad or funnel trackers.
- **Looks for:** list/audience growth trend, publishing consistency vs. stated intent, which channel actually produces (by whatever attribution exists — stated honestly).

### 5. Goals & Execution
*What did the owner say they'd do, and what actually happened?*
- **Typical sources:** the goals/task file, the previous review's plan, pulse-log focus notes.
- **Looks for:** stated goals vs. visible activity, drift (effort flowing somewhere other than the plan), stalled items, the gap between intention and calendar.

---

## The analyst brief (fixed prompt shape)

Each analyst gets exactly this, filled in from the profile:

> You are a business analyst. Read ONLY these sources: `<the domain's mapped paths/read patterns
> from the profile>`. Do not read anything else. Do not invent, estimate, or extrapolate a number.
> `<For full reviews:>` Here is what the last review recorded for this domain: `<scorecard lines>`.
> Report what CHANGED, not just what is.
>
> Return, as structured markdown:
> - **Findings** — each one line: the claim, then `(source file, date/row)`. Facts only.
> - **Trend** — only what the data actually shows, with the span it shows it over ("flat across
>   the 3 logged months"), never a smoothed story.
> - **Anomalies** — anything that broke pattern, with the citation.
> - **Gaps** — what this domain can't answer because the data isn't there (name the missing data,
>   don't apologize for it).
> - **Freshness** — the date of the newest data point you read.
>
> Keep it under ~400 words. Evidence, not advice — recommendations are not your job.

## Rules of the fan-out

- **Cheapest model available** for analysts. This is extraction against a fixed contract, not judgment.
- **Parallel where the environment allows.** A full review is five analysts at once; a Mode 1
  question is only the 1–3 domains it touches — never all five out of habit.
- **Scope discipline:** an analyst that reports on files outside its mapped sources has failed —
  its output gets re-run, not trusted.
- **No-subagent fallback:** in an environment without subagents, the main session reads the same
  mapped sources sequentially under the same evidence contract. Tell the user the review will take
  a bit longer; on a very large workspace, suggest scoping the question tighter.
- **A failed read is a finding.** "Books unreadable — file moved?" goes into the evidence verbatim,
  flows into the synthesis footer as a fix-this note, and is never papered over.

## What the synthesis does with the evidence

The main session receives only the analysts' structured evidence (never the raw files) and:
1. Cross-reads domains — the interesting findings live at intersections ("leads up, revenue flat →
   conversion leak, not a marketing problem").
2. Takes positions. Every recommendation carries its citing evidence and the strongest
   counter-argument.
3. Converts gaps into "start tracking this" recommendations, ranked by which would most improve the
   next review.
4. Never re-litigates a number an analyst cited — if a figure looks wrong, the fix is one targeted
   re-read of that source, not a from-memory override.
