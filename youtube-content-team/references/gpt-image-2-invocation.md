# Generating the Thumbnails (gpt-image-2) — with graceful hand-off

The `gpt-image-2` skill generates the images locally via the user's ChatGPT subscription + the `codex` CLI.
It works in **Claude Code / the desktop app on the user's own machine** — not in remote sandboxes with no shell.
**No client is ever stranded:** if the engine isn't available, hand over the finished prompts for manual paste.

## STEP 1 — Environment check FIRST (before any generation call)

```bash
which codex
```
- **Returns a path** → the codex CLI is installed. Proceed to Step 2.
- **Returns nothing** → the engine can't auto-generate here. Skip to **Hand-off mode** below. Do NOT attempt a bash generation call — it will fail.

## STEP 2 — Locate the gpt-image-2 generation script

```bash
GEN_SH=$(find ~ -name "gen.sh" -path "*gpt-image-2*" 2>/dev/null | head -1)
echo "$GEN_SH"
```
If empty, the `gpt-image-2` skill isn't installed. Tell the user to install it, then use **Hand-off mode** for now.

## STEP 3 — Verify the headshot exists

```bash
ls "<absolute path to chosen headshot in assets/headshots/>"
```
If missing, list what's in `assets/headshots/` and pick another, or run onboarding to collect one.

## STEP 4 — Generate both variations

```bash
bash "$GEN_SH" \
  --prompt "<full v1 prompt from thumbnail-prompt-template.md, all placeholders filled>" \
  --ref "<absolute path to chosen headshot>" \
  --out "content-drafts/youtube-thumb-<slug>-v1.png"
```
Run again for v2 with the second prompt + output path.

### If gen.sh fails with an auth error
`which codex` succeeding doesn't guarantee a logged-in session. If `gen.sh` exits non-zero with an auth error,
do NOT retry in a loop. Tell the user: *"codex is installed but the ChatGPT session looks stale — run `codex login` and try again."* Then drop to Hand-off mode so they still get the prompts.

## Hand-off mode (engine unavailable — the graceful fallback)

Deliver the two finished prompts + the headshot path so the user pastes them into ChatGPT (Images 2.0) or any
image tool. The pipeline still fully delivered — auto-gen was just the bonus tier.

```
## Thumbnail prompts ready — paste these into ChatGPT (Images 2.0) or your image tool

I can't auto-generate here (the codex CLI / ChatGPT session isn't available in this environment),
so here are the two finished prompts and your reference headshot. Attach the headshot, paste the prompt,
save the result.

### Variation 1 — <expression name>
Attach: <absolute path to headshot>
Prompt:
<full v1 prompt, ready to paste>

### Variation 2 — <expression name>
Attach: <absolute path to headshot>
Prompt:
<full v2 prompt, ready to paste>

Save results to content-drafts/youtube-thumb-<slug>-v1.png and -v2.png.
```

## Hard rules
- Two variations. Not one, not three.
- Always attach a real headshot — never generate the face from text.
- 16:9, 1280×720 minimum.
- Don't switch image models mid-pipeline. Use gpt-image-2 (or hand off its prompts). Don't fall back to a different generator or an HTML mockup.
