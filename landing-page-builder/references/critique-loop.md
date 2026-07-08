# The Critique Loop — render, look at the pixels, fix, upgrade

This is the engine that turns "plausible output" into design judgment. Code review cannot see a widow, a muddy button, or a dead zone. **Only rendering the real page and looking at the pixels can.** Closing that loop — written code → rendered screenshot → the agent's own hostile critique → fix → repeat — is the single most important thing this agent does.

**Non-negotiable: every page goes through at least THREE full critique passes before it ships.** Not "until it looks fine after one." Three, minimum, each ending in real changes.

---

## One pass = four steps

### Step A — Render the real page in a real browser

Serve the page locally and screenshot it headless, at both **desktop (1440×900)** and **mobile (390×844)**, at **top / mid-scroll / bottom**, capturing console errors and document height.

Use the tiny harness below (`shot.js`). Dependency: **Playwright** (Chromium). This mirrors the render story in `social-media-manager` — in Claude Code or the desktop app, install it on the fly the first time (the user just approves); it is not something they set up in advance. Only if the environment genuinely blocks installs do you fall back to hand-off (see the bottom of this file).

```js
// shot.js — the whole harness. Run: node shot.js <url> <out.png> [WxH] [waitMs] [scrollY]
const { chromium } = require('playwright');
(async () => {
  const [,, url, out, size='1440x900', waitMs='2500', scrollY='0'] = process.argv;
  const [w,h] = size.split('x').map(Number);
  const errors = [];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport:{ width:w, height:h }, deviceScaleFactor:2 });
  p.on('console', m => { if (m.type()==='error') errors.push(m.text()); });
  p.on('pageerror', e => errors.push(String(e)));
  await p.goto(url, { waitUntil:'networkidle' });
  await p.waitForTimeout(Number(waitMs));
  if (Number(scrollY)>0) { await p.evaluate(y=>window.scrollTo(0,y), Number(scrollY)); await p.waitForTimeout(600); }
  const docHeight = await p.evaluate(()=>document.body.scrollHeight);
  await p.screenshot({ path: out });
  console.log(JSON.stringify({ out, docHeight, errors }));
  await b.close();
})();
```

Serve the folder first (e.g. `npx serve -l 4179 .` or any static server), then:

```
node shot.js http://localhost:4179/ top.png     1440x900 3000 0
node shot.js http://localhost:4179/ mid.png     1440x900 3000 <docHeight/2>
node shot.js http://localhost:4179/ bottom.png  1440x900 3000 <docHeight>
node shot.js http://localhost:4179/ m-top.png   390x844  3000 0
node shot.js http://localhost:4179/ m-mid.png   390x844  3000 <docHeight/2>
node shot.js http://localhost:4179/ m-bottom.png 390x844 3000 <docHeight>
```

`errors` in the output MUST be empty. If it isn't, that's the first thing you fix — a page with console errors is not shippable (Constitution §6).

**Harness note (learned under load):** if a screenshot call hangs, pin the stable render mode and give animations a fixed settle time rather than racing them. For GPU/particle scenes that warm up, start the clock later (a longer `waitMs`) instead of screenshotting a half-built frame.

### Step B — Look at the pixels like a hostile design director

Actually **read the screenshots with vision.** Do not critique the code — critique the rendered image. Be the meanest art director you've worked with. Hunt specifically for:

- **Widows & orphans** — a headline breaking mid-word, one lonely word on its own line.
- **Contrast failures** — a CTA or headline you have to squint at. If you're not sure it passes AA, it fails.
- **Alignment & rhythm** — things that don't line up to a grid; inconsistent spacing; a section that's cramped next to one that's loose.
- **Dead zones** — a hero corner that's empty and lifeless; a fold with nothing pulling the eye down.
- **Copy drowning** — text competing with artwork/gradient so it can't be read.
- **The AI-default smell** — centered everything, a purple gradient, three evenly-spaced feature cards, a generic hero-then-features-then-CTA with no point of view. If it looks like every other AI landing page, it fails.
- **Flatness / no art direction** — the whole page is evenly-lit flat blocks with no depth, texture, or imagery. Brand-correct but lifeless. A page can pass every color rule and still look undesigned; that's a defect (Constitution §8).
- **Untreated imagery** — a photo that reads as raw stock or default AI output, sitting *on* the brand instead of *in* it (wrong palette, no grain, no scrim, hard rectangle). If an image wasn't toned/treated to belong, flag it.
- **Conversion leaks** — the primary CTA not obvious above the fold on mobile; competing CTAs; the "one thing this page must prove" not actually proven visually.

Write the findings down as specific, addressable notes ("mid-word break in the H1 on mobile," "the amber CTA on cream is ~3:1, under AA," "bottom third is a dead gray slab"). Vague notes = no fix.

### Step C — Fix everything found

Address **every** finding from Step B. Not the easy ones. All of them. Then re-render (Step A) to confirm each is actually gone in the pixels — not just changed in the code.

### Step D — Add one deliberate complexity upgrade

This is the rule that stops iteration from converging on bland, safe output. On **every** pass, after fixing, add **one** deliberate upgrade that raises the craft:

- a texture or grain that kills flatness
- a purposeful micro-interaction (a hover that rewards, a scroll-triggered reveal with custom easing)
- editorial marginalia, a footnote, a numeral treatment
- a small easter egg or a moment of delight
- a signature detail that makes the page feel authored, not generated

The upgrade must serve the page (and never break the Constitution). One per pass, deliberately chosen — not ten random flourishes.

---

## When is it done? (the stopping rule — bounded, so it can't run forever)

A self-critiquing loop with a forced complexity-upgrade every pass will keep finding "one more thing" indefinitely if you let it — and every pass costs real tokens (each pass reads 6 screenshots with vision, which is the heaviest part of this whole agent). So the stop rule is deliberately bounded:

- **Floor — always run at least 3 full passes.** Non-negotiable. Three is the minimum, even if the page looks clean after one. (This is his standard, and it's what separates a real critique from a rubber stamp.)
- **From pass 3 onward, stop as soon as BOTH are true:**
  1. The Constitution self-check is **all-YES from the rendered pixels** (not from intention), AND
  2. The latest pass surfaced **only cosmetic nits** — no Constitution-level defect (no widow, no contrast fail, no console error, no dead zone, no conversion leak). If the only things left are optional "could add another micro-interaction" upgrades, you're done.
- **Ceiling — never exceed 5 passes.** Hard cap. If you hit pass 5 and a real defect still isn't fixed, stop looping, ship the best rendered version, and **tell the user plainly** what's still imperfect and why — don't silently burn a sixth, seventh pass chasing it. A named limitation beats an unbounded spend.

**"Done" is a property of the screenshots, not a feeling** — but it is also bounded by the ceiling. Between the floor of 3 and the cap of 5, the page is done the moment a pass comes back with nothing material left to fix.

> **Note on the complexity-upgrade rule near the end:** the +1 upgrade (Step D) is what stops early passes from converging on bland safety. But once you're at the ceiling and the Constitution is clean, an upgrade that would risk re-introducing a defect is not worth it — polish should *settle*, not thrash. Prefer shipping a clean pass 4 over a riskier pass 5.

---

## Graceful degradation (never strand the user)

The render step depends on Playwright. Handle a missing/blocked environment like this, in order:

1. **Missing but installable (the normal case — Claude Code, desktop app, any shell):** install Playwright on the fly; the user just approves. Continue the full loop.
2. **Installs genuinely blocked (locked-down machine, or a chat surface with no code execution):** you cannot render here. Do NOT fake the critique. Instead: build the page to the Constitution as carefully as you can *without* pixel feedback, hand over the finished self-contained HTML, and **say plainly that the screenshot-critique passes could not run in this environment** — recommend the user open it in a browser (or run the agent in Claude Code / the desktop app) to get the full loop. Honesty over a hollow "looks great."

Never claim you ran the critique loop if you didn't render the page.
