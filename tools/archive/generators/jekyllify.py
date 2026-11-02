"""One-off conversion of the TCL site from repeated-header HTML to Jekyll."""
import html, json, pathlib, re, subprocess

R = pathlib.Path("/home/user/tcl-website")
S = pathlib.Path("/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad")

PAGES = {  # file: (new file, permalink)
    "index.html": ("index.html", "/"),
    "book.html": ("book.html", "/book/"),
    "research.html": ("papers.html", "/papers/"),
    "references.html": ("references.html", "/references/"),
    "consulting.html": ("consulting.html", "/consulting/"),
    "author.html": ("author.html", "/author/"),
    "contact.html": ("contact.html", "/contact/"),
    "404.html": ("404.html", "/404.html"),
}
LINKMAP = {old: perm for old, (_, perm) in PAGES.items() if old != "404.html"}

def fix_links(body):
    def rep(m):
        target, anchor = m.group(2), m.group(3) or ""
        return f'{m.group(1)}"{{{{ \'{LINKMAP[target]}\' | relative_url }}}}{anchor}"'
    return re.sub(r'(href=)"/?(' + "|".join(re.escape(k) for k in LINKMAP) + r')(#[^"]*)?"', rep, body)

# ---------------------------------------------------------------- data
# References: pair each record with its rendered entry to keep the italics
refs = json.load(open(R / "data/references.json"))
page = (R / "references.html").read_text()
lis = re.findall(r'<li>\s*<span class="cite-title">(.*?)</span>\s*<span class="cite-meta">(.*?)</span>\s*(.*?)\s*</li>', page, re.S)
assert len(lis) == len(refs), (len(lis), len(refs))
def sort_letter(a):
    import unicodedata
    s = unicodedata.normalize("NFKD", a).encode("ascii", "ignore").decode()
    s = re.sub(r"^(de|van der|van) ", "", s, flags=re.I)
    return s[:1].upper()
out = []
for rec, (t_html, meta_html, link_html) in zip(refs, lis):
    title = html.unescape(t_html)
    assert re.sub(r"\W", "", title.replace("\u2018", "'").replace("\u2019", "'").lower())[:30] == \
           re.sub(r"\W", "", rec["title"].replace("\u2018", "'").replace("\u2019", "'").lower())[:30], (title, rec["title"])
    m = re.match(r"(.*?) \(([^)]*)\)\.\s?(.*)$", meta_html, re.S)
    authors, year, src = html.unescape(m.group(1)), m.group(2), m.group(3).strip()
    src = src[:-1] if src.endswith(".") else src
    if 'class="doi"' in link_html and "doi.org/" in link_html:
        kind = "doi"
    elif 'class="doi"' in link_html:
        kind = "free"
    elif "Book" in link_html:
        kind = "book"
    else:
        kind = "none"
    url = rec["url"] if kind == "free" else None
    out.append({
        "letter": sort_letter(authors),
        "authors": authors, "year": year, "title": title,
        "source_html": src,
        "type": rec["type"],
        "link": kind,
        "doi": rec["doi"] if kind == "doi" else None,
        "url": url,
        "host": re.sub(r"^www\.", "", re.sub(r"^https?://([^/:]+).*", r"\1", url)) if url else None,
        "doi_basis": rec.get("doi_basis"), "url_kind": rec.get("url_kind") if url else None,
        "book_note": rec.get("book_note"), "cited_in": rec.get("cited_in", ["the-culture-ladder"]),
        "check": rec.get("check"), "verified": False,
    })
(R / "_data").mkdir(exist_ok=True)
json.dump(out, open(R / "_data/references.json", "w"), ensure_ascii=False, indent=1)

# Papers: rebuild from the generator's GROUPS so the italics survive
m = (S / "papers/make.py").read_text()
ns = {"__name__": "x"}
exec(m[: m.index("def entry")], ns)
def curly(t):
    t = re.sub(r"(^|[\s(])'", "\\1\u2018", t)
    return t.replace("'", "\u2019")
INTRO_FIX = {  # intros that named papers now held back as in press
    "skill": "Structure decides who holds authority; skill decides whether they can carry it. These papers set out the skill framework and its interaction with the risk space.",
    "risk-space": "The risk space describes every condition an operation's safety turns on, and sets the floor a culture has to hold. These papers define it and apply it to road transport.",
}
groups = []
for anchor, head, intro, items in ns["GROUPS"]:
    groups.append({"id": anchor, "heading": head, "intro": INTRO_FIX.get(anchor, intro), "papers": [
        {"authors": a, "year": y, "title": curly(t), "source_html": v, "spe_number": i or None,
         "doi": d, "in_press": p, "hudson": "Hudson" in a,
         "doi_basis": "SPE pattern" if d.startswith("10.2118/") else "printed in the book or confirmed by search",
         "cited_in": ["the-culture-ladder"], "verified": False}
        for a, y, t, v, i, d, p in items]})
json.dump(groups, open(R / "_data/papers.json", "w"), ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- pages
DESC = {}
for old, (new, perm) in PAGES.items():
    s = (R / old).read_text()
    title = re.search(r"<title>(.*?)</title>", s).group(1).replace(" | The Culture Ladder", "")
    desc = html.unescape(re.search(r'name="description" content="([^"]*)"', s).group(1))
    body = s.split('  <main id="main">\n', 1)[1].split("  </main>", 1)[0]
    if old in ("research.html", "references.html"):
        body = None  # written by hand below
    else:
        body = fix_links(body)
        body = re.sub(r"<svg class=\"fit-chart\".*?</svg>", "{% include fit.html %}", body, flags=re.S)
    fm = f"---\nlayout: default\ntitle: {json.dumps(title)}\ndescription: {json.dumps(desc)}\npermalink: {perm}\n---\n"
    DESC[old] = (new, fm, body)
for old, (new, fm, body) in DESC.items():
    if body is not None:
        (R / new).write_text(fm + body)
    if new != old:
        subprocess.run(["git", "-C", str(R), "rm", "-q", old], check=True)
json.dump({k: v[1] for k, v in DESC.items()}, open(S / "frontmatter.json", "w"))
print("done:", len(out), "references,", sum(len(g["papers"]) for g in groups), "papers")
