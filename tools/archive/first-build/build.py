"""Assemble the static pages: shared header and footer around each page body.
Output is plain HTML written into the website repo; the repo itself needs no build step."""
import pathlib, sys

HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(sys.argv[1])

NAV = [("index.html", "Home"), ("book.html", "The book"), ("consulting.html", "Consulting"),
       ("author.html", "The author"), ("contact.html", "Contact")]

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false">'
        '<path d="M9 3v26M23 3v26" stroke="currentColor" stroke-width="2.5" fill="none"/>'
        '<path d="M9 9h14M9 15h14M9 21h14" stroke="currentColor" stroke-width="2" fill="none"/>'
        '<path d="M9 27h14" stroke="#b5651d" stroke-width="3" fill="none"/></svg>')

def page(slug, title, desc, body):
    nav = "\n".join(
        f'        <li><a href="{href}"{" aria-current=\"page\"" if href == slug else ""}>{label}</a></li>'
        for href, label in NAV)
    full_title = "The Culture Ladder" if slug == "index.html" else f"{title} | The Culture Ladder"
    return f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://thecultureladder.com/{'' if slug == 'index.html' else slug}">
  <link rel="canonical" href="https://thecultureladder.com/{'' if slug == 'index.html' else slug}">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/site.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="index.html">{LOGO}<span>The Culture Ladder</span></a>
      <nav aria-label="Main">
        <ul class="nav">
{nav}
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
{body.rstrip()}
  </main>

  <footer class="site-footer">
    <div class="wrap">
      <div>
        <p><strong>The Culture Ladder</strong> by T. G. L. Hudson. CRC Press, February 2027.</p>
        <p>The safety culture ladder originates with Dr P. T. W. Hudson, the author's father.</p>
        <p>Consulting is delivered through <a href="https://hudsonglobalconsulting.com">Hudson Global Consulting</a>, Leiden, The Netherlands.</p>
      </div>
      <div>
        <h2>Site</h2>
        <ul>
{chr(10).join(f'          <li><a href="{h}">{l}</a></li>' for h, l in NAV)}
        </ul>
      </div>
      <div>
        <h2>Elsewhere</h2>
        <ul>
          <li><a href="https://hudsonglobalconsulting.com">Hudson Global Consulting</a></li>
          <li><a href="https://www.linkedin.com/in/tgl-hudson">LinkedIn</a></li>
        </ul>
      </div>
    </div>
  </footer>
</body>
</html>
"""

for f in sorted((HERE / "pages").glob("*.html")):
    head, body = f.read_text().split("\n---\n", 1)
    body = body.replace("{{FIT}}", (HERE / "fit.svg").read_text().rstrip())
    meta = dict(line.split(": ", 1) for line in head.strip().splitlines())
    (OUT / f.name).write_text(page(f.name, meta["title"], meta["description"], body))
    print("wrote", f.name)
