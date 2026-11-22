# Something's not working

Find your problem, try the fix. If it's still stuck, paste **Prompt 5 (Health check)** in the Lead chat, or ask whoever set the project up with you.

| What happened | Most likely why | What to do |
|---|---|---|
| A scheduled report or brief didn't arrive | The home computer was asleep or off, the Claude app was closed, or it was outside your work window | Wake the computer, open the Claude app, then paste **Prompt 14** in the Lead chat: it checks every task and catches up what was missed |
| A task ran on the wrong computer, or "needs this computer" | It was set up on a different computer (often a laptop) | On the home computer, paste **Prompt 14** and say OK to move the tasks |
| A task stopped and is waiting for approval | Its approval setting asks before acting, and nobody was there | Open the task in the Claude app and approve it; ask Lead whether it should be set to approve automatically |
| "I can't see that folder" / Claude can't find a file | The folder isn't connected to this chat, or it's still syncing | **+ › Add folder** and pick it again; check Dropbox / Google Drive / iCloud is running and synced |
| Claude can't find the kit's files | The plugin isn't installed (or was added mid-chat), or the kit folder isn't connected | Install it: **Plugins** (left sidebar) › **Add** (top right) › **Add marketplace** › **Add from a repository** › type **Wrbeckett/project-kickoff-kit** › **Sync**, then click **Project kickoff kit** › **Add**, then start a **new** chat. Or: GitHub page › **Code** › **Download ZIP**, unzip, and connect that folder (+ › Add folder) |
| You ran out of Claude usage mid-week | Too many heavy jobs, or a long chat | Wait for the reset (Settings › Usage shows when); then ask Lead to pause items on the "pause first" list and move heavy jobs to early in the week |
| A chat got slow, long or forgetful | Long chats get heavy | Ask it: "Update the handover and your brief for a fresh start." Then open a new chat with **Prompt 4** |
| Claude gave a wrong or weak answer | It was missing information, or the model/effort was too low | Check it had the right files; then raise the effort one step; then move up a model (06 Models and sessions cheat sheet) |
| A file looks wrong or got changed | A write went wrong | Claude never deletes: look in the project's **Archive** or **_to_delete** folders, and in Dropbox/Drive version history; tell Lead what you expected |
| Two chats are doing the same job | A session was started twice | Tell Lead: it says which one to keep; turn the other's scheduled tasks off (don't delete) |
| You don't know what to do next | | Ask any project chat **what's next?** |
| You don't know which chat to ask | | Ask **Lead**. When in doubt, always Lead |
| Someone changed or broke a shared file | A mistake, or a change nobody approved | Type **restore <file> to <when>** (Prompt 16): Claude shows the saved versions and what's different, and restores after the project lead's OK |
| Your change to a shared file wasn't made | It's a protected file and is waiting for the lead's OK | Check UPDATES-INBOX.md for your ASK: line; the lead answers it in their Lead chat |
| Two versions of a file ("conflicted copy") | Two people's computers changed it at once | Don't pick one yourself: tell the file's owner; their Claude compares both and asks which to keep (the other goes to Archive) |
| Someone used an old logo or file | The current version wasn't marked | Ask the file's owner to update **04 Assets/ASSETS.md**; everyone's Claude uses what's marked CURRENT |
| A teammate's updates aren't being picked up | They wrote in the wrong place | Their updates go in **UPDATES-INBOX.md** in the project folder, one line each |

**Still stuck?** In the Lead chat, describe what you expected and what happened instead. Claude will look and tell you what it finds before changing anything.
