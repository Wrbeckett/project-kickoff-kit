# Prompts to copy

Copy the text in the box and paste it into a Claude chat. Replace anything in <angle brackets>.

## Prompt 1: Start a new project
Use in a new chat, inside the project's Claude Project, with the project folder connected (it contains KICKOFF.md).

```
Please read KICKOFF.md in the connected folder and start the new-project kickoff. Ask me everything you need before you build anything.
```

## Prompt 2: Audit an existing project
Use in a new chat, inside the project's Claude Project, with the project folder connected (it contains AUDIT.md).

```
Please read AUDIT.md in the connected folder and audit this project: folders, files, this Project's docs, past chats, scheduled tasks, websites and connected apps. Read only; change nothing. Then ask me about anything unclear before you write the report.
Websites and links for this project: <paste them here>
```

## Prompt 3: Start a work session
Claude fills this in for each session in "<Project> - Session prompts.pdf", with the model and effort to pick first (click the model name next to the send button). Start every session on the project's home computer. The general form:

```
This is the <Project> – <Session name> session. Before doing anything, read PROJECT-HANDOVER.md and SESSION-BRIEF-<Session name>.md in the connected folder (or the Project docs), plus the docs that brief lists. Take over any scheduled tasks the handover gives this session. Then reply with: the rules for this session, the model and effort it should run on (tell me if this chat is on a different one), my open tasks, your open tasks, and what you'll do first. If something isn't in the docs, ask me; don't guess.
```

## Prompt 4: Fresh start for a session that got long or forgetful
Use in a new chat that replaces an old one (same session name + a date).

```
This replaces the old <Project> – <Session name> chat, which got long. Read PROJECT-HANDOVER.md and SESSION-BRIEF-<Session name>.md first, take over this session's scheduled tasks (turn the old copies off, don't delete them), check this chat is on the session's model from MODEL-GUIDE.md, and tell me what's open. Ask me if anything is unclear.
```

Before you switch, ask the old chat: "Update the handover and your brief for a fresh start."

## Prompt 5: Health check (any time)
Use in any session.

```
Health check: re-read the handover, your brief and the rules. Is anything out of date, contradicting, or stuck? Are your scheduled tasks all there and working, and set to run on the home computer (or the cloud)? Is this chat on the right model and effort for its job? List what you find and fix only what I approve.
```

## Prompt 6: Give the lead session an update
Use in the Lead session (only the owner can post there; anyone else adds the same lines to UPDATES-INBOX.md in the project folder). Short forms work:

```
done 3, 5, 7; 9 tomorrow; skip 12
```
```
workflow idea: <your idea>
```

## Prompt 7: Add the skill (if someone shared the kit folder with you)
Use in any chat with the kit folder connected.

```
Read "05 Skill/SKILL.md" in the connected Project Kickoff Kit folder and propose it as a skill for me.
```

## Prompt 8: Which model for this job?
Use in any session before a big or unusual job. Model guide for the kit: **06 Models and sessions cheat sheet**.

```
Which Claude model and effort should I use for this job: <describe the job>? Check MODEL-GUIDE.md (or the kit's Models and sessions cheat sheet) and my plan, and answer in two lines. If it's a new kind of job, offer to add it to MODEL-GUIDE.md.
```

## Prompt 9: Upgrade a project to the latest kit
Use in the project's Lead session, with the project folder connected and the kit available (plugin installed, or the kit folder connected).

```
Upgrade this project to the latest Project Kickoff Kit. Check the kit version line in PROJECT-HANDOVER.md (no line means 1.1 or older), read the kit's CHANGELOG.md, and list only the changes that would help this project and don't clash with PROJECT-CHOICES.md, as one numbered decision list, each marked CLAUDE CAN DO / YOU DO / NEEDS A CONNECTOR. Change nothing until I answer, then update the kit version line.
```

## Prompt 10: Change how this project works
Use in the Lead session. Anything in the setup can change: names, sessions, reports, rhythm, models, folders, rules.

```
change: <what you want different, e.g. no morning brief; a Monday plan instead>
```

Lead says which files it will update, waits for your OK, updates them all, and logs it in PROJECT-CHOICES.md, so reviews and upgrades keep it. To reverse it: `undo change <number>`. To change your defaults for all future projects: `Update my MY-DEFAULTS.md: <what>` (with the folder it's in connected).

## Prompt 11: Make a handover pack (for someone joining or taking over)
Use in the project's Lead chat, or in a new chat inside the Claude Project where the work lives, with the kit connected.

```
Read "07 Join or take over a project/HANDOVER-PACK.md" in the Project Kickoff Kit and make a handover pack for <name>, who is <joining / taking over> this project. Read only; show me the pack before saving it.
```

## Prompt 12: Join a teammate's project
Use in a new chat in your own Claude Project, with the shared project folder (it holds the pack) and the kit connected.

```
I'm joining <Project>. Read "07 Join or take over a project/JOIN.md" in the Project Kickoff Kit and the handover pack in the connected folder. Confirm what's already known with me, ask only what's specific to my role, and change nothing in the shared files except my own.
```

## Prompt 13: Take over a project someone started for you
Use in a new chat in your own Claude Project, with your project folder (holding the pack and its files) and the kit connected.

```
I'm taking over <Project> from <name>. Read "07 Join or take over a project/TAKEOVER.md" in the Project Kickoff Kit and the handover pack in the connected folder. Go through the pack with me, ask only what's missing, then set the project up for me.
```

For the plain-words version of 12 and 13, just type **join this project** or **take over this project** (with the pack in the connected folder).

## Prompt 14: Check (or move) the home computer setup
Use in the Lead session, opened on the computer you want as the home computer.

```
Check this project's home computer setup: which computer is this chat on, which computer (or the cloud) each scheduled task runs on, and whether any runs failed or didn't fire because a computer was asleep, offline, had Claude closed or needed an approval. List what to fix, including moving tasks to this computer, and change nothing until I say OK.
```

Using a laptop? Add: `Set up a work window: <days and times>. Fit the computer tasks inside it, remind me <30> minutes before by <phone notification / email>, and tell me when I can close the laptop.`

To move a task (Prompt 14), Claude re-creates it from this computer, checks it, and turns the old copy off (it doesn't delete it). In the Claude desktop app you can also turn on **"Require this computer"** in a task's settings on the computer it should use.

## Prompt 15: Close (or pause) a finished project
Use in the Lead session.

```
close this project
```

Claude follows 08 Close a project/CLOSE.md: turns off its scheduled tasks (doesn't delete them), writes a final summary, archives drafts, and notes lessons for next time. Nothing happens until you OK the plan. Say **pause this project** instead to keep everything and just stop the runs.

## Prompt 16: Undo a change (restore a shared file)
Use in any chat on the project.

```
restore <file> to <when, e.g. before Tuesday>
```

Claude lists the saved versions (Archive/_versions, the weekly backups, then Dropbox or Google Drive's version history), shows what's different, saves the current version first, and restores after the project lead's OK. It's logged in CHANGES.md.

## Prompt 17: Change the project lead
Use in the Lead chat.

```
change project lead to <name>
```

Needs the current lead's OK (or the owner's, if the lead is unavailable). Claude updates the handover, the rules and the cheat sheet, moves the weekly backup task to the new lead's home computer (with their OK), and logs it.

## Prompt 18: What's next?
Use in any chat on the project, whenever you're not sure what to do.

```
what's next?
```

Claude reads the handover, your brief and the trackers, skips anything that's still waiting on something else, and gives you one next step: what, where (which chat and model), and about how long.

## Prompt 19: Fresh chat test (after setup)
Use once, right after Claude builds the project: open a **new** chat in the same Claude Project, connect the project folder, and paste:

```
Fresh chat test: using only PROJECT-HANDOVER.md and the files it points to, tell me (1) the project's goal and deadline, (2) the most important open item right now, and (3) which session and model I should use for <a typical job>. Then tell me anything in the handover that was unclear or missing.
```

If it can't answer, go back to the setup chat and say "the fresh chat test failed: <what was missing>".
