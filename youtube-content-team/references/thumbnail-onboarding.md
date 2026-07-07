# First-Run Thumbnail Onboarding

Run this ONLY when there's no *real* YouTube profile (folder holds only `_TEMPLATE.md`, or nothing)
OR `assets/headshots/` has no photos. A real profile is any file not starting with `_`. Goal: set the
user up once so every future run is hands-off. Keep it warm and quick — this is a guided setup, not an interrogation.

## The flow (one guided pass)

### 1. Likeness — the most important input
Say plainly why: *"The whole reason these thumbnails will look like YOU — not a generic AI face — is that
I use your real photos as a reference. Drop 2–4 headshots into `assets/headshots/`."*

Ask for **varied expressions** so the agent can match the face to the video's mood:
- one **confident/neutral** (default)
- one **excited/energized**
- one **thoughtful/serious**
- optional: one **surprised/shocked**

Accept uploaded files (resolve absolute paths) or a folder they point at. Note per-photo which expression it
captures. If they can only give one, that's fine — the model adjusts expression from the prompt, but flag that
2–4 gives better variety.

### 2. Thumbnail brand
Capture the visual identity for their thumbnails (distinct from any other brand file — this is specifically the
YouTube thumbnail look):
- **Colors** — 2–3 hex values (primary, accent, background). If they don't know hex, ask for color names and convert.
- **Style register** — bold/loud (MrBeast-style, high saturation, big text) vs. clean/editorial vs. warm/approachable.
- **Text treatment** — all-caps punchy, mixed case, or minimal.
- **Reference thumbnails (optional but powerful)** — ask them to paste 1–2 thumbnails (theirs or ones they admire).
  Use these ONLY as aesthetic reference for the prompt, never to copy exactly.

### 3. Niche + audience (skip if already in their Brain)
- What the channel is about, who watches, what a good video should move for their business.

### 4. Write the profile
Copy the shape from `profiles/_TEMPLATE.md`, fill in everything gathered, and save to
`references/profiles/<their-channel-slug>.md` (no leading underscore). Confirm it back to them in a short summary.

### 5. Continue
Once saved + headshots present, resume the pipeline at the thumbnail stage. From now on, future runs skip
onboarding entirely and read the saved profile.

## Guardrails
- Never write real data into `_TEMPLATE.md`. Always create a new `<channel>.md`.
- Never proceed to generate thumbnails without at least one real headshot — if none provided, stop and ask again.
- Don't over-collect. Four things: photos, colors, style, niche. Everything else is optional.
