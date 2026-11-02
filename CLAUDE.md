# TCL website: working brief for Claude

This repository holds the website for *The Culture Ladder* by T. G. L. Hudson, due from CRC Press in February 2027. Read this file before doing any work here.

## The book and the author

- *The Culture Ladder* reframes the safety culture ladder, asking what culture fits the risks an organisation runs rather than how "mature" it is.
- The ladder originates with Dr P. T. W. Hudson, the author's father, and James Reason. That relationship is declared openly, never left for readers to discover.
- T. G. L. Hudson works on operational risk, safety culture and barrier analysis, operating through Hudson Global Consulting from Leiden, The Netherlands. He has published some 25 peer-reviewed conference papers and book chapters with the Society of Petroleum Engineers (SPE).
- The stance running through the work: safety is not the opposite of dangerous work, it is the condition of being able to repeat it. The work is pro-worker and pro-union.

## Rules for this repository

1. **This repository is public.** Nothing confidential goes in: no client or tender material, no unpublished manuscript text, no private contact details.
2. **Voice.** Formal, precise, information-dense. No marketing padding, no hype words. Where the author's voice is unclear, flag it rather than inventing.
3. **Acronyms.** Spell out every acronym in full on first use on each page.
4. **Spelling.** British English.
5. **Claims.** Do not invent endorsements, reviews, sales figures or credentials. Leave a clearly marked placeholder instead.
6. **Provenance.** Credit Dr P. T. W. Hudson and James Reason for the original ladder wherever the ladder's origin is described.
7. **Name.** The author appears on the site as Tim Hudson.

## Tim's rulings (2 Nov 2026)

- The home page opens on the book's claim, not on the Deepwater Horizon scene. The scene stays in the book.
- The ladder's track record is "more than two decades", never "twenty years".
- The author page's personal paragraph is Tim's to write. Leave the placeholder; do not draft it.

## Technical defaults (until decided otherwise)

- A static site that GitHub Pages can serve directly from this repository. Plain HTML and CSS, no framework and no build step (proposed in `docs/PROPOSAL.md`, section 4). The header and footer are repeated in every page: change all of them together. Move to Eleventy if the site grows past about ten pages.
- Anything awaiting a decision or a real asset is marked in the page with `<p class="todo">`, which renders as a striped "Placeholder" box.
- Plain, fast, accessible pages that work without JavaScript and pass basic accessibility checks.

## Open decisions (ask before assuming)

- Domain name: decided, `thecultureladder.com` (see `CNAME`).
- Pages: first build has home, the book, consulting, the author, contact. Mailing list form awaits a provider.
- Pre-order links once CRC Press publishes them.
- Visual identity: decided. Follow `docs/STYLE.md`, the Hudson family style guide shared with hudsonglobalconsulting.com and hudsonriskculture.com. Any departure needs Tim's agreement. Fonts are self-hosted in `assets/fonts`. Still awaiting the CRC Press cover and a hero photograph.
- The open questions for Tim are listed in `docs/PROPOSAL.md`, section 6 and 8.
