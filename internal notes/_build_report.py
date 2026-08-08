r"""Build the Unification Report PDF in its original style.

The original (per pdffonts on the v3 archive) is pandoc + xelatex with:
  main = Cambria, mono = Consolas, math = Latin Modern Math (unicode-math),
rendering the source Unicode DIRECTLY (symbols stay symbols — no transliteration).
Consolas lacks a handful of exotic glyphs used inside inline-code spans; those few
are mapped to a Latin Modern Math fallback via \symbol (works inside \texttt, unlike
\ensuremath). Status emoji map to dingbats. That's the whole trick.

Usage: python _build_report.py
"""
import subprocess, os, sys

EDG = r"C:\Users\allen\GitHub\ED Generative"
SRC = "ED_UnifiedFramework_Report.md"
BASE = "ED_UnifiedFramework_Report"

HEADER = r"""
\usepackage{fontspec}
\usepackage{unicode-math}
\usepackage{newunicodechar}
\usepackage{xcolor}
\usepackage{pifont}
\setmainfont{Cambria}
\setmonofont{Consolas}[Scale=0.92]
\setmathfont{Latin Modern Math}
\newfontfamily\symfb{Latin Modern Math}
\setcounter{secnumdepth}{-1}
\providecommand{\tightlist}{}
\usepackage{longtable,booktabs}
% glyphs Consolas lacks inside inline-code spans -> render from Latin Modern Math
% (\symbol works inside \texttt; \ensuremath does not)
\newunicodechar{∈}{{\symfb\symbol{"2208}}}
\newunicodechar{ℝ}{{\symfb\symbol{"211D}}}
\newunicodechar{ℂ}{{\symfb\symbol{"2102}}}
\newunicodechar{ℍ}{{\symfb\symbol{"210D}}}
\newunicodechar{ℤ}{{\symfb\symbol{"2124}}}
\newunicodechar{⟨}{{\symfb\symbol{"27E8}}}
\newunicodechar{⟩}{{\symfb\symbol{"27E9}}}
\newunicodechar{⊕}{{\symfb\symbol{"2295}}}
\newunicodechar{⊗}{{\symfb\symbol{"2297}}}
\newunicodechar{⊊}{{\symfb\symbol{"228A}}}
\newunicodechar{↦}{{\symfb\symbol{"21A6}}}
\newunicodechar{≅}{{\symfb\symbol{"2245}}}
\newunicodechar{≡}{{\symfb\symbol{"2261}}}
\newunicodechar{⟺}{{\symfb\symbol{"27FA}}}
\newunicodechar{⟹}{{\symfb\symbol{"27F9}}}
\newunicodechar{∀}{{\symfb\symbol{"2200}}}
\newunicodechar{ℏ}{{\symfb\symbol{"210F}}}
\newunicodechar{∇}{{\symfb\symbol{"2207}}}
\newunicodechar{∓}{{\symfb\symbol{"2213}}}
\newunicodechar{∝}{{\symfb\symbol{"221D}}}
% status marks -> dingbats (the §2 legend explains them)
\newunicodechar{✅}{{\color{green!55!black}\ding{52}}}
\newunicodechar{⚠}{{\color{orange!90!black}\textbf{!\!}}}
\newunicodechar{📏}{{\color{gray!45!black}\rule[0.05em]{0.9em}{0.5pt}}}
\newunicodechar{⭐}{{\color{orange}\ding{72}}}
\newunicodechar{️}{}
"""

def main():
    os.chdir(EDG)
    open("_report_header.tex", "w", encoding="utf-8").write(HEADER)
    r = subprocess.run(
        ["pandoc", SRC, "-s", "--include-in-header=_report_header.tex",
         "--toc", "--toc-depth=2",
         "-V", "geometry:margin=1in", "-V", "fontsize=10pt",
         "--highlight-style=tango", "-o", BASE + ".tex"],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print("PANDOC FAIL:", (r.stderr or "")[-600:]); sys.exit(1)
    log = ""
    for _ in range(2):
        r = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", BASE + ".tex"],
            capture_output=True, text=True, encoding="utf-8", errors="replace")
        log = r.stdout or ""
    ok = os.path.exists(BASE + ".pdf") and r.returncode == 0
    # report any residual missing glyphs (should be none)
    miss = sorted(set(l for l in log.splitlines() if "Missing character" in l))
    if miss:
        sys.stdout.buffer.write(b"MISSING GLYPHS:\n" +
            "\n".join(miss[:20]).encode("utf-8", "replace") + b"\n")
    if not ok:
        i = log.find("\n!"); print("XELATEX FAIL:\n" + (log[i:i+700] if i >= 0 else log[-700:]))
    for f in [BASE + e for e in (".aux", ".out", ".toc", ".log", ".tex")] + ["_report_header.tex"]:
        if os.path.exists(f):
            try: os.remove(f)
            except OSError: pass
    if ok:
        print(f"OK  {BASE}.pdf  ({os.path.getsize(BASE + '.pdf')//1024} KB)")
    sys.exit(0 if ok and not miss else 1)

if __name__ == "__main__":
    main()
