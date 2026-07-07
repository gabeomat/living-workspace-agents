# Bookkeeping Method — pull, categorize, maintain

How the agent keeps a clean, portable set of books regardless of which connector the user has.

## The two-layer model (keep these separate)
- **The books** = the source-of-truth **bookkeeping spreadsheet** the agent maintains. Portable, connector-agnostic.
- **The analysis** = the dashboard + advisory findings that sit ON TOP of the books.

The connector (Era / QuickBooks / bank MCP) is the **data feed**, not the source of truth. Pull from it, but
own a clean spreadsheet so the structure survives connector changes and reconciles cleanly.

## The bookkeeping spreadsheet structure
- **`Chart of Accounts`** — the valid income + expense categories (imported or template, per intake).
- **`Transactions`** — one row per transaction: date, description, vendor, amount (positive), account, category.
- **`P&L`** — revenue, expenses by category, net, margin — computed from Transactions (use formulas, don't hand-type totals).
- Optional **`Spending Summary`** — category rollups by month.

## Pulling from the connector
1. **Identify all in-scope accounts** — including any hidden sub-accounts (see `money-safety-rules.md`, Trap 1).
2. **Paginate fully** — don't stop at the first page; get every transaction in the period.
3. **Separate income vs. expense vs. transfer** — exclude internal transfers (Trap 3).
4. **Categorize by vendor** into the Chart of Accounts — build a reusable vendor→category map; never use the
   connector's auto-categories (Trap 2).
5. **Handle contra items** — refunds as negative revenue, vendor credits against the right category (Trap 4).
6. **Write to the spreadsheet**, then **verify totals** independently (recompute in code and confirm they tie out).

## Connector notes
- **Era** (recommended default) — pull per-account with full pagination; categorize in code. Watch for the
  hidden-sub-account pattern where a card shows only payments and the purchases post to a linked sub-account.
- **QuickBooks** — may already hold a Chart of Accounts and categorized data; in RECONCILE mode, adopt it and
  spot-check rather than rebuild.
- **Any other trusted MCP / bank connection** — same method: pull, categorize by vendor, reconcile.
- **No connector** — work from a CSV export or user-provided figures; explain how to connect a source to automate.

## Maintenance rhythm (Mode 4)
On each refresh: pull new transactions since the last update, categorize, append to the spreadsheet, recompute
the P&L, refresh the dashboard, and report what changed vs. last period. Keep the spreadsheet closed in any
desktop app while writing to avoid lock collisions.

## Verification (always)
After any write, recompute revenue/expenses/net independently and confirm they match the sheet. If a total
can't be reconciled to a known anchor (a statement total, a payout report), say so — don't hide the gap.
