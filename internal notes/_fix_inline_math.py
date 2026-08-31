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
    "∼≈→↔∝∞√∇∂±×·≤≥≠≡∈∉⊂⊃∪∩°−∓⟨⟩⊗⊕□⋆⊊"
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
    # command lines: a long flag, or a familiar executable at the head. These
    # often contain '=' or '/', which would otherwise read as math.
    if " --" in s: return True
    if re.match(r"^(git|python|pip|pandoc|xelatex|cd|ls|grep|find|sed|awk)\s", s): return True
    return False

# Symbol-shaped spans that carry no math CHARACTER but are still math.
# Kept deliberately tight so code spans (paths, calls, filenames) are not caught:
# is_codey() runs first, and these require a short capitalised head or a known
# operator word, not a general identifier.
GROUPY = re.compile(r"^[A-Z][A-Za-z]{0,2}\([^()]*\)$")        # SU(2) SO(3) U(1) Cl(3,1) N(R)
BRACKETY = re.compile(r"^\[[A-Za-z]\w{0,2},\s?[A-Za-z]\w{0,2}\]$")   # [A,A] [A_1, A_2]
#   Deliberately narrow: two SHORT identifiers separated by a comma. A looser rule
#   swept up numeric intervals ([8, 19], [0.3, 0.7]) and prose placeholders
#   ([TO BE FILLED AFTER EXPERIMENT]). Intervals matter most: [3%, 6%] pushed into
#   $...$ puts a LaTeX comment character inside math and eats the rest of the line.
OPWORD = re.compile(r"^(det|tr|Tr|dim|ker|rank|sgn|log|exp)\b")  # det H(k), Tr F

def looks_math(s):
    if len(s) == 1 and (s.isalpha() or s in MATH_CHARS): return True   # single var
    if any(c in MATH_CHARS for c in s): return True
    if GROUPY.match(s): return True      # group / algebra names
    if BRACKETY.match(s): return True    # commutators, anticommutators
    if OPWORD.match(s): return True      # operator applied to something
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

# Operator names must be upright, not italic. LaTeX builtins take a backslash;
# the rest need amsmath's \operatorname. Same word list as OPWORD, so the
# "is an operator" test and the "render an operator" step cannot drift apart.
OPS_BUILTIN = ("det", "dim", "exp", "ker", "log")
OPS_OPNAME = ("Tr", "tr", "rank", "sgn")
_OPRE = re.compile(r"(?<![A-Za-z\\_{])(" + "|".join(OPS_BUILTIN + OPS_OPNAME)
                  + r")(?![A-Za-z])(?!\s*[)\],;=]|$)")   # must have an argument:
#   `1/(2*dim)` uses the word as a noun (followed by a closer), so it stays italic,
#   while `dim V`, `det H(k)`, `Tr(F^2)` are operators applied to something.

def upright_operators(s):
    r"""det H(k) -> \det H(k);  Tr F -> \operatorname{Tr} F. Leaves \det alone."""
    def sub(m):
        w = m.group(1)
        return "\\" + w if w in OPS_BUILTIN else "\\operatorname{" + w + "}"
    return _OPRE.sub(sub, s)

def convert_span(inner):
    if is_codey(inner) or not looks_math(inner):
        return "`" + inner + "`"
    return "$" + upright_operators(brace_subscripts(inner)) + "$"

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
