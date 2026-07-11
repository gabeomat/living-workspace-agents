# First-Run Onboarding — "how do you sell?"

Run this the first time, before any call work. It's an interview, not a form — ask conversationally, a few questions at a time, and confirm what you learn back to the user. Check their `CLAUDE.md`/Brain first and **don't ask what the workspace already answers.** At the end, write their real profile and build the `sales/` structure.

## 1. The offers — "what can someone buy from you?"

For each offer: name, one-line promise, **the real price**, and the typical path to buying it (straight from a call? proposal first? contract?). Get this exactly right — **proposals only ever quote these numbers.** If pricing is custom-per-deal, capture the floor, the typical range, and who sets the final number (spoiler: the user, never the agent).

Also ask: any payment terms they offer (plans, deposits), and any they *don't* want offered even if a prospect asks.

## 2. The sales motion — "how does a deal usually go?"

- **Where calls come from** — workshops, referrals, inbound DMs, a booking page? (Context that makes pre-call briefs smarter.)
- **The typical arc** — one call and close? discovery → proposal → decision call? How long is a healthy cycle, so "gone quiet" means something real for *their* business.
- **What a won deal looks like** — signed? paid? started?
- **The objections they already know** — every seller can name their top three. Seed `playbook/objections.md` with them and how the user currently answers.
- **Existing pipeline** — deals in flight *right now*? Capture each as a deal file from what the user can tell you (and any transcripts/emails they can drop in `sales/inbox/`), so the pipeline is honest on day one instead of empty.

## 3. Transcripts — "how do your calls get recorded?"

- Which recorder (Zoom, Fathom, Meet, Otter, phone notes…)? How do they get the transcript out of it — and to `sales/inbox/`?
- If a meeting-recorder MCP is connected, note it (pull-only).
- If they don't record at all: rough typed notes after each call work honestly (the debrief just says "from notes" and skips talk-ratio scoring). Also mention: recording works best when it follows consent norms wherever they operate — their call to manage, worth saying once.

## 4. Rhythm, voice, and lines not to cross

- **Follow-up window** — how many days of silence before a nudge is due? Default 5 business days.
- **Voice** — a brand-voice skill installed? If not, 2–3 samples of their writing (sent emails are ideal — that's the exact register follow-ups need) and any voice rules.
- **Coaching appetite** — confirm plainly: scores will be honest, delivery will be kind, and each call ends with one thing to work on, not a pile. (Nobody has ever meant "inflate my scores" by "be nice" — but let them say how direct they want it.)
- **Exclusions** — anyone whose calls should *not* be debriefed or filed (existing clients' delivery calls, internal calls, personal calls that share the same recorder).

## 5. Build and confirm

1. Create `sales/` per `references/debrief-and-deal-spec.md` (folders + empty `pipeline.md` with the header row + empty `processed.log` + seeded `playbook/objections.md`).
2. Copy `profiles/_TEMPLATE.md` → `profiles/<their-business>.md` and fill it from the interview. Read it back in two sentences and correct anything.
3. Tell them the first move: **drop one recent call transcript into `sales/inbox/` and say "debrief my call."** Best first pick: a call they *lost* or felt wobbly on — that's where the coaching shows its value fastest.
4. Offer the rhythm: if scheduled tasks are available, offer a weekly pipeline check; if not, give them the one-line command.

**The wow to aim for:** within one session of onboarding, the user should be reading an honest scorecard of a real call — with their own words quoted back at the exact moment the deal wobbled — and holding a follow-up draft they'd actually send.
