# The Story Bank — format, belief tags, and how to elicit stories

Stories are the fuel of every sequence — and they're the one input that must NEVER be baked into the agent, because they change: new client wins land, new offers need different proof, old stories get stale. The bank is a growing file the user owns; every build reads it, every run can feed it.

## The file: `nurture/stories/story-bank.md`

One entry per story:

```markdown
## [short handle, e.g. "43-subscriber launch"]
- **Told:** YYYY-MM-DD · **Kind:** origin | client win | failure-lesson | moment | borrowed (with permission)
- **Shifts the belief:** [tag(s) — see below]
- **Serves offer(s):** [which offers this is proof for | "any"]
- **Usable publicly:** yes | first-name only | anonymized only  ← ask when filing; never assume
- **The story:** [4–10 lines, in the user's words tightened — keep their phrases, their texture,
  the specific numbers and moments. A story stripped of its specifics stops being proof.]
- **Used in:** [sequence dates — track so the same list doesn't hear one story three sequences running]
```

## Belief tags (match these to the sequence's checkpoints)

The tag answers: *what does a reader believe after hearing this?*

- `this-problem-is-real` — names/normalizes the pain (unaware → problem-aware)
- `its-not-your-fault` — the old way was the flaw, not the reader
- `theres-a-different-way` — the mechanism shift
- `works-for-people-like-me` — proof from a relatable someone (the workhorse tag — collect many, varied: different niches, list sizes, starting points)
- `works-without-X` — kills a specific objection (without a big list / tech skills / time / ad budget…) — tag the X
- `the-seller-is-one-of-us` — origin credibility
- `the-seller-is-honest` — a failure or refund story told straight (rare and disproportionately powerful)
- `waiting-costs-more` — honest urgency: what staying stuck actually cost someone
- `buying-was-the-easy-part` — post-purchase reassurance; the first-win story

## Eliciting stories (onboarding seeds 3–5; every build asks for fresh ones)

Ask like a person, not a form — one at a time, and chase the specifics:

- *"Tell me about a client or customer you're proud of. Where were they when they found you — and what changed?"* (→ `works-for-people-like-me`)
- *"What's the moment you figured out your way of doing this? What weren't you able to do before?"* (→ origin / `theres-a-different-way`)
- *"What do people always say they're worried about before buying — and who bought anyway and was glad?"* (→ `works-without-X`)
- *"What's something that went wrong that you handled honestly?"* (→ `the-seller-is-honest`)
- *"Who almost didn't buy — and what did waiting nearly cost them?"* (→ `waiting-costs-more`)

Capture rules: keep their phrasing and specifics (numbers, timeframes, the actual words a client said) · tighten, don't rewrite · **ask the "usable publicly" question every time** and honor it in drafting (anonymize means changing identifying details AND saying nothing false — "a member," not a fake name presented as real) · a thin story is filed as thin, and flagged: "this one needs one more detail to be usable — what did X actually say?"

## Using the bank in a build (Mode 1, step 3)

1. Open with the refresh: *"any new stories since last time — a client win, a moment, a lesson?"* File anything new first.
2. Map the sequence's belief checkpoints (from the brief) to tags; pick the freshest, most specific story per checkpoint. Prefer stories not used on this same audience recently (`Used in:`).
3. **A checkpoint with no matching story is a conversation, not a gap to paper over:** ask targeted elicitation for it, use a weaker-but-real story, or restructure the checkpoint. Never invent, never "compose a representative example" presented as real.
4. After delivery, update each used story's `Used in:` line.
