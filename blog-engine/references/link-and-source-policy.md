# Link & Source Policy

Every factual claim in a post needs a real, verifiable source, and every link
in the published post must actually resolve. This is non-negotiable: a single
404 or a fabricated URL destroys trust with both readers and AI search engines,
and it's the fastest way to look careless on the exact topic where the post is
claiming authority.

Research is encouraged. Write factual claims from the live internet, not from
memory. Then **show the receipts** — cite where each fact came from.

## The five rules

1. **Research real sources.** For any factual claim (a price, a stat, a product
   capability, a date, a quote), search the live web and find the actual source.
   Never write a specific number or capability claim from memory — the AI space
   and pricing both move fast, and stale specifics read as sloppy.

2. **Verify every link returns 200 before publishing.** Do not guess URL slugs.
   After drafting, check each external link with an actual request and confirm it
   resolves (HTTP 200, or a clean redirect to a live page). If a link 404s or
   can't be verified, replace it or remove the claim. See "Verification" below.

3. **Give the receipts.** Every post ends with a `Sources Checked` list (the
   house style already supports `.post-sources`). Each external factual claim
   should trace to a source in that list. In the publishing kit, report the
   verification status of each link (the actual status code you saw) so the user
   has proof, not a promise.

4. **Never link to competitors or similar products.** Do not send the post's
   readers to anyone who competes with the person the post is written for. That
   includes direct competitors, similar offers/courses/programs, and any page
   whose call-to-action competes with the profile's funnel. Linking out to a
   competitor is doing their marketing for free. If a competitor is the only
   place a fact lives, paraphrase and attribute the idea in plain text instead of
   hyperlinking, or find a neutral primary source for the same fact.

5. **Safe sources to cite.** Prefer, in this order:
   - **Primary toolmakers** — the company that made the thing. For AI claims that
     means OpenAI, Anthropic, Google/Gemini, and similar model/platform makers
     (their announcements, docs, pricing, model cards). Linking to the toolmaker
     is not linking to a competitor — it's linking to the source.
   - **Neutral institutions & established publications** — QuickBooks/Intuit,
     government and research data, major business/tech journalism (e.g. The
     Verge, Business Insider, Reuters). They don't compete with the profile for
     clients.
   - **Non-competing thought leaders** — credible voices in the space who are NOT
     a competitor to whoever the post is for. A respected researcher or commenter
     is fine; a rival coach/agency selling the same outcome is not. When unsure
     whether someone competes, treat them as a competitor and don't link them.

## Verification (do this before the post ships)

After the draft and humanize passes, before opening the PR / publishing:

1. Extract every external `href` in the post.
2. Check each one resolves. A quick, reliable check:
   ```bash
   curl -s -o /dev/null -w "%{http_code}  %{url_effective}\n" -L \
     -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)" "URL"
   ```
   Treat `200` (or a clean redirect to a live page) as pass; `404`/`410`/`000`
   as fail and fix.
3. **Caveat — bot-blocking false negatives.** Some authoritative sites (e.g.
   QuickBooks/Intuit, some large publishers) block plain `curl` and return `000`
   or `403` even though the page is live in a real browser. If a normally-solid
   source fails curl, re-verify it with a browser-grade fetch (the Firecrawl
   scrape tool, or a real browser) and confirm a `200` + sane page title/metadata
   before trusting OR discarding it. Don't drop a good source over a bot block,
   and don't keep a genuinely dead one.
4. Report the result list in the publishing kit: each URL + the status you
   confirmed and how (curl 200, or "curl blocked → verified live via browser-grade
   fetch, 200 + title").

## The one-line version
Research the real internet, link only to verified-live pages, source every fact
with receipts, and never hand traffic to a competitor.
