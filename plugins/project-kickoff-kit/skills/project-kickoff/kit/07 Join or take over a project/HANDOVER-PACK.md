# HANDOVER-PACK.md: instructions for Claude (making a handover pack)

You are helping the **giver** (the person who has the project's information) make a handover pack: one Markdown file that lets another person's Claude start from what is already known instead of a blank interview. The **receiver** is the person who gets it. Write for the giver in plain words. Never assume; ask.

**Finding the kit:** the files named here ("03 Templates/…", "07 Join or take over a project/…") are in the Project Kickoff Kit, wherever this person has it: (1) **installed as a plugin**: the project-kickoff skill's own folder holds the whole kit (in its kit/ subfolder); (2) a **connected "Project Kickoff Kit" folder**; (3) the kit's **GitHub page** (https://github.com/Wrbeckett/project-kickoff-kit; read the raw files). Use the first you can reach and say which. If none, ask the owner to install the plugin or connect the folder, and don't build anything until the full kit is reachable.

There are two kinds of pack:
- **JOIN:** a teammate joins a project already set up with this kit. The giver stays the owner. The receiver gets their own sessions for their own responsibilities (JOIN.md).
- **TAKEOVER:** the receiver becomes the owner of a project the giver started for them, set up with this kit or not (for example, a consultant handing work over to a client). The giver stays on as an adviser or steps out (TAKEOVER.md).

## Rules
- **Read only.** Making a pack changes nothing in the project, except the one log line in step 7.
- **Label every fact with where it came from** (labels below). Never turn a suggestion into a decision, or the giver's notes into the receiver's own words.
- **Leave out by default** (step 4), and show the giver what was left out.
- **The giver reviews the pack before it is saved,** and the giver sends it. Claude never emails, shares or uploads it.
- Keep it short: about 6 pages at most. Point to files instead of copying big ones.

## Labels
- **[DECIDED]**: agreed by the person who decides (say who and when).
- **[CONFIRMED BY <receiver>]**: the receiver said it themselves (in a message, meeting notes, a form).
- **[GIVER'S NOTES]**: what the giver observed, gathered or wrote.
- **[CLAUDE'S SUGGESTION]**: ideas, drafts, plans or recommendations nobody has agreed to yet.
- **[VERIFY]**: unclear, old or contradicting; the receiver's Claude must ask.

## Step 1: Three questions (multiple choice, recommendation first)
1. JOIN or TAKEOVER?
2. Who is the receiver: name, role, and how they'll use Claude (their own account? plan, if known).
3. The giver's role afterwards. JOIN: owner (default). TAKEOVER: **stay as adviser** (recommended; say how they can be reached and what they'll help with) or **hand off fully**.

## Step 2: Gather (read only; say what you're reading)
- **Project set up with this kit:** PROJECT-HANDOVER.md, WORKFLOW-RULES.md, PROJECT-CHOICES.md, CHEAT-SHEET.md, the briefs, trackers (summary only), open tasks, setup level, kit version.
- **Project not set up with this kit:** the Claude Project's docs and instructions, past chats in this Project (past-chats search), connected folders, related scheduled tasks, notes, emails or forms the giver points to.
- Note the source of every fact (file, chat and date). Say which sources you couldn't reach.

## Step 3: Sort and label
Fill the sections of 03 Templates/HANDOVER-PACK-template.md. For each fact, add its label. Where your notes and the receiver's own words disagree, keep both and mark it [VERIFY].

## Step 4: Leave out by default (the giver can tick any of these back in)
- The giver's own Claude plan, usage, MY-DEFAULTS and other projects.
- **The giver's private notes and opinions about the receiver**: their budget, how they work, their personality, anything the receiver would be surprised or hurt to read. (The receiver will read this pack.)
- Passwords, keys, logins, account and card numbers: write only "exists; ask <giver>".
- Personal information about other people (the kit's sensitive-information rule).
- Chats and files unrelated to this project.
Then ask: "Anything else to leave out, or anything to add?"

## Step 5: Write the pack
Save as **"HANDOVER-PACK - <Project> - <receiver> - <YYYY-MM-DD>.md"** (new name; check it). In section 11 mark which interview topics are already answered, so the receiver's Claude skips them. List the files to send with it in section 10, split into **in this zip / folder** and **online** (e.g. a kit guide on GitHub), so nothing is listed as "sent" that isn't; with the giver's OK, copy them into a folder "<Project> handover files" next to the pack.

## Step 6: Review with the giver
Show a short summary: what's in, what's left out (headings only), the [VERIFY] list, the files to send. Make their changes, then save the final version and check it.
**Offer a zip (TAKEOVER; recommended for anyone new to this):** with the giver's OK, make **"<Project> - handover for <receiver>.zip"** next to the pack, holding one top folder named after the project with:
- the pack;
- the "handover files" folder, if any;
- **READ ME FIRST.txt** in plain words, in this order:
  0. **Get Claude:** sign up (a paid plan is needed for the kit plugin; the pack says which plan was discussed) and install the **Claude desktop app** on the computer that stays on.
  1. **Unzip this** (double-click, Mac or Windows).
  2. **Move the folder** to where you'll keep the project, ideally Dropbox, Google Drive or iCloud on that computer.
  3. **Install the kit plugin** (before making the chat, so it's loaded): in the Claude desktop app: **Plugins** (left sidebar) › **Add** (top right) › **Add marketplace** › **Add from a repository** › type **Wrbeckett/project-kickoff-kit** › **Sync**, then click **Project kickoff kit** › **Add**. If that doesn't work: GitHub page › **Code** › **Download ZIP**, unzip, and connect that folder in step 4. (Using a shared kit folder instead? Connect it in step 4.)
  4. **Make a Claude Project** with the same name, start a **new** chat in it, **+ › Add folder** › this folder, pick **Opus** with **Medium** effort.
  5. **Type "take over this project".**
  Then: who to ask (<giver, how to reach them>), and "no passwords or logins are in this folder".
Never put passwords, keys or logins in the zip (they're shared separately, in person). Never include the kit itself. Check the zip opens and lists the right files; tell the giver its size (email usually takes up to about 20 MB; bigger, send a Dropbox or Drive link).
Tell the giver how to send it: the zip by email or link (or a shared folder) for a TAKEOVER; for a JOIN, share the project folder (and the pack in it). Point the receiver to **07 Join or take over a project › Join or take over - step by step.pdf**.

## Step 7: Log it
- JOIN (kit project): add one line to WORKFLOW-REVIEW.md and the handover's §12 Next steps: "Handover pack for <receiver> made <date>; add them to People and the cheat sheet once they've joined." If UPDATES-INBOX.md doesn't exist, offer to create it (Team level), with the owner's OK.
- TAKEOVER: add "Handover pack for <receiver> made <date>" to the giver's project handover or notes, and list what the giver still owes (files, intros, access).
