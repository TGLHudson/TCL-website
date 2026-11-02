"""Make a copy of the built site whose links work from any folder (for previews
such as the claude.ai demo page), by turning root links like /book/ into
relative ones like ../book/index.html.

Usage:
  bundle exec jekyll build            # or: JEKYLL_NO_BUNDLER_REQUIRE=true jekyll build
  python3 tools/build-demo.py _site demo
"""
import pathlib, re, shutil, sys

src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst)
for f in dst.rglob("*.html"):
    pre = "../" * (len(f.relative_to(dst).parts) - 1)
    def rep(m):
        path, rest = m.group(2), m.group(3) or ""
        if path.endswith("/") or path == "":
            path += "index.html"
        return f'{m.group(1)}="{pre}{path}{rest}"'
    f.write_text(re.sub(r'(href|src)="/(?!/)([^"#?]*)([#?][^"]*)?"', rep, f.read_text()))
print("demo copy written to", dst)
