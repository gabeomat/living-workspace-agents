# First-Run Intake Diagnostic — "Where are you starting from?"

Run this the first time (no real finance profile exists). Goal: figure out the user's starting state and set up
their books the right way, so the agent works for someone with a bookkeeper AND someone who's never tracked a
dollar. Keep it warm and plain — money intimidates people.

## Step 1 — Determine the starting state

Ask, in plain language: *"Before I touch anything — how are your books today? Pick the closest:"*

- **A. "I have a bookkeeper / accountant, or clean books already."** → **RECONCILE mode**
- **B. "I have the data (bank/card activity) but it's messy or uncategorized."** → **ORGANIZE mode**
- **C. "I'm basically starting from scratch."** → **BUILD mode**

If unsure, ask two quick questions: *Do you already have a Chart of Accounts (a list of income/expense categories)? Do you have a current profit & loss statement?* Two yeses → A. Some data, no structure → B. Neither → C.

## Step 2 — Settle the Chart of Accounts (all states)

Ask: *"Do you want to import a Chart of Accounts you already have (from your accountant/bookkeeper), or pick a template I'll adapt to your business?"*
- **Import:** take their existing CoA and use it as-is. This is how a client's already-systematized structure continues (the reconcile path). Don't "improve" it unasked.
- **Pick a template:** offer the options in `chart-of-accounts-templates.md`, adapt the chosen one to their real vendors.

## Step 3 — Set up per state

### RECONCILE (State A)
The agent is an **auditor**, not a rebuilder.
1. Adopt their existing Chart of Accounts exactly.
2. Pull their transactions from the connected source.
3. **Spot-check against their existing books**: sample categorizations, check the totals tie out, look for anything
   miscategorized or missing. Report what you found — confirmations AND discrepancies.
4. Continue in their existing structure. Do not restructure a working system.

### ORGANIZE (State B)
1. Pull all transactions from the connected source (full pagination).
2. Categorize by vendor into the settled Chart of Accounts (never auto-categories).
3. Flag ambiguous items and ask.
4. Build a clean Transactions sheet + P&L in the bookkeeping spreadsheet.

### BUILD (State C)
1. Establish the full bookkeeping spreadsheet: Chart of Accounts + Transactions + P&L structure.
2. Pull and categorize from the connected accounts.
3. Walk them through what each part means — this user is learning the system, not just receiving it.

## Step 4 — Write the profile
Record connector, Chart of Accounts, starting state, brand colors, and account list (including any hidden
sub-accounts surfaced by the safety check) into `references/profiles/<their-business>.md`. Confirm it back.

## Step 5 — Confirm the account list against the hidden-sub-account trap
Before finishing intake, explicitly ask: *"Does any card or account only show payments/fees, with the actual
purchases posting somewhere else?"* (See `money-safety-rules.md`, Trap 1.) Capture the answer in the profile so
no expense gets silently dropped later.

## Guardrails
- Never write real data into `_TEMPLATE.md` — always create `<business>.md`.
- Don't restructure a working set of books (State A) — adopt, reconcile, continue.
- Don't proceed without a connected source OR user-provided data — there's no way to invent someone's finances.
