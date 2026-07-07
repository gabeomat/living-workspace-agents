# Finance Profile — <Your Business Name>

> This is a SCAFFOLD. It is never used as real data — the `<angle-bracket>` prompts are instructions, not values.
> The agent builds a real copy of this WITH you on first run (intake). To fill it in by hand instead: copy this
> file to `<your-business>.md` (no leading underscore) and replace every `<...>`. Delete any line you don't use.

## Connector (data feed)
- **Source:** <Era (recommended) | QuickBooks | other trusted financial MCP | CSV export | manual>
- **Notes:** <account nicknames, anything the agent should know to pull correctly>

## Accounts in scope
- **Accounts to include:** <list bank + card accounts that hold real business activity>
- **Hidden sub-account check:** <does any card show ONLY payments/fees, with purchases posting elsewhere? name it — this prevents silently dropping expense>
- **Exclude / transfers:** <internal transfers, paycheck deposits, anything that isn't real income/expense>

## Starting state (from intake)
- **State:** <A Reconcile (have a bookkeeper/clean books) | B Organize (messy data) | C Build (from scratch)>

## Chart of Accounts
- **Source:** <imported from accountant | template: Solo/Service | template: Product | template: Local | custom>
- **Location:** <path to the bookkeeping spreadsheet the agent maintains>

## Vendor → category notes
- <any special cases the agent should always apply — e.g. "Vendor X = category Y", refunds handling, etc.>

## Revenue recognition
- **What counts as revenue:** <e.g. Stripe payouts, Skool payouts, invoices paid — name your real income sources>

## Brand (for the dashboard)
- **Colors:** <2–3 hex colors for the P&L dashboard>
- **Style:** <clean/calm default, or a note on the look you want>

## Cadence
- **Refresh rhythm:** <monthly close | weekly glance | on demand>
