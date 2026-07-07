# Thumbnail Prompt Template (locked structure)

This is the fixed structure for every thumbnail prompt. Fill the `{{placeholders}}` from the chosen video,
the hook, and the user's thumbnail brand tokens (from `thumbnail-brand-system.md`). Do not improvise outside
this structure — the consistency is what makes a channel's thumbnails look like a set.

## The prompt

```
A professional 16:9 YouTube thumbnail (1280x720), high click-through-rate style.

SUBJECT: The person from the attached reference photo, rendered with a {{FACE_EXPRESSION}} expression.
Preserve their real facial identity and features from the reference — this must clearly look like the same person.
Face occupies about {{FACE_SIZE}}% of the frame, positioned {{FACE_POSITION}}.

STYLE: {{STYLE_REGISTER}} YouTube thumbnail aesthetic. {{STYLE_NOTES}}

COLORS: Dominant {{PRIMARY_COLOR}}, accent {{ACCENT_COLOR}}, background {{BG_COLOR}}.
Keep strictly to this palette for brand consistency.

TEXT OVERLAY: The words "{{HEADLINE}}" in a bold, heavy, highly readable font ({{TEXT_TREATMENT}}),
placed {{TEXT_POSITION}}. The word "{{PUNCH_WORD}}" is emphasized in {{ACCENT_COLOR}}.
Text must be legible at small (mobile) size.

COMPOSITION: Strong separation between the face and background (rim light or solid color block behind the face).
One clear focal point. No clutter, no collage. {{CONSISTENCY_RULE}}

Do NOT add logos, watermarks, or extra text beyond the overlay specified.
```

## Placeholder fill guide

| Placeholder | Fill from |
|-------------|-----------|
| `{{FACE_EXPRESSION}}` | `expression-mapping.md` (video angle → expression) |
| `{{FACE_SIZE}}` | 35–55 (bigger for bold register, smaller for editorial) |
| `{{FACE_POSITION}}` | "left third" or "right third" — alternate between the two variations |
| `{{STYLE_REGISTER}}` | profile → style register |
| `{{STYLE_NOTES}}` | interpretation from `thumbnail-brand-system.md` |
| `{{PRIMARY_COLOR}}` / `{{ACCENT_COLOR}}` / `{{BG_COLOR}}` | profile colors |
| `{{HEADLINE}}` | 3–5 words drawn FROM the chosen hook (never invented) |
| `{{PUNCH_WORD}}` | the one word in the headline to emphasize |
| `{{TEXT_TREATMENT}}` | profile → text treatment |
| `{{TEXT_POSITION}}` | opposite side from the face |
| `{{CONSISTENCY_RULE}}` | profile → consistency rule, if any (else omit the sentence) |

## The two variations

Generate **two** prompts that differ on at least ONE axis:
- **Expression** — e.g. confident (v1) vs. surprised (v2)
- **Headline phrasing** — direct claim (v1) vs. provocative question (v2)
- **Composition** — face left/text right (v1) vs. face right/text left (v2)

Make them genuinely different — real choice, not microvariants.

## Hard rules
- Headline ≤5 words, pulled from the hook, matching the script's real payoff (no clickbait).
- Always reference the real headshot — never generate the face from text alone.
- Stay in the profile's palette — don't add colors "for pop."
