# The Page Brief — how to art-direct one page

His system built 25 sites that never converged because each one got a **real, specific brief** — not "make a website." A brief is a set of deliberate constraints that force a point of view. This agent writes one brief per page before building. The brief structure is FIXED; the values in it are PULLED from the user's brand, offer, and audience.

Write the brief, show the key choices to the user, get a nod, then build. Don't skip to building — an un-briefed page defaults to the AI-average, which the critique loop then has to claw back.

---

## The brief format (fill every field with a real, specific choice)

**Page & goal**
- **What page is this?** (sales page / opt-in / workshop or event registration / waitlist / product / service / book-a-call)
- **The ONE conversion goal.** A single action. (e.g. "get the email + register for the July 11 workshop.")
- **The one thing this page must PROVE.** The single job the design + copy exist to accomplish. (e.g. "that this workshop is worth an hour of a busy person's time.") Everything serves this.

**Audience & promise** *(pulled from profile / Brain)*
- **Who is this for**, specifically. Their situation and the language they use.
- **The core promise** — the shift/outcome, in one line.
- **The top 2–3 objections** to dissolve.

**Visual direction** *(pulled from brand; art-directed here)*
- **Concept / mood** — one clear idea the whole page expresses (e.g. "calm authority," "kinetic and bold," "editorial and premium"). Name it.
- **Palette** — the brand colors + how they're used (background, text, one decisive accent for the CTA). Ensure the accent-on-background contrast passes AA.
- **Typefaces** — a display face + a text face (from the brand if specified; a deliberate pairing otherwise). Never the default stack as the choice.
- **Signature technique** — the ONE distinctive craft move that makes this page memorable and un-templated. Pick one that fits the concept and the budget:
  - procedural/free: a subtle canvas flow-field or grain, a scroll-driven reveal with custom easing, kinetic/variable type, an SVG illustration, a CSS-only texture, a well-built interactive element
  - media (only if the business has/needs real assets): a treated hero image, a short muted looping video, a product shot
  - Restraint is a valid signature. One strong move beats five weak ones.
- **Motion feel** — the easing personality (snappy? slow and luxurious?) as a `cubic-bezier` direction, plus the reduced-motion path.

**Assets**
- What real media exists (logo, headshots, product photos)? Use the real thing — never invent a face or a fake logo.
- What's needed but missing? Prefer a procedural/CSS signature over a generated stand-in unless the user has a real image tool connected and wants generated media. If media is generated, treat it like production: optimize (WebP ≤1920w, video h264/CRF~26/muted/faststart).

---

## Briefing discipline

- **One page must prove one thing.** If the brief's "must prove" is fuzzy, the page will be too. Sharpen it first.
- **Constrain to force a point of view.** Naming the palette, the type, and the single signature technique is what prevents the generic hero-features-CTA default.
- **Pull, don't invent, identity.** Colors, fonts, voice, offer, audience all come from the profile/Brain. The brief *art-directs*; it does not fabricate a brand.
- **Confirm the few high-leverage choices** (concept, signature technique, the one goal, the CTA) with the user before building. Everything else you can decide and show in the render.
