# Image-Generation Preflight — check BEFORE you promise imagery

Image generation is the most failure-prone dependency in this agent. It fails in a handful of predictable ways, and each one has a different fix. **Run this preflight at the start of Stage 2.5 (Art Direction), before you tell the user the page will have generated imagery.** If a backend is broken, say so up front with the exact fix — never fail mid-run with a cryptic error or let a scary OS popup be the user's first signal.

The rule: **probe first, promise second, degrade gracefully.** Only claim generated imagery once a backend actually answers.

**Probe with a real (tiny, throwaway) generation, not just a presence check.** The hard lesson: a backend can pass every "is it installed / is there a key" check and still fail to produce an image (broken binary that only errors on spawn; a valid key whose project has zero image quota). The only trustworthy probe is one cheap actual generate. If it returns a file, the backend is real; if it errors, read the error against the table below. Delete the throwaway.

---

## The two backends, in preference order

1. **`gpt-image-2`** — via the user's ChatGPT plan (no separate API key/billing). Runs through the `codex` CLI or the `gpt-image-2` skill.
2. **`nano-banana`** — via the Gemini CLI's `nanobanana` extension. Needs a Google auth method.

Probe #1; if unhealthy, probe #2; if both are down, degrade to treated stock, then to a fully procedural signature (per `art-direction.md`). The page must still ship looking designed.

---

## Preflight checks + the exact fix for each failure

### gpt-image-2 / codex

**Probe:** confirm the CLI resolves AND its native binary actually exists (the #1 real-world failure is a partial install where the launcher is present but the compiled binary never landed).

```bash
which codex && codex --version 2>&1 | head -3
```

- **`ENOENT` / "spawn … codex … ENOENT"** → the platform binary is missing from a partial npm install (the launcher is on PATH but its `vendor/.../codex/` folder is empty). **`npm install -g @openai/codex@latest` may NOT fix this** — on some setups npm updates the launcher but still never lands the native binary. **The reliable fix is Homebrew**, which ships the properly-signed binary:
  ```bash
  npm uninstall -g @openai/codex      # remove the broken launcher
  brew install codex                  # installs the real notarized binary to /opt/homebrew/bin
  codex --version && codex login status
  ```
  **A working binary often already exists on the machine** even when the PATH one is broken — inside `/Applications/Codex.app/Contents/Resources/codex` or the VS Code ChatGPT extension (`~/.vscode/extensions/openai.chatgpt-*/bin/macos-*/codex`). These are logged into the same ChatGPT session. But **do NOT silently repoint the PATH command at an app-bundle binary** — a security layer may (correctly) block reaching into an app bundle for a previously-flagged binary. The clean fix is the brew install above, which makes `codex` on PATH a legitimate, trusted install with nothing to bypass. If you can't run brew for the user, tell them to run these three commands themselves.
- **A macOS "malware"/"cannot be opened" block on codex** → almost always a **Gatekeeper/XProtect false positive on an unsigned or freshly-updated build**, NOT malware in this agent or the user's skill. Codex ships as three legitimate OpenAI things — the npm CLI (`@openai/codex`), the desktop app (`/Applications/Codex.app`, bundle id `com.openai.codex`, Sparkle auto-update), and a VS Code extension. **Fix:** verify it's genuine, then allow it:
  ```bash
  codesign -dv --verbose=4 /Applications/Codex.app 2>&1 | grep -i "authority\|identifier"
  spctl -a -vvv /Applications/Codex.app 2>&1
  ```
  If the authority is Apple/OpenAI and identifier `com.openai.codex`, it's signed/notarized — approve it in **System Settings → Privacy & Security → Security → Allow Anyway**, and clear any duplicate installer `.dmg`s from Downloads that trigger repeated blocked auto-updates. Do not tell the user to disable Gatekeeper system-wide.
- **`command not found: codex`** → not installed. **Fix:** `npm install -g @openai/codex`, or use nano-banana instead.

### nano-banana / gemini

**Probe:** confirm the CLI, the extension, AND a persisted auth method all exist.

```bash
gemini --version && gemini extensions list 2>/dev/null | grep -i nanobanana
[ -n "$GEMINI_API_KEY" ] && echo "key: env" || (ls ~/.gemini/settings.json >/dev/null 2>&1 && echo "auth: settings.json" || echo "auth: MISSING")
```

- **`auth: MISSING`** (no `GEMINI_API_KEY` in env, no `~/.gemini/settings.json`) → the most common nano-banana failure; a one-time `export` doesn't persist to new sessions. **Fix, made permanent:**
  ```bash
  # Option A — API key (matches the skill), permanent:
  echo 'export GEMINI_API_KEY="YOUR_KEY_FROM_AISTUDIO"' >> ~/.zshrc && source ~/.zshrc
  # Option B — OAuth, no key:
  gemini      # choose "Login with Google" → writes ~/.gemini/settings.json
  ```
- **extension missing** → `gemini extensions install https://github.com/gemini-cli-extensions/nanobanana`
- **CLI missing** → install the Gemini CLI, or use gpt-image-2 instead.
- **Auth present but generation returns HTTP 429 / `RESOURCE_EXHAUSTED` / "quota exceeded … limit: 0"** → the key is VALID and authenticating fine; the problem is the Google Cloud project behind it has **no image quota on the free tier**. Image models (`gemini-2.5-flash-preview-image` / nanobanana) generally require **billing enabled**, even though text calls work free. This is why "auth present" is NOT the same as "can generate" — a real probe must survive a generate call, not just check for a key. **Fix:** enable billing on the key's project at aistudio.google.com (pay-as-you-go, ~$0.04/image), or switch to gpt-image-2 (ChatGPT plan, no per-image billing). **A missing shell-profile key is a common upstream cause** — if `export GEMINI_API_KEY=...` was added but new shells don't see it, check `~/.zshrc` for a *parse error above the export line* (an unmatched quote earlier in the file stops everything after it from loading) and confirm the export wasn't pasted malformed (key must be the VALUE inside the quotes, `export GEMINI_API_KEY="<key>"` — not the variable name).

---

## How to communicate a failure (tone matters)

- **Diagnose, don't alarm.** "Your gpt-image-2 backend has a partial install — here's the one command to fix it" beats a raw stack trace. If the user hit an OS malware popup, proactively explain it's a known false positive on a signed OpenAI app, so they're not left scared.
- **Offer the fastest working path.** If codex is down but gemini is one `gemini` login away, say so — don't send them down a reinstall rabbit hole when the other backend is closer.
- **Never block the whole page on imagery.** If neither backend can be fixed right now, proceed with a treated-procedural art direction and note that imagery was procedural (not generated) — the user gets a finished, designed page regardless, and can re-run for photographic imagery once a backend is live.

---

## Preflight self-check

- [ ] Probed the preferred backend's health (CLI resolves + binary/auth present) BEFORE promising generated imagery.
- [ ] On failure, gave the specific cause + the exact fix command — not a generic error.
- [ ] Fell through backends in order, then to treated stock, then to procedural — page still ships designed.
- [ ] If an OS security block appeared, explained the false-positive context instead of leaving the user alarmed.
