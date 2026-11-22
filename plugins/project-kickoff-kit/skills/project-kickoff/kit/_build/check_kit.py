#!/usr/bin/env python3
"""Check the Project Kickoff Kit before a release.

Run:  python3 "_build/check_kit.py"            (report only; changes nothing)
      python3 "_build/check_kit.py" --publish  (also lists files that must NOT be published)

Checks:
 1. Every kit file the instructions mention exists (paths like "03 Templates/X.md", KICKOFF.md, ...).
 2. Every "Prompt N" mentioned exists in 04 Prompts to copy.md.
 3. Every PDF the build script makes exists and is newer than its .md source.
 4. Privacy: personal names, emails, phone numbers, computer paths and private project names
    in files that would be published. Edit PRIVATE_TERMS below to suit.
 5. Placeholders still to fill in before publishing (e.g. <KIT-URL>).
"""
import os, re, sys, glob

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"Accessible versions", "_build", ".git"}
# Files that stay private (never published)
PRIVATE_FILES = {"KIT-FEEDBACK.md", "MY-DEFAULTS.md", "private-terms.txt"}
# Words that point to a real person, client or private project. They live in a private
# file that is never published (_build/private-terms.txt, one per line), so this script can be.
PRIVATE_TERMS = ["/Volumes/", "/Users/"]
_pt = os.path.join(os.path.dirname(os.path.abspath(__file__)), "private-terms.txt")
if os.path.exists(_pt):
    PRIVATE_TERMS += [w.strip() for w in open(_pt, encoding="utf-8") if w.strip() and not w.startswith("#")]
PLACEHOLDERS = ["<KIT-URL>", "<COPYRIGHT HOLDER>"]
# Public addresses that are meant to be published (ignored by the privacy scan)
ALLOWED = ["github.com/Wrbeckett/project-kickoff-kit", "Wrbeckett/project-kickoff-kit", "W.R. Beckett"]
# Template placeholders like <Project> are fine; these are not.

problems, warnings = [], []


def md_files():
    out = []
    for root, dirs, files in os.walk(KIT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.join(root, f))
    return sorted(out)


def rel(p):
    return os.path.relpath(p, KIT)


all_md = md_files()
names = {os.path.basename(p) for p in all_md}
relpaths = {rel(p) for p in all_md}

# 1. referenced files
path_re = re.compile(r"(0\d [A-Z][A-Za-z' ]+?)/([A-Za-z0-9\-' ]+?\.(?:md|pdf))")
bare_re = re.compile(r"\b([A-Z][A-Z\-]+(?:-template)?\.md)\b")
generated = {"PROJECT-HANDOVER.md", "SESSION-BRIEF.md", "WORKFLOW-RULES.md", "WORKFLOW-REVIEW.md", "CHEAT-SHEET.md",
             "USAGE-PLAN.md", "MODEL-GUIDE.md", "UPDATES-INBOX.md", "PROJECT-CHOICES.md", "PROJECT-BLUEPRINT.md",
             "ARCHIVE-LOG.md", "AUDIT-REPORT.md", "MY-DEFAULTS.md", "TRACKER.md", "SKILL.md"}
for p in all_md:
    text = open(p, encoding="utf-8").read()
    for m in path_re.finditer(text):
        target = m.group(1) + "/" + m.group(2)
        if not os.path.isdir(os.path.join(KIT, m.group(1))):
            continue  # a project folder (e.g. "04 Assets/"), not part of the kit
        if not os.path.exists(os.path.join(KIT, target)):
            problems.append(f"{rel(p)}: mentions missing file '{target}'")
    for m in bare_re.finditer(text):
        n = m.group(1)
        if n in names or n in generated:
            continue
        if n.endswith("-template.md") and not os.path.exists(os.path.join(KIT, "03 Templates", n)) and n not in names:
            problems.append(f"{rel(p)}: mentions missing template '{n}'")

# 2. prompts
prompts_md = os.path.join(KIT, "04 Prompts to copy.md")
have = set(int(n) for n in re.findall(r"^## Prompt (\d+)", open(prompts_md, encoding="utf-8").read(), re.M))
for p in all_md:
    for n in re.findall(r"\bPrompt (\d+)\b", open(p, encoding="utf-8").read()):
        if int(n) not in have:
            problems.append(f"{rel(p)}: mentions Prompt {n}, which doesn't exist (have {sorted(have)})")

# 3. PDFs up to date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from make_pdfs import DOCS
    for src, _, _ in DOCS:
        md = os.path.join(KIT, src)
        pdf = os.path.splitext(md)[0] + ".pdf"
        if not os.path.exists(pdf):
            problems.append(f"PDF missing for {src} (run make_pdfs.py)")
        elif os.path.getmtime(pdf) < os.path.getmtime(md):
            problems.append(f"PDF older than its text: {src} (run make_pdfs.py)")
except Exception as ex:
    warnings.append(f"couldn't check PDFs: {ex}")

# 4. privacy + 5. placeholders (only files that would be published)
email_re = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
phone_re = re.compile(r"\b\d{3}[-. ]\d{3}[-. ]\d{4}\b")
for p in all_md:
    if os.path.basename(p) in PRIVATE_FILES:
        continue
    for i, line in enumerate(open(p, encoding="utf-8"), 1):
        for a in ALLOWED:
            line = line.replace(a, "")
        for term in PRIVATE_TERMS:
            if re.search(r"(?<![A-Za-z])" + re.escape(term) + r"(?![a-z])", line):
                warnings.append(f"PRIVACY {rel(p)}:{i}: '{term}' :: {line.strip()[:110]}")
        if email_re.search(line) and "noreply" not in line:
            warnings.append(f"PRIVACY {rel(p)}:{i}: email address :: {line.strip()[:110]}")
        if phone_re.search(line):
            warnings.append(f"PRIVACY {rel(p)}:{i}: phone number :: {line.strip()[:110]}")
        for ph in PLACEHOLDERS:
            if ph in line:
                warnings.append(f"FILL IN {rel(p)}:{i}: {ph}")

print(f"Checked {len(all_md)} text files.")
print(f"\nPROBLEMS ({len(problems)}):")
for x in problems:
    print("  - " + x)
print(f"\nTO REVIEW BEFORE PUBLISHING ({len(warnings)}):")
for x in warnings:
    print("  - " + x)
if "--publish" in sys.argv:
    print("\nNEVER PUBLISH: " + ", ".join(sorted(PRIVATE_FILES)) + " (and anything under a project's own folders)")
sys.exit(1 if problems else 0)
