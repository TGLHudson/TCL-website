# Tools

Helpers for maintaining the site. Not published (excluded in `_config.yml`). None is needed to build the site: GitHub Pages runs Jekyll itself.

| Path | What it does |
|---|---|
| `build-demo.py` | Copies the built site (`_site`) with relative links, for previews opened from a folder or a demo page. |
| `share-card/` | `card.html` is the 1200 × 630 share image; `node tools/share-card/render.js` renders it to `assets/share-card.png`. Replace with the cover when CRC Press releases it. |
| `archive/` | Superseded working files, kept for the record. See below. |

## archive/

- `first-build/`: the generator and page bodies of the first plain-HTML build (2 November 2026), before the move to Jekyll.
- `generators/`: the scripts that built the Papers and References pages before they were generated from `_data/` (`make.py`, `refs.py`, `refs2.py`), and the one-off conversion to Jekyll (`jekyllify.py`). Their file paths point at the cloud session's temporary folder, so they will not run as they stand.
- `screenshot-scripts/`: the Playwright scripts used to check pages during the build.
