# Existing project: step by step

About 10 minutes of setup. Claude then audits everything it can reach, asks you questions, and gives you a recommendations report. Nothing changes until you approve it.

## 1. Put the audit file in the project folder (1 min)
1. Open the **Project Kickoff Kit** folder › **02 Existing project**.
2. **Copy** (don't move) **AUDIT.md** into the project's main folder.

## 2. Open (or make) the Claude Project (2 min)
Do this on your **home computer**, the Mac or PC that stays on (see START HERE, "Your home computer"). Scheduled tasks run on the computer you set them up on.
- **If the project already has a Claude Project:** open it and start a **new chat** there. Claude can then read the Project's docs and its past chats.
- **If not:** in the Claude app click **Projects** › **New project**, name it after the project, and start a new chat inside it. Past chats outside the Project can still be searched if "Search and reference chats" is on in Settings.
- **Pick the model:** click the model name next to the send button and choose **Opus** with **High** effort for the audit. It reads a lot and has to judge what matters. Free plan: **Sonnet**.

## 3. Connect everything Claude should look at (2–5 min)
1. In the chat, click **+** › **Add folder** and pick the project folder. Add any other folders the project uses. If you've filled in your own **MY-DEFAULTS.md**, add the folder it's in. Using the kit folder instead of the plugin? Add it too.
2. Make sure the apps the project uses are connected, if you want them audited (Google Drive, Dropbox, GitHub, calendar, email, design tools…): **Settings › Connectors**. You can also add these later, when Claude suggests them.
3. Have ready: the website addresses and any shared links the project uses, and a screenshot of **Settings › Usage** (your Claude plan, weekly limit and reset time).

## 4. Paste the audit prompt (1 min)
Copy **Prompt 2** from **04 Prompts to copy**:

> Please read AUDIT.md in the connected folder and audit this project: folders, files, this Project's docs, past chats, scheduled tasks, websites and connected apps. Read only; change nothing. Then ask me about anything unclear before you write the report.

Or, with the skill added: type **"audit this project"**.

Paste the project's website addresses and links in the same message.

## 5. Let Claude read, then answer its questions (20–40 min)
- Claude tells you what it's reading. It doesn't move or change anything.
- Then it asks about anything unclear: what's current, what's working, what's frustrating, who decides, your time and rules, and how much of your weekly Claude usage the project should take.
- At the end it reads back a summary. Correct anything that's off.

## 6. Read the report and choose
Claude saves **"<Project> - Audit and recommendations.pdf"** in your project folder:
- the bottom line, what exists, what's working, problems found;
- the recommended workflow, tools, how the project uses your Claude usage (and how to make it lighter), which Claude model and effort each session and job should use, and a clean-up list;
- **one numbered list of decisions.** Each says whether **Claude can do it** (with your OK), **you do it** (with steps), or it **needs a connector**.

Reply with something like **"OK 1, 3, 5; not 2; later 4."** Want something done differently from what Claude suggests? Say so; it's recorded in the project's PROJECT-CHOICES.md and kept.

## 7. Claude builds what you approved
Claude makes the approved changes and checks each one. It never deletes: old files go into an "Archive" or "_to_delete" folder for you to clear. Then it makes:
- **"<Project> - START HERE.pdf"** and **"<Project> - Session prompts.pdf"**,
- and, if you agree, scheduled briefs, reports and a weekly review.

## 8. Start your sessions
Same as for a new project: for each session in the Session prompts PDF, start a new chat in the Claude Project, rename it, connect the folder, pick the model the PDF lists, paste its prompt. Your audit chat becomes the **Lead session**: give it all your updates from now on. Team members add theirs to **UPDATES-INBOX.md**.
