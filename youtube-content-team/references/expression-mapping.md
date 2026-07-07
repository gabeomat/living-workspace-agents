# Expression Mapping (video angle → facial expression)

Pick the face expression from the video's angle. This drives `{{FACE_EXPRESSION}}` in the prompt template and
which headshot to reference (choose the closest match in `assets/headshots/`).

| Video angle | Primary expression | Secondary (for variation 2) | Why |
|-------------|--------------------|-----------------------------|-----|
| **Tactical / how-to** | Confident, focused | Slight smile, approachable | "I'll show you exactly how" — competence sells the click |
| **Contrarian / myth-bust** | Skeptical / raised brow | Surprised | The face signals "you've been doing it wrong" |
| **Story / personal** | Warm, open | Thoughtful | Invites the viewer into a real moment |
| **Announcement / news** | Excited, energized | Shocked | Urgency and novelty |
| **Insight / big idea** | Thoughtful, intent | Confident | "This changed how I think" |
| **Warning / mistake** | Serious / concerned | Wide-eyed alarm | Stakes and caution |

## How to use it
1. Determine the chosen video's angle from the Director's pick + the hook.
2. Look up the primary + secondary expressions.
3. Use the **primary** for variation 1, the **secondary** for variation 2 (this is one easy way to make the two variations genuinely different).
4. Pick the headshot in `assets/headshots/` whose captured expression is closest to each target. The model
   re-renders the expression but preserves identity — so a closer starting pose gives a better result.
5. Honor the profile's `FACE_REGISTER` — if they said "warm, never shouty," dial even the excited expression
   toward genuine enthusiasm, not open-mouthed screaming.

If only one headshot exists, use it for both and let the prompt drive the expression difference.
