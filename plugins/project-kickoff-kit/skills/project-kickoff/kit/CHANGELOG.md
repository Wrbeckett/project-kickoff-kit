# Project Kickoff Kit changelog

Each version lists what changed and **what a project built on an older version would need**, so Prompt 9 ("upgrade this project") can offer just those changes. Newest first.

## 1.8.3 (Nov 22, 2026)
From the first real handover pack: READ ME FIRST now starts with getting Claude and the desktop app, installs the kit plugin before the project chat is made (with the exact steps), and the pack's files list separates "in this zip" from "online".
Projects: nothing to change.

## 1.8.2 (Nov 22, 2026)
Hand-off: Claude offers a zip for a takeover (the pack, handover files and a plain-words READ ME FIRST.txt; never logins). Step-by-step guides: with the kit plugin, no need to copy KICKOFF.md or AUDIT.md into the project folder.
Projects: nothing to change.

## 1.8.1 (Nov 22, 2026)
First-run test fixes: the kickoff stops until the chat is inside a Claude Project with the project folder connected (the chat becomes the Lead); when the full kit can't be reached, Claude says so and doesn't build from the summary.
Projects: nothing to change.

## 1.8 (Nov 22, 2026)
Kit (ideas borrowed from other Claude frameworks, rewritten for this kit): "what's next?" helper (10 What's next/NEXT.md, Prompt 18); starter presets (03 Templates/Presets: event, course, website, client job, research); blueprint shown in sections; "what could go wrong" check in the blueprint, handover §11 and weekly review; fresh chat test after building (Prompt 19); "Waits on" in trackers and briefs; keep-it-lean step in MAINTAINING; LICENSE.md; **plugins** recommended as optional tools in the kickoff, audit, blueprint, weekly review and presets.
Projects on 1.7 could add: the "Waits on" column, a what-could-go-wrong table in §11, and a fresh chat test.

## 1.7 (Nov 22, 2026)
Kit: for shared-folder projects, a **project lead** (named in the handover, changed with the current lead's OK), **protected files** that change only with the lead's OK, and **backups**: version copies before every edit, a weekly snapshot task, and **restore** (Prompt 16) with the lead's OK. Rules 22–23, Prompts 16–17, owners table with a Protected column, troubleshooting rows, Quick start line.
Projects with a shared folder could add: the lead line and Protected column in the handover, rules 22–23, the Archive/_versions and Archive/Backups folders, and the weekly snapshot task.

## 1.6 (Nov 22, 2026)
Kit: shared-folder option for Team projects: 09 Shared folder/Working from a shared folder (PDF + MD), CHANGES and ASSETS templates, the handover's "Shared files and owners" table, People/<name>/ folders, rules 20–21, a CHANGES line in briefs, sync-conflict and old-asset rows in Something's not working.
Projects with more than one person could add: the shared-folder layout (tell Lead "set this project up for a shared folder"), rules 20–21 and the owners table.

## 1.5 (Nov 22, 2026)
Kit: works wherever the kit is (plugin, connected folder or GitHub; "Finding the kit" in every instruction file); 00 QUICK START; 00 Something's not working; 08 Close a project (CLOSE.md, Prompt 15: close or pause); phone use in START HERE; MY-DEFAULTS.md is now MY-DEFAULTS-template.md (each person keeps their own copy); _build/check_kit.py and release tests.
Projects on 1.4 could add: nothing required. Close finished projects with Prompt 15 so their scheduled tasks stop.

## 1.4 (Nov 22, 2026)
Kit: a third path, **07 Join or take over a project**: HANDOVER-PACK.md (make a pack), JOIN.md (a teammate joins), TAKEOVER.md (a new owner takes over), two step-by-step guides with PDFs, the HANDOVER-PACK template, Prompts 11–13.
Also: **home computer** guidance (START HERE section for Mac and Windows, interview §4b, blueprint, rule 19, scheduled-task check, handover §9 columns, review check, Prompt 14; **work windows** for laptops with a reminder before and a "done" message after).
Projects on 1.3 or older could add: a home computer line in the handover, rule 19, the "Runs on" and "Approval" columns, and a Prompt 14 check (especially if tasks were set up from a laptop). When someone joins, the owner makes a pack (Prompt 11); JOIN adds MEMBER-<name>.md and the joiner's own briefs, and uses UPDATES-INBOX.md (create it if missing).

## 1.3 (Nov 21, 2026)
Kit: setup levels (Solo / Standard / Team), MAINTAINING.md, KIT-FEEDBACK.md, this changelog, accessible versions of the guides, monthly model check, Prompt 9, MY-DEFAULTS.md (personal defaults for every new project), PROJECT-CHOICES template, Prompt 10 ("change: …").
Projects on 1.2 or older could add:
- **Kit version line** at the top of PROJECT-HANDOVER.md.
- **Setup level** recorded in the handover; Solo projects may fold USAGE-PLAN and MODEL-GUIDE into handover §13.
- **UPDATES-INBOX.md** (Team projects, or anyone besides the owner gives updates); Lead reads it at the start of every run.
- **WORKFLOW-RULES:** rule 5 now trims the handover too (about 2 pages); rule 15 sensitive information; rule 16 updates inbox; rule 17 kit feedback.
- **WORKFLOW-REVIEW:** "Numbers" section (usage share used, jobs redone, reports read) and kit-level ideas sent to KIT-FEEDBACK.md.
- **Handover §5:** sensitive-information rule.
- **PROJECT-CHOICES.md** (every level): what this project does differently from the kit; it wins over kit defaults and upgrades. Make it first in an upgrade, recording the project's existing differences, so the other upgrade steps don't undo them.
- **WORKFLOW-RULES** rule 18 (the owner's choices win) and Prompt 10 ("change: …").

## 1.2 (Nov 21, 2026)
Kit: model and effort recommendations; MODEL-GUIDE template; 06 Models and sessions cheat sheet; _build/make_pdfs.py; Prompt 8.
Projects on 1.1 or older could add:
- **MODEL-GUIDE.md**, a "Model:" line on each session brief, a model column on the cheat sheet, the handover's scheduled-task table and USAGE-PLAN.
- **WORKFLOW-RULES** rule 14 (right model, right effort); **WORKFLOW-REVIEW** "Models" check.

## 1.1 (Nov 19, 2026)
Kit: Claude plan and usage budget; USAGE-PLAN template.
Projects on 1.0 could add: USAGE-PLAN.md, WORKFLOW-RULES rule 13, the usage check in WORKFLOW-REVIEW.

## 1.0
First version.
