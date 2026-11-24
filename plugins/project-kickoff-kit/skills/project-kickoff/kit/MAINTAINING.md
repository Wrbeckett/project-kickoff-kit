# Maintaining the Project Kickoff Kit (for whoever updates the kit, and for Claude)

The same process is described in several places on purpose (plain-language guides for people, instruction files for Claude, templates, the skill). This checklist keeps them in step.

## Every change
1. Read KIT-FEEDBACK.md and pick what to change. Agree it with the kit owner.
   **Keep it lean:** with every update, also look for parts of the kit that Claude or the Claude app now does well on its own (new features, better defaults) and remove or shorten them. A smaller kit is easier to follow.
2. Edit the **source of truth** first (table below), then every file listed for that kind of change.
3. Never overwrite in place: write a new file, check it, then replace. Never delete; use _to_delete.
4. Rebuild the PDFs and accessible versions: `python3 _build/make_pdfs.py`. Open every page.
5. Bump the version line in README.md and add an entry to CHANGELOG.md, including what older projects would need (Prompt 9 uses it).
6. If 05 Skill/SKILL.md changed: **propose the skill update** in a Claude chat ("Read 05 Skill/SKILL.md and propose it as an update to my project-kickoff skill"), then click Save. The saved skill is a separate copy.
7. Move the handled lines in KIT-FEEDBACK.md to "Done" with the version.
9. **Run the checker** before every release: `python3 _build/check_kit.py`. It checks that every file and prompt the kit mentions exists and flags personal details before anything is published. Then do the live tests in "Release tests" below.
8. **Never overwrite someone's filled-in MY-DEFAULTS.md** when sharing a new kit version: add new questions as blank lines only. When you share the kit, tell people to keep their own copy.

## Which files each kind of change touches
| Change to… | Source of truth | Also update |
|---|---|---|
| Interview topics or questions | 01 New project/Interview question bank.md | KICKOFF.md step 2, AUDIT.md step 2, SKILL.md, the step-by-step guides if people see it |
| The kickoff process | 01 New project/KICKOFF.md | SKILL.md, New project - step by step.md, 00 START HERE.md (5 steps) |
| The audit process | 02 Existing project/AUDIT.md | SKILL.md, Existing project - step by step.md, 00 START HERE.md |
| A standing rule | 03 Templates/WORKFLOW-RULES-template.md | PROJECT-HANDOVER-template §5 (if it's a core rule), SKILL.md "Standard workflow rules", USAGE-PLAN or MODEL-GUIDE template if it's about usage or models |
| Usage budget | 03 Templates/USAGE-PLAN-template.md | WORKFLOW-RULES rule 13, question bank §6b, KICKOFF step 3, AUDIT step 3 §7, WORKFLOW-REVIEW |
| Models and effort | 06 Models and sessions cheat sheet.md | MODEL-GUIDE template, SKILL.md "Match the model", WORKFLOW-RULES rule 14, step-by-step guides (model picks), CHEAT-SHEET template |
| Setup levels | 03 Templates/Setup levels.md | KICKOFF step 3, AUDIT step 3 §5, SKILL.md, 00 START HERE.md |
| A template's sections | the template itself | KICKOFF step 4 + AUDIT step 4 lists, Standard folder structure.md, README.md, 00 START HERE.md folder table |
| A prompt | 04 Prompts to copy.md | step-by-step guides that quote it, SKILL.md if it names the prompt |
| How projects override the kit | 03 Templates/PROJECT-CHOICES-template.md | WORKFLOW-RULES rule 18, KICKOFF.md, AUDIT.md, SKILL.md, Prompt 10, 00 START HERE.md "Make it yours" |
| Hand off, join, take over | 07 Join or take over a project/HANDOVER-PACK.md, JOIN.md, TAKEOVER.md | the two step-by-step guides in 07, 03 Templates/HANDOVER-PACK-template.md, Prompts 11–13, SKILL.md, 00 START HERE.md (path table), Setup levels.md (Team) |
| Home computer and unattended runs | 00 START HERE.md "Your home computer" | Interview question bank §4b, KICKOFF.md steps 1, 3 and 4.5, AUDIT.md item 11, WORKFLOW-RULES rule 19, handover §9, WORKFLOW-REVIEW "Runs", Prompt 14, SKILL.md, step-by-step guides |
| Shared folder | 09 Shared folder/Working from a shared folder.md | CHANGES and ASSETS templates, handover §8 owners table (lead, Protected column), WORKFLOW-RULES 22–23, Prompts 16–17, WORKFLOW-RULES 20–21, Setup levels (Team), Standard folder structure, JOIN.md, KICKOFF.md step 4, SKILL.md, Something's not working |
| Closing a project | 08 Close a project/CLOSE.md | Prompt 15, SKILL.md, 00 START HERE.md, 00 QUICK START.md |
| Beginner pages | 00 QUICK START.md, 00 Something's not working.md | keep them in step with START HERE, the prompts and the step-by-step guides |
| Where Claude finds the kit | README.md "Finding the kit" | the "Finding the kit" line in KICKOFF, AUDIT, HANDOVER-PACK, JOIN, TAKEOVER, CLOSE and SKILL.md; the GitHub page is https://github.com/Wrbeckett/project-kickoff-kit |
| What's next helper | 10 What's next/NEXT.md | Prompt 18, SKILL.md, 00 QUICK START.md, TRACKER template (Waits on) |
| Starter presets | 03 Templates/Presets/ | KICKOFF.md step 2, 03 Templates/Presets/README.md, Standard folder structure.md (common additions) |
| Blueprint, risks, fresh chat test | 01 New project/KICKOFF.md step 3–4 | AUDIT.md step 4, handover §11, WORKFLOW-REVIEW, Prompt 19, SKILL.md |
| License | LICENSE.md | _build/repo/LICENSE.md (same text), README.md |
| Grow a project | 11 Grow a project/ADD.md, PEOPLE.md | the step-by-step guide in 11, MEMBER template, Prompts 20–22, JOIN.md (role card), HANDOVER-PACK.md, NEXT.md, WORKFLOW-REVIEW, SKILL.md, 00 START HERE, 00 QUICK START, 00 What to type |
| Prompt sheet | 00 What to type.md | keep in step with 04 Prompts to copy, 00 QUICK START and the repo README table (every new prompt goes on all of them) |
| Personal defaults | MY-DEFAULTS-template.md | Interview question bank (keep the two in step) |
| A new file in the kit | — | README.md contents, 00 START HERE.md folder table, _build/make_pdfs.py (if it has a PDF), this table |

## Release tests (before publishing a new version)
1. `python3 _build/check_kit.py` shows no problems.
2. A fresh kickoff in a test Claude Project ("start a new project") gets through the interview and the blueprint.
3. A takeover with a test handover pack ("take over this project") confirms the pack before asking new questions.
4. The kit is found as a plugin (or from GitHub) as well as from the folder.
5. Open every rebuilt PDF.

## Checks every few months
- Keep it lean: which parts could go because Claude now does them itself? (or when the monthly model check flags something)
- Model names, plans and effort levels against Anthropic's help pages (06 cheat sheet; update its "checked" date).
- Menu wording in the step-by-step guides against the current Claude app.
- Lines marked VERIFY anywhere in the kit.

## Publishing to GitHub ("publish the kit")
The public copy lives at https://github.com/Wrbeckett/project-kickoff-kit as a plugin marketplace. Claude does this when you say "publish the kit":
1. Run `python3 _build/check_kit.py` (no problems; review every privacy line).
2. Pack the kit without private files (KIT-FEEDBACK.md, any filled-in MY-DEFAULTS.md, _build/private-terms.txt, .DS_Store, _build/publish, _build/repo) into `_build/publish/`.
3. In the repo: replace `plugins/project-kickoff-kit/skills/project-kickoff/kit/` with the packed kit; copy `05 Skill/SKILL.md` to `plugins/project-kickoff-kit/skills/project-kickoff/SKILL.md`.
4. Bump `version` in `plugins/project-kickoff-kit/.claude-plugin/plugin.json` to match README.md (e.g. 1.6.0), so installed plugins see the update. The repo's own files are kept in `_build/repo/` (README.md for people, marketplace.json, plugin.json, gitignore.txt).
5. `claude plugin validate .` passes; commit ("Kit v<version>") and push. Check the repo page and one PDF link.
