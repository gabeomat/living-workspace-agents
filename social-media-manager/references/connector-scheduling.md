# Connector & Scheduling — connector-agnostic, Metricool default

How finished assets get hosted and scheduled as drafts. The connector comes from the user's profile.
**Nothing is ever auto-published** — every item is a draft for the user's review.

## Hosting the assets first

Most schedulers need a public URL for each image/video. Default host: **catbox.moe** (no account needed).
1. Upload each final delivery asset (statics, carousel bundles, the Reel MP4). Collect the returned URLs.
2. Do NOT upload intermediate Reel frame PNGs — they're only inputs to ffmpeg.
3. If the user's connector accepts direct file upload (some do), you can skip hosting for those.

## Connector options

Read `connector` from the profile and follow the matching path.

### Metricool (default)
Create one draft per post via the Metricool MCP, at the profile's days/times/timezone.
- Set `draft: true` and `autoPublish: false` on every post.
- Use the profile's account/profile IDs. If they're missing, ask the user for them once and note them
  back into the profile so future runs don't ask again.
- After creating all drafts, call the "get scheduled posts" method to confirm they saved.

### Buffer / Later / other MCP-connected schedulers
Same shape: one draft per post, at the profile's schedule, never auto-publish. Use whatever
create-draft method that connector exposes. Confirm afterward if the tool supports a read-back.

### GoHighLevel
If the profile names GHL, use its social-posting create-post method to stage drafts. Same no-auto-publish rule.

### Manual (default when no connector is set up)
Don't try to schedule. Instead, produce a clean **posting schedule doc** the user can act on:

```
WEEK OF <date>
─────────────────────────────────────────────
MON  <time tz>  · Static   · <caption first line…>  · asset: <url or filename>
TUE  <time tz>  · Carousel · <caption first line…>  · assets: <urls>
...
```
Include, for each post: day + time + timezone, format, the full caption, and the asset link(s). The user
posts these themselves. This mode still delivers 100% of the copy + design work.

## Verification (Phase 7)

- Connected mode: confirm the count of created drafts equals the number of posts in the profile's mix.
  If any are missing, find and create the missing one before reporting done.
- Manual mode: confirm the schedule doc has one complete row per post in the mix.

## Guardrails
- Never `autoPublish`. Drafts only. The user publishes on their own review.
- Never invent account IDs. If they're missing, ask once and record them in the profile.
- If hosting fails for an asset, report which one — don't schedule a post pointing at a broken/missing asset.
