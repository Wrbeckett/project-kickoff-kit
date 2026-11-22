# Claude models and sessions: cheat sheet

**Which Claude model and effort to pick for each part of the Project Kickoff Kit.** Kit defaults, checked Nov 21, 2026 against Anthropic's model guides. Each project keeps its own version in MODEL-GUIDE.md; the weekly review and audits update it. Every pick here is a default: change it for one project ("change: Lead runs on Sonnet") or for all your projects (MY-DEFAULTS.md).

**How to pick:** click the model name next to the send button, choose the model, then **Effort**. Do it before the first message of a session. You can switch mid-chat if a job turns out harder or easier than expected.

## The four models (smallest to biggest)

| Model | Best for | Speed | Uses your limit |
|---|---|---|---|
| **Haiku 5.5** | Reminders, quick checks, lookups, sorting, short summaries | Fastest | Least |
| **Sonnet 5.5** | Clear, well-scoped work from a brief: polish a doc, a deck from a template, posts from a plan, routine reports | Fast | About half of Opus |
| **Opus 5.5** | Most real work: interviews, planning, research, analysis, judgment calls, coding, docs and decks that need thinking | Moderate | The baseline |
| **Fable 5.2** | The hardest, longest jobs: deep multi-step research, big builds, or when Opus at High still falls short | Moderate | About twice Opus |

**Which plan has what:** Free has Haiku and Sonnet. Paid plans add Opus (the default on Pro, Max, Ultra and Team). Fable is on all paid plans, but on Pro and standard Team seats it uses paid usage credits, so ask the owner first. Work and school accounts: an admin may limit the list.

**Effort** has five settings: Low, Medium, High, Extra high and Max. Higher effort thinks longer, checks more and uses your limit faster; Low and Medium stretch your usage for routine work. Opus 5.5 starts at **Medium**; move to **High** when Medium stalls. Extra high is for long coding and agent jobs.

## The kit's steps

| Kit step | Where | Model | Effort | Notes |
|---|---|---|---|---|
| Kickoff interview + blueprint | New chat in the Project (becomes Lead) | **Opus** | Medium | High for big, multi-person projects. Free plan: Sonnet |
| Audit of an existing project | New chat in the Project (becomes Lead) | **Opus** | High | Fable only for very large projects, with OK if it uses credits |
| Building the approved setup | Same chat | **Opus** | Medium | Folders, templates, PDFs |
| Lead session | <Project> – Lead | **Opus** | Medium | Routing and judgment. Small, simple project: Sonnet is fine |
| Health check (Prompt 5) | Any session | **Sonnet** | Medium | |
| Fresh start (Prompt 4) | Replaces a session | Same as the old session | Same | |
| Weekly review + audit | Lead (scheduled) | **Opus** | Medium | Needs judgment across every doc |
| Morning brief | Lead (scheduled) | **Sonnet** | Medium | **Haiku** if it's only a task list |
| Weekly report | Lead or work session (scheduled) | **Sonnet** | Medium | **Opus** if it needs analysis |
| Reminders, "anything new?" checks | Scheduled | **Haiku** | Low | Stops with one line when nothing's new |

## Work sessions, by kind of work

| Kind of work | Model | Effort | Move up / down |
|---|---|---|---|
| Build, code, websites | **Opus** | Medium | High for hard bugs and big changes; **Fable** for long builds handed off to subagents; **Sonnet** for small routine edits |
| Design and visuals (concepts, layouts, print files) | **Opus** | Medium | **Sonnet** for variations of an approved design |
| Writing that needs judgment (proposals, reports, policy, curriculum) | **Opus** | Medium | High for high-stakes documents |
| Writing from a clear brief (posts, captions, emails from notes, formatting) | **Sonnet** | Medium | **Haiku** for very short, repetitive items |
| Research and analysis | **Opus** | High | **Fable** for deep research across many sources |
| Data, admin, sorting, extracting, summaries | **Sonnet** | Medium | **Haiku** for high-volume, simple items |
| Marketing and social | **Sonnet** | Medium | **Opus** for strategy and campaign plans |
| Teaching and course materials | **Opus** | Medium | **Sonnet** to turn approved outlines into handouts and slides |

## When to switch

1. **Missed the mark?** First check the prompt and files gave Claude what it needed.
2. **Then raise the effort** one step.
3. **Still wrong**, even though it had the context and clearly tried? Move up one model.
4. **Easy every time?** Lower the effort first, then try a smaller model (well-scoped work only).
5. **Sonnet always at Extra high or Max?** Use Opus at Medium instead; it usually costs about the same per job.
6. **Fable on Pro or a standard Team seat** uses paid credits: owner's OK first.
7. **A new model comes out?** Rerun one go-to job on it; you may get the same result at lower effort.

## Keeping it current

- **Each project:** MODEL-GUIDE.md lists the model and effort for every session, scheduled task and kind of job. It also appears on each session's brief and on the project cheat sheet.
- **Weekly review:** checks the fit (repeated misses mean move up; easy routine runs mean move down) against the usage plan, and suggests changes. The owner answers "OK 1, 3; not 2".
- **Audits:** compare what each chat and scheduled task actually runs on with this sheet.
- **Monthly model check:** a scheduled task compares this sheet with Anthropic's help pages and logs any change in KIT-FEEDBACK.md for the kit owner to approve.
- **The kit:** when Anthropic releases or retires a model, update this sheet, change the "checked" date, and rebuild the PDF (python3 _build/make_pdfs.py).

Sources: Anthropic's "Choosing a Claude model for knowledge workers" (Claude Academy), "Using Claude Opus 5.5 as your daily driver for knowledge work" (claude.com), the Models overview (platform.claude.com) and "Claude Fable models on your plan" and "Change the model, effort, and thinking settings" (support.claude.com). Usage comparisons are rough, based on Anthropic's published prices.
