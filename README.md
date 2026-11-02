# The Culture Ladder (TCL) website

Source for [thecultureladder.com](https://thecultureladder.com), the website for *The Culture Ladder* by T. G. L. Hudson (CRC Press, February 2027).

Work on this site happens in Claude Code sessions. The working brief, with rules and open decisions, is in [CLAUDE.md](CLAUDE.md). Colours, type and components follow [STYLE.md](STYLE.md), the style guide shared with [hudsonglobalconsulting.com](https://hudsonglobalconsulting.com) and [hudsonriskculture.com](https://hudsonriskculture.com).

## Structure

The site is built with Jekyll, the same as hudsonriskculture.com. GitHub Pages builds it from `main`.

| Path | What it is |
|---|---|
| `_config.yml` | Site settings and the menu (`nav`) |
| `_layouts/default.html` | The page shell: head, header, footer |
| `_includes/` | Header, footer and the fit chart |
| `index.html`, `book.html`, `papers.html`, `references.html`, `consulting.html`, `author.html`, `contact.html`, `404.html` | The pages |
| `_data/papers.json`, `_data/references.json` | The Papers and References lists. Edit these, not the pages |
| `assets/` | Stylesheet, fonts and icon |
| `docs/` | Proposal, how-to guides and checklists (not published) |

To add a publication or a reference, follow [docs/PAPERS.md](docs/PAPERS.md). Further references work is briefed in [docs/PROMPT-desktop-references.md](docs/PROMPT-desktop-references.md).

## Preview locally

```bash
bundle install
```

```bash
bundle exec jekyll serve
```

Then open http://localhost:4000.

## Going live

1. In the repository's Settings, Pages: Source "Deploy from a branch", `main`, `/ (root)`. The custom domain comes from the `CNAME` file.
2. At the domain registrar, set these records for thecultureladder.com, removing any other `A` or `CNAME` records for `@` and `www`:

   | Type | Name | Value |
   |---|---|---|
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | CNAME | www | tglhudson.github.io |

3. Once DNS has propagated, tick "Enforce HTTPS" in the Pages settings.
