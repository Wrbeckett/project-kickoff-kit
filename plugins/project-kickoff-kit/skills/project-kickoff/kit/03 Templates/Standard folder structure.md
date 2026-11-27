# Standard project folder structure (Claude adapts this per project)

Start from this, then add, remove or rename folders to fit. Solo-level projects (Setup levels.md) usually need only 00 Admin, 02 Work in progress, 03 Final and Archive. Numbered folders sort to the top in the order people use them.

```
<Project name>/
  <Project> - START HERE.pdf          ← open first (made at kickoff)
  <Project> - Session prompts.pdf     ← one prompt per session
  KICKOFF.md or AUDIT.md              ← kit file that started it all
  00 Admin/
     Handover and briefs/             ← PROJECT-HANDOVER.md, SESSION-BRIEF-*.md, WORKFLOW-RULES.md,
                                         WORKFLOW-REVIEW.md, CHEAT-SHEET.md, USAGE-PLAN.md,
                                         MODEL-GUIDE.md, UPDATES-INBOX.md,
                                         PROJECT-CHOICES.md, DASHBOARD-*.md, trackers
     FILE-MOVES.md                    ← only if Claude organized existing files (undo list)
                                         (or keep these in the Claude Project's docs instead)
     Decisions and notes/
     Receipts and money/              ← only if the project spends money
  01 Briefs and reports/              ← morning briefs, weekly reports, reviews (PDF)
  02 Work in progress/                ← drafts, exports, temporary files, _sync for Claude
  03 Final/                           ← approved, finished deliverables
  04 Assets/                          ← logos, photos, fonts, raw footage, source files
  05 Reference/                       ← research, inspiration, specs, contracts, guides
  Archive/                            ← old versions (nothing is deleted)
     Backups/                         ← zips, e.g. the original files before they were organized
  _To sort/                           ← existing files Claude wasn't sure about (you decide)
  _to_delete/                         ← files waiting for the owner to delete
```

**Team level (shared folder):** add `People/<name>/` for each person's own work, `Archive/_versions/` (copies saved before every edit), `Archive/Backups/` (weekly snapshots), `00 Admin/CHANGES.md` (the change log) and `04 Assets/ASSETS.md` (current versions). See kit › 09 Shared folder.

Common additions, by project type:
- **Website or software:** "Website (deploy this folder)", "Backend", "Releases (private)"; code in GitHub.
- **Product or shop:** "Catalogue", "Orders and shipping", "Suppliers".
- **Marketing or social:** "Social" (Posts, Stories, Captions), "Video" (Raw, Rough cuts, Final).
- **Teaching or course:** "Course outline", "Lessons", "Assessments", "Student-facing".
- **Event:** "Venue", "Guests", "Run sheet", "Vendors".
- **Client work:** "Client brief", "Proofs", "Invoices".

Naming rules: dates as YYYY-MM-DD at the start ("2026-11-19 Morning brief.pdf"); no "final-final"; version numbers as v1, v2.
