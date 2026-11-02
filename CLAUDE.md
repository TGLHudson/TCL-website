# The Culture Ladder (TCL) website: working brief for Claude

This repository holds the website for *The Culture Ladder* by T. G. L. Hudson, due from CRC Press in February 2027. It is served at **thecultureladder.com**. Read this file before doing any work here.

Further books by the author will follow. Build this site for *The Culture Ladder*, but do not design it in a way that assumes it is the author's only book. Whether later books get their own sites is not yet decided.

## The book and the author

- *The Culture Ladder* reframes the safety culture ladder, asking what culture fits the risks an organisation runs rather than how "mature" it is.
- The ladder originates with Professor P. T. W. Hudson, the author's father, and Professor James Reason. That relationship is declared openly, never left for readers to discover.
- T. G. L. Hudson works on operational risk, safety culture and barrier analysis, operating through Hudson Global Consulting from Cambridge, United Kingdom, and Leiden, The Netherlands. His consulting and methods practice, Hudson Risk Culture (HRC), has its own site at hudsonriskculture.com (the Risk-culture repository). Keep the two sites distinct, but link between them. He has published some 25 peer-reviewed conference papers and book chapters with the Society of Petroleum Engineers (SPE).
- The stance running through the work: safety is not the opposite of dangerous work, it is the condition of being able to repeat it. The work is pro-worker and pro-union.

## Rules for this repository

1. **This repository is public.** Nothing confidential goes in: no client or tender material, no unpublished manuscript text, no private contact details.
2. **Voice.** Formal, precise, information-dense. No marketing padding, no hype words. Where the author's voice is unclear, flag it rather than inventing.
3. **Acronyms.** Spell out every acronym in full on first use on each page.
4. **Spelling.** British English.
5. **Claims.** Do not invent endorsements, reviews, sales figures or credentials. Leave a clearly marked placeholder instead.
6. **Provenance.** Credit Professor P. T. W. Hudson and Professor James Reason for the original ladder wherever the ladder's origin is described, and declare that Professor P. T. W. Hudson is the author's father.
7. **Publications.** List published work only, linked to the publisher's DOI or record. Never put copies of papers in this repository. (The References page is the book's own citation list and follows its own ruling below.)
8. **Name.** The author appears on the site as Tim Hudson.

## Tim's rulings (2 Nov 2026)

- The home page opens on the book's claim, not on the Deepwater Horizon scene. The scene stays in the book.
- The ladder's track record is "more than two decades", never "twenty years".
- The author page's personal paragraph is Tim's to write. Leave the placeholder; do not draft it.
- P. A. R. Hudson is described as "a director at Hudson Global Consulting".
- Titles: "Professor P. T. W. Hudson" and "Professor James Reason" in prose; citations keep the plain "Hudson, P. T. W." and "Reason, J." form.
- The 2020 bowtie papers (SPE-199380, -199424, -199496) were at the 2020 virtual SPE International Conference and Exhibition on Health, Safety, Environment, and Sustainability.
- The References page lists every source the book cites: DOI link where there is one, otherwise a link to a free copy from the issuing body, an official archive or an open-access publisher, otherwise "Book" or "Not freely available online". The Shell internal reports stay as citations without links.
- Copy requests for the Hudsons' papers are parked: the route and the SPE copyright terms stay as placeholders until Tim returns to them.

## Technical decisions

- Built with Jekyll, the same as hudsonriskculture.com, so both sites are maintained the same way. GitHub Pages builds it directly from `main`, for the custom domain thecultureladder.com. The layout is `_layouts/default.html`; the header, footer and figure are in `_includes/`; the menu is the `nav` list in `_config.yml`. Pages are HTML or Markdown with front matter; the output is static HTML and CSS.
- The Papers and References pages are generated from `_data/papers.json` and `_data/references.json`. Edit the data, never the generated lists. How-to: `docs/PAPERS.md`.
- Plain, fast, accessible pages that work without JavaScript and pass basic accessibility checks.
- Styling follows `STYLE.md`, the Hudson family style guide shared with hudsonglobalconsulting.com and hudsonriskculture.com, with gold leading for this site. Agreed departure, as on the HRC site: links inside running text stay underlined at rest, for accessibility. Any other departure needs Tim's agreement.
- Fonts (Montserrat, Source Sans 3) are self-hosted in `assets/fonts`, as on the HRC site.
- Anything awaiting a decision or a real asset is marked with `<p class="todo">`, which renders as a striped "Placeholder" box.
- Do not change domain or DNS settings. Tim owns the domains. The DNS records to set at the registrar are listed in the README.

## Open decisions (ask before assuming)

- Pages: home, the book, papers, consulting, the author, contact in the menu; references linked from the footer, the book page and the Papers page. Mailing list form awaits a provider.
- Contact email: an address on thecultureladder.com, or the HRC addresses (enquiries@hudsonriskculture.com for consulting, info@hudsonriskculture.com for general mail)?
- Accent colour: gold leads, as `STYLE.md` proposes for this site, with the cover adding any further colour. Confirm with Tim.
- Cover image use, once CRC Press supplies the cover. Pre-order links once CRC Press publishes them.
- Section labels on teal panels are cream, because teal on deep teal fails contrast. Departure from `STYLE.md` awaiting Tim's agreement.
- Whether later books get their own sites or share this one. Until decided: the author page lists books (`id="books"`), and every record in `_data/` carries `cited_in` so a source can belong to more than one book.
- References: open checks are in `docs/REFERENCES-CHECKS.md`; further work is briefed in `docs/PROMPT-desktop-references.md`.
- The open questions for Tim are listed in `docs/PROPOSAL.md`, sections 6 and 8.
