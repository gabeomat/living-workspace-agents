# Structure: SEO + AEO + GEO

Three audiences read every post: a **searcher** (Google ranking), an **answer engine** (ChatGPT, AI Overviews, Perplexity, Gemini quoting you), and a **real human in need** (who takes the next step / CTA). This structure serves all three. It is built on the keyword brief from Step 2.

## The three jobs
- **SEO** = rank in Google's blue links. Won by relevance, depth, on-page signals, and trust.
- **AEO** (Answer Engine Optimization) = be the answer a voice/AI assistant reads back. Won by clear, extractable, well-structured answers.
- **GEO** (Generative Engine Optimization) = be the source a generative model cites. Won by authoritative, specific, citation-worthy, entity-rich content with clear author expertise.

The good news: they reward the same thing — a genuinely helpful, well-organized, trustworthy answer. Write that, structured deliberately.

## Post skeleton

```
TITLE (H1)        primary keyword near the front, human and clickable
INTRO (answer-first)
                  Sentence 1–3 = the extractable answer to the primary question.
                  Then 1–2 sentences of empathy + what the post will give them.
                  Primary keyword appears naturally in the first ~100 words.
H2 = Question 1   (a real question from the cluster)
  short answer-first paragraph, then depth, example, or steps
H2 = Question 2
  …
H2 = Question 3
  …
(optional H2s for remaining cluster questions)
soft-transition section → the profile's CTA (matched to intent)
FAQ (H2)          3–5 cluster questions, each answered in 2–4 sentences
CLOSE             warm, one clear next step (the profile's CTA / offer)
```

## On-page SEO rules
- **Primary keyword placement:** title, first ~100 words, at least one H2, meta description, and the URL slug. Natural density — if it reads stuffed, cut it. Never sacrifice voice for a keyword.
- **Secondary keywords / entities:** weave the related terms and named concepts (attachment styles, "secure attachment," "emotional flooding," "bids for connection," etc.) where they fit. Entities signal topical authority to both Google and generative engines.
- **Headers:** descriptive, question-shaped, scannable. One H1 only. Logical H2 → H3 nesting.
- **Meta description:** <=155 characters, primary keyword in the front half, written to earn the click (promise + empathy), not just summarize.
- **Slug:** short, keyword-forward, hyphenated, no filler words.
- **Scannability:** short paragraphs (2–4 sentences), bolded key phrases sparingly, bullet/numbered lists where steps or options exist. Hurting readers skim first.
- **Internal links:** 2–4 contextual links to the relevant service/course (see context reference). Descriptive anchor text, never "click here."
- **External links:** cite 1–3 reputable sources (research, established institutions) when a claim needs backing. Builds E-E-A-T and gives generative engines something to trust.

## AEO rules (be the quoted answer)
- **Answer-first everywhere.** Every H2 section opens with a 1–2 sentence direct answer, then expands. Engines lift the opening.
- **One clean extractable answer** to the primary question, ideally in the intro: a self-contained 2–3 sentence definition/answer that makes sense out of context.
- **FAQ block** with real cluster questions, each answered in 2–4 tight sentences. This is the single highest-leverage AEO element — it maps directly to "People Also Ask" and AI Overviews.
- **Definitions and lists** are extraction-friendly. When a concept has a clean definition or a stepwise process, format it as such.
- **FAQ schema (JSON-LD) must end up ON the page, not just in the chat.** Note 2023+: Google retired FAQ rich results for most sites, so the value now is AEO/GEO — it gives AI answer engines (AI Overviews, ChatGPT, Perplexity, Claude) an unambiguous question→answer mapping to quote. It's a Tier-2 booster, not a magic bullet; the answer-first HTML does most of the work, but the schema is cheap insurance worth always including. **Make it automatic, never a manual paste step** (manual pasting is exactly how schema silently gets dropped between "skill generated it" and "site shipped it"). If the publishing target has a templated layout, add/extend it to emit `FAQPage` JSON-LD from an `faqs` data prop, then pass the Q/A pairs on every post with an FAQ. Only fall back to handing over paste-in JSON-LD when there's no templated layout to wire it into. After build, verify exactly one `application/ld+json` FAQPage block with the correct Question count is in the rendered HTML.

## GEO rules (be the cited source)
- **Specificity and depth** beat breadth. Generative engines cite the page that actually answers the question fully, with concrete detail, not the one that skims.
- **Author authority is explicit.** Make clear who wrote/reviewed it and why they're credible (the profile names the author identity and authority). A short author line and credentials matter enormously for who gets cited, and they matter most on YMYL topics.
- **Statistics, research, and named frameworks / entities** make a page quote-worthy (e.g. attachment theory for Couples Learn; The Living Workspace, Business Brain for Gabriel Omat). Use them accurately and with attribution.
- **Up-to-date and accurate.** Note recency where relevant. Never fabricate a study or a stat — a single fake citation poisons trust and can get the page distrusted.

## E-E-A-T (always) and YMYL (when the profile is YMYL)
Write from **real experience and authority** (Experience, Expertise, Authoritativeness, Trust) for every profile — let the author's genuine credibility and point of view show. Cite real sources for factual claims. Accuracy is a ranking and citation asset, not just ethics.

**If the profile is YMYL** (health, mental health, relationships, finance, legal — see the active profile's trust rules), hold it to the highest bar:
- No outcome guarantees or overpromises. Use careful, honest framing ("many people find," "research suggests," "in my experience").
- Make author authority and credentials explicit.
- Encourage professional support where appropriate, with a light safety note on heavy topics (abuse, crisis, self-harm) directing readers to appropriate help. Never position a blog post as treatment or professional advice.

## Quality bar (the post must clear all of these)
1. Opens by answering the searcher's actual question, fast.
2. Every H2 is a question a real person types, answered clearly.
3. Reads like the profile's voice (a specific, credible person), not a content mill.
4. Has an FAQ + clean extractable answers (AEO).
5. Shows author authority and cites real sources where needed (GEO/E-E-A-T).
6. Links to the profile's offer and ends with one confident CTA.
7. Primary keyword present where it should be, never stuffed.
