# Flowback to the Hudson Risk Culture site

From: the TCL-website repository (thecultureladder.com), 2 November 2026.
For: the Claude session working on the Risk-culture repository (hudsonriskculture.com).

This note carries back the decisions Tim made while the TCL site was built, so the two sites stay consistent. It is written here, not on a branch of Risk-culture, because this session has read access only to that repository. Read it, apply what fits the HRC site, record the rulings in the HRC `CLAUDE.md`, and tell Tim what you changed.

The TCL repository's own brief, `CLAUDE.md`, has the full set of rulings. Everything below is already live on thecultureladder.com (`main`, commit 05eeb59 or later).

## 1. Rulings from Tim that apply to both sites

### Titles and credit for the ladder

- **Professor P. T. W. Hudson**, not "Dr", in prose. He is the author's father; declare that wherever his work is described.
- **Professor James Reason** shares the credit for the original ladder. Wherever the ladder's origin is described, credit both: "The safety culture ladder originates with Professor P. T. W. Hudson, the author's father, and Professor James Reason."
- Citations keep the plain form: "Hudson, P. T. W." and "Reason, J."

### P. A. R. Hudson

- On the TCL site he is described as **"a director at Hudson Global Consulting"** (Tim's wording). That answers the open placeholder on `parhudson.md`. Whether HRC should also state the family relationship is Tim's call: the TCL site gives the role only.

### Papers and DOIs

- Paper titles are quoted exactly as published; never expand an acronym inside a title.
- SPE DOIs take the form `10.2118/<number>-MS` (journal papers `-PA`).
- The 2020 bowtie papers (SPE-199380, -199424, -199496) were presented at the **2020 virtual SPE International Conference and Exhibition on Health, Safety, Environment, and Sustainability**, not the "Security… Social Responsibility" conference the book's Note on Sources names.
- Published work only on a publications list. The TCL Papers page holds back the five 2026 papers listed in the book as in press (SPE-233645, -233662, -233663, -233678, -233694) until OnePetro lists them, which matches what the HRC publications page already does.
- Copy requests: the TCL site has a "Request a copy" link beside each Hudson paper, pointing to its contact page. The route and the SPE copyright terms are **parked** by Tim, so nothing should be copied across yet.

### Accessibility

- On teal panels (`--deep-teal` background), `--teal` text is about 3.3:1, which fails WCAG AA for small text. The TCL site sets section labels on teal panels in `--cream` instead. This departure from `STYLE.md` still awaits Tim's agreement; if HRC puts teal eyebrows on deep teal panels, it has the same problem.

## 2. Changes for the HRC site

| File | Line (on branch `claude/quirky-bohr-bfv6fy`) | Now | Change to |
|---|---|---|---|
| `CLAUDE.md` | rule 6 | "originates with Dr P. T. W. Hudson, the author's father" | Professor P. T. W. Hudson and Professor James Reason; add the titles ruling |
| `CLAUDE.md` | pages list | "sub-pages for Dr P. T. W. Hudson" | Professor |
| `about.md` | 22 | "originates with Dr P. T. W. Hudson, T. G. L. Hudson's father" | Professor P. T. W. Hudson, T. G. L. Hudson's father, and Professor James Reason |
| `approach.md` | 18 | "originates with Dr P. T. W. Hudson" | as above, adding Professor James Reason |
| `books.md` | 14 | "originates with Dr P. T. W. Hudson, the author's father" | as above |
| `publications.md` | 16, 18 | heading and text "Dr P. T. W. Hudson"; link text "Papers by Dr P. T. W. Hudson" | Professor |
| `pthudson.md` | 4, 5, 8, 12 | title, description, text "Dr P. T. W. Hudson" | Professor |
| `parhudson.md` | 10 | placeholder asking for his relationship | "a director at Hudson Global Consulting", with the family relationship only if Tim wants it |

## 3. Links the HRC site can now use

- **Papers by theme:** https://thecultureladder.com/papers/ lists 25 published papers behind the book, in eight themes, each with its DOI.
- **References:** https://thecultureladder.com/references/ lists all 330 sources the book cites, with a DOI or a free-copy link where one exists.
- The `books.md` entry for *The Culture Ladder* could link to both.

## 4. Data the HRC site can reuse

- `_data/papers.json` in the TCL repository holds 30 papers (25 published, 5 in press), many by Professor P. T. W. Hudson, each with authors, year, exact title, venue, SPE number and DOI. It could fill the placeholder on `pthudson.md`. The SPE DOIs were formed from paper numbers and are not yet click-tested (`verified: false`), so check each at doi.org first.
- `docs/REFERENCES-CHECKS.md` lists differences between the book's notes and the published records, including the SPE-179436-MS first-author question the HRC session raised.

## 5. Already the same on both sites

The Jekyll setup, `STYLE.md`, self-hosted fonts, underlined links inside running text, Cambridge, United Kingdom, and Leiden, The Netherlands, and the publications rule. TCL leads with gold, HRC with teal.

## 6. Still open, for Tim

- The contact address: an address on thecultureladder.com, or the HRC addresses (enquiries@hudsonriskculture.com, info@hudsonriskculture.com). The TCL contact page currently names the HRC addresses as the option.
- The cream-on-teal contrast departure.
- Whether later books get their own sites.
