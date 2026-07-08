# First-Run Onboarding — write the user's real profile

The first time this agent runs for a new user (no real profile in `references/profiles/`, i.e. only `_TEMPLATE.md` and the fictional example exist), do a short setup that ends by **writing the user's real profile file for them.** This is the wow moment and the best teaching tool — after this, every run reads the profile and the agent already knows their business.

Prefer to **pull answers from the environment first, then confirm** — don't interrogate someone whose Brain already holds the answers. Ask only for what you genuinely can't find.

## What to gather (pull from Brain/workspace first, ask to fill gaps)

**Business & audience**
- Business/personal brand name, what they do, who they serve.
- The core offer(s) these pages will sell/promote, and the price point if relevant.
- The one audience these pages target, and the language that audience uses.

**Brand system** *(check for a brand skill / brand docs / existing site first)*
- Colors (background, text, one accent for CTAs) — as hex if possible.
- Typefaces (display + text). If unknown, note it and you'll art-direct a pairing per page.
- Logo location, and any real media (headshots, product photos).

**Voice**
- Is there a brand-voice / voice-writing skill available? If yes, name it — page copy will route through it.
- If no voice skill, point to the best voice source (existing posts, an About page, brand docs) so copy can match.

**Conversion defaults**
- Typical primary CTA + where it points (a scheduler link, an email opt-in, a checkout, a Skool/community join).
- Any trust/privacy rules (names you can/can't use, claims you can't make, compliance needs).

**Environment / connectors**
- Can this environment run a shell + install Playwright (Claude Code / desktop app), or is it a locked-down / no-code surface? This decides whether the critique loop renders here or hands off. (See `critique-loop.md`.)
- Any image-generation tool connected (for pages that need generated media), or should pages stay procedural?

## Then write the profile

Create `references/profiles/<their-slug>.md` (a real profile is any file NOT starting with `_`), filling the `_TEMPLATE.md` structure with their real values. Confirm the file back to them in one line ("Saved your profile — future pages will use it automatically") and proceed to the first brief.

## Guardrails
- **Never** treat `_TEMPLATE.md` or the `example-fictional-*` profile as real data. They are scaffolds/teaching examples only. If they're the only profiles present, you are in first-run onboarding.
- Don't block on perfection. A profile with a few "unknown — art-direct per page" fields is fine and better than an interrogation. Fill more over time.
- Pull before you ask. An answer already in the Brain shouldn't become a question.
