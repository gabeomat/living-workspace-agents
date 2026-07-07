# HTML Render Engine — brand-tokenized

This is the mechanical layer: how captions + the user's brand tokens become finished PNG cards and an
MP4 Reel. **Every color, font, and treatment value comes from the user's profile** (`references/profiles/<their-business>.md`) — nothing here is hard-coded to any one brand. Build each card by
substituting the profile's tokens into the layout that the profile calls for.

## The token model

Read these from the profile and treat them as CSS variables you inject into every card:

| Token | From profile | Example |
|-------|-------------|---------|
| `--ink` | primary/dark color | borders, primary text, dark backgrounds |
| `--paper` | light color | light backgrounds, text on dark |
| `--accent` | accent color | highlights, badges, CTAs |
| `--surface` | panel color (optional) | inner panels on light backgrounds |
| `--font-headline` | headline font | main statements |
| `--font-accent` | accent font | quotes / pull-quotes |
| `--font-body` | body font | body copy |
| `--font-label` | label font | day tags, labels |
| brand mark text | wordmark | the name on each card |
| treatment rules | treatment | border weight, corner radius, shadow style, whitespace |

**Load fonts** via Google Fonts CDN using whatever fonts the profile names, e.g.:
```html
<link href="https://fonts.googleapis.com/css2?family=<HEADLINE>&family=<ACCENT>&display=swap" rel="stylesheet">
```

**Apply the treatment rules consistently across every card.** The profile's treatment is what makes cards
recognizably *this brand* beyond color. Translate the treatment words into concrete CSS and hold it everywhere:

| Treatment says… | Then use… |
|-----------------|-----------|
| thick borders / brutalist | `border: 4–6px solid var(--ink)` |
| thin / delicate | `border: 1–2px solid var(--ink)` |
| square corners | `border-radius: 0` |
| soft / rounded | `border-radius: 16–24px` |
| hard offset shadow | `box-shadow: 10px 10px 0 var(--ink)` (zero blur) |
| soft shadow | `box-shadow: 0 8px 24px rgba(0,0,0,.12)` |
| airy / generous whitespace | larger padding, fewer elements per card |
| bold / loud | oversized headlines, high contrast, filled accent blocks |

## Card dimensions

Use the ratios from the profile (defaults shown):

| Card | Size | Ratio |
|------|------|-------|
| Statics + carousel slides | 1080×1350 | 4:5 |
| Reel frames | 1080×1920 | 9:16 |

## Building each format

### Statics
The profile defines 2–4 distinct static layout variants (e.g. "Statement", "Numbered Steps", "Quote").
Build the day's static using the variant the profile's mix assigns to that day. Each variant is a small
HTML template: brand mark + day tag + the variant's composition, all using the tokens. **No two statics in
one week should look identical** — that's the whole point of having variants.

Standard placeholders per variant: a headline, a supporting line, and (for step layouts) numbered items,
or (for quote layouts) a pull-quote + context line. Wrap one key word in an accent highlight span where the
layout calls for emphasis.

### Carousels
Structure: **cover → N numbered content slides → CTA close slide.** The final slide is always the CTA, never
a numbered point.
- **Cover:** honor the profile's cover rule. If it's photo-on-cover, place the supplied photo as the cover
  (full-bleed or framed per the aesthetic), with the headline overlaid legibly (add a subtle scrim behind
  text over photos). If text-only, build a bold text cover using the tokens.
- **Content slides:** numbered, one beat each, consistent template across the set.
- **CTA slide:** the profile's standing CTA (or the run's approved CTA).
- If the profile's carousel needs a supplied photo, that photo was already collected in Phase 0.

### Reels
Build one HTML file per frame in the profile's Reel arc (default 5: Hook → Tension → Interrupt → Payoff →
CTA). Each frame is a full 9:16 card using the tokens, with the per-frame look the profile specifies
(e.g. an inverted accent-background Interrupt frame). Save as `reel-frame-01.html` … `reel-frame-0N.html`.

## Rendering — Playwright (HTML → PNG)

Render each HTML to its own temp dir to avoid filename collisions, then copy to the named output.

```bash
PLAYWRIGHT_BROWSERS_PATH=/var/tmp/playwright-browsers TMPDIR=/var/tmp \
  bash -c "cd /var/tmp/html-to-png && node capture.mjs '/path/to/monday-card.html' '/var/tmp/render-monday/'"
cp /var/tmp/render-monday/card-01.png /path/to/outputs/monday-card.png
```

Notes:
- Install Playwright to `/var/tmp/html-to-png/` and set `TMPDIR=/var/tmp` — session partitions fill fast.
- Render statics + carousel slides at the profile's image ratio; render Reel frames at the Reel ratio.

## Rendering — ffmpeg (Reel frames → MP4)

Render each Reel frame to a PNG, then crossfade them into one silent MP4. The Reel is a **multi-frame video,
never a single looped PNG.** Default: 3s per frame, 0.5s crossfades, ~15s total for 5 frames. Adjust offsets
if the profile uses a different frame count.

```bash
cd OUTPUTS_DIR
ffmpeg \
  -loop 1 -t 3.5 -i reel-frame-01.png \
  -loop 1 -t 3.5 -i reel-frame-02.png \
  -loop 1 -t 3.5 -i reel-frame-03.png \
  -loop 1 -t 3.5 -i reel-frame-04.png \
  -loop 1 -t 3.5 -i reel-frame-05.png \
  -filter_complex "\
    [0:v]scale=1080:1920,setsar=1,format=yuv420p[v0]; \
    [1:v]scale=1080:1920,setsar=1,format=yuv420p[v1]; \
    [2:v]scale=1080:1920,setsar=1,format=yuv420p[v2]; \
    [3:v]scale=1080:1920,setsar=1,format=yuv420p[v3]; \
    [4:v]scale=1080:1920,setsar=1,format=yuv420p[v4]; \
    [v0][v1]xfade=transition=fade:duration=0.5:offset=3[x1]; \
    [x1][v2]xfade=transition=fade:duration=0.5:offset=6[x2]; \
    [x2][v3]xfade=transition=fade:duration=0.5:offset=9[x3]; \
    [x3][v4]xfade=transition=fade:duration=0.5:offset=12,format=yuv420p[v]" \
  -map "[v]" -c:v libx264 -pix_fmt yuv420p -movflags +faststart -an -y reel.mp4
```

For N ≠ 5 frames: chain N−1 `xfade` filters, each offset by (frame_hold × index). Keep the final `format=yuv420p`.

**Verify:** `ffprobe -i reel.mp4 2>&1 | grep Duration` — confirm it exists, is non-zero, and is close to the
expected length (frames × hold − crossfades).

## If Playwright/ffmpeg aren't installed

First, just install them — in an agentic environment (Claude Code, desktop app with a shell) that's a normal
step the user approves, not something they set up in advance. Install Playwright to `/var/tmp/html-to-png/`
and ensure ffmpeg is present, then continue rendering.

Only if the environment genuinely blocks installs (a locked-down machine, or a chat surface with no code
execution) should you stop: produce all the HTML files + finished captions, hand them to the user, and clearly
say the environment couldn't render here — they can render the HTML elsewhere or run the agent where installs
are allowed. The copy + design work is still fully delivered either way.
