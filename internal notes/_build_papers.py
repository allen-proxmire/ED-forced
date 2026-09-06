"""Build .tex + .pdf for each Paper_*.md at the EDG root.
Drops the preamble + Series/Status metadata; keeps title + author (Allen Proxmire)
+ date (June 2026) + Abstract onward. Pre-latexifies unicode BEFORE pandoc:
- prose: maximal runs of math-class chars become ONE $...$ expression
  (superscript/subscript runs merged: 'b⁻¹' -> b$^{-1}$, never $^{-}$$^{1}$)
- $$/$ math: chars -> LaTeX commands with letter-guard spacing
- code spans: ASCII transliteration (verbatim-safe)
xelatex compiles; aux files cleaned."""
import subprocess, glob, os, sys, re

EDG = r"C:\Users\allen\GitHub\ED Generative"
os.chdir(EDG)

SUP = {'²': '2', '³': '3', '¹': '1', '⁶': '6', '⁻': '-', '⁰': '0', '⁵': '5',
       '⁴': '4', '⁷': '7', '⁸': '8', '⁹': '9'}
SUB = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', 'ₜ': 't', 'ᵢ': 'i'}
CMD = {  # math-class char -> LaTeX (math mode, no $)
 'ρ': r'\rho', 'Σ': r'\Sigma', 'α': r'\alpha', 'μ': r'\mu', 'ν': r'\nu',
 'π': r'\pi', 'β': r'\beta', 'φ': r'\varphi', 'ε': r'\varepsilon',
 'Δ': r'\Delta', 'Γ': r'\Gamma', 'κ': r'\kappa', 'τ': r'\tau', 'ξ': r'\xi',
 'γ': r'\gamma', 'δ': r'\delta', 'Λ': r'\Lambda', 'Φ': r'\Phi',
 'λ': r'\lambda', 'σ': r'\sigma', 'Ω': r'\Omega', 'θ': r'\theta',
 '∇': r'\nabla', '∂': r'\partial', '∼': r'\sim', '≈': r'\approx',
 '→': r'\to', '∝': r'\propto', '·': r'\cdot', '∈': r'\in', '±': r'\pm',
 '∓': r'\mp', '×': r'\times', '↔': r'\leftrightarrow', '∫': r'\int', '∗': r'\ast', '°': r'^\circ',
 '∞': r'\infty', '≪': r'\ll', '≫': r'\gg', '≠': r'\neq', '⊥': r'\perp',
 '⇒': r'\Rightarrow', '≲': r'\lesssim', '≳': r'\gtrsim', '≡': r'\equiv',
 '⟺': r'\Longleftrightarrow', '⟹': r'\Longrightarrow', '∏': r'\prod',
 '√': r'\surd', '−': '-', 'ℤ': r'\mathbb{Z}', 'ℝ': r'\mathbb{R}', 'ℂ': r'\mathbb{C}',
 'ℍ': r'\mathbb{H}', 'ℓ': r'\ell', 'ℏ': r'\hbar', 'ħ': r'\hbar', '✓': r'\checkmark', '⅓': r'\tfrac{1}{3}',
 '¼': r'\tfrac{1}{4}', '½': r'\tfrac{1}{2}', '⋉': r'\ltimes',
 '≤': r'\le', '≥': r'\ge', '∘': r'\circ', '⊕': r'\oplus', 'ḃ': r'\dot{b}',
 'Θ': r'\Theta', '𝒲': r'\mathcal{W}', 'Ψ': r'\Psi', 'ω': r'\omega', 'ḧ': r'\ddot{h}',
 'ψ': r'\psi', '𝒜': r'\mathcal{A}', '⟨': r'\langle', '⟩': r'\rangle', '□': r'\Box', '′': r"'",
 '⋆': r'\star', 'Π': r'\Pi', '⊊': r'\subsetneq', '⊗': r'\otimes',
 # added 2026-09-06 for ED_UnifiedFramework_Report: three from the currency
 # pass, four scorecard marks no Paper_* had ever used.
 'ℰ': r'\mathcal{E}', '↦': r'\mapsto', '∀': r'\forall', '≅': r'\cong',
 '✅': r'\checkmark', '⚠': r'\triangle', '📏': r'\square', '⭐': r'\bigstar',
}
CODE = {  # transliteration for code spans / fenced code (verbatim-safe ASCII)
 'ℰ': 'E', '↦': '->', '∀': 'forall', '≅': '~=', '✅': '[ok]',
 '⚠': '[!]', '📏': '[m]', '⭐': '[*]', 'ᵢ': 'i',
 'ρ': 'rho', 'Σ': 'Sigma', 'α': 'alpha', 'μ': 'mu', 'ν': 'nu', 'π': 'pi',
 'β': 'beta', 'φ': 'phi', 'ε': 'eps', 'Δ': 'Delta', 'Γ': 'Gamma',
 'κ': 'kappa', 'τ': 'tau', 'ξ': 'xi', 'γ': 'gamma', 'δ': 'delta',
 'Λ': 'Lambda', 'Φ': 'Phi', 'λ': 'lambda', 'σ': 'sigma', 'Ω': 'Omega',
 'θ': 'theta', '∇': 'grad ', '∂': 'd', '∼': '~', '≈': '~=', '→': '->',
 '∝': '~', '·': '*', '∈': ' in ', '±': '+-', '∓': '-+', '×': 'x',
 '↔': '<->', '∫': 'int ', '∞': 'inf', '≪': '<<', '≫': '>>', '≠': '!=', '∗': '*',
 '⊥': 'perp', '⇒': '=>', '≲': '<~', '≳': '>~', '≡': '==', '⟺': '<=>',
 '⟹': '==>', '∏': 'prod ', '√': 'sqrt', '−': '-', 'ℤ': 'Z', 'ℝ': 'R', 'ℂ': 'C',
 'ℍ': 'H', 'ℓ': 'l', 'ℏ': 'hbar', 'ħ': 'hbar', '✓': 'OK', '⅓': '1/3', '¼': '1/4', '½': '1/2',
 '⋉': 'x', '≤': '<=', '≥': '>=', '∘': 'o', '⊕': '(+)', '⋆': '*',
 '—': '--', '–': '-', '§': 'sec.', '…': '...', 'ḃ': 'b-dot',
 'Θ': 'Theta', '𝒲': 'Wcal', 'Ψ': 'Psi', 'ω': 'omega', 'ḧ': 'h_tt',
}
TEXT_OK = set('—–§…öřČéüïàáèó“”')  # raw text chars Latin Modern handles
# U+FE0F is a zero-width emoji variation selector and U+0304 a combining
# macron; both are stripped/folded before anything else looks at the text.
PRESTRIP = {'\ufe0f': ''}
# A combining macron always trails its base. Both uses in the report are
# SU(N) rep labels inside code spans (`2` vs `2-bar`, `N` vs `N-bar`), so the
# conventional particle-physics ASCII is the base plus 'bar'.
BAR = re.compile('([A-Za-z0-9])' + chr(0x0304))

MATHCLASS = set(SUP) | set(SUB) | set(CMD)

def is_letter(c): return c.isalpha() and ord(c) < 128

def run_to_math(seg):
    """Convert a run of math-class chars to LaTeX (math mode, no $),
    merging sup/sub runs and guarding command-letter collisions."""
    out, i = [], 0
    while i < len(seg):
        c = seg[i]
        if c in SUP:
            j = i
            while j < len(seg) and seg[j] in SUP: j += 1
            out.append('^{' + ''.join(SUP[x] for x in seg[i:j]) + '}'); i = j
        elif c in SUB:
            j = i
            while j < len(seg) and seg[j] in SUB: j += 1
            out.append('_{' + ''.join(SUB[x] for x in seg[i:j]) + '}'); i = j
        else:
            out.append(CMD[c]); i += 1
    return ''.join(out)

def prose_repl(s):
    """In prose: wrap maximal math-char runs as pandoc raw-latex inline spans.
    Raw spans (`\\(...\\)`{=latex}) avoid pandoc's $-adjacency rules (e.g. a
    closing $ followed by a digit is not parsed as math, which breaks tables).
    A bare minus becomes a plain hyphen (no math span needed)."""
    s = re.sub(r'√\s*([0-9]+|[A-Za-z](?:_[A-Za-z0-9])?)',
               lambda m: '`\\(\\sqrt{' + m.group(1) + '}\\)`{=latex}', s)
    s = s.replace('√', '`\\(\\sqrt{\\,}\\)`{=latex}')
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c in MATHCLASS:
            j = i
            while j < len(s) and s[j] in MATHCLASS: j += 1
            seg = s[i:j]
            if set(seg) <= {'−'}:
                out.append('-' * len(seg))          # plain text minus
            else:
                out.append('`\\(' + run_to_math(seg) + '\\)`{=latex}')
            i = j
        else:
            out.append(c); i += 1
    return ''.join(out)

def math_repl(s):
    """Inside $...$ / $$...$$: replace maximal math-char runs with commands,
    merging sup/sub runs (so 'b⁻¹' -> b^{-1}, never b^{-}^{1}); letter-guard spacing."""
    # √ -> proper \sqrt{...} (the CMD map's \surd sits low and leaves its operand uncovered):
    #   √(...) -> \sqrt{...}; √token (with an optional _sub) -> \sqrt{token}; bare √ -> \sqrt{\,}
    s = re.sub(r'√\s*\(([^()]*)\)', r'\\sqrt{\1}', s)
    s = re.sub(r'√\s*([A-Za-z0-9]+(?:_(?:\{[A-Za-z0-9]+\}|[A-Za-z0-9]))?)', r'\\sqrt{\1}', s)
    s = s.replace('√', r'\sqrt{\,}')
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c in MATHCLASS:
            j = i
            while j < len(s) and s[j] in MATHCLASS:
                j += 1
            rep = run_to_math(s[i:j])   # merges consecutive SUP/SUB into one ^{}/_{}
            # a sub/superscript operand that is a brace-bearing macro (e.g. 𝒲 -> \mathcal{W})
            # must be wrapped, so '_𝒲' -> '_{\mathcal{W}}' not the invalid '_\mathcal{W}'
            if i > 0 and s[i - 1] in '_^' and '{' in rep:
                rep = '{' + rep + '}'
            # if command ends in a letter and next source char is an ASCII letter, pad
            if rep and rep[-1].isalpha() and j < len(s) and is_letter(s[j]):
                rep += ' '
            out.append(rep)
            i = j
        else:
            out.append(c)
            i += 1
    return ''.join(out)

def code_repl(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c in SUP:  # merge sup runs: 10⁻¹⁶ -> 10^-16
            j = i
            while j < len(s) and s[j] in SUP: j += 1
            out.append('^' + ''.join(SUP[x] for x in s[i:j])); i = j
        elif c in SUB:
            j = i
            while j < len(s) and s[j] in SUB: j += 1
            out.append('_' + ''.join(SUB[x] for x in s[i:j])); i = j
        else:
            out.append(CODE.get(c, c)); i += 1
    return ''.join(out)

TOKEN = re.compile(r'(```.*?```|\$\$.*?\$\$|`[^`\n]*`|\$[^$\n]+\$)', re.DOTALL)

def prepass(text):
    for k, v in PRESTRIP.items():
        text = text.replace(k, v)
    text = BAR.sub(lambda m: m.group(1) + 'bar', text)
    return text


def latexify(text):
    text = prepass(text)
    out, last = [], 0
    for m in TOKEN.finditer(text):
        out.append(prose_repl(text[last:m.start()]))
        seg = m.group(0)
        out.append(code_repl(seg) if seg.startswith('`') else math_repl(seg))
        last = m.end()
    out.append(prose_repl(text[last:]))
    return ''.join(out)

def coverage_check(targets):
    miss = set()
    for f in targets:
        for ch in prepass(open(f, encoding='utf-8').read()):
            if ord(ch) > 127 and ch not in MATHCLASS and ch not in TEXT_OK:
                miss.add(ch)
    if miss:
        print('UNMAPPED:', ' '.join(f'U+{ord(c):04X}' for c in sorted(miss)))
        sys.exit(2)

def header(workdir):
    open(os.path.join(workdir, 'header.tex'), 'w', encoding='utf-8').write(
        '\\usepackage{amsmath}\n\\usepackage{amssymb}\n'
        '\\setcounter{secnumdepth}{-1}\n\\providecommand{\\tightlist}{}\n'
        '\\usepackage{microtype}\n')

def yesc(s): return s.replace('\\', '').replace('"', '\\"')

_META = ('series:', 'status:', 'repository:', 'companions:', 'allen proxmire')
_DATE = re.compile(r'(january|february|march|april|may|june|july|august|september'
                   r'|october|november|december)\s+\d{4}$')

def front_matter(lines):
    """(meta, body_index) if the file opens with YAML front matter, else ({}, None).

    Front matter is an explicit statement of what is metadata and what is body,
    so when it is present it wins: nothing after it is dropped as preamble.
    """
    if not lines or lines[0].strip() != '---':
        return {}, None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            meta = {}
            for l in lines[1:i]:
                if ':' in l:
                    k, v = l.split(':', 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            return meta, i + 1
    return {}, None


def body_start(lines):
    """Index where the rendered body begins.
    House papers: jump to '## Abstract' (drops the does-not-claim preamble + metadata).
    Letters / maps (no Abstract): keep everything after the title's front-matter block
    (author/date/Series/Status/Repository lines + the '---' rule) — so intro content
    that sits ABOVE the first '## ' heading is NOT dropped."""
    for i, l in enumerate(lines):
        if l.strip() == '## Abstract':
            return i
    ti = next(i for i, l in enumerate(lines) if l.startswith('# '))
    i = ti + 1
    while i < len(lines):
        bare = lines[i].strip().replace('*', '').strip()
        low = bare.lower()
        if bare == '' or bare == '---' or low.startswith(_META) or _DATE.match(low):
            i += 1
        else:
            break
    return i

def build(md):
    """Build tex+pdf BESIDE the source md (in its own directory)."""
    workdir = os.path.dirname(os.path.abspath(md)) or '.'
    name = os.path.basename(md)
    base = name[:-3]
    lines = open(md, encoding='utf-8').read().splitlines()
    meta, fm_end = front_matter(lines)
    if meta:
        title = meta.get('title', base)
        subtitle = meta.get('subtitle', '')
        ai = fm_end                      # front matter declared it; keep all of it
    else:
        title = next(l[2:].strip() for l in lines if l.startswith('# '))
        # subtitle = the first '## ' heading before '## Abstract' (the part-line)
        subtitle = next((l[3:].strip() for l in lines
                         if l.startswith('## ') and l.strip() != '## Abstract'), '')
        ai = body_start(lines)
    body = latexify('\n'.join(lines[ai:]))
    front = ('---\n'
             f'title: "{yesc(title)}"\n'
             + (f'subtitle: "{yesc(subtitle)}"\n' if subtitle else '')
             + f'author: "{yesc(meta.get("author", "Allen Proxmire"))}"\n'
             + f'date: "{yesc(meta.get("date", "June 2026"))}"\n'
             + 'geometry: margin=1.1in\nfontsize: 11pt\n---\n\n')
    header(workdir)
    open(os.path.join(workdir, '_tmp.md'), 'w', encoding='utf-8').write(front + body)
    r = subprocess.run(['pandoc', '_tmp.md', '-s', '--include-in-header=header.tex',
                        '-o', base + '.tex'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', cwd=workdir)
    if r.returncode != 0:
        print(('  PANDOC FAIL ' + md + ': ' + (r.stderr or '')[-400:])
              .encode('ascii', 'replace').decode())
        return False
    log = ''
    for _ in range(2):
        r = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error',
                            base + '.tex'], capture_output=True, text=True,
                           encoding='utf-8', errors='replace', cwd=workdir)
        log = r.stdout or ''
    ok = os.path.exists(os.path.join(workdir, base + '.pdf')) and r.returncode == 0
    if not ok:
        idx = log.find('\n!')
        snip = log[idx:idx + 600] if idx >= 0 else log[-600:]
        print(('  XELATEX FAIL ' + md + ':\n' + snip).encode('ascii', 'replace').decode())
    clean(workdir, base)
    return ok

def clean(workdir, base):
    for f in [base + '.aux', base + '.out', base + '.toc', base + '.log',
              'header.tex', '_tmp.md']:
        p = os.path.join(workdir, f)
        if os.path.exists(p):
            try: os.remove(p)
            except OSError: pass

if __name__ == '__main__':
    # argument: a glob (may include a path), e.g. "physics-papers/gravity/Paper_KM*.md";
    # default: Paper_*.md at the repo root (legacy behavior).
    pattern = sys.argv[1] if len(sys.argv) > 1 else 'Paper_*.md'
    targets = sorted(glob.glob(pattern))
    if not targets:
        print('no targets match', pattern); sys.exit(2)
    coverage_check(targets)
    res = {}
    for md in targets:
        print('building', md, flush=True); res[md] = build(md)
    print('\n=== SUMMARY ===')
    for md, ok in res.items():
        pdf = md[:-3] + '.pdf'
        sz = os.path.getsize(pdf) if os.path.exists(pdf) else 0
        print(f'  {"OK " if ok else "FAIL"}  {md[:-3]}  ({sz // 1024} KB)')
    sys.exit(0 if all(res.values()) else 1)
