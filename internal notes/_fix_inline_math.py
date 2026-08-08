"""
Convert inline backtick-math to $...$ in a markdown paper, prose-preserving.

The build renders `...` (inline code) as monospace; $...$ as proper math. Older
gravity papers wrote inline math in backticks, so it came out as ugly monospace.
This converts ONLY backtick spans that look like math into $...$, braces multi-char
subscripts, and leaves code-like spans (paths, Paper_NNN refs, file names) and all
prose untouched. Display $$...$$ and fenced ``` blocks are protected.

Usage: python _fix_inline_math.py <file.md> [<file2.md> ...]
"""
import re, sys

MATH_CHARS = set(
    "∼≈→↔∝∞√∇∂±×·≤≥≠≡∈∉⊂⊃∪∩°−∓⟨⟩⊗⊕"
    "ρϱΓΦαβγδεζηθϑικλμνξπϖστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    "²³¹⁰⁴⁵⁶⁷⁸⁹⁻⁺ₐₑₒₓₕₖₗₘₙₚₛₜ₀₁₂₃₄₅₆₇₈₉"
    "ℓℏℝℤℂ𝒲𝒩𝒪ϕΘσ"
)

def is_codey(s):
    """Spans that should stay verbatim: file paths, paper refs, filenames.
    A bare '/' is NOT a path signal here — it usually means division."""
    if s.startswith("Paper_") or s.startswith("Papers_"): return True
    if any(d in s for d in ("physics-papers", "event-density",
                            "evaluation/", "foundations/", "position-paper")):
        return True
    if re.search(r"\.(md|py|tex|json|csv|txt|pdf|png)\b", s): return True
    return False

def looks_math(s):
    if len(s) == 1 and (s.isalpha() or s in MATH_CHARS): return True   # single var
    if any(c in MATH_CHARS for c in s): return True
    if "\\" in s: return True            # a LaTeX macro
    if "^" in s: return True             # a superscript
    if "{" in s: return True             # a braced sub/superscript
    if "/" in s: return True             # division
    if re.search(r"[A-Za-z0-9)]_", s): return True   # subscript like r_s, b_int
    if re.search(r"[=<>]", s): return True           # a relation
    return False

def brace_subscripts(s):
    """Brace bare multi-character subscripts: _abc -> _{abc} (leave _{...} and _x)."""
    return re.sub(r"_(?!\{)([A-Za-z0-9]{2,})", r"_{\1}", s)

def convert_span(inner):
    if is_codey(inner) or not looks_math(inner):
        return "`" + inner + "`"
    return "$" + brace_subscripts(inner) + "$"

TOKEN = re.compile(r"(```.*?```|\$\$.*?\$\$|\$[^$\n]+\$|`[^`\n]+`)", re.DOTALL)

def process(text):
    out, last = [], 0
    for m in TOKEN.finditer(text):
        out.append(text[last:m.start()])
        seg = m.group(0)
        if seg.startswith("`") and not seg.startswith("```"):
            out.append(convert_span(seg[1:-1]))
        else:
            out.append(seg)          # protect $$..$$, $..$, ```..```
        last = m.end()
    out.append(text[last:])
    return "".join(out)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            src = f.read()
        new = process(src)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)
        n_before = src.count("`") // 2
        n_after = new.count("`") // 2
        print(f"{path}: backtick spans {n_before} -> {n_after} "
              f"(converted ~{n_before - n_after})")
