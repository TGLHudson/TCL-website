# Research records

## references/

How the References page was built on 2 November 2026.

- `brief.md`: the brief given to four research agents, each covering a quarter of the book's notes (manuscript v87).
- `refs_A.json` to `refs_D.json`: what each agent found for sources the book cites without a DOI: type, DOI or free-copy link where found, the search result that confirmed it (`evidence`), and anything uncertain (`comment`). These records were merged, de-duplicated and screened into `_data/references.json`; links to Scribd, test servers, withdrawn pages and dead addresses were dropped at that stage.
- `agent-scripts/`: the scripts the agents used to write their JSON.
- `dois-printed-in-book.txt`: the DOIs printed in the manuscript (one entry is truncated at a parenthesis; the full DOI is in `_data/references.json`).
- `dois-on-first-references-page.txt`: the DOIs on the first version of the page.

Bibliographic details only. No manuscript prose is kept here: the repository is public.
