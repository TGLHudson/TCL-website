# TCL website: working brief for Claude

This repository holds the website for *The Culture Ladder* by T. G. L. Hudson, due from CRC Press in February 2027, served at **thecultureladder.com**. Read this file before doing any work here.

Further books by the author will follow. Build this site for *The Culture Ladder*, but do not design it in a way that assumes it is the author's only book. Whether later books get their own sites is not yet decided.

## The book and the author

- *The Culture Ladder* reframes the safety culture ladder, asking what culture fits the risks an organisation runs rather than how "mature" it is.
- The ladder originates with Dr P. T. W. Hudson, the author's father. That relationship is declared openly, never left for readers to discover.
- T. G. L. Hudson works on operational risk, safety culture and barrier analysis, operating through Hudson Global Consulting from Cambridge, United Kingdom, and Leiden, The Netherlands. His consulting and methods practice, Hudson Risk Culture (HRC), has its own site at hudsonriskculture.com (the Risk-culture repository). Keep the two sites distinct, but link between them. He has published some 25 peer-reviewed conference papers and book chapters with the Society of Petroleum Engineers (SPE).
- The stance running through the work: safety is not the opposite of dangerous work, it is the condition of being able to repeat it. The work is pro-worker and pro-union.

## Rules for this repository

1. **This repository is public.** Nothing confidential goes in: no client or tender material, no unpublished manuscript text, no private contact details.
2. **Voice.** Formal, precise, information-dense. No marketing padding, no hype words. Where the author's voice is unclear, flag it rather than inventing.
3. **Acronyms.** Spell out every acronym in full on first use on each page.
4. **Spelling.** British English.
5. **Claims.** Do not invent endorsements, reviews, sales figures or credentials. Leave a clearly marked placeholder instead.
6. **Provenance.** Credit Dr P. T. W. Hudson for the original ladder wherever the ladder's origin is described, and declare that he is the author's father.
7. **Publications.** List published work only, linked to the publisher's DOI or record. Never put copies of papers in this repository.

## Technical decisions

- Built with Jekyll, the same as hudsonriskculture.com, so both sites are maintained the same way. GitHub Pages builds it directly from this repository, for the custom domain thecultureladder.com. Pages are Markdown; the output is static HTML and CSS. Reuse the Risk-culture repository's layout, includes and stylesheet as the starting point.
- Plain, fast, accessible pages that work without JavaScript and pass basic accessibility checks.
- Styling follows `STYLE.md`, the Hudson family style guide shared with hudsonglobalconsulting.com and hudsonriskculture.com. Agreed departure from `STYLE.md`, as on the HRC site: links inside running text stay underlined at rest, for accessibility.
- Fonts (Montserrat, Source Sans 3) are self-hosted, as on the HRC site.
- Do not change domain or DNS settings. Tim owns the domains. When the site is ready to go live, list the DNS records to set at the registrar in the README.

## Open decisions (ask before assuming)

- Pages: home, the book, the author, contact, mailing list?
- Pre-order links once CRC Press publishes them.
- Accent colour: `STYLE.md` proposes gold leading for this site, with the cover adding any further colour. Confirm with Tim.
- Cover image use, once CRC Press supplies the cover.
- Contact email: an address on thecultureladder.com, or the HRC addresses (info@hudsonriskculture.com for general mail)?
- Whether later books get their own websites.
