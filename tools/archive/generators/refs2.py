"""Build references.html: every source cited in The Culture Ladder (v87).
- Sources with a DOI link to it.
- Sources without a DOI link to a free, legitimate copy where one was found
  (issuing body, official archive, open-access publisher page).
- Everything else is listed as a citation only.
Inputs: the DOI list in refs.py (REFS), plus refs_A..D.json from the research agents."""
import html, json, pathlib, re, unicodedata

S = pathlib.Path("/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad")
SITE = pathlib.Path("/home/user/tcl-website")

# 1. The 75 DOI entries already on the page
src = (S / "papers/refs.py").read_text()
ns = {}
exec(src[: src.index("def key")], ns)
entries = []
for a, y, t, so, doi in ns["REFS"]:
    entries.append(dict(authors=a, year=y, title=t, source=so, doi=doi, url=None, type="doi-list", html_source=True))

# Two DOIs printed in the book that the first pass missed
entries += [
    dict(authors="Amalberti, R.", year="2001", title="The paradoxes of almost totally safe transportation systems", source="<i>Safety Science</i>, 37 (2–3), 109–126", doi="10.1016/S0925-7535(00)00045-X", url=None, type="journal", html_source=True),
    dict(authors="Guldenmund, F. W.", year="2000", title="The nature of safety culture: A review of theory and research", source="<i>Safety Science</i>, 34 (1–3), 215–257", doi="10.1016/S0925-7535(00)00014-X", url=None, type="journal", html_source=True),
]

# Papers from the book's Note on Sources that no note cites: take them from the Papers page data
_m = (S / "papers/make.py").read_text()
_ns = {"__name__": "x"}
exec(_m[: _m.index("def entry")], _ns)
_have = {e["doi"].lower() for e in entries}
for _g in _ns["GROUPS"]:
    for a, y, t, v, ident, doi, press in _g[3]:
        if doi.lower() not in _have:
            src = v + (f". {ident}" if ident else "")
            entries.append(dict(authors=a, year=y + (", in press" if press else ""), title=t, source=src, doi=doi, url=None, type="conference", html_source=True))
            _have.add(doi.lower())

# 2. The agents' records
BAD_URL = re.compile(r"bp\.com/bakerpanelreport|acceptatie|theclio\.com|scribd|academia\.edu|researchgate|bit\.ly|"
                     r"iogp\.org/bookstore/product/a-guide-to-selecting")
agent = []
for x in "ABCD":
    agent += json.load(open(S / f"refs_{x}.json"))

def nt(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)[:50]

have_doi = {e["doi"].lower() for e in entries}
have_title = {nt(e["title"]) for e in entries}
added = {}
for r in agent:
    doi = (r.get("doi") or "").strip() or None
    url = r.get("url")
    if url and (BAD_URL.search(url) or r.get("url_kind") not in ("official", "open-access", "given-in-book")):
        url = None
    if doi and doi.lower() in have_doi:
        continue
    k = (doi or "").lower() or nt(r["title"]) + r["year"]
    if nt(r["title"]) in have_title:
        continue
    if k in added:
        # keep the record that has a pointer
        old = added[k]
        if not (old["doi"] or old["url"]) and (doi or url):
            old.update(doi=doi, url=url)
        continue
    rec = dict(authors=r["authors"], year=r["year"], title=r["title"], source=r.get("source") or "",
               doi=doi, url=url, type=r["type"], html_source=False,
               note=r.get("note"), doi_basis=r.get("doi_basis") or ("search" if doi else None),
               url_kind=r.get("url_kind") if url else None, check=r.get("comment") or None)
    added[k] = rec
entries += list(added.values())

def initials(a):
    return re.sub(r"(?<=[A-Z]\.)(?=[A-Z]\.)", " ", a).replace(".-", ". -")

def fmt_source(e):
    if e["html_source"]:
        return e["source"]
    s = html.escape(e["source"], quote=False)
    if e["type"] in ("journal",) and "," in s:
        j, rest = s.split(",", 1)
        s = f"<i>{j}</i>,{rest}"
    return s

def sort_key(e):
    s = unicodedata.normalize("NFKD", e["authors"]).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"^(de|van der|van) ", "", s)
    return (s, e["year"], e["title"].lower())

def letter(e):
    return sort_key(e)[0][:1].upper()

def host(u):
    h = re.sub(r"^https?://([^/:]+).*", r"\1", u)
    return re.sub(r"^www\.", "", h)

def entry(e):
    t = html.escape(e["title"], quote=False); t = re.sub(r"(^|[\s(])'", "\\1&#8216;", t).replace("'", "&#8217;")
    src = fmt_source(e)
    meta = f"{html.escape(initials(e['authors']), quote=False)} ({e['year']})."
    if src:
        meta += f" {src.rstrip('.')}."
    if e["doi"]:
        link = f'<a class="doi" href="https://doi.org/{html.escape(e["doi"])}">doi.org/{html.escape(e["doi"])}</a>'
    elif e["url"]:
        link = f'<a class="doi" href="{html.escape(e["url"])}">Free copy at {html.escape(host(e["url"]))}</a>'
    elif e["type"] == "book":
        link = '<span class="ref-note">Book</span>'
    else:
        link = '<span class="ref-note">Not freely available online</span>'
    return (f'            <li>\n'
            f'              <span class="cite-title">{t}</span>\n'
            f'              <span class="cite-meta">{meta}</span>\n'
            f'              {link}\n'
            f'            </li>')

entries.sort(key=sort_key)
groups = {}
for e in entries:
    groups.setdefault(letter(e), []).append(e)
letters = sorted(groups)
n_doi = sum(1 for e in entries if e["doi"])
n_url = sum(1 for e in entries if not e["doi"] and e["url"])
n_book = sum(1 for e in entries if not e["doi"] and not e["url"] and e["type"] == "book")
n_none = len(entries) - n_doi - n_url - n_book

blocks = []
for L in letters:
    lis = "\n".join(entry(e) for e in groups[L])
    blocks.append(f'''        <h2 class="ref-letter" id="ref-{L.lower()}">{L}</h2>
        <ol class="papers">
{lis}
        </ol>''')
jump = " ".join(f'<a href="#ref-{L.lower()}">{L}</a>' for L in letters)

body = f'''    <section class="hero deep">
      <div class="wrap">
        <div class="prose">
          <p class="eyebrow">References</p>
          <h1>Reference material</h1>
          <p class="lede">Every source cited in the book, in alphabetical order by first author, with a link wherever the source can be reached.</p>
          <p>Sources with a Digital Object Identifier (DOI) link to it. Reports, laws, inquiry findings and papers without a DOI link to a free copy from the body that issued them, an official archive or an open-access publisher, where one exists. Commercial books and sources with no free copy are listed without a link. Papers from the Society of Petroleum Engineers (SPE) are held in OnePetro, the SPE's online library. The research programme behind the book is set out by theme on the <a href="research.html">Papers</a> page.</p>
          <p class="todo">Check that every link resolves before launch.</p>
        </div>
        <dl class="facts">
          <dt>Sources</dt><dd>{len(entries)}</dd>
          <dt>With a DOI</dt><dd>{n_doi}</dd>
          <dt>Free copy</dt><dd>{n_url}</dd>
          <dt>Books</dt><dd>{n_book}</dd>
          <dt>No free copy</dt><dd>{n_none}</dd>
        </dl>
      </div>
    </section>

    <section>
      <div class="wrap">
        <nav class="az" aria-label="Jump to letter">{jump}</nav>
        <div class="refs">
{chr(10).join(blocks)}
        </div>
      </div>
    </section>
'''

page = (SITE / "references.html").read_text()
head, rest = page.split('  <main id="main">', 1)
foot = rest.split("  </main>", 1)[1]
desc = "Every source cited in The Culture Ladder by Tim Hudson, with a link to its Digital Object Identifier (DOI) or to a free copy wherever one exists."
head = re.sub(r'(name="description" content=")[^"]*', r"\g<1>" + desc, head)
head = re.sub(r'(property="og:description" content=")[^"]*', r"\g<1>" + desc, head)
(SITE / "references.html").write_text(head + '  <main id="main">\n' + body + "  </main>" + foot)
print(f"{len(entries)} sources: {n_doi} DOI, {n_url} free copy, {n_book} books, {n_none} no free copy; {len(letters)} letters")

# Data file for future maintenance: one record per source, as shown on the page
def plain(x):
    return re.sub(r"<[^>]+>", "", html.unescape(x or ""))
def infer_type(e):
    if not e["html_source"]:
        return e["type"]
    so = plain(e["source"])
    if so.startswith("In "):
        return "chapter"
    if "SPE" in so or "Conference" in so:
        return "conference"
    if "<i>" in e["source"] and re.search(r"\d", so):
        return "journal"
    return "book"
out = []
for e in entries:
    if e["html_source"]:
        basis = "Papers page (SPE number)" if (e["doi"] or "").startswith("10.2118/") else "printed in the book or confirmed by search"
    else:
        basis = e.get("doi_basis")
    out.append({
        "authors": initials(e["authors"]), "year": e["year"], "title": e["title"], "source": plain(e["source"]),
        "type": infer_type(e),
        "doi": e["doi"], "doi_basis": basis if e["doi"] else None,
        "url": None if e["doi"] else e["url"], "url_kind": None if e["doi"] else e.get("url_kind"),
        "book_note": e.get("note"), "check": e.get("check"),
        "verified": False,
    })
(SITE / "data").mkdir(exist_ok=True)
json.dump(out, open(SITE / "data/references.json", "w"), ensure_ascii=False, indent=1)
print("wrote data/references.json")
