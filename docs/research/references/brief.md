# Brief: sources without a DOI in The Culture Ladder

You are helping build a public "References" page for the website of *The Culture Ladder*, a book on safety culture by Tim Hudson (CRC Press, 2027). The page already lists every source the book cites WITH a DOI (75 of them, listed one per line in `/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/already_on_page_dois.txt`). Your job is the sources WITHOUT a DOI in one slice of the book's notes.

Source file: `/home/user/culture-ladder/manuscript/full_book_v87_reference.md`. Read only the line range(s) you are given.

## Step 1: list the sources

From your line range, list every distinct source that is cited in full (author, year, title, publisher or journal). Skip:
- short back-references such as "Hopkins (2006) (note 14)" or "Reason (1997) (note 116), ch. 9", where the full citation is given elsewhere. Only include the source if its FULL citation is in your range.
- anything whose DOI is in `already_on_page_dois.txt`, or that already shows a DOI in the text.
- editorial flags in square brackets such as "[⚠ page to add]". Never copy these.
- the book's own commentary. Take only the bibliographic facts.

Corporate authors are often split oddly by line wrapping in the notes; give them in full (for example "US Chemical Safety and Hazard Investigation Board (CSB)").

## Step 2: classify and look up

For each source, decide its type: `book`, `chapter`, `journal`, `report` (government, inquiry, regulator, company, white paper, working paper), `conference`, `thesis`, `legislation`, `web` (news article, web page), `other`.

Then, using WebSearch (mode "standard"; direct fetching of most sites is blocked in this environment):
- **journal articles and chapters**: find the DOI. Report it only if it appears in a search result for that exact work (journal, volume, pages must match). SPE papers (Society of Petroleum Engineers) have DOIs of the form 10.2118/<number>-MS; for those you may give the DOI from the paper number without searching, and mark `doi_basis: "SPE pattern"`.
- **reports, legislation, theses, working papers, white papers, conference papers, web articles**: find whether it is freely and legitimately available online. Acceptable: the issuing body's own site (government, inquiry, regulator, university repository, professional body), the publisher's open-access page, an official archive (for example the UK National Archives, govinfo.gov, the Internet Archive's copy of an official page). NOT acceptable: Scribd, Academia.edu uploads, ResearchGate uploads, personal file shares, anything that looks pirated. If the notes already give a URL, use it (check it is still the right document if you can).
- **books**: do not search. Commercial books are not "publicly available" for this purpose. Exception: a book you know is officially free online (for example a government publication or an open-access book) — then search to confirm.

Only report a URL or DOI that appeared in your search results. Never construct or guess a URL. If you cannot confirm one, leave it null; that is a fine answer. Budget: about 40 searches. Spend them on reports and journal articles first.

## Step 3: write the result

Write a JSON array to the output file you are given, one object per source:

```json
{
  "note": 63,
  "authors": "US Chemical Safety and Hazard Investigation Board (CSB)",
  "year": "2016",
  "title": "Tesoro Martinez Refinery Process Safety Culture Case Study",
  "source": "Report No. 2014-02-I-CA. Washington, DC: CSB",
  "type": "report",
  "doi": null,
  "doi_basis": null,
  "url": "https://www.csb.gov/...",
  "url_kind": "official",
  "evidence": "the search result URL or title that confirmed it",
  "comment": "anything uncertain"
}
```

`url_kind` is one of `official`, `open-access`, `given-in-book`, or null. Titles exactly as the book gives them, in the book's capitalisation. Use straight quotes. British spelling in your comments.

Finish with a short summary: how many sources, how many with a DOI found, how many with a public URL, how many left with neither, and anything you were unsure of.
