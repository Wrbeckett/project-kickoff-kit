# New project: step by step

About 10 minutes of setup, then a 20–40 minute interview with Claude. You'll need the Claude desktop app and a place for the project's files.

## 1. Make the project folder (2 min)
1. In Finder (or your file app), open the place your projects live, e.g. **Dropbox**.
2. Make a new folder named after the project, e.g. **"Spring Gala 2027"**.
3. **Using the kit plugin? Stop here:** an empty folder is all you need.
4. **Using the shared kit folder instead?** Open **Project Kickoff Kit › 01 New project** and **copy** (don't move) **KICKOFF.md** into your new project folder.

## 2. Make a Claude Project (2 min)
1. Open the **Claude** app **on your home computer**: the Mac or PC that stays on (see START HERE, "Your home computer"). Scheduled tasks run on the computer you set them up on.
2. In the left sidebar click **Projects** › **New project** (wording may vary slightly by version).
3. Give it the same name as the folder, e.g. **"Spring Gala 2027"**. Add a one-line description.
4. Inside the Project, start a **new chat**.
5. Click the model name next to the send button and pick **Opus** with **Medium** effort for the kickoff (Free plan: **Sonnet**).

## 3. Connect the folder to the chat (1 min)
1. In the new chat, click the **+** button next to the message box.
2. Choose **Add folder** and pick your project folder.
3. Approve the access prompt.

You should see: the folder's name shown as connected in the chat.

## 4. Paste the start prompt (1 min)
With the plugin, just type **start a new project**. With the kit folder, copy **Prompt 1** from **04 Prompts to copy** and paste it into the chat:

> Please read KICKOFF.md in the connected folder and start the new-project kickoff. Ask me everything you need before you build anything.

Or, if you've added the skill: just type **"start a new project"**.

If you've filled in your own **MY-DEFAULTS.md** (a copy of the kit's MY-DEFAULTS-template.md, kept in your own folder), connect that folder too (+ › Add folder) so Claude starts from your defaults. Using the kit folder instead of the plugin? Connect it too.

## 5. Answer the interview (20–40 min)
- Claude asks a few questions at a time, often as buttons. Pick one or type your own answer.
- "I don't know yet" is a fine answer; Claude will note it as an open question.
- Want something done differently from the kit? Say so. Claude records it in the project's PROJECT-CHOICES.md and keeps it.
- Claude also asks which Claude plan you have and how much of your weekly usage the project may use. **Settings › Usage** shows your plan, your weekly limit and when it resets; a screenshot is the easiest answer.
- At the end, Claude reads back a summary. Correct anything that's off.

## 6. Approve the blueprint (5 min)
Claude shows the plan: the setup level (Solo, Standard or Team), folders, sessions (separate chats with their own jobs), trackers, briefs and reports, a usage plan (what each part costs from your weekly usage, and what to pause first if you run high), the Claude model and effort for each session and scheduled job, tools worth adding, and rules. Change anything you like, then say **"OK, build it."**

## 7. Let Claude build, then open your PDFs
Claude creates the folders and files, then two PDFs in your project folder:
- **"<Project> - START HERE.pdf"**: how this project runs and your first steps.
- **"<Project> - Session prompts.pdf"**: the chat name, the model to pick and the one prompt to paste for each extra session.

If Claude suggests scheduled briefs or reports, it asks before creating them.

## 8. Start your other sessions (2 min each)
For each session in the Session prompts PDF:
1. On your home computer, in the same Claude Project, start a **new chat**.
2. Rename it to the name in the PDF (click the chat title).
3. Connect the project folder (+ › Add folder).
4. Pick the model and effort the PDF lists: click the model name next to the send button.
5. Paste its prompt.

## Day to day
- Your first chat is now the **Lead session**. Give it all your updates ("done 3, 5", "workflow idea: …").
- Working with others? They add their updates to **UPDATES-INBOX.md** in the project folder, because only you can post in your Lead chat.
- Want to change anything later? Tell Lead **"change: …"** (Prompt 10).
- Each session reads the handover before it starts and updates it after each finished task.
- Not sure which model a job needs? Check **06 Models and sessions cheat sheet.pdf** in the kit, or ask the session (Prompt 8).
- The weekly review tells you what's working and suggests improvements, including model changes. You choose what changes.
