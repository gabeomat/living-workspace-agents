# Design Onboarding — first-run setup (build the user's Social Design System)

Run this ONLY when `references/profiles/` has no *real* profile — i.e. the folder holds only
`_TEMPLATE.md` (a scaffold with `<angle-bracket>` prompts, never a brand source), or nothing at
all. A real profile is any file that does not start with `_`. Goal: build the user's profile
*with* them in one guided pass, using example
images to capture their aesthetic — then write it to `references/profiles/<their-business>.md` so
every future run is automatic.

Keep it warm and simple. The user may be non-technical. One thing at a time. Don't dump the whole
template on them.

## The frame to open with

> "First time running this, so let's set up your look once — takes a few minutes, and after this every
> week is automatic. I'll ask about your brand, have you show me a few examples of the style you want,
> and I'll build your design system from that. Ready?"

## Step 1 — Brand kit

Ask for, one beat at a time:
- **Colors** — "What are your brand colors? Hex codes if you have them; if not, describe them or paste a logo/site link and I'll pull them." Capture 2–4 with names + where each is used.
- **Fonts** — "Any brand fonts? If not, I'll suggest a clean pairing." (Steer to Google Fonts so they load via CDN.) Capture headline / accent / body / label roles.
- **Brand mark** — "What name or wordmark should sit on each card?"
- **Feel words** — "Give me 3–5 words for the vibe — e.g. bold and raw, or soft and airy."

## Step 2 — Capture the aesthetic from EXAMPLES (the important step)

> "Now show me the look you want. Upload 3–5 example images — your own best posts, or posts from
> anyone whose Instagram style you'd want yours to feel like. I'll read the aesthetic from these:
> layout, spacing, how bold or soft, where text sits, whether covers use a photo."

When images come in:
1. Resolve their paths (uploads live under the session's uploads dir).
2. **Look at them.** Describe back what you see so the user can correct you: "These read soft and
   editorial — lots of whitespace, thin borders, serif headlines, photo-forward covers. Matching that?"
3. Extract the **treatment rules** (borders thick/thin, corners square/rounded, shadows hard/soft,
   whitespace tight/generous, photo-forward or text-forward). These become the profile's treatment rules.
4. Note anything about **carousel covers** specifically — do their examples put a photo of them on the
   cover? That sets the carousel cover rule.

## Step 3 — Post mix

> "Here's a proven weekly mix: 3 image posts, 2 carousels, and 1 Reel, Monday through Saturday. Want to
> start there, or change the days/formats?"

Capture: which days, which format each, static layout variants (how many distinct looks), timezone,
posting times, and which networks. Default to the proven mix if they're unsure — beginners should not
have to design a whole content calendar from scratch.

## Step 4 — Carousel + Reel specifics

- **Carousel cover rule** — confirm from Step 2: photo-on-cover (whose photo?) or text-only. Confirm slide
  structure (cover → N content → CTA) and default count.
- **Reel arc** — offer the default Hook → Tension → Interrupt → Payoff → CTA (5 frames). Adjust if they want.

## Step 5 — Connector

> "How do you want posts scheduled? Metricool is the smooth default — I can create drafts directly. I can
> also do Buffer, Later, GoHighLevel, or just hand you finished posts + a schedule to post yourself."

Capture the connector and any account/profile IDs. If they don't have one set up, default to **manual**
(the agent will hand off finished assets + a schedule) and note they can add a connector later.

## Step 6 — Voice + Brain pointers

- Ask if they have a **brand-voice skill**; capture its name. If not, note that captions will use a neutral
  clear/human pass until they build one, and that a voice skill is the biggest single upgrade to output quality.
- Ask where their **Business Brain** lives so CTAs can pull real offers. Capture their current priority CTA
  as the fallback.

## Step 7 — Write the profile & confirm

1. Assemble everything into the `_TEMPLATE.md` structure.
2. Write it to `references/profiles/<their-business>.md` (kebab-case the business name).
3. Show the user a tight summary — colors, mix, cover rule, connector — and ask: "Anything to change before
   I lock this in?"
4. On approval, tell them setup is done and every future run just reads this file. Then proceed to the pipeline.

## Notes
- If a brand-voice skill or Business Brain is missing, that's fine — record the gap in the profile and keep
  going. The agent degrades gracefully; it just tells the user what would sharpen the output.
- Don't over-engineer. A good-enough profile they can refine beats a perfect one that stalls onboarding.
