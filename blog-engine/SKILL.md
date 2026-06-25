---
name: blog-engine
description: Write a complete, search-optimized, publish-ready blog post in the user's brand voice, using an SEO/AEO/GEO-first pipeline where keyword research drives the post. Adapts to whoever runs it — it learns the user's business, audience, and voice from the workspace it's in (files, memory, connected context), and can load an optional saved profile if one exists. Use whenever someone wants to write, draft, plan, or create a blog post, article, or website post; gives a topic, keyword, or rough idea to turn into a ranking post; or says "write a blog," "blog about," "I need a post on," "turn this into a blog," "what should I blog about," or any variation. Runs a five-step pipeline (trending, keyword research, write, humanize, images) and can run the whole chain or jump in at any step.
---

# Blog Engine

A blog is not content. It is a **discovery and client-acquisition channel.** Every post exists to get found by someone searching, and to move them one step closer to a yes. So this engine is built SEO/AEO/GEO-first: the keyword and the question come **before** the writing, and the structure is built to rank in Google *and* get quoted by AI answer engines (ChatGPT, Google AI Overviews, Perplexity, Gemini).

The engine is **user-agnostic and context-driven.** The pipeline, structure, keyword research, and humanizing are the same for everyone. What makes a post *theirs* is the business layer — audience, topics, voice, funnel, CTA, trust rules — and the engine learns that from **wherever it's running**, not from a hardcoded identity. Run it in a user's own workspace and it writes as them; run it somewhere else and it adapts to that user. The skill never assumes whose blog this is.

## Step 0 — Establish the user (always do this first)

Figure out who the post is for and load their business layer, in this order of preference:

1. **A saved profile, if one matches.** Check `references/profiles/` — if a profile clearly fits the current user/site, read it and defer to it (it names the voice source, funnel, CTA, trust rules). Saved profiles are an optional accelerator, not a requirement, and the set is open-ended; never assume a specific person.
2. **The surrounding context.** If no profile fits, infer the user from what's available in the environment: workspace files (an `About` page, brand/voice docs, existing posts, a CLAUDE.md, a site repo), connected memory or knowledge about the user, and anything the user's preferred AI already knows about them. This is the normal case and it's the whole point — the skill pulls identity from where it's being used.
3. **Ask, briefly.** If context is thin and no profile fits, ask a few quick questions (whose site, audience, topics, voice source, funnel/CTA, trust rules) and offer to save the answers as a new profile in `references/profiles/` for reuse. Then proceed.

Whatever the source, lock these before writing: **who the audience is, the voice to write in, the funnel/CTA, and the trust/privacy rules.** If a voice source is named (a profile, a voice skill, brand docs), defer to it.

## The pipeline

```
1. TRENDING / TOPIC   →  what to write about (demand + relevance)
2. KEYWORD RESEARCH   →  the exact phrase + question cluster to win
3. WRITE              →  the post, structured to rank + get quoted (sourced facts only)
4. HUMANIZE           →  strip AI tells, lock in the profile's voice
4.5 VERIFY LINKS      →  every link live + non-competing; receipts (hard gate)
5. IMAGES             →  on-brand hero (from saved spec) + body images
6. PUBLISH            →  build, PR, working preview → human review → ship on say-so
```

Run the whole chain by default, or start at whichever step is asked for. Always say which step you're on. Never skip keyword research — it's the difference between a post that ranks and a diary entry. If a finished keyword is handed to you, confirm it and skip to Step 3, but still pull the question cluster in Step 2.

---

## Step 1 — Trending / topic selection

Pick a topic with **real search demand** that sits squarely in the profile's territory.

- If a topic, keyword, or question is already given, use it and move to Step 2. Don't re-interview.
- If ideas are wanted, find what's being searched and discussed now: web-search recent trends and seasonal angles, and mine the profile's own demand signals (its named topics, courses/offers, recurring audience questions).
- Offer **3–5 angles**, each with a one-line reason it's worth writing now (search demand + how it feeds the profile's funnel). Let the user pick before you spend effort researching.

Choose well, not fast. Don't write yet.

---

## Step 2 — Keyword research (the part that makes it SEO)

This step leads. Full instructions and the tool tiers: `references/keyword-research.md`.

Use the cheapest path that yields a confident primary keyword and a real question cluster:
1. **Default — the free, native path (works anywhere, including Claude Code, no browser or login):** pull the keyword + question cluster from Google's free Autocomplete endpoint via `curl`, judge demand/competition with web search, and (if available) mine Google Search Console for the site's "almost-ranking" queries. See `references/keyword-research.md` for the exact commands. Gives the full cluster; volume is estimated, not exact.
2. **Optional upgrades (only if hard volume/difficulty numbers are wanted):** a cheap tool (Ubersuggest, Keywords Everywhere ~$7/mo, Mangools $29/mo) or an API that runs in Claude Code (SerpApi free tier, or DataForSEO pay-per-call). Ahrefs/Semrush only for pro-grade needs.
3. **If a keyword MCP/API is connected,** detect and use it for real numbers. Otherwise run the free native path. Say which path you used.

Deliver a **keyword brief** (primary keyword + secondary/entities + the 4–8 question cluster + intent + the one extractable answer + internal-link target) and get a quick yes on the primary keyword before drafting.

> **Runs end-to-end in Claude Code.** With the free native keyword path (this step) plus the `gpt-image-2` image step, the whole pipeline runs in one place, free: keyword research → write → humanize → images. No browser dependency, no paid tool required.

---

## Step 3 — Write the post

Build on the keyword brief. Structure and on-page rules: `references/seo-aeo-geo-structure.md`. Voice: the source named in the active profile (read it before writing).

Non-negotiables every post:
- **Answer-first.** The intro answers the primary question in the first 2–3 sentences (the extractable answer), then earns the depth below.
- **Question-based H2s** drawn from the cluster, phrased the way people search.
- **Primary keyword** in the title, first ~100 words, one H2, and the meta description, naturally.
- **E-E-A-T discipline** per the profile (author authority, real sources; extra-strict for YMYL profiles like Couples Learn).
- **Sourced facts, no fabricated links.** Research factual claims (prices, stats, capabilities, dates) on the live web — never from memory — and cite them. Every link must point to a real, currently-live page; never guess a URL slug. Link only to safe, non-competing sources (primary toolmakers like OpenAI/Anthropic/Google, neutral institutions, non-competing thought leaders); **never link a competitor or similar product.** Full rules: `references/link-and-source-policy.md`. Read it before adding any link.
- **An FAQ block** (3–5 cluster questions, 2–4 sentences each) — the highest-leverage AEO element.
- **Internal links** to the profile's relevant offer + a **CTA matched to intent** (the profile names the offer ladder and CTA).
- **Length follows the keyword,** usually ~1,500–2,200 words, never padded.

Deliver a markdown file plus a **publishing kit**: 3 title options, meta description (<=155 chars, keyword in front), URL slug, the FAQ in clean Q/A form, FAQ schema (JSON-LD) when useful, and the internal-link list.

---

## Step 4 — Humanize

Switch to editor mode: strip every AI tell and lock the profile's voice. Run `references/humanize-checklist.md`, applying the voice source named in the active profile. Then re-verify the SEO structure survived the edit (keyword placement, question H2s, FAQ intact).

---

## Step 4.5 — Verify links & sources (gate before publishing)

Do not ship a post with a dead or fabricated link. Before images/publishing, run the full `references/link-and-source-policy.md` check:

1. Extract every external `href` in the post.
2. Confirm each resolves (`curl -s -o /dev/null -w "%{http_code}" -L -A "Mozilla/5.0 ..." URL`). `200` or a clean redirect = pass; `404`/`410`/`000` = fix.
3. Handle bot-block false negatives: if a normally-authoritative source fails curl (often `000`/`403`), re-verify with a browser-grade fetch (Firecrawl scrape or a real browser) and trust only a confirmed live `200` + sane title.
4. Confirm no link points to a competitor or similar product (per the active profile).
5. Report each link's verified status in the publishing kit — receipts, not promises.

If any factual claim has no live, non-competing source, fix the claim or cut it. This step is a hard gate.

---

## Step 5 — Images

Generate images at blog dimensions (a hero, plus body images if the profile uses them), matched to the profile's visual tone.
- **Use the profile's stored hero/brand image spec if it has one** (e.g. a `blog-hero-spec.md` in the site repo). A saved spec means you generate on-brand automatically — the user should NOT have to hand you a reference thumbnail each time. If no spec exists, offer to capture one from a reference the user provides, then save it for reuse.
- **Preflight the image tool before relying on it:** `gpt-image-2` needs `codex` + `python3` (uses a ChatGPT subscription, no API key). `nano-banana` needs `GEMINI_API_KEY` set (often it is NOT — check first). If neither is usable, hand off the prompt + an Unsplash term and proceed. **Never block publishing on the image step.**
- After generating, **read the image back** to confirm any on-image text spelled correctly.
- Always add descriptive **alt text** with the topic keyword.

---

## Step 6 — Publish (if the profile has a publishing target)

Some users publish to a real site (e.g. an Astro repo with Netlify auto-deploy that builds a preview per PR). When the user's setup defines a publishing workflow, the goal is **one command → full pipeline → a working preview → human review → ship on the user's say-so.** Encode the user's site-specific mechanics (repo path, host, branch) in a command or profile, not here. The durable, user-agnostic lessons:

- **Don't rediscover the environment.** Pin the live repo path, remote, branch, and that `git`/`gh` are authenticated locally. (A repo can exist twice on disk — one copy may have no `.git`; use the real one.)
- **Branch-first, PR-gated, human-in-the-loop.** Never push to the default branch or merge until the user approves. The deploy preview + their go-ahead IS the approval. Auto-merge attempts on the default branch will (correctly) be blocked.
- **Build-check before pushing** so the host's build doesn't fail on a typo.
- **Verify the preview actually serves the new content** (poll the deploy-preview URL) before handing it over — don't hand over a URL that still 404s.
- **Preview-tool caveat:** a local preview MCP can latch onto a stale cached server; if a screenshot looks wrong, trust the host's preview URL + curl/WebFetch against the built page.
- **Wait, then ship.** Hand over preview URL + PR link + link receipts, then stop. On "push/publish/go ahead," merge and confirm the page is live in production.

---

## How to behave across the run

- **Sequence, don't sprawl.** One step at a time: topic, then keyword, then draft. Confirm and move on.
- **Match the user's level.** Gauge it from context — show the keyword reasoning and structure choices to power users; explain more for newcomers. Don't hand-hold someone who clearly knows their stuff.
- **Confident CTA, never apologetic.** "Book a call" / "start here," not "if you maybe want to, you could possibly reach out." Follow the user's funnel.
- **Privacy.** Public-facing content. Never invent or use real client/member stories or details; composite or general examples only. Respect the user's privacy/trust rules.
