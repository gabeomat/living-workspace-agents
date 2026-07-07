# Social Design System Profile — TEMPLATE

Copy this file to `references/profiles/<your-business>.md` and fill it in — or just run the
Social Media Manager agent and let its **design onboarding** build it for you from example
images you upload. This profile is what makes the agent produce *your* look, in *your* voice,
on *your* schedule. The agent reads it at the start of every run.

Delete these instructions once filled in. Anything in `<angle brackets>` is a prompt for you.

---

## 1. Brand Kit (the raw identity)

**Colors** — give each a name, a hex, and where it's used:

| Name | Hex | Used for |
|------|-----|----------|
| <e.g. Ink> | <#1F3A33> | <borders, primary text, dark backgrounds> |
| <e.g. Paper> | <#F0EBE0> | <light backgrounds, text on dark> |
| <e.g. Accent> | <#D65A3A> | <highlights, badges, CTAs> |
| <optional 4th> | <#...> | <panel surfaces / secondary> |

**Fonts** (use Google Fonts so they load via CDN):

| Role | Font | Notes |
|------|------|-------|
| Headline | <e.g. Inter Black 900> | <main statements> |
| Accent | <e.g. Cormorant Garamond italic> | <quotes, pull-quotes> |
| Body | <e.g. Inter 400> | <body copy> |
| Label | <e.g. Inter Medium 500> | <day tags, small labels> |

**Brand mark / wordmark:** <your name or logo text that appears on each card, e.g. "YOUR BRAND">
**Feel words (3–5):** <e.g. bold, grounded, editorial, warm> — the vibe every card should carry.
**Treatment rules (optional but powerful):** <the visual "signature" — e.g. "thick borders, hard offset shadows, square corners" or "soft, airy, lots of whitespace, rounded corners." This is what makes cards recognizably yours beyond color.>

## 2. Post Mix (what a standard week produces)

The default is **3 statics + 2 carousels + 1 Reel, Monday–Saturday.** Change any of it.

| Day | Format | Layout variant | Time | Networks |
|-----|--------|----------------|------|----------|
| Monday | Static | <Layout A name> | <9:00 AM> | <IG + FB> |
| Tuesday | Carousel | <cover + N + CTA> | <9:00 AM> | <IG + FB> |
| Wednesday | Static | <Layout B name> | <9:00 AM> | <IG + FB> |
| Thursday | Carousel | <cover + N + CTA> | <9:00 AM> | <IG + FB> |
| Friday | Static | <Layout C name> | <9:00 AM> | <IG + FB> |
| Saturday | Reel | <5-frame arc> | <12:00 PM> | <IG only> |

**Timezone:** <e.g. America/Los_Angeles>
**Image ratio (statics + carousels):** <default 1080×1350 (4:5)>
**Reel ratio:** <default 1080×1920 (9:16)>

## 3. Static Layouts (your text-on-image variants)

You want a few *distinct* static looks so the same week doesn't repeat itself. Describe each.
(The agent turns these into HTML using your brand kit. See `references/html-render-engine.md`.)

- **Layout A — <name, e.g. "Dark Statement">:** <description: background color, headline treatment, where the accent/highlight goes, any badge/day tag. What content type it suits.>
- **Layout B — <name, e.g. "Numbered Steps">:** <description>
- **Layout C — <name, e.g. "Quote Card">:** <description>

## 4. Carousel Template

- **Cover rule:** <THE important one — e.g. "always a photo of me on the cover slide, headline overlaid" or "bold text-only cover, no photo">
- **Slide structure:** <e.g. cover → N numbered content slides → CTA close slide>
- **Default slide count:** <e.g. 6 (1 cover + 4 content + 1 CTA)>; **range:** <e.g. 6–11>
- **Does it need a supplied photo each run?** <yes/no — if yes, the agent asks you for the photo(s) before writing>
- **Standing CTA(s):** <your default carousel CTAs, e.g. "link in bio," "DM me [word]," "join [offer]">

## 5. Reel Template

- **Frame arc (locked sequence):** <e.g. Hook → Tension → Interrupt → Payoff → CTA>
- **Number of frames:** <e.g. 5>
- **Per-frame look:** <optional: any background/color rules per frame, e.g. "Interrupt frame inverts to accent color">
- **Runtime target:** <e.g. ~15s, 3s per frame with 0.5s crossfades>
- **Silent?** <yes/no — most Reels ship silent and add music natively when publishing>

## 6. Connector (how posts get scheduled)

- **Scheduler:** <Metricool (default) / Buffer / Later / GoHighLevel / manual>
- **Account / profile IDs (if applicable):** <the agent needs these to create drafts; fill in per your tool, or leave blank for manual>
- **Manual mode?** <if "manual," the agent hands you finished assets + a posting schedule instead of creating drafts>

## 7. Voice & Offers (pointers, not duplicates)

- **Brand-voice skill:** <name of your brand-voice skill, if you have one — the agent loads it for the copy pass>
- **Business Brain location:** <where your workspace context lives, so the agent can pull real offers/CTAs>
- **Current priority CTA:** <what you're driving to this season — the fallback CTA if the Brain isn't readable>
