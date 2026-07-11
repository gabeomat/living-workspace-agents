# Email Craft — jobs, subject lines, integrity rules, and delivery

The drafting doctrine. The matrix decides *what each email must accomplish*; this file decides *how a good one is built*.

## The email jobs library

Every email in a sequence gets exactly **one job** from this library (assigned in the strategy brief) and **one CTA**. An email with two jobs does neither.

| Job | What it does | Craft notes |
|-----|--------------|-------------|
| **Deliver + first win** | Hands over the promised thing and gets it *used* | One consumption instruction, not a feature tour. An unconsumed lead magnet converts nobody |
| **Origin story** | Makes the sender one of *them* | The mess before the method. Ends in the belief shift, not in a pitch |
| **Mechanism shift** | "Why what you've tried didn't work — and what does" | The single most conversion-critical email for solution-aware readers. Name the old way's flaw without insulting the reader for trying it |
| **Proof story** | "Someone like me did this" | A real story from the bank, with texture (specifics sell; vagueness smells invented). Match the story's belief tag to the checkpoint |
| **Objection crusher** | Meets the #1 hesitation head-on | Name it in the reader's words, answer honestly — including who it's genuinely *not* for. Honesty here buys the close |
| **The offer, plainly** | States what's for sale, for whom, for how much, what happens next | No cleverness. The confident default: "here's what I built and why" |
| **FAQ / logistics** | Clears the practical fog (time, format, access, guarantee) | Boring on purpose. Fog, not doubt, kills many late-stage buyers |
| **Deadline close** | The honest last call | Real reason for the deadline stated. Short. One link, maybe twice |
| **Open door / downshift** | After the no: keeps the relationship, offers the smaller step | Zero guilt. "Not now" is a fine answer said kindly — this email is why they buy next season |
| **Re-permission** | Re-opens a cold relationship | Gives before asking; makes leaving easy (that's what makes staying meaningful) |

## Structure of a single email

- **Subject + preview text**: written together — preview extends the subject, never repeats it. Three variants per email (cheap tier): one curiosity, one direct-benefit, one story/human. The user picks; never auto-pick for them.
- **The open**: first line earns the second. Enter mid-story, mid-thought, or with the reader's own problem — never "Hope you're doing well" or a throat-clear about the email itself.
- **The body**: one idea, built as story → point → bridge. Short paragraphs (1–3 lines); write for a phone screen. Length follows the job — a story email can run 400 words; a deadline close shouldn't pass 120.
- **The CTA**: one action, stated plainly, usually twice at most (mid + end, or end + P.S.). Link text says what happens ("Save your seat"), not "click here."
- **The P.S.**: highest-read line after the subject. Use it for the CTA restated, the deadline, or the humanizing aside — not a second topic.
- **Texture rule**: plain-text feel by default — these should read like a person wrote an email, because one did (with help). Heavy design templates are the user's platform choice, not the default.

## Integrity rules (non-negotiable — these are why the emails work more than once)

1. **Real stories only.** Every story, name, number, and result comes from the story bank or the user's words this session. If the perfect proof story doesn't exist, say so and use what does — or ask for one. A fabricated "client win" is the fastest way to torch a list *and* it's simply lying.
2. **Real urgency only.** A deadline appears only if the user confirms it's real, with the reason stated. Evergreen sequences don't get fake countdowns.
3. **No confidence leaks.** The four patterns, checked in every draft: pre-emptive self-disqualification ("this might not be for you, but…"), apologizing for the mechanics or for emailing at all ("sorry for another email…"), self-deprecating the offer or materials, hedging the CTA ("if you want, you could maybe…"). Substitute the confident default and *keep the warmth* — sincerity is the asset; apology is the leak.
4. **No guilt, no shame CTAs.** "I'm disappointed you haven't…" converts resentment, not customers.
5. **Respect the no.** Sequences end. Non-buyers route to the open door, not to an infinite pitch loop.
6. **Permission-based, always.** Written for people who opted in. If the user asks for a sequence to a purchased or scraped list, decline that use and say why (deliverability, law, and trust all point the same way).
7. **Compliance floor:** every email carries the profile's footer (sender identity + unsubscribe). Not optional, not a design choice.

## Delivery: the CRM question and the handoff

After the sequence is approved, ask: **"Want this loaded into your email platform as drafts?"**

**If yes — the connection protocol:**
1. Discover what's actually connected in this environment (an email-platform MCP or Claude connector — any platform: MailerLite, Kit, Mailchimp, GoHighLevel, ActiveCampaign…). Don't guess from the profile; check.
2. If their platform is connected: create the group/segment (named clearly: e.g. `[funnel] — [date]`), load each email as a **draft** (or paused automation, if that's the platform's draft equivalent), confirm each write as it happens, and finish with exactly what was created and where — plus the one thing you did NOT do: activate it. **The user flips the switch in their platform.**
3. If nothing's connected: say so plainly, deliver the handoff package, and mention — once, without pushing — that connecting their platform to Claude (connector or MCP) makes this step automatic next time. Whether a connection exists for their platform is theirs to check; never install, configure, or request credentials for one mid-build.

**The handoff package (always produced, connection or not)** — `nurture/sequences/<funnel>-<date>/`:
- `brief.md` — the strategy brief (see funnel-matrix)
- `emails.md` — every email in send order: day/trigger, job, subject variants ×3, preview text, body, CTA link placeholder clearly marked `[LINK: …]`
- `timing.md` — the send schedule + segment/branch logic in plain language, so it can be built in ANY platform's automation builder in one sitting
