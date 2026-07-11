# Living Workspace Agents

**AI employees you install once and put to work.**

This is a collection of installable AI agents (Claude calls them "skills") that do
real jobs in your business, end to end, on your say-so. Drop one into your AI
workspace and it stops being a chat you have to babysit and becomes a worker that
runs a whole workflow for you.

Built by [Gabriel Omat](https://gabrielomat.com) as part of teaching people to set
up their own **Living Workspace** — an AI setup that actually knows your business
and does the repeatable work with you instead of waiting on you.

---

## What's inside

| Agent | What it does |
|-------|--------------|
| **blog-engine** | Writes a search-optimized blog post in *your* voice, end to end: keyword research → draft → verified non-competing source links → an FAQ-schema'd, AI-search-ready post. It learns your business from your own workspace, so the post sounds like you, not like a template. |
| **social-media-manager** | Turns one piece of long-form content (a transcript, video, or post) into a full week of on-brand social posts — written in *your* voice, rendered as branded image cards + a Reel, and scheduled as drafts. On first run it builds your **Social Design System** from example images you upload; after that every week is automatic. It stops for your approval before it builds anything. |
| **youtube-content-team** | Runs your whole YouTube pipeline in one pass: mines trending topics in your niche → picks the best video idea for your business → writes the filmable script in *your* voice → designs two branded thumbnails **with your face in them**. On first run it collects a few of your headshots and your thumbnail-brand look; after that every video is one command. Works out of the box (trend research via web search) and upgrades to a real YouTube-API feed if you set one up. |
| **money-manager** | Your AI bookkeeper *and* financial advisor. Connects to your financial data (Era, QuickBooks, or any trusted MCP), keeps a clean set of books, and shows you a **branded profit-and-loss dashboard** — revenue, expenses, margin, month over month. It flags unusual spend, narrowing margins, and recurring subscriptions worth cutting, and advises where your money should go. On first run it figures out where you're starting from (existing books to reconcile, messy data to organize, or from scratch) and sets you up. It analyzes and recommends — it **never moves money, cancels anything, or files taxes.** |
| **landing-page-builder** | Builds one production-grade **landing page** in *your* brand and voice — sales page, opt-in, workshop registration, waitlist — then does what most tools skip: it **renders the page in a real browser, critiques its own screenshots** like a hostile design director (widows, weak contrast, dead zones, anything that smells like an AI default), and rebuilds across three passes before handing you a live preview. Copy is written to convert using real direct-response craft and buyer psychology, routed through your brand-voice skill when you have one — persuasive, never hard-sell. On first run it learns your business and saves your profile; after that every page just reads it. |
| **lead-manager** | The follow-up team you never had. Mines the warm people **already in your world** — your email list, community, event attendees, past clients — into one **Lead Ledger**, scores who's warmest (rules, not vibes), and hands you a small weekly batch of personal outreach drafts in *your* voice, each referencing what that person actually said. You approve and send — **it never sends anything itself.** On first run it interviews you (your pools, your offers, your rhythm) and builds the ledger; after that it's a 15-minute weekly ritual that turns an audience you already paid to attract into conversations. |
| **sales-call-copilot** | Your AI sales team working every call you take. Feed it a call transcript and you get a structured **debrief**, an honest **coaching scorecard** (seven fixed dimensions, every score citing the transcript, one thing to fix next call), and the **follow-up email drafted in *your* voice within the hour**. Before your next call it hands you a one-page **brief** from the deal's own history so you never walk in cold; when a call earns it, it drafts the **proposal from the prospect's own recorded words** with your real pricing. A living pipeline tracks **who's waiting on what** — and as calls stack up, so does the coaching: objection playbook, buyer-language swipe file, cross-call trends. It works after the call, never during — and **it never sends anything itself.** |
| **nurture-sequence-builder** | Your AI email funnel team. Tell it **what kind of funnel you're building** — lead-magnet welcome, webinar/workshop follow-up (attendee / non-buyer / no-show branches), launch, application, re-engagement, post-purchase, or custom — and it designs the **belief journey first** (where your reader is on the awareness ladder × how warm they are), then writes every email to walk it: one job and one CTA per email, in *your* voice, powered by **your real stories** from a story bank it builds with you and grows every run. Nothing is invented — every story, result, and deadline is one you actually gave it. If your email platform is connected it creates the segment and loads the sequence as **drafts**; otherwise you get a paste-ready package with subject-line variants and a timing plan. **It never sends or activates anything** — you flip the switch. |

More agents coming. Each one is self-contained and user-agnostic — it adapts to
whoever installs it.

---

## How to install (2 minutes)

These agents are files that live in Claude's skills folder. "Installing" just means
copying them there. Two ways:

### Option A — the install script (easiest)
```bash
git clone https://github.com/gabeomat/living-workspace-agents.git
cd living-workspace-agents
bash install.sh blog-engine
```
That copies the agent into `~/.claude/skills/` so it's available in every Claude
session. Run `bash install.sh` with no name to see what's available.

### Option B — copy it yourself
Copy the agent's folder (e.g. `blog-engine/`) into `~/.claude/skills/`. That's it.

Then start a new Claude session and the agent is available — just describe what you
want ("write me a blog post about X") and it runs.

---

## Make it *yours*

Every agent here is **user-agnostic** — it doesn't assume whose business it is. What
makes it yours is running it in *your* workspace, where Claude can see your files,
your brand voice, and what it already knows about you.

For the blog-engine specifically: it works with zero setup (it infers your business
from context), but you can make it sharper by creating a **profile**. Copy
`blog-engine/references/profiles/_TEMPLATE.md`, fill in your business/audience/voice,
and save it. The agent loads it automatically. See the fictional
`example-fictional-coach.md` for a filled-in example.

For the social-media-manager: the first time you run it, it walks you through a quick
**design onboarding** — you show it a few example images of the look you want, and it
builds your **Social Design System profile** (your colors, fonts, layouts, weekly post
mix, and scheduler). After that, every run reads that profile and just goes. You can also
set it up by hand: copy `social-media-manager/references/profiles/_TEMPLATE.md` to
`references/profiles/<your-business>.md` and fill it in. It's sharpest when you also have
a **brand-voice skill** so captions sound like you.

For the youtube-content-team: the first time you run it, it walks you through a quick
**thumbnail onboarding** — you drop 2–4 of your own headshots into `assets/headshots/`
(varied expressions) and tell it your thumbnail-brand look. It saves that as your YouTube
profile, and after that every video is one command: it researches trends, picks the idea,
writes the script in your voice, and makes two thumbnails with your face. Trend research
works out of the box via web search; if you set up a YouTube Data API feed it'll use that
instead. Thumbnails auto-generate when `gpt-image-2` is available (see below) — otherwise
it hands you the two finished prompts to paste into ChatGPT yourself.

For the money-manager: the first time you run it, it runs a quick **intake** to find out
where you're starting from — you have a bookkeeper and clean books (it reconciles and
continues your structure), you have messy data (it organizes it), or you're starting from
scratch (it builds your books). It keeps a clean bookkeeping spreadsheet as the source of
truth and reads your financial data from a connected source — **Era** (recommended),
**QuickBooks**, or any trusted financial MCP you connect to Claude. That connection is the
one real requirement for automatic books; without it, it works from a CSV export or figures
you provide. Then it shows you a branded P&L dashboard and, when you ask, digs into your
spend. It **never moves money or cancels anything** — it tells you what it sees and what it
would do; you decide.

For the landing-page-builder: the first time you run it, a quick **setup** pulls your brand,
voice, audience, and offer from your workspace (and asks only for what it can't find), then
saves your profile — after that every page just reads it. Each page starts from a real
art-directed brief (concept, palette, type, one signature technique) so it never defaults to
a generic template, and the copy runs on direct-response structure routed through your
**brand-voice skill** when you have one. To run its screenshot-critique loop it uses
**Playwright** (headless Chrome), which installs automatically the first time in Claude Code /
the desktop app — you just approve. Only a locked-down, no-code environment can't render;
then it builds carefully and tells you the pixel-review passes couldn't run there. It builds
**one page at a time** and hands you a live preview to ship on your say-so — it doesn't
auto-publish.

For the lead-manager: the first time you run it, a quick **onboarding interview** maps where
your people already live (email list, community, events, past clients — one pool is enough to
start), your offers (an entry offer for cold people, your core offer, a premium offer reserved
for warm people), and your weekly rhythm — then it builds your **Lead Ledger**. After that:
drop any export into `leads/inbox/` and say "feed the ledger." Extraction happens once per
file on a lightweight model, scoring runs as a plain script (no AI guessing, no token cost),
and each week you get a small batch of personal drafts in your voice, each tied to something
that person actually said. No connector required — everything works from exports you can
already download. It drafts; **you** send. A **brand-voice skill** is recommended so the
messages sound like you.

For the sales-call-copilot: the first time you run it, a quick **onboarding interview** maps
how you sell — your offers and real prices (proposals only ever quote these), how a deal
usually goes, your known objections, and how your calls get recorded — then it builds your
`sales/` pipeline, capturing any deals already in flight. After that: drop a transcript into
`sales/inbox/` and say "debrief my call." Each transcript is read **once** on a lightweight
model and distilled into a deal file; every later brief, proposal, and pipeline check reads
the distillation, which is what keeps it cheap at any volume. Any recorder works (Zoom,
Fathom, Meet, Otter — export or paste; typed notes too); no connector required. It coaches
honestly, drafts in your voice (**brand-voice skill** recommended), and never sends anything
— you approve, you send. Pairs naturally with the lead-manager: closed-lost prospects hand
across to its ledger for long-term nurture.

For the nurture-sequence-builder: the first time you run it, a quick **onboarding interview**
captures your offers and real prices, your platform and voice — and then banks your first
**3–5 real stories**, each tagged by the belief it shifts. After that, any build starts with
one question: *"what kind of funnel are you building?"* It designs the architecture first
(awareness stage × temperature decide length, pacing, and what each email must accomplish),
gets your yes, asks for any fresh stories, then drafts — strategy in the main session, email
copy on a mid-tier model, subject-line variants on a cheap one. Stories and offers live in
your files, never in the agent, so new wins and new offers mean fresh sequences from the same
machine. If your email platform is connected to Claude it loads the sequence as **drafts** and
builds the segment; otherwise you get a paste-ready package any platform can absorb. It never
sends — you activate. A **brand-voice skill** is recommended so every email sounds like you.

---

## What you'll need

- **Claude** (Claude Code, the desktop/web app with skills, or any setup that loads
  skills from `~/.claude/skills/`).
- For the blog-engine's **automatic hero images**: an image tool. It prefers
  `gpt-image-2` (uses your ChatGPT subscription, no API key) and falls back to
  `nano-banana` (needs a Gemini API key) — or it'll hand you the image prompt to run
  yourself. Image generation never blocks the writing.
- Everything else (keyword research, writing, link-checking) runs with no extra
  tools or accounts.
- For the **social-media-manager**: to render the branded image cards and Reel video,
  it uses **Playwright** and **ffmpeg**. In Claude Code or the desktop app it installs
  these for you automatically the first time — you just approve when asked, no setup on
  your end. (Only if your environment blocks installs — a locked-down work laptop, or a
  plain chat with no code execution — will it hand you the HTML to render elsewhere
  instead.) To auto-schedule, it uses a connector like **Metricool** (its default); with
  no connector it hands you a ready-to-post schedule. A **brand-voice skill** is
  recommended so captions sound like you (it works without one, but the copy is more generic).

---

## A note on how publishing works

The blog-engine writes and prepares the post. If you want it to publish straight to
a real website, that part is specific to *your* site (your repo, your host), so it
lives in a small command you set up for your own setup — not in the shared agent.
The agent's job is to produce a publish-ready post in your voice; wiring it to your
live site is a short follow-on step.

---

## License

Proprietary — see [LICENSE](LICENSE) for the full terms. In short:

- ✅ **Use them** in your own business and in work you do for your clients.
- ✅ **Sell the output** you create with them (e.g. posts you write for clients).
- ❌ **Don't resell or redistribute the agents themselves** as your own product,
  template, or library.
- ⚠️ **Provided "as is," with no warranty.** You're responsible for reviewing any
  AI output before you publish or rely on it. The author isn't liable for how the
  agents are used. (This isn't legal advice; your own program's terms still apply.)

---

Questions or want help setting up your Living Workspace? → [gabrielomat.com](https://gabrielomat.com)
