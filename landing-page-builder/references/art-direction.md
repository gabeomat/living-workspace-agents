# Art Direction — the stage that makes it look like a designer built it

A page that only obeys a brand's colors and fonts is *correct*. It is not *designed*. The difference — the thing that makes someone say "a real designer made this" — is **art direction**: imagery, texture, depth, and motion chosen for a concept and treated so they belong to the brand instead of sitting on top of it.

This stage runs **after the brief (Stage 2) and before the build (Stage 4).** It gives the critique loop something with real depth to react to. Without it, the loop is polishing an empty room.

**The discipline that separates designed from slop:** imagery is chosen for a *concept* and *treated* to the brand — never a raw stock photo or a default AI hero dropped in. A generic photo pasted onto a page is the exact "AI-landing-page smell" the critique loop exists to kill. If you can't treat an image to belong, don't use it.

---

## Step 1 — Decide the visual concept (before any image exists)

From the brief's concept + "the one thing this page must prove," commit to a **visual world**, not a list of pictures. Name:

- **The imagery role** — is imagery the hero (a full-bleed treated photograph), the atmosphere (backgrounds, section dividers, textures), or the accent (a single arresting object)? Pick one lead role; don't scatter.
- **The depth strategy** — how the page gets dimensionality: layered planes, a treated hero behind glass/blur, a grain overlay, a duotone photograph bleeding under text, a fixed background with content scrolling over. Flatness is the enemy; name the specific move.
- **The motion-of-imagery** — does an image drift, parallax, reveal on scroll, or hold still with grain shimmer? Tie it to the brand's motion feel (custom easing, reduced-motion path).
- **The restraint line** — what you will NOT do. One hero image treated well beats five decorative ones. Name what you're leaving out so the page stays authored, not busy.

Write this as 3–5 sentences. This is the art director's point of view — the thing plain generation can't produce on its own.

---

## Step 2 — Spec each image as a real brief (not "a photo of X")

For every image the concept needs, write a generation/sourcing brief with:

- **Subject + composition** — what's in frame, where the focal point sits, and crucially **where the negative space goes** (that's where copy will live — plan it now, don't fight it later).
- **Light + mood** — direction, hardness, time of day, emotional register. This is 80% of whether it feels premium or generic.
- **Palette intent** — shot/generated so it will *survive brand treatment*: if you'll duotone into forest+persimmon, generate something tonally simple with clear light-to-dark range, not a busy rainbow.
- **Aspect + safe zone** — the ratio it renders at and the region that must stay clear for text/UI.
- **The "not this" line** — steer away from the obvious (no stock-y smiling-people-at-laptops, no generic gradient blobs, no literal clip-art of the concept).

A vague prompt yields a generic image. A directed prompt yields an asset.

---

## Step 3 — Generate (or source), then TREAT to the brand

**Generate first** (the default — bespoke beats stock):

**Run the image-generation preflight before you promise imagery** — see `image-preflight.md`. Probe the backend's health (CLI resolves + binary/auth actually present) so you catch a broken install or missing auth *up front* with the exact fix, instead of failing mid-run. Only claim generated imagery once a backend answers.

- **`gpt-image-2`** (via the user's ChatGPT plan through the `codex`/`gpt-image-2` skill) — preferred; no per-image API cost.
- **`nano-banana`** (Gemini) — strong alternative / fallback.
- Feed it the Step-2 brief, not a one-liner. Generate 1–2 candidates per slot; pick the one whose light and negative space fit.

**If no generation tool is available**, source from free stock (Unsplash-grade) using the same brief — but treatment then matters *more*, because untreated stock is the fastest way to look generic.

**Then treat every image so it belongs to the brand** — this is the non-negotiable step that turns a picture into design:

- **Tone it to the palette.** Duotone or color-grade toward the brand (e.g. shadows → Deep Forest, highlights → Bone/Sand, a persimmon glow in one spot). A CSS approach works well and stays editable: put the image in a container, overlay the brand color with `mix-blend-mode: multiply` / `soft-light` / `color`, or use an SVG `<feColorMatrix>`/duotone filter. ffmpeg can bake a duotone/grade for a static asset.
- **Add grain/texture** to kill digital flatness (a subtle noise overlay via a tiled PNG or an SVG `feTurbulence`).
- **Create depth** — mask the image under text with a gradient scrim so copy stays AA-legible (this is both a design move AND the contrast fix), or let it bleed behind a translucent panel.
- **Optimize like production media** — WebP, ≤1920w, lazy-load below the fold; a hero over ~300KB is a defect. If a short motion loop is used, ffmpeg → h264, CRF ~26, muted, faststart, under ~600KB.

The treatment is what makes generated imagery feel *authored by this brand* rather than *pasted from an AI*. An untreated image is not done.

---

## Step 4 — Compose for depth, not decoration

When placing treated imagery in the build:

- **Layer.** Foreground copy, a mid layer (translucent panel / scrim), a background image plane. Depth comes from layers, not from one flat photo.
- **Bleed and crop confidently.** Full-bleed edges, decisive crops, and imagery that runs under or behind type read as designed. Timid centered thumbnails read as templated.
- **Let one image carry the page.** A single hero treated with real craft, plus texture elsewhere, beats an image in every section. Restraint is the signature.
- **Every image earns its place** by creating mood or depth toward the conversion goal — never as filler. If it's decoration, cut it (Constitution §8 applies to imagery too).

---

## Graceful degradation

- **No generation tool + no stock access:** fall back to a fully **procedural** signature (CSS/canvas/SVG texture, gradient-mesh-free depth via layered flat planes, generative grain). The page must still feel designed — procedural restraint is a valid art direction, not a failure. Say that imagery was procedural, not generated.
- **Generation tool present but a slot fails:** treat the ones that succeeded, make the failed slot procedural, never ship a broken/placeholder image box.
- **Never invent a real thing** — no fake logo, and no generated image of a *real person* (especially not the user's face unless they supplied real headshots). Generated imagery is for atmosphere/objects/abstraction, not fabricated proof.

---

## Self-check before handing to the build

- [ ] A named visual concept exists (world + depth strategy + restraint line), not just "add images."
- [ ] Every image was specced as a real brief with planned negative space — not "a photo of X."
- [ ] Every image is TREATED to the brand (toned + grain + depth), not raw stock/AI output.
- [ ] Imagery creates depth via layering, bleed, and scrims — not flat decoration.
- [ ] Assets optimized (WebP/h264, weight budget); text over imagery still passes AA.
- [ ] Nothing invented (no fake logo, no fabricated person); degraded gracefully if a tool was missing.
