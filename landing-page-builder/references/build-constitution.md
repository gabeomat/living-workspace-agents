# The Build Constitution

This is the non-negotiable build standard for every page this agent ships. The agent **cannot negotiate it away** — not to save time, not because a brief seems to want otherwise, not because a pass is "good enough." If the page violates any rule here, it is not done.

Think of this as the floor, not the ceiling. Briefs raise the ceiling (concept, palette, signature technique). This file sets the floor no page falls below.

---

## 1. Copy is real, and it converts

- **No lorem ipsum. No placeholder. No "[insert benefit here]."** Every word is real, final, and specific to this business's actual offer, audience, and promise.
- Copy is **written to convert**, using the persuasion structure and psychology in `copywriting-engine.md` — not decorated. A beautiful page with weak copy is a failed page.
- Copy sounds like **the user**, not like a template and not like another user. If a brand-voice skill or voice source is available, the copy is passed through it. See `copywriting-engine.md`.
- **No hype the business can't back.** No fake urgency, no invented testimonials, no "join 10,000 others" unless it's true. Honesty is a conversion asset, not a constraint.

## 2. Type is distinctive

- **Never** the default system stack as the design choice. A page's typography is art-directed in its brief (a display face + a readable text face, real pairing, real hierarchy).
- Real typographic hierarchy: a clear scale, deliberate line-height and measure (45–75 characters per line for body), no muddy same-size blocks.
- **No widows or orphans** in headlines or key lines. A headline that breaks mid-word or drops one lonely word to its own line is a defect the critique pass must catch.
- Fonts loaded reliably (Google Fonts or self-hosted); never depend on a font the user's browser might not have.

## 3. Motion is intentional and custom

- **No default/linear easing** as the motion signature. Motion uses custom easing curves (`cubic-bezier`) chosen to fit the page's feel.
- Motion serves attention and hierarchy — it guides the eye toward the conversion goal. Motion for its own sake is noise; cut it.
- Respect `prefers-reduced-motion`: provide a reduced/no-motion path. Non-negotiable.

## 4. Responsive, genuinely

- The page works and looks **intentional** at mobile (~390px), tablet (~768px), and desktop (~1440px). Not just "doesn't break" — *designed* at each size.
- Tap targets ≥44px. No horizontal scroll on mobile. The primary CTA is reachable without hunting on every viewport.
- Test all three in the critique loop, not just desktop. Most landing-page traffic is mobile.

## 5. Accessible (WCAG AA floor)

- **Text contrast ≥ 4.5:1** (≥ 3:1 for large text). A low-contrast CTA or hero headline is a defect, not a style.
- Semantic HTML: real `<h1>`/`<h2>` order, `<button>`/`<a>` for actions, `alt` on every meaningful image, labels on every form field.
- Keyboard-navigable: visible focus states, logical tab order, the CTA reachable and operable by keyboard.

## 6. Zero console errors

- The rendered page produces **zero console errors and zero uncaught exceptions.** The critique harness captures the console; a page that logs errors is not shippable.
- No broken asset requests (404s), no missing fonts falling back silently, no dead script tags.

## 7. Static, self-contained, fast

- **One self-contained page.** No build step, no framework required. Plain HTML/CSS/JS; libraries (Three.js, GSAP) from a CDN only if the brief's signature technique needs them.
- Assets optimized like production media: images ≤1920w, WebP where possible, lazy-loaded below the fold. A 5MB hero is a defect.
- Loads fast on a mid-tier phone. Performance is a conversion factor, not an afterthought.

## 8. Designed, not just correct — depth and art direction

- The page must have a **point of view and depth**, not just brand-correct colors on flat sections. It should look like a designer made deliberate choices — treated imagery, layering, texture, a signature move — per `art-direction.md`.
- **Any imagery is treated to the brand** (toned/duotoned, grained, masked under scrims) — never a raw stock photo or default AI hero dropped on top. Untreated imagery = the AI-landing-page smell, and it fails.
- **Flatness is a defect.** If the whole page is evenly-lit flat blocks with no depth, layering, or texture, it isn't done — even if every color is on-brand.

## 9. One page, one job

- Every landing page has **exactly one conversion goal** (named in the brief) and one primary CTA repeated at natural decision points. Competing CTAs dilute conversion — cut them.
- Every section earns its place by moving the visitor toward that one action. If a section doesn't, it goes.

---

## The self-check (run before declaring done)

Answer YES to all — with evidence from the rendered page, not intention:

- [ ] Copy is real, specific, conversion-structured, and in the user's voice — no placeholder anywhere.
- [ ] Type is distinctive with real hierarchy; no widows/orphans in headlines.
- [ ] Motion uses custom easing and honors reduced-motion.
- [ ] Designed (not just unbroken) at 390 / 768 / 1440.
- [ ] Contrast ≥ AA everywhere; semantic + keyboard-accessible.
- [ ] Zero console errors in the rendered page.
- [ ] Static, self-contained, optimized assets, fast.
- [ ] Designed, not just correct — real depth, treated (never raw) imagery, no flatness.
- [ ] One conversion goal, one primary CTA, every section earns its place.

Any NO → not done. Back to the critique loop.
