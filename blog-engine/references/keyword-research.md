# Keyword Research

This is the engine's center of gravity. A post earns its place by targeting a real search someone is typing when they need help. Do this step properly before any writing.

You do **not** need an expensive tool for this. A small or solo site wins on long-tail, question-shaped, intent-rich keywords, and those are findable for free. Use the cheapest path that gives you a confident primary keyword and a real question cluster.

## Default: the free, native path (works anywhere, including Claude Code)

This is the recommended path. It needs no browser, no login, no paid tool, and runs entirely inside Claude Code (or Cowork) using bash + web search. Use it unless the user has a paid keyword tool connected.

**Step A — Pull the keyword + question cluster from Google's free Autocomplete endpoint.** This is a public JSON endpoint. Run it with the seed term, then with question prefixes to expand:

```bash
# core expansion
curl -s "http://suggestqueries.google.com/complete/search?client=firefox&q=SEED+TERM"
# question + intent expansion (repeat with each prefix)
for p in "how to" "what is" "best" "why" "how can" "are"; do
  curl -s "http://suggestqueries.google.com/complete/search?client=firefox&q=$(echo "$p SEED TERM" | sed 's/ /+/g')"
done
```

Each call returns the seed plus ~10 real autocomplete suggestions. Run a few seeds and prefixes and you have the full long-tail + question cluster (the questions become your H2s and FAQ). Replace `SEED TERM` with the topic, URL-encoded with `+` for spaces.

**Step B — Judge demand and competition with web search.** Use Claude Code's built-in web search to read the top 3–5 ranking pages for the primary term: note their H2s, their FAQs, their depth, and how strong the sites are. This tells you the angle to beat and roughly how winnable the term is.

**Step C — (Optional, free, highest-value) Google Search Console.** If the user has a site with traffic, pull or paste their Search Console queries and target the ones ranking positions 5–20 (the fastest wins). Paste-in works; the GSC API works too if wired.

**What you get:** the real keyword cluster, the exact questions people search, the long-tails, and a read on competition. **What you don't get:** precise monthly search-volume numbers or a difficulty score. For most blog decisions that's fine, since intent and the question cluster drive the post. Label volume as "estimated" in the brief and move on.

## Other paths (optional upgrades)

Only reach for these if the user wants hard volume/difficulty numbers or has a tool already.

**Free, more numbers (browser, no install):** the native path gives you the cluster but not volume. If the user wants free volume estimates too, **Google Keyword Planner** (free with a Google Ads account, volume in ranges) and **AnswerThePublic / AlsoAsked** (freemium, a few searches a day, nice question visualizations) are worth a manual look. **Google Search Console** stays the highest-value free source for a site with traffic.

**Cheap paid tool (for hard volume + difficulty in one place):** pick ONE.
- **Keywords Everywhere** — ~$84/yr (~$7/mo), pay-as-you-go credits, browser extension. Cheapest, lowest friction.
- **Ubersuggest** — $12/mo, real free tier (3 web searches/day, ~40/day via the Chrome extension). No public API, so use it browser-in-the-loop or paste-in (see the section below). Good budget all-in-one.
- **Mangools KWFinder** — $29/mo. Friendliest difficulty score for a non-SEO.

**API that runs inside Claude Code (automatable, cheap or free-tier):** for real volume numbers without leaving Claude Code.
- **SerpApi** — free tier (~100 searches/mo), then paid. Returns autocomplete, related questions, and SERP data via API (curl).
- **DataForSEO** — pay-per-call (fractions of a cent per query), real volume + difficulty, MCP servers exist. Best cheap automation path.

**Premium (optional):** **Ahrefs / Semrush** (~$129–140/mo) only if the user wants pro-grade competitive data and will pay. Overkill for a solo site's blog.

**Detect what's connected first.** If any keyword MCP/API (DataForSEO, SerpApi, Ahrefs, Semrush, etc.) is already wired in, use it for real numbers. Otherwise run the free native path at the top. Never claim a tool is missing without checking what's connected.

## Using Ubersuggest (browser-in-the-loop)

Ubersuggest has **no public API or webhooks**, so it can't be cleanly wired to an MCP. The free tier is fine if used the right way:

- **Free web account = 3 searches/day.** A "search" is one report (one seed keyword or one domain), and each returns the keyword plus a small cluster of related ideas with volume + difficulty (free shows ~10 suggestions; paid shows 300+). So it's 3 lookups per day, not 3 keywords total.
- **Free Chrome extension = ~40 searches/day** — far more headroom than the web account. Prefer the extension for keyword work.

Two clean ways to run it inside this engine:

1. **Browser-in-the-loop (recommended, "live").** If Claude-in-Chrome (browser control) is available and the user is logged into Ubersuggest, drive it directly: open Ubersuggest (or trigger the extension on a Google search for the seed term), read the keyword table off the page (keyword, volume, difficulty, related ideas, and the questions), and load those into the keyword brief. Respect the daily free limit — pick the 1–3 most valuable seed searches rather than burning lookups. Real numbers, no API, no copy-paste.
2. **Paste-in (simplest).** The user runs the seed search in Ubersuggest, copies the keyword table, and pastes it in. Structure the brief and post around it.

If hands-off, automated keyword data inside the workspace is the goal, Ubersuggest can't do it — use DataForSEO (Tier 2) instead.

## What to pull, whatever the tool

You want the same five things every time:
1. **Primary keyword** — the phrase the post targets, with volume + difficulty if the tool provides them. Prefer **moderate-volume, lower-difficulty, long-tail, question-shaped** terms a solo site can realistically rank for. ("How to rebuild trust after emotional withdrawal" beats "relationships.")
2. **Secondary keywords / entities (3–6)** — related terms and named concepts to weave in (attachment styles, "secure attachment," "emotional flooding," "bids for connection").
3. **The question cluster (4–8 real questions)** — straight from PAA / AnswerThePublic / AlsoAsked / Search Console. These become the H2s and the FAQ.
4. **Search intent** — informational, comparison, or ready-to-buy/book. Sets how hard the CTA pushes.
5. **The one extractable answer** — a self-contained 2–3 sentence answer to the primary question that an AI engine could quote.

If a tool needs an input you don't have (the Search Console login, a region, an API key), ask the user for that one thing rather than guessing.

## Note: the free native path IS the no-tools path
The "Default: free, native path" section at the top (Autocomplete endpoint + web search + Search Console) is the zero-cost, zero-install method. It's the same approach a paid tool replaces, just without the volume number. Use it directly rather than treating it as a last resort.

## The keyword brief (deliver this every time)

```
PRIMARY KEYWORD:  [phrase]   (vol: __ / difficulty: __  — or "estimated")
SECONDARY (3–6):  [phrase], [phrase], [entity], …
QUESTION CLUSTER (4–8 real questions → become H2s + FAQ):
  - …
SEARCH INTENT:    informational | comparison | ready-to-book
EXTRACTABLE ANSWER (2–3 sentences an AI engine could quote verbatim):
  …
INTERNAL-LINK TARGET(S): [service or course this post should funnel to]
CONSULT CTA STRENGTH: soft (top-of-funnel) | direct (high intent)
SOURCE/TOOL USED: [Search Console / Keyword Planner / Ubersuggest / fallback / …]
```

Confirm the primary keyword with the user, then write. Everything in Step 3 is built on this brief.

## Keyword instincts (small / solo sites)
- Favor **long-tail, specific, question-shaped** terms. That's where a small site wins and where AEO/GEO lives.
- **Local / buyer-intent terms** (e.g. "[service] near me," "online [service]," "[tool] for [audience]") convert hardest. Flag these; they're close to the sale.
- **Mine Search Console for "almost-ranking" queries** (positions 5–20) — the fastest wins are posts that strengthen pages the site is already near page 1 for.
- Map most posts to an offer or service so ranking traffic has somewhere to go (see the active profile's funnel map).
