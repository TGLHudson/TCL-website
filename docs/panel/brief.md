# Review panel brief: thecultureladder.com

You are one member of a review panel for the draft website of *The Culture Ladder* by Tim Hudson (CRC Press, February 2027). The book reframes the safety culture ladder (Pathological, Reactive, Calculative, Proactive, Generative): instead of asking how high an organisation has climbed, it asks what culture fits the risk the organisation actually runs. The site has three jobs: make the case for the book and sell it, turn readers into consulting enquiries (handled by Hudson Risk Culture, Tim's practice), and build a mailing list.

## The site

The built site is served at http://127.0.0.1:8765/ with pages `/`, `/book/`, `/papers/`, `/references/`, `/consulting/`, `/author/`, `/contact/`. The source is in `/home/user/tcl-website` (read `CLAUDE.md` there for the rules the site follows; `STYLE.md` for the visual style). Read the pages as built: use `curl` for the HTML, and Playwright (`require('playwright')`, `chromium.launch()`; it is pre-installed, do not install it) to look at pages at desktop (1280px) and phone (390px) widths. Save any screenshots under `/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/panel/`. Do not edit any file in the repository.

## Things that are deliberate, not faults

- Striped boxes headed "Placeholder" mark content still to come (cover, photographs, endorsements, contact address, mailing list provider, the author's own paragraph, pre-order links). Do not report their absence as a fault. You may say which matter most to you before launch.
- The site does not invent endorsements, credentials or figures, and it must not. Do not recommend adding any you cannot point to.
- Five 2026 papers are held back from the Papers page until they are published.
- The visual style (dark navy, teal, gold; Montserrat and Source Sans 3) is a family style shared with two sister sites. Comment on how well it works, but do not propose a different brand.
- Writing rules: British English; no hype; acronyms spelled out on first use on each page; formal and precise.

## Your report

Stay in your role. Be concrete: name the page and the passage or element. Under 450 words, in this shape:

1. **First impression** (two or three sentences): what you understood the site to offer within ten seconds of landing.
2. **What works** (up to three points).
3. **What I would change**, ranked by importance, up to six points. For each: the page, what is wrong for someone like you, and a specific fix.
4. **Would I act?** Would you pre-order the book, make a consulting enquiry, sign up, or share it, and what would tip you over.
