# The Lead Ledger — file layout & schema

One ledger, many doors. Every source (an email export, a chat log, a member list, a manual add) is just a different way of writing to the same file. Scoring and outreach only ever read from here — never from raw sources.

## Workspace layout (created on first run, in the user's workspace)

```
leads/
├── ledger.csv          ← one row per person — THE source of truth
├── inbox/              ← drop zone: raw exports land here (CSV, chat logs, lists, pasted text saved as .txt/.md)
├── processed.log       ← one filename per line: files already ingested. NEVER re-read anything listed here.
├── needs-review.md     ← flagged possible duplicates + anything ambiguous, awaiting the user's call
├── dossiers/           ← <slug>.md deep profiles — top-scored people only, not everyone
└── outreach/           ← YYYY-MM-DD-batch.md approval batches (drafts, never sent by the agent)
```

## ledger.csv schema

One row per person. Quote fields properly (standard CSV). Semicolons separate items *within* a field.

| Column | What it holds |
|--------|---------------|
| `id` | stable slug, e.g. `jane-castillo` (from name; add a digit on collision) |
| `name` | full name as best known |
| `email` | **primary key for matching.** Empty allowed (e.g. a community-only contact) |
| `handles` | other identities, `platform:handle` — e.g. `community:JaneC;instagram:@janec` |
| `sources` | where they've appeared, semicolon list of tokens — e.g. `email_list;event_2026-06-13;community` |
| `status` | `new` · `nudged` · `replied` · `conversation` · `customer` · `past_customer` · `not_interested` · `unsubscribed` |
| `segment` | written by the scoring script: `warm` · `engaged` · `cold` · `customer` · `excluded` |
| `score` | written by the scoring script — don't hand-edit |
| `first_seen` | YYYY-MM-DD |
| `last_activity` | YYYY-MM-DD of their most recent action (not ours) |
| `last_touch` | YYYY-MM-DD we last reached out personally (empty = never — that's the point) |
| `signals` | semicolon list of `YYYY-MM-DD|type|verbatim-or-faithful-note` — see signal types below |
| `interests` | short comma phrases inferred ONLY from their own words/actions |
| `offer_fit` | which ask-path slot they currently route to: `entry` · `core` · `premium` |
| `notes` | anything else, brief |

### Signal types (the `type` in each signal)

`asked_question` · `replied` (to an email/DM) · `posted` (in community) · `attended` (event/workshop) · `registered` (but unknown/no attendance) · `joined` (community/list) · `purchased` · `referred` · `requested_info` · `personal_share` (volunteered something about their business/life)

A signal is something the person **did or said**. "Opened an email 6 times" is tracking data, not a signal — it never goes in `signals` and is never referenced in outreach.

## The ingest-once discipline (why this stays cheap)

1. Raw files are read **once**, at ingestion, by the cheapest capable model. The extract goes into the ledger; the filename goes into `processed.log`.
2. After that, every run — scoring, batching, reporting — reads the ledger and dossiers only. No agent ever spelunks through raw transcripts twice.
3. New data = new file in `inbox/`. Same export re-dropped with new rows? Save it under a dated filename (`list-2026-07.csv`) so the log stays honest; the email-key merge makes re-imports safe (existing people update, new people append).

## Merge rules

- **Email match → same person.** Merge: union of sources/handles/signals, earliest `first_seen`, latest `last_activity`.
- **Name-only match → NEVER auto-merge.** Write both candidates to `needs-review.md` with what's known about each; the user confirms or splits. A wrong merge produces outreach referencing something the person never said — the most trust-destroying failure this system has.
- `unsubscribed` and `not_interested` are permanent unless the user themselves reverses them.

## Dossiers

Only the warmest people (roughly the top 50, or whoever enters a batch) get `dossiers/<id>.md`: who they are, every signal in full with dates and context, what they do (their words), which ask-path and why, and a touch history. The other hundreds stay as ledger rows — tiered storage matches tiered attention.
