#!/usr/bin/env python3
"""Rebuild the Project Kickoff Kit PDFs from their Markdown sources.

Run from anywhere:  python3 "_build/make_pdfs.py"            (all PDFs)
                    python3 "_build/make_pdfs.py" "06 Models"  (only names containing the text)
Needs: Python 3 + reportlab (pip install reportlab).
Writes each PDF under a new temporary name, checks it, then replaces the old one.\nAlso writes an accessible HTML copy of each guide into "Accessible versions/" (needs: pip install markdown).
"""
import os, re, sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                ListFlowable, ListItem, HRFlowable, KeepTogether)

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (markdown source, footer label, compact layout?)
DOCS = [
    ("00 START HERE.md", "Start Here", False),
    ("00 QUICK START.md", "Quick start", True),
    ("00 Something's not working.md", "Something's not working", True),
    ("01 New project/New project - step by step.md", "New project - step by step", False),
    ("02 Existing project/Existing project - step by step.md", "Existing project - step by step", False),
    ("04 Prompts to copy.md", "Prompts to copy", False),
    ("06 Models and sessions cheat sheet.md", "Models and sessions cheat sheet", True),
    ("07 Join or take over a project/Hand off - step by step.md", "Hand off - step by step", False),
    ("07 Join or take over a project/Join or take over - step by step.md", "Join or take over - step by step", False),
    ("09 Shared folder/Working from a shared folder.md", "Working from a shared folder", False),
]

INK = colors.HexColor("#1F2328")
BLUE = colors.HexColor("#2563A8")
GREY = colors.HexColor("#6B7280")
RULE = colors.HexColor("#D0D7DE")
HEAD_BG = colors.HexColor("#EEF2F7")
CODE_BG = colors.HexColor("#F3F4F6")
MODEL_COLORS = {"Haiku": "#0F766E", "Sonnet": "#1D4ED8", "Opus": "#6D28D9", "Fable": "#B45309"}

# Helvetica (built-in) covers WinAnsi only; swap anything it can't draw.
CHAR_MAP = {"→": "›", "⇨": "›", "≤": "<=", "≥": ">=", "✓": "x",
            "←": "‹", "≈": "~"}


def styles(compact):
    b = 9.2 if compact else 10
    s = {
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=22, leading=27,
                                textColor=INK, spaceAfter=4),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13.5 if compact else 15,
                             leading=18, textColor=BLUE, spaceBefore=10 if compact else 14,
                             spaceAfter=5, keepWithNext=1),
        "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=11.5, leading=15,
                             textColor=INK, spaceBefore=8, spaceAfter=3, keepWithNext=1),
        "body": ParagraphStyle("body", fontName="Helvetica", fontSize=b, leading=b * 1.38,
                               textColor=INK, spaceAfter=5),
        "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=b - 1, leading=(b - 1) * 1.3,
                               textColor=INK),
        "hcell": ParagraphStyle("hcell", fontName="Helvetica-Bold", fontSize=b - 1,
                                leading=(b - 1) * 1.3, textColor=INK),
        "code": ParagraphStyle("code", fontName="Courier", fontSize=b - 1, leading=(b - 1) * 1.35,
                               textColor=INK, backColor=CODE_BG, borderPadding=7,
                               spaceBefore=6, spaceAfter=10, leftIndent=7, rightIndent=7),
        "quote": ParagraphStyle("quote", fontName="Helvetica-Oblique", fontSize=b,
                                leading=b * 1.38, textColor=INK, leftIndent=14,
                                borderColor=BLUE, borderWidth=0, spaceAfter=6),
    }
    return s


def inline(text):
    for k, v in CHAR_MAP.items():
        text = text.replace(k, v)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)

    def bold(m):
        inner = m.group(1)
        mm = re.fullmatch(r"(Haiku|Sonnet|Opus|Fable)( [\d.]+)?", inner)
        if mm:
            return '<font color="%s"><b>%s</b></font>' % (MODEL_COLORS[mm.group(1)], inner)
        return "<b>%s</b>" % inner
    text = re.sub(r"\*\*(.+?)\*\*", bold, text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", text)
    return text


def make_table(rows, st, width):
    ncol = len(rows[0])
    weights = []
    for c in range(ncol):
        longest = max(len(r[c]) if c < len(r) else 0 for r in rows)
        weights.append(max(8, min(longest, 48)) + 4)
    # every column at least as wide as its longest word, the rest shared by content length
    from reportlab.pdfbase.pdfmetrics import stringWidth
    fs = st["cell"].fontSize
    mins = []
    for c in range(ncol):
        words = [w for r in rows if c < len(r) for w in re.sub(r"[*`]", "", r[c]).split()]
        mins.append(max([stringWidth(w, "Helvetica-Bold", fs) for w in words] + [20]) + 12)
    tot = sum(weights)
    widths = [max(m, width * w / tot) for m, w in zip(mins, weights)]
    extra = sum(widths) - width
    if extra > 0:
        flex = [i for i in range(ncol) if widths[i] > mins[i]]
        room = sum(widths[i] - mins[i] for i in flex) or 1
        for i in flex:
            widths[i] -= extra * (widths[i] - mins[i]) / room
    data = []
    for i, r in enumerate(rows):
        r = (r + [""] * ncol)[:ncol]
        data.append([Paragraph(inline(c), st["hcell"] if i == 0 else st["cell"]) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEAD_BG),
        ("GRID", (0, 0), (-1, -1), 0.5, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def split_row(line):
    line = line.strip().strip("|")
    return [c.strip() for c in line.split("|")]


def parse(md, st, width):
    lines = md.splitlines()
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith("```"):
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            txt = "<br/>".join(re.sub(r"(?<= ) |^ ", "&nbsp;", inline(x)) for x in buf)
            out.append(Paragraph(txt, st["code"]))
            continue
        if s.startswith("# "):
            out.append(Paragraph(inline(s[2:]), st["title"]))
            out.append(HRFlowable(width="100%", thickness=2, color=BLUE, spaceBefore=2, spaceAfter=10))
            i += 1
            continue
        if s.startswith("### "):
            out.append(Paragraph(inline(s[4:]), st["h3"]))
            i += 1
            continue
        if s.startswith("## "):
            out.append(Paragraph(inline(s[3:]), st["h2"]))
            i += 1
            continue
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                r = split_row(lines[i])
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in r if c):
                    rows.append(r)
                i += 1
            out.append(make_table(rows, st, width))
            out.append(Spacer(1, 7))
            continue
        if s.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(Paragraph(inline(" ".join(buf)), st["quote"]))
            continue
        m_b = re.match(r"^[-*] (.*)", s)
        m_n = re.match(r"^(\d+)\. (.*)", s)
        if m_b or m_n:
            numbered = bool(m_n)
            first_no = int(m_n.group(1)) if m_n else 1
            items = []
            pat = r"^(\d+)\. (.*)" if numbered else r"^[-*] (.*)"
            while i < len(lines):
                m = re.match(pat, lines[i].strip())
                if not m or lines[i].startswith("   "):
                    break
                text = m.group(2) if numbered else m.group(1)
                i += 1
                while (i < len(lines) and lines[i].startswith("   ") and lines[i].strip()
                       and not re.match(r"^\s+[-*] ", lines[i])):
                    text += " " + lines[i].strip()
                    i += 1
                sub = []
                while i < len(lines) and re.match(r"^\s{2,}[-*] ", lines[i]):
                    sub.append(re.sub(r"^\s+[-*] ", "", lines[i]))
                    i += 1
                flow = [Paragraph(inline(text), st["body"])]
                if sub:
                    flow.append(ListFlowable([ListItem(Paragraph(inline(x), st["body"]), leftIndent=12)
                                              for x in sub], bulletType="bullet", start="–",
                                             leftIndent=12, bulletFontSize=8))
                items.append(ListItem(flow, leftIndent=14))
            if numbered:
                lf = ListFlowable(items, bulletType="1", start=first_no, leftIndent=14, bulletFontName="Helvetica",
                                  bulletFontSize=st["body"].fontSize, bulletColor=BLUE)
            else:
                lf = ListFlowable(items, bulletType="bullet", start="•", leftIndent=14,
                                  bulletFontSize=7, bulletColor=BLUE)
            out.append(lf)
            continue
        buf = [s]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||```|> |[-*] |\d+\. )", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        out.append(Paragraph(inline(" ".join(buf)), st["body"]))
    return out


def build(src, label, compact):
    path = os.path.join(KIT, src)
    pdf = os.path.splitext(path)[0] + ".pdf"
    tmp = pdf + ".new.pdf"
    md = open(path, encoding="utf-8").read()
    st = styles(compact)
    margin = 0.6 * inch if compact else 0.75 * inch
    doc = SimpleDocTemplate(tmp, pagesize=letter, leftMargin=margin, rightMargin=margin,
                            topMargin=margin, bottomMargin=0.8 * inch,
                            title=label, author="Project Kickoff Kit")
    width = letter[0] - 2 * margin

    def footer(canvas, d):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(GREY)
        canvas.drawString(margin, 0.45 * inch, "Project Kickoff Kit  ·  " + label)
        canvas.drawRightString(letter[0] - margin, 0.45 * inch, "Page %d" % d.page)
        canvas.restoreState()

    doc.build(parse(md, st, width), onFirstPage=footer, onLaterPages=footer)
    if os.path.getsize(tmp) < 1000:
        raise SystemExit("Check failed, kept the old PDF: " + tmp)
    os.replace(tmp, pdf)
    print("built", os.path.relpath(pdf, KIT))
    build_html(md, pdf, label)


HTML_CSS = """body{font-family:-apple-system,Helvetica,Arial,sans-serif;max-width:46em;margin:2em auto;
padding:0 1em;line-height:1.55;color:#1F2328;font-size:1.05rem}h1{border-bottom:3px solid #2563A8;padding-bottom:.3em}
h2{color:#1d4f88;margin-top:1.6em}table{border-collapse:collapse;width:100%;margin:1em 0}
th,td{border:1px solid #9aa4b2;padding:.45em .6em;text-align:left;vertical-align:top}th{background:#E6ECF4}
pre{background:#F3F4F6;padding:.8em;white-space:pre-wrap;border:1px solid #d0d7de}code{font-size:.95em}
blockquote{border-left:4px solid #2563A8;margin-left:0;padding-left:1em}"""


def build_html(md, pdf, label):
    """Accessible copy: real headings, lists and table headers, readable in any browser and screen reader."""
    try:
        import markdown
    except ImportError:
        print("  (skipped accessible version: pip install markdown)")
        return
    # Python-Markdown needs a blank line before a list or table that follows a paragraph
    fixed, prev = [], ""
    for ln in md.splitlines():
        starts = re.match(r"^(\s*)([-*] |\d+\. |\|)", ln)
        prev_is = re.match(r"^\s*([-*] |\d+\. |\|)", prev)
        if starts and not starts.group(1) and prev.strip() and not prev_is:
            fixed.append("")
        fixed.append(ln)
        prev = ln
    body = markdown.markdown("\n".join(fixed), extensions=["tables", "fenced_code", "sane_lists"])
    body = body.replace("<table>", '<table>').replace("<th>", '<th scope="col">')
    title = "Project Kickoff Kit: " + label
    page = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            "<title>%s</title>\n<style>%s</style>\n</head>\n<body>\n<main>\n%s\n</main>\n"
            "</body>\n</html>\n") % (title, HTML_CSS, body)
    outdir = os.path.join(KIT, "Accessible versions")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, os.path.splitext(os.path.basename(pdf))[0] + ".html")
    tmp = out + ".new"
    open(tmp, "w", encoding="utf-8").write(page)
    if open(tmp, encoding="utf-8").read() != page:
        raise SystemExit("Check failed: " + tmp)
    os.replace(tmp, out)
    print("built", os.path.relpath(out, KIT))


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else ""
    for src, label, compact in DOCS:
        if only in src:
            build(src, label, compact)
