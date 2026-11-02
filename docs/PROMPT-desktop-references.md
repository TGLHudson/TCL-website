# Prompt: references work for Claude on the desktop

Paste everything below the line into a new Claude Code session in the Claude desktop app, opened on a local clone of the TCL-website repository (github.com/TGLHudson/TCL-website). If the book's manuscript repository (culture-ladder) or the local book folder is on this computer, open the session where it can read them too.

---

You are taking over the references work for thecultureladder.com, the website for *The Culture Ladder* by Tim Hudson (CRC Press, February 2027). The site was built in a cloud session that could not open doi.org or most websites, so nothing has been click-tested. You can reach the web from here, so your first job is verification, then finishing the gaps, then a proposal for how the references should be organised on the site.

## Read first

1. `CLAUDE.md`: the working brief. Its rules bind you: the repository is public, so no unpublished manuscript text and nothing confidential; British English; spell out every acronym on first use on each page; never invent credentials or endorsements; credit Dr P. T. W. Hudson and James Reason wherever the ladder's origin is described; Tim's rulings are final.
2. `STYLE.md`: the Hudson family style guide. Any visual change follows it.
3. `docs/REFERENCES-CHECKS.md`: everything known to be uncertain.
4. `docs/PAPERS.md`: how entries are written by hand today.
5. `research.html` (the Papers page: 30 papers by the Hudsons and the ladder's foundation papers, in eight themes) and `references.html` (every source cited in the book: 330 entries, A to Z).
6. `data/references.json` and `data/papers.json`: the same content as structured records. Each reference has `authors`, `year`, `title`, `source`, `type`, `doi`, `doi_basis`, `url`, `url_kind`, `book_note` (the note number in manuscript v87, where known), `cited_in` (which books cite it), `check` (what the cloud session was unsure of) and `verified` (all `false`).

The HTML pages are what the site serves. The JSON files were exported from the same build and match the pages; they are not yet wired to anything.

## Task 1: verify every link

For every DOI and URL in both data files:

- Resolve each DOI at `https://doi.org/<doi>` and confirm the landing page is the right work: title, authors, year and venue. SPE DOIs (`10.2118/<number>-MS`) were formed from paper numbers without checking, and the four 2026 papers marked in press may not exist yet; check those on OnePetro.
- Open each free-copy URL and confirm it is the full document, still live, and hosted by the issuing body, an official archive or an open-access publisher. Never accept Scribd, Academia.edu, ResearchGate uploads, file-sharing sites or anything that looks pirated.
- Set `verified: true` only for links you have opened and matched. Record the date checked.
- Where a link is wrong or dead, find the right one if it exists. Where nothing legitimate exists, remove the link and the entry falls back to "Book" or "Not freely available online".

Use a script for the bulk checking (HTTP status and redirects), then look by eye at anything that redirects somewhere unexpected, every SPE paper, and everything in sections 3 and 4 of `docs/REFERENCES-CHECKS.md`.

## Task 2: close the gaps

- Journal articles and chapters without a DOI: look each one up (Crossref search is the fastest route) and add the DOI when the record matches exactly.
- Reports, legislation, inquiry findings and theses without a link: look for an official free copy. The checks file lists several near misses worth another try (the Health and Safety Executive's Piper Alpha copy, the full Dryden inquiry, the Buncefield final report on the National Archives, the Fleming 2001 report on hse.gov.uk).
- Resolve each row of section 2 of `docs/REFERENCES-CHECKS.md` against the published record. Do not change the manuscript. Produce a separate list, `docs/BOOK-CORRECTIONS.md`, of corrections Tim should make to the book's notes before it goes to print, each with the note number, what the book says, what the published record says, and the evidence.

## Task 3: propose how to organise the references

Today the site has two lists: the Papers page, by theme, for the Hudsons' own research, and a single A to Z References page for everything, linked only from the footer, the book page and the Papers page. 330 entries on one page is a lot to scan. Propose how a reader should find things. Consider at least:

- **Who uses the page.** A practitioner who has just read a chapter and wants the sources; a researcher checking one citation; someone deciding whether to buy the book.
- **Options:** keep A to Z; group by chapter (the `book_note` numbers map to chapters, but chapter titles may only go public once CRC Press confirms them); group by type (papers, reports and inquiries, legislation, books); group by topic; add a "free to read" view; split into several pages; a filter that works without JavaScript and is improved by it.
- **Overlap with the Papers page.** The Hudsons' papers appear on both. Decide whether that is right, and how each page should point to the other.
- **Maintenance.** Entries are hand-edited HTML today, and the brief says no build step. The JSON files make a single source of truth possible. Compare: keep hand-editing; a small script in the repository that regenerates the two pages from the JSON, run by hand; or moving the site to Eleventy, which the brief allows past about ten pages. Recommend one, with the trade-offs.
- **Accessibility and speed:** the page must work without JavaScript, pass basic accessibility checks, and stay fast on a phone.

Write the proposal as `docs/REFERENCES-PROPOSAL.md`: two or three options with a recommendation, a sketch of each page's structure, and what it costs to maintain. **Do not restructure the site until Tim has agreed the proposal.**

## Task 4: after Tim agrees

Implement the agreed structure, keeping the visual style of the existing pages and `STYLE.md`. Update `docs/PAPERS.md` so that Tim can add a reference himself, update the counts on the pages and in `CLAUDE.md`, and keep `docs/REFERENCES-CHECKS.md` current.

## Settled: do not reopen

Tim agreed all of the following on 2 November 2026. Build on them; do not ask about them again or change them without his say-so.

**The site**

- The domain is thecultureladder.com. Claude never changes domain or DNS settings; when the site is ready, list the records for Tim to set at his registrar.
- The site is plain HTML and CSS served by GitHub Pages from `main`, with no framework, no build step and no JavaScript needed. Move to Eleventy only if the site grows past about ten pages (Task 3 may recommend it, with reasons).
- The look follows `STYLE.md`, the family style shared with hudsonglobalconsulting.com and hudsonriskculture.com: dark navy, teal and gold; Montserrat headings and Source Sans 3 body text, self-hosted in `assets/fonts`; square outline buttons, one per hero; cream divider rules; no shadows, gradients or rounded corners.
- The pages are home, the book, papers, consulting, the author and contact in the menu, with references linked from the footer, the book page and the Papers page. Every footer links to Hudson Global Consulting, Hudson Risk Culture and LinkedIn.
- Anything waiting for a decision or a real asset shows as a striped "Placeholder" box (`<p class="todo">`), never as invented content.

- Further books will follow. Build for *The Culture Ladder*, but do not design anything that assumes it is the author's only book. Whether later books get their own sites is not decided. Every record in `data/` carries `cited_in` (today always `["the-culture-ladder"]`); keep it, so references can be shared across books later, and let the Task 3 proposal say how a second book's references would fit.

**Names, credit and wording**

- The author appears as Tim Hudson throughout.
- The ladder's origin is credited to Dr P. T. W. Hudson, the author's father, and James Reason, wherever it is described.
- P. A. R. Hudson is "a director at Hudson Global Consulting".
- The home page opens on the book's claim, not on the Deepwater Horizon scene; the scene stays in the book.
- The ladder's track record is "more than two decades", never "twenty years".
- The personal paragraph on the author page is Tim's to write. Leave the placeholder.

**Papers and references**

- The Papers page lists the research behind the book by theme, every entry with a DOI link. The References page lists every source the book cites, A to Z.
- Every source with a DOI links to it. Sources without a DOI are included too, with a link to a free copy where one is publicly available, and otherwise marked "Book" or "Not freely available online".
- A free copy counts only if it comes from the body that issued it, an official archive or an open-access publisher.
- Paper titles are quoted exactly as published; never expand an acronym inside a title. Acronyms are spelled out in the page's own text instead.
- SPE DOIs take the form `10.2118/<number>-MS`.
- The 2020 bowtie papers (SPE-199380, -199424, -199496) were presented at the 2020 virtual SPE International Conference and Exhibition on Health, Safety, Environment, and Sustainability. The book's Note on Sources gives the wrong conference name; that goes in the corrections list.
- The Shell internal reports (Verschuur et al., 1996; EP 2003-5112) stay listed as citations without links.
- The confidential 2007 fatal-accident review is not listed.
- Copy requests for the Hudsons' papers are parked: leave the "Request a copy" links and their placeholders as they are.

**Still open (ask Tim, do not decide)**

- The contact address or form, and the mailing list provider.
- Whether the SPE author agreement allows sharing copies.
- Two departures from `STYLE.md` awaiting Tim's agreement: cream section labels on teal panels (teal on deep teal fails contrast), and underlined links inside paragraphs.
- The hero photograph, the book cover and pre-order links.
- Whether later books get their own sites or share this one.

## How to work

- Work on a new branch. Commit in small steps with clear messages. Do not merge into `main` until Tim says so.
- Ask Tim before anything that changes what the public sees beyond fixing a wrong link: removing sources, renaming pages, or changing the menu.
- When you finish each task, report in plain terms: what you checked, what you changed, what is still uncertain, and what Tim needs to decide.
