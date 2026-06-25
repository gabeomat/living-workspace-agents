# Living Workspace Agents

**AI employees you install once and put to work.**

This is a collection of installable AI agents (Claude calls them "skills") that do
real jobs in your business, end to end, on your say-so. Drop one into your AI
workspace and it stops being a chat you have to babysit and becomes a worker that
runs a whole workflow for you.

Built by [Gabriel Omat](https://gabrielomat.com) as part of teaching people to set
up their own **Living Workspace** — an AI setup that actually knows your business
and does the repeatable work with you instead of waiting on you.

---

## What's inside

| Agent | What it does |
|-------|--------------|
| **blog-engine** | Writes a search-optimized blog post in *your* voice, end to end: keyword research → draft → verified non-competing source links → an FAQ-schema'd, AI-search-ready post. It learns your business from your own workspace, so the post sounds like you, not like a template. |

More agents coming. Each one is self-contained and user-agnostic — it adapts to
whoever installs it.

---

## How to install (2 minutes)

These agents are files that live in Claude's skills folder. "Installing" just means
copying them there. Two ways:

### Option A — the install script (easiest)
```bash
git clone https://github.com/gabeomat/living-workspace-agents.git
cd living-workspace-agents
bash install.sh blog-engine
```
That copies the agent into `~/.claude/skills/` so it's available in every Claude
session. Run `bash install.sh` with no name to see what's available.

### Option B — copy it yourself
Copy the agent's folder (e.g. `blog-engine/`) into `~/.claude/skills/`. That's it.

Then start a new Claude session and the agent is available — just describe what you
want ("write me a blog post about X") and it runs.

---

## Make it *yours*

Every agent here is **user-agnostic** — it doesn't assume whose business it is. What
makes it yours is running it in *your* workspace, where Claude can see your files,
your brand voice, and what it already knows about you.

For the blog-engine specifically: it works with zero setup (it infers your business
from context), but you can make it sharper by creating a **profile**. Copy
`blog-engine/references/profiles/_TEMPLATE.md`, fill in your business/audience/voice,
and save it. The agent loads it automatically. See the fictional
`example-fictional-coach.md` for a filled-in example.

---

## What you'll need

- **Claude** (Claude Code, the desktop/web app with skills, or any setup that loads
  skills from `~/.claude/skills/`).
- For the blog-engine's **automatic hero images**: an image tool. It prefers
  `gpt-image-2` (uses your ChatGPT subscription, no API key) and falls back to
  `nano-banana` (needs a Gemini API key) — or it'll hand you the image prompt to run
  yourself. Image generation never blocks the writing.
- Everything else (keyword research, writing, link-checking) runs with no extra
  tools or accounts.

---

## A note on how publishing works

The blog-engine writes and prepares the post. If you want it to publish straight to
a real website, that part is specific to *your* site (your repo, your host), so it
lives in a small command you set up for your own setup — not in the shared agent.
The agent's job is to produce a publish-ready post in your voice; wiring it to your
live site is a short follow-on step.

---

## License

Proprietary — see [LICENSE](LICENSE) for the full terms. In short:

- ✅ **Use them** in your own business and in work you do for your clients.
- ✅ **Sell the output** you create with them (e.g. posts you write for clients).
- ❌ **Don't resell or redistribute the agents themselves** as your own product,
  template, or library.
- ⚠️ **Provided "as is," with no warranty.** You're responsible for reviewing any
  AI output before you publish or rely on it. The author isn't liable for how the
  agents are used. (This isn't legal advice; your own program's terms still apply.)

---

Questions or want help setting up your Living Workspace? → [gabrielomat.com](https://gabrielomat.com)
