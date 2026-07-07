# Thumbnail Brand System (tokenized)

This file defines HOW to apply the user's thumbnail brand — the fixed rules — while pulling the actual
values (colors, style, register) from the user's profile. **Nothing here is hard-coded to any one brand.**
Read the user's `references/profiles/<channel>.md` for the real tokens, then apply these rules.

## Tokens (pulled from the profile — never invent them)

| Token | Source | Fallback if missing |
|-------|--------|---------------------|
| `PRIMARY_COLOR` | profile → Thumbnail Brand → Colors[0] | ask the user; don't guess |
| `ACCENT_COLOR` | profile → Colors[1] | derive a high-contrast complement to primary |
| `BG_COLOR` | profile → Colors[2] | dark neutral if loud style, cream if warm style |
| `STYLE_REGISTER` | profile → Style register | bold/high-contrast (safest for YouTube CTR) |
| `TEXT_TREATMENT` | profile → Text treatment | all-caps, heavy weight |
| `FACE_REGISTER` | profile → Emotional register of face | confident, warm, not shouty |

## Fixed composition rules (apply to every thumbnail, any brand)

These are the CTR fundamentals — they hold regardless of the user's brand:

1. **16:9, 1280×720 minimum.** YouTube spec.
2. **Face is the hero.** The user's real face (from `assets/headshots/`) occupies 35–55% of the frame. Face left → text right, or face right → text left (pick per variation).
3. **High face/background separation.** The face must pop off the background — via a rim light, a solid color block behind, or a subtle outline. Never blend the face into a busy background.
4. **≤5 words of text.** Big, heavy, readable at phone size. Drawn from the hook.
5. **One focal tension.** A single expression + a single idea. No collage, no clutter.
6. **Brand colors do the work.** Use `PRIMARY_COLOR` for the dominant block/text, `ACCENT_COLOR` for the punch word or highlight, `BG_COLOR` behind. Keep it to these — consistency across a channel's thumbnails is what builds recognition.
7. **Consistency rule** — honor any `Consistency rule` in the profile (e.g. "face always right side"). This is what makes a channel's thumbnails feel like a set.

## Style-register interpretation

- **bold/loud** → high saturation, thick outlines, big all-caps text, strong expression, hard color blocks.
- **clean/editorial** → restrained palette, generous space, tasteful type, calmer expression, one accent color.
- **warm/approachable** → softer light, inviting expression, rounded warmth, lower contrast but still readable.

Apply the register from the profile — don't default to loud unless that's what they chose (or nothing was set).
