# First-Run Onboarding — mapping who's already in your world

Run this the first time, before any lead work. It's an interview, not a form — ask conversationally, a few questions at a time, and confirm what you learn back to the user. Check their `CLAUDE.md`/Brain first and **don't ask what the workspace already answers.** At the end, write their real profile and build the `leads/` structure.

## 1. The pools — "where do your people already live?"

Walk through the common pools; capture the ones that exist and how to get an export of each:

- **Email list** — which platform (any works: MailerLite, Kit, Mailchimp, ActiveCampaign, GoHighLevel…)? Can they download a subscriber CSV? If a platform MCP is connected, note it (for pulling exports only — never sending).
- **Community** — Skool, Circle, Facebook Group, Discord…? Can they export or paste the member list? Chat/post history?
- **Events** — webinars, workshops, challenges, livestreams? Registrant/attendee lists? **Event chat logs are gold** — people ask real buying questions in them.
- **Past + current clients** — even just a remembered list. Past customers are the warmest pool most owners ignore.
- **CRM / spreadsheet** — anything they already track people in.
- **Social followers** — note it, and set expectations honestly: there's no clean automated export, so social feeds the ledger through the manual door (Mode 4 — "add this person") whenever the owner spots a repeat engager. Also mention the ManyChat-style pattern: a welcome DM automation whose *replies* can be exported into `leads/inbox/` like any other file.

One pool is enough to start. Recommend starting with the **richest** pool, not the biggest — an event chat log beats a 2,000-row subscriber list.

## 2. The offers — filling the three ask-path slots

| Slot | What goes here | Who it's for |
|------|----------------|--------------|
| **Entry offer** | The low-commitment front door: free/paid workshop, webinar, audit, consult call | Cold people — no history with them yet |
| **Core offer** | The always-open thing: membership, service, package, program | Anyone showing a real signal |
| **Premium offer** | The high-ticket path: intensive, done-with-you, retainer | **Warm only** — attended, member, past client, or in conversation |

Get: name, one-line promise, price point (roughly), and the link or next step for each. Fewer than three offers is fine — fill what exists, leave the rest empty, and route everything to the slots they have. If they have no Entry offer, cold contacts simply stay in nurture (say so — that's a fine answer, and a product idea for later).

Ask one preference: when someone qualifies as warm, default them to the Premium invite or the Core offer first?

## 3. The rhythm

- **Batch size** — default 10. Smaller is fine; bigger only if they *really* clear batches fast.
- **Cadence** — default weekly. Name the day.
- **Cooldown** — default 14 days between personal touches to the same person.
- **Channels they'll actually send on** — email replies, community DMs, social DMs. Only channels the owner will personally use.
- **Voice** — do they have a brand-voice skill installed? If not, ask for 2–3 links/samples of writing that sounds like them and note voice rules in the profile.
- **Exclusions** — anyone the agent should never draft to (current clients mid-engagement, personal contacts, a competitor watching the list).

## 4. Build and confirm

1. Create `leads/` per `references/ledger-spec.md` (folders + empty `ledger.csv` with the header row + empty `processed.log`).
2. Copy `profiles/_TEMPLATE.md` → `profiles/<their-business>.md` and fill it from the interview. Read it back to the user in two sentences and correct anything.
3. Tell them the first move: **drop one export into `leads/inbox/` and say "feed the ledger."** Name the specific file you recommended starting with.
4. Offer the weekly rhythm: if scheduled tasks are available, offer to schedule the batch run (their cadence day); if not, give them the one-line command to run it themselves each week.

**The wow to aim for:** within one session of onboarding, the user should see real names from their own audience, ranked, with real quotes attached — people they'd forgotten were there.
