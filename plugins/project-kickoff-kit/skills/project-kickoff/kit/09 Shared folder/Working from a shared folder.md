# Working from a shared folder

For projects with more than one person (the **Team** level). Everyone's Claude works from **one shared project folder**, so everyone works from the latest information, with no copies passed around. These habits keep it trustworthy when several people's Claudes read and write the same files.

## Set it up (owner, 10 min)
1. **Put the project folder in a shared place:** Dropbox, Google Drive or OneDrive. Share it with each collaborator (**Can edit**).
2. **Each person syncs it to their home computer** and makes it **available offline** (Dropbox: right-click › Make available offline; Google Drive for desktop: right-click › Offline access › Available offline). Claude can only read what's on the computer.
3. **Each person connects it** to their own Claude chats: **+ › Add folder**.
4. Tell the Lead session: **"set this project up for a shared folder"**. Claude adds the layout, CHANGES.md, ASSETS.md and the owners table, names the **project lead** and sets up **backups** (with your OK).

On a Team or Enterprise Claude plan you can also share one Claude Project, so everyone's chats see the same Project docs. On individual plans, the shared folder does that job.

## The layout
```
<Project>/
  <Project> - START HERE.pdf
  00 Admin/
    Handover and briefs/   shared docs + UPDATES-INBOX.md
    CHANGES.md             the change log
  People/
    <name>/                each person's own files
  02 Work in progress/     shared drafts (one owner each)
  03 Final/                approved work only
  04 Assets/
    ASSETS.md              current versions
  05 Reference/
  Archive/
    _versions/             copies saved before every edit
    Backups/               weekly snapshots
  _to_delete/
```

## The five habits
1. **Every shared file has one owner.** The handover lists them ("Shared files and owners"). Only the owner's Claude edits that file. **Protected** files (marked in the same table) also need the project lead's OK first. Everyone else adds an **ASK:** line to UPDATES-INBOX.md, or edits only their own columns in a tracker.
2. **Read CHANGES.md first.** Before any job, each Claude reads the new lines since its last run, then re-reads the files that changed. That's how everyone stays current without re-reading everything.
3. **Log every change to a shared file:** one line in CHANGES.md: date, who, which file, what changed.
4. **Use the current asset.** ASSETS.md marks one version of each asset as current. Claude uses that one, and warns if asked to use a retired version.
5. **Your own work goes in People/<you>/** until it's ready to share. Then the file's owner moves it to the shared place and logs it.

## The project lead
- One person is the **project lead**, named in the handover (usually the project's owner). The lead approves changes to **protected** files and restores.
- **Protected files** (default): the handover, rules, project choices, the owners table, everything in 03 Final and 04 Assets, and ASSETS.md. **Working files** (drafts, trackers, People/ folders) are edited by their owners as usual.
- **To change a protected file:** add an ASK: line to UPDATES-INBOX.md ("ASK: update the logo in ASSETS.md to v4"). The lead's Lead session lists the requests waiting; the lead answers "OK" or "not now". The file's owner then makes the change, and CHANGES.md records "approved by <lead>".
- **Changing the lead:** in the Lead chat, **Prompt 17** ("change project lead to <name>"). It needs the current lead's OK (or the owner's, if the lead is unavailable), and it's logged in CHANGES.md and PROJECT-CHOICES.md.
- **These are rules every collaborator's Claude follows, not locks.** A person can still edit a file by hand. For real protection, the lead makes the protected folders **view-only** for everyone else in Dropbox or Google Drive (folder › Share › set people to "Can view"), where their plan allows it. Claude checks what's possible rather than assuming.

## Backups and undo
1. **Before every edit:** each Claude copies a shared file to `Archive/_versions/<file> <YYYY-MM-DD HHMM>` before changing it. Any change can be undone in seconds.
2. **Weekly snapshot:** a scheduled task zips 00 Admin, 03 Final and 04 Assets into `Archive/Backups/<date>.zip`. It runs on the lead's home computer (or inside the work window, on a laptop) and keeps the last 8; older ones move to _to_delete for the lead to clear.
3. **The sync service's version history** (Dropbox or Google Drive: right-click a file › Version history) is the last safety net. How far back it goes depends on the service and plan.

**To undo something:** in any chat on the project, type **restore <file> to <when>** (Prompt 16), e.g. "restore ASSETS.md to before Tuesday". Claude lists the saved versions and shows what's different, saves the current version first (so the restore can be undone too), and restores after the lead's OK. It's logged in CHANGES.md.

## When something clashes
- **Sync conflict:** Dropbox makes a "conflicted copy" (Google Drive shows two versions). Claude never picks one itself: it lists both, says what differs, and asks the file's owner.
- **Two people need the same file changed:** both send ASK: lines; the owner decides.
- **Someone's Claude edited a file it doesn't own:** the owner's Claude spots it from CHANGES.md and asks before keeping or undoing it. Nothing gets deleted; the old version stays in Archive or the sync service's version history.

## For Claude
- Shared-folder projects follow WORKFLOW-RULES rules 20–23 and this page.
- Before any job: read CHANGES.md since your last run (your brief records the last line you read), then the files it names; check for sync-conflict copies of the files you'll touch.
- Write only files your owner owns (handover "Shared files and owners") or files in People/<your owner>/. Anything else becomes an ASK: line in UPDATES-INBOX.md.
- After every change to a shared file: one line in CHANGES.md (re-read it right before writing; add at the bottom; never edit others' lines).
- Use only the assets ASSETS.md marks current; if a request points to a retired one, say so and ask.
- Protected files (owners table): change only after the project lead's OK, recorded in CHANGES.md ("approved by <lead>"). When running for the lead, list waiting ASK: lines for protected files at the start of each Lead run.
- Before editing any shared file, copy it to Archive/_versions/<file> <YYYY-MM-DD HHMM>; never overwrite or delete a version copy.
- Restore (Prompt 16): list versions (Archive/_versions, Archive/Backups, then the sync service's history), show the differences, save the current version, restore after the lead's OK, log it.
