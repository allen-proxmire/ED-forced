r"""Build every standalone paper in this folder (Paper_*.md) to .pdf/.tex, corpus report style:
pandoc + xelatex, main=Cambria, mono=Consolas, math=Latin Modern Math (unicode-math),
rendering source Unicode DIRECTLY. Glyphs the mono/main font lacks inside code spans map to a
Latin Modern Math fallback via \symbol (works in \texttt, unlike \ensuremath).

Each paper is expected to open with the 6-line title block:
    # Title / (blank) / **Allen Proxmire** / (blank) / **Month Year** / (blank) / **Series:** ...
The block is stripped and the title/author/date passed as metadata for a centered \maketitle.

Outputs per paper: PDF next to the .md AND to the Zenodo folder; .tex to the tex folder.
Usage: python _build_paper.py            (build all Paper_*.md here)
       python _build_paper.py Paper_X    (build just one, by basename)
"""
import subprocess, os, sys, glob, shutil

FOLDER = os.path.dirname(os.path.abspath(__file__))
ZENODO = r"C:\Users\allen\Desktop\ED Important\ED_pdf_files"
TEXDIR = r"C:\Users\allen\Desktop\ED Important\ED_tex_files"

HEADER = r"""
\usepackage{fontspec}
\usepackage{unicode-math}
\usepackage{newunicodechar}
\setmainfont{Cambria}
\setmonofont{Consolas}[Scale=0.92]
\setmathfont{Latin Modern Math}
\newfontfamily\symfb{Latin Modern Math}
\providecommand{\tightlist}{}
\usepackage{longtable,booktabs,graphicx}
\newunicodechar{∇}{{\symfb\symbol{"2207}}}
\newunicodechar{∝}{{\symfb\symbol{"221D}}}
\newunicodechar{√}{{\symfb\raisebox{1.05ex}{\scalebox{0.62}{\symbol{"221A}}}}}
\newunicodechar{⟹}{{\symfb\symbol{"27F9}}}
\newunicodechar{→}{{\symfb\symbol{"2192}}}
\newunicodechar{↔}{{\symfb\symbol{"2194}}}
\newunicodechar{∈}{{\symfb\symbol{"2208}}}
\newunicodechar{⊥}{{\symfb\symbol{"22A5}}}
\newunicodechar{⟨}{{\symfb\symbol{"27E8}}}
\newunicodechar{⟩}{{\symfb\symbol{"27E9}}}
\newunicodechar{ℏ}{{\symfb\symbol{"210F}}}
\newunicodechar{≫}{{\symfb\symbol{"226B}}}
\newunicodechar{≪}{{\symfb\symbol{"226A}}}
\newunicodechar{⟺}{{\symfb\symbol{"27FA}}}
"""


def build_one(base):
    src = base + ".md"
    raw = open(src, encoding="utf-8").read().splitlines()
    title = raw[0].lstrip("# ").strip()
    body = "\n".join(raw[6:])  # drop the 6-line title block
    open("_paper_header.tex", "w", encoding="utf-8").write(HEADER)
    open("_body.md", "w", encoding="utf-8").write(body)
    common = ["--include-in-header=_paper_header.tex", "-V", "geometry:margin=1in",
              "-V", "fontsize=11pt", "-V", "title=" + title,
              "-V", "author=Allen Proxmire", "-V", "date=July 2026"]
    r = subprocess.run(["pandoc", "_body.md", "-s"] + common + ["-o", base + ".tex"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(f"PANDOC(tex) FAIL [{base}]:", (r.stderr or "")[-800:]); return False
    log = ""
    for _ in range(2):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", base + ".tex"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        log = r.stdout or ""
    ok = os.path.exists(base + ".pdf") and r.returncode == 0
    miss = sorted(set(l for l in log.splitlines() if "Missing character" in l))
    dollar = [l for l in log.splitlines() if "Missing $ inserted" in l]
    if miss:
        sys.stdout.buffer.write((f"MISSING GLYPHS [{base}]:\n").encode() +
                                "\n".join(miss[:25]).encode("utf-8", "replace") + b"\n")
    if dollar:
        print(f"MISSING-$ errors [{base}]: {len(dollar)}")
    if not ok:
        i = log.find("\n!"); print(f"XELATEX FAIL [{base}]:\n" + (log[i:i+900] if i >= 0 else log[-900:]))
    good = ok and not miss and not dollar
    if good:
        shutil.copyfile(base + ".pdf", os.path.join(ZENODO, base + ".pdf"))
        shutil.copyfile(base + ".tex", os.path.join(TEXDIR, base + ".tex"))
        print(f"OK  {base}.pdf  ({os.path.getsize(base + '.pdf')//1024} KB)  -> repo + Zenodo; .tex -> tex folder")
    for f in [base + e for e in (".aux", ".out", ".toc", ".log", ".tex")] + ["_paper_header.tex", "_body.md"]:
        if os.path.exists(f):
            try: os.remove(f)
            except OSError: pass
    return good


def main():
    os.chdir(FOLDER)
    targets = ([sys.argv[1].replace(".md", "")] if len(sys.argv) > 1
               else sorted(b[:-3] for b in glob.glob("Paper_*.md")))
    allok = all(build_one(b) for b in targets)
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
