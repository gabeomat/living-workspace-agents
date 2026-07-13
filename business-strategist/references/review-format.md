# Review Format — the six-section spine, the scorecard, and honest scoring

The full review (Mode 2) always renders on this spine, in this order. The structure is locked —
it's what makes review #4 comparable to review #1. The content is entirely the user's.

Output: `strategy/reviews/review-YYYY-MM-DD.md` (the document) + one block appended to
`strategy/scorecard-log.md` (the memory). Markdown, readable in any editor. In Cowork, offer to
also surface the review as an artifact; the file remains the source of truth.

---

## The six sections

### 1. What Changed
Since the last review (or "first review — baseline" if none): the 3–7 most material shifts across
all domains, each one line with its citation. Material = would change a decision. Not a data dump —
the analysts' evidence is the appendix, not the opening.

### 2. Where the Momentum Is
What's genuinely working, with the evidence. This section earns the honesty of section 3 — real
wins named specifically ("close rate up 15 points since the pricing change — pipeline, May–Jun
deals"), never generic praise. If nothing has momentum, say so; that IS the finding.

### 3. Where the Leak Is
The single biggest thing costing money, time, or compounding progress — plus runner-ups if they're
close. Cross-domain reads live here ("leads up 40%, revenue flat → the leak is conversion, not
marketing"). Name one leak clearly rather than five vaguely.

### 4. Last Period Scored
Every goal/priority from the previous review's plan, scored:

| Score | Means |
|-------|-------|
| ✅ hit | The stated outcome happened — evidence cited |
| 🟡 partial | Real movement, outcome incomplete — state what's true and what's missing |
| ❌ missed | Didn't happen — one honest line on why, from the evidence, not blame |

**Honest-scoring rules:** the score judges the *outcome as stated*, not the effort ("launched but
zero sales" scores against whatever the goal actually said — if the goal was "launch," it's a hit
AND the review says the goal was too soft; if the goal was "launch and sell 10," it's a miss).
Every score carries the one evidence line that decides it. A goal that can't be scored because
nothing tracked it gets `⚪ unscoreable` — and the new plan inherits a tracking fix.

### 5. The Plan — max 3 priorities
Next period's priorities, **capped at three**, each with: the outcome (written so it can be scored
✅/🟡/❌ next time — a number or a done/not-done, not a vibe), why this over the alternatives, and
the first concrete action. If more than three candidates exist, the review names what waits and
why. Sharpening soft goals into scoreable ones is part of the job.

### 6. Hard Questions
2–4 questions the owner should sit with — the ones the data raises but can't answer. Not
rhetorical, not motivational: *"Your premium offer produces 80% of revenue from 20% of your
attention — what would the business look like if that inverted?"* No answers here; that's the
point.

**Footer:** data-health notes — sources that failed or went stale, domains still untracked (ranked
by which would most improve the next review), and the date of the newest data point used.

---

## The scorecard block (appended to `strategy/scorecard-log.md`)

One block per review — this is what the next review's analysts receive as baseline. Keep it
mechanical and compact:

```markdown
## Review YYYY-MM-DD
- **Domains read:** money ✓ · leads ✓ · clients ✓ · audience ✓ · goals ✓  (✗ = untracked)
- **Key figures:** <one line per profiled headline number: name — value (source, date)>
- **Leak named:** <one line>
- **Plan set (score next review):**
  1. <priority — its scoreable outcome>
  2. <...>
  3. <...>
- **Last plan scored:** <#1 ✅ / #2 🟡 / #3 ❌ — one line total> | "first review — baseline"
```

Rules: append-only, never rewrite old blocks. Retired metrics/domains stay in old blocks. If a
review is run off-cadence ("reset review" mid-quarter), append it like any other — the log records
what happened, not what was scheduled.
