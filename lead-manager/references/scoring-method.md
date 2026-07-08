# Scoring method — who's actually warm

Scoring is **rules, not vibes, and code, not tokens**. `scripts/score_leads.py` runs the whole thing deterministically so it's auditable, repeatable, and free. A model only gets involved (optionally, cheaply) to break ties near the batch cut-line.

## The formula

```
score = (source points + signal points) × multi-source multiplier × recency factor
```

### Source points (per source token present)

| Source | Points | Why |
|--------|-------:|-----|
| `event_*` attended | 25 | They gave you an hour of their life |
| `community` member | 20 | They joined your room |
| `past_customer` | 25 | They've already paid you once |
| `manual_add` | 15 | The owner personally noticed them |
| `event_*` registered (attendance unknown) | 10 | Intent, unproven |
| `email_list` | 5 | The baseline |

### Signal points (per signal, by type)

| Signal | Points |
|--------|-------:|
| `purchased` | 30 |
| `asked_question` | 20 |
| `replied` | 15 |
| `personal_share` | 15 |
| `posted` | 12 |
| `requested_info` | 12 |
| `referred` | 12 |
| `attended` | 10 |
| `joined` / `registered` | 5 |

### Multi-source multiplier
Appearing in 2 pools → ×1.15. In 3+ → ×1.3. Someone who's on the list AND in the community AND came to an event is telling you something.

### Recency factor (from the latest of `last_activity` / newest signal)
≤30 days ×1.0 · ≤90 ×0.85 · ≤180 ×0.65 · older ×0.4. Warmth decays; it doesn't vanish.

## Segments → ask-paths

| Segment | Definition | Routes to |
|---------|-----------|-----------|
| **warm** | attended an event, OR community member, OR past customer, OR has a `replied`/`asked_question`/`personal_share` signal | **Premium offer** (or Core, per profile preference) |
| **engaged** | has at least one signal, but doesn't meet the warm bar | **Core offer** |
| **cold** | subscriber-only, zero signals | **Entry offer** — and usually stays in general nurture, not personal outreach |
| **customer** | `status = customer` | serve/renew/expand path — per profile; never re-pitched what they own |
| **excluded** | `not_interested` / `unsubscribed`, or inside cooldown | untouchable |

**Hard rule: the Premium ask goes only to warm.** Cold people get invited through the front door (Entry offer), not proposed to.

## Batch eligibility

A person enters the weekly batch only if ALL of: score above the floor · at least one real signal · `last_touch` empty or older than [[Cooldown Days]] · status not excluded · nudge limit not reached (see `outreach-rules.md`).

**Sparse-signal honesty:** a big list means most rows are cold with zero signals. Don't pretend to know them — they stay in the general nurture the user already runs. This agent only claims the people it has actual evidence about. That honesty is also what keeps batches good.

## Tuning

Defaults live in the script. To adjust, write overrides to `leads/weights.json` (same keys, only what changes) — the script picks it up automatically. Tune AFTER two or three real batches: the user's "no way is this person a 9" reactions are the tuning data. Record what changed and why in the profile.

## The optional tie-break pass

For people within a few points of the batch cut-line, one cheap-model read of their verbatim signals may adjust ±10: does this read like real buying interest or polite noise? That's the only model call in scoring — everything else is arithmetic, and arithmetic shouldn't cost tokens.
