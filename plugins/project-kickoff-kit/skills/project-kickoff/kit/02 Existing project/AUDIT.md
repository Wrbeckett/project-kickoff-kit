# AUDIT.md: instructions for Claude (existing project)

You are auditing a project that's already under way and setting it up with the Project Kickoff Kit. The person who connected this folder is the **owner**. Follow these steps in order. Write for the owner in plain words: short sentences, exact menu and file names, no jargon. Never assume; ask.

**Finding the kit:** the files named here ("03 Templates/…", "07 Join or take over a project/…") are in the Project Kickoff Kit, wherever this person has it: (1) **installed as a plugin**: the project-kickoff skill's own folder holds the whole kit (in its kit/ subfolder); (2) a **connected "Project Kickoff Kit" folder**; (3) the kit's **GitHub page** (https://github.com/Wrbeckett/project-kickoff-kit; read the raw files). Use the first you can reach and say which. If none, ask the owner to install the plugin or connect the folder.

## Rules for the whole audit
- **Read everything before you conclude anything.** Note where each fact came from.
- **Ask, don't assume.** Anything unclear, missing, out of date or contradictory becomes a question for the owner. Use the multiple-choice question tool when you have it (2–4 options, your recommendation first), otherwise numbered questions; 3–5 at a time.
- **The audit only reads.** Never move, rename, delete, send, post, buy, connect or change anything during the audit. Changes come later, one by one, with the owner's OK.
- **Check every file you write** and say where it is.
- **Check the model fit.** Note which model each chat and scheduled task runs on where you can see it, and recommend a model and effort for each session and kind of work (kit defaults in "06 Models and sessions cheat sheet"; 03 Templates/MODEL-GUIDE-template.md). Recommend only models the owner's plan has.
- Respect privacy: don't copy passwords, keys, card or account numbers into any file; just note that they exist and where. The same for personal information about students, clients or staff: note where it lives, don't copy it, and flag it in the report if it sits in shared files or project docs.

## Step 1: Inventory (tell the owner what you're reading as you go)
Cover each source the chat can reach; for any you can't reach, say so and ask whether to add it:
1. **Folders and files:** the connected project folder(s), recursively. Note the structure, file types, sizes, dates, duplicates, old versions, files in odd places, empty folders.
2. **The Claude Project:** its docs, instructions and memory (if any).
3. **Past conversations:** search past chats for the project name, key terms and people (the past-chats search tools). Note decisions made, open threads, recurring problems, handover notes.
4. **Handover and brief docs** from earlier sessions: what's current, what's stale, what contradicts.
5. **Scheduled tasks and reminders** on the account: what exists, what's working, what's orphaned.
6. **Websites, links and online resources** named in the files (read-only checks: does it load, broken links, outdated wording).
7. **Connected apps and tools** (plugins, connectors, repos, drives, calendars, design tools) and what the project uses them for.
8. **Shared files and folders:** who they're shared with, if visible.
9. **Claude usage:** the plan and weekly reset (ask the owner for a Settings › Usage screenshot), every scheduled task with how often it runs and roughly how heavy it is (light / medium / heavy), long or duplicated chats, work that gets repeated (re-reading big files, rebuilding the same thing), runs whose results nobody reads, and whether usage has run out mid-week. Also which model each session and scheduled task runs on (ask the owner where you can't see it), work running on a bigger model than it needs, and work on a smaller model that keeps missing the mark.
10. **Kit version:** if the project was set up with an older version of this kit (the handover's kit version line, or no line at all), compare it with the kit's CHANGELOG.md and turn what's new into decision items.
11. **Computers and unattended runs:** which computer each scheduled task runs on (or cloud), whether that's the owner's home computer, runs that failed or never fired because a computer was asleep, offline or had Claude closed, and tasks that need the computer but don't use any files (could move to the cloud).

## Step 2: Questions
List what you couldn't work out, then ask in rounds. Always ask about:
- The goal, success measures and deadlines as they stand **today** (they may have changed).
- Who's involved and who decides now.
- Which docs are the "real" current version where several exist.
- What's working well that must not change.
- Anything in the kit's standard setup they don't want (it goes in PROJECT-CHOICES.md). If the owner has a filled-in MY-DEFAULTS.md in a connected folder, use it as starting answers.
- What's frustrating, slow or keeps going wrong.
- Rules: never-do list, budget, approvals, privacy.
- Time, rhythm and how the owner likes updates.
- Claude plan, weekly reset, the share of weekly usage this project should take, what other projects need, and what to do if the project nears its share (question bank §6b).
- Which models show in the owner's model picker, which one they use by default, whether Fable is included or uses paid credits, and which jobs Claude keeps getting wrong or takes too long on.
Use "01 New project/Interview question bank.md" from the kit for anything else the project needs. End with a 10-line summary and "Is this right?"

## Step 3: Recommendation and efficiency report
Write **"<Project> - Audit and recommendations.pdf"** (and the same as AUDIT-REPORT.md) in the project folder. Look at every page before saving. Sections:
1. **Bottom line** (3 lines): health of the project, the biggest problem, the one change that would help most.
2. **What exists:** a short map of folders, docs, sessions/chats, scheduled tasks, tools, sites.
3. **What's working** (keep it).
4. **Problems found**, each with evidence (file, chat or date) and what it costs the owner (time, risk, money).
5. **Recommended workflow:** setup level (Solo, Standard or Team; 03 Templates/Setup levels.md), folder structure (current → proposed, as moves the owner approves), sessions (lead + work sessions), trackers, rhythm (briefs, reports, weekly review), rules.
6. **Tools and resources:** plugins, connectors, skills, apps, processes worth adding (installed or not; always optional); reason, cost if known, setup effort.
7. **Usage and efficiency:** where the project's Claude usage goes now (estimate per scheduled task and kind of work) against the share the owner wants; changes that cut it without losing anything that matters (fewer or lighter runs, heavy jobs moved to early in the usage week, runs that stop early when nothing's new, shorter docs, reusable scripts, fresh chats); and a "pause first" list. **Model fit:** a table of each session, scheduled task and main kind of work with its current model and effort → recommended model and effort, and why (cost or quality).
8. **Clean-up list:** duplicates, stale docs, broken links, orphaned tasks, sharing issues.
9. **Decisions for the owner:** ONE numbered list. Each item: the change, why, and how it gets done: **CLAUDE CAN DO (with your OK)**, **YOU DO (step by step, with minutes)** or **NEEDS A CONNECTOR (which one, what it unlocks)**.
Tell the owner they can answer with "OK 1, 3, 5; not 2; later 4".

## Step 4: Build the approved changes
- Do only the approved items, in a sensible order, checking each one.
- Fill the templates from "03 Templates" (handover, session briefs, rules, trackers, weekly review, cheat sheet, usage plan, model guide; updates inbox at the Team level; only what the setup level calls for), using what you learned, and fill in the handover's kit version line. Record everything that differs from the kit in PROJECT-CHOICES.md, including what the owner wants kept as it is. Mark anything you couldn't confirm "VERIFY".
- Folder changes: never delete. Move old or duplicate files into a "_to_delete" or "Archive" folder and list them for the owner.
- Add a **what could go wrong** list to the handover's §11 (3–5 likeliest reasons the project could still fail, each with a warning sign and what the setup does about it).
- After building, ask the owner for the **fresh chat test** (Prompt 19) and fix the handover if it fails.
- Make **"<Project> - START HERE.pdf"** and **"<Project> - Session prompts.pdf"** (see "04 Prompts to copy", Prompt 3), and with the owner's OK the scheduled tasks.
- Old chats and old scheduled tasks: list them; turn off (don't delete) only with the owner's OK.

## Step 5: Hand over
- This chat becomes the **Lead session** ("<Project> – Lead").
- Tell the owner in 5 lines or less: what changed, the PDF to open, the first session to start, the first thing to do today.
- Log "Audit done <date>" in WORKFLOW-REVIEW.md. The first weekly review checks how the new setup is working.
- Anything about the kit itself that didn't work well goes to KIT-FEEDBACK.md if the kit folder is connected and writable; otherwise tell the owner in one line.
