# The Branded P&L Dashboard (Cowork + Claude Code)

The dashboard is the visible payoff — the thing the owner opens to see, at a glance, what they're making and
where it's going. It must look like THEIR business (their brand colors) and stay current.

## Environment awareness (important)
This agent must work in BOTH environments:
- **Cowork** — build the dashboard as a **living artifact** that updates in place. This is where most owners will
  "keep" their dashboard and glance at it. The heavier data-pull may be more limited here; lean on already-pulled
  books when possible, and guide the user to Claude Code (or an MCP-connected session) for a full re-pull.
- **Claude Code** — full file + MCP access for the heavy bookkeeping work (pull, categorize, reconcile, write the
  spreadsheet). Render the dashboard as HTML here.

Detect where you're running and behave accordingly. The analysis + dashboard should work globally in Cowork even
when the deep data pull happened in Claude Code — because the books (spreadsheet) are the shared source of truth.

## What the dashboard shows
Compute all of these **fresh from the books** (never re-render a stale snapshot):
- **Metric cards:** revenue, expenses, net profit, profit margin (for the current month + the period).
- **Net by month** — a bar/line of monthly net over time.
- **Revenue vs. expenses** — side by side, month over month, so the margin gap is visible.
- **Optional overlays** the user cares about (e.g. a specific big cost line like ad spend, overlaid on revenue —
  this is how an owner sees whether a lever is paying off).
- **Top expense categories** — where the money actually goes.

## Branding
Pull brand colors from the user's finance profile (or their main brand file / Brain). The dashboard should feel
like their business, not a generic accounting screen. Clean, readable, calm — money dashboards should reduce
anxiety, not add to it. Big honest numbers, no clutter.

## The "show my P&L" ritual (Mode 2 + Mode 4)
When the user asks to see their P&L (or on a monthly cadence):
1. Recompute revenue/expenses/net/margin fresh from the latest books.
2. Render/refresh the dashboard (living artifact in Cowork, HTML in Claude Code).
3. If numbers changed from the last saved version, update the saved dashboard + the written analysis so the saved
   copy stays current.
4. Surface the one or two things that changed most, and offer to dig in (hands off to the advisory playbook).

## Companion: "how to build your dashboard in Cowork"
Setting up the living artifact in Cowork can be its own short onboarding/training for the user. Offer to walk them
through pinning it as a living artifact so it becomes their standing money view. Keep this as an optional guided
step — some users just want the numbers, others want the permanent dashboard.
