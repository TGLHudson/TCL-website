# Review panel: thecultureladder.com, 2 November 2026

*Status, 2 November 2026: every item in section A is fixed, and section B is built as far as it can go without Tim (structure, published facts, a drafted critics paragraph for his voice pass), with a placeholder for each remaining decision.*

Six reviewers read the draft site (built from `main` at commit 8dbf6de), each as a different visitor. Placeholders were treated as deliberate. Nothing here has been acted on yet. Reviewers' suggestions that would need new content are listed for Tim to decide; none may be written without him, under the brief's rules on voice and claims.

The panel: (1) head of health, safety and environment at an offshore drilling contractor; (2) professor of safety science; (3) non-executive director chairing a safety committee, reading on a phone; (4) marketing manager at a professional publisher; (5) national health and safety officer of a trade union; (6) accessibility and web-quality auditor.

## What the panel agreed works

- The opening question on the home page, and "A village bakery does not need a Generative culture. A deepwater rig cannot survive a Reactive one." Four of five readers singled these out.
- No hype, and the provenance of the ladder declared openly.
- The Papers page with DOIs counts for more than credentials would (practitioner, academic).
- The References page is usable as a bibliography once tidied (academic).
- Technically clean: contrast passes on every text pair used, no horizontal scroll down to 320px, works without JavaScript, light pages (auditor).

## A. Fixes that need no new content (ready to make)

Ranked by how many reviewers raised them and how much they matter.

1. **"Pre-order the book" leads to a placeholder** (practitioner, board member, marketer). Until CRC Press opens pre-orders, relabel it "Get notified" and point it at the mailing list; switch back on launch day.
2. **The sign-up forms fail on submit** (auditor): they post to "#", and GitHub Pages will return an error, losing what was typed. Hide or disable them until a list provider is connected.
3. **Social sharing shows no image** (marketer): add `og:image`, `og:site_name` and `twitter:card` with a plain share card (title and author on navy), to be replaced by the cover.
4. **No structured data** (marketer): JSON-LD `Book` on the book page (CRC Press, February 2027, author), `Person` on the author page; ISBN and offers added when they exist.
5. **Page titles miss the subject** (marketer): the home title is only "The Culture Ladder". Add "safety culture" and the author's name.
6. **Accessibility defects** (auditor):
   - the "About the book" link on the author page is told apart by colour alone: underline it;
   - A to Z letters on References are below the 24px target size;
   - the chart's shaded band is 1.43:1, below the 3:1 needed for meaningful graphics;
   - chart labels shrink to about 6 to 8px on phones;
   - the chart's text alternative leaves out three labels;
   - one citation overflows at 320px with text spacing applied;
   - "Request a copy" and "Free copy at …" links need the paper's name in their accessible label.
7. **Citation format on References** (academic):
   - "BP ()" has no year;
   - "Le Coze, J. -C." has a stray space;
   - the same authors appear with different initials (Dekker; Reason);
   - title case and sentence case are mixed;
   - hyphens and en dashes are mixed in page ranges;
   - spacing is mixed in volume and issue ("67(3–4)" beside "44 (6)");
   - SPE numbers are in two formats.
8. **The book page misdescribes the References page** as sources "with a DOI": it now lists all of them.
9. **The papers count clashes with itself** (academic): "some 25 papers" in the credentials, and "25 papers" on the Papers page, of which 15 are Tim's and some are not SPE papers. Split the Papers page into "Our papers" and "Foundations", and count each.
10. **"Risk space" is used on the home page before it is defined** (board member). One plain sentence, drawn from the book page.

## B. Content only Tim can supply or decide

Grouped by theme. Several reviewers converge on the first two.

1. **Make the pro-worker, pro-union stance visible** (union officer, practitioner). It appears once, as a bare line on the author page. Reviewers ask for:
   - what it means in the book: culture read from management's decision structures, not graded from worker behaviour;
   - whether safety representatives take part in assessments, and whether the workforce sees the findings;
   - whether Tim offers joint or representative sessions and speaks to union audiences.
2. **Bring the chapter for boards, the workforce and regulators forward** (board member, union officer, practitioner). It is one buried sentence on the book page, and for three readers it is the reason to buy. Each audience wants a short section saying what the book gives them. The board member wants two or three sample board-level questions, which must be Tim's.
3. **Engage the critics** (academic). The book page offers adoption as the only evidence. The book itself cites Boskeljon-Horst, Sillem and Dekker (2023), who found ladder-based assessments inversely predict outcomes. The academic suggests:
   - a short "the critiques, and how the book answers them" paragraph;
   - naming the closest prior work: Hopkins (2019) on structure creating culture, and Amalberti and Grote on fit.
4. **Provenance** (academic). Should Parker and Lawrie, who built and tested the five-level framework with Professor P. T. W. Hudson, be credited alongside Hudson and Reason? The academic also says Hearts and Minds was Shell-funded and should be declared. That is unverified here; Tim to confirm before anything is said.
5. **"Peer-reviewed"** (academic): most SPE conference papers are accepted on an abstract. Keep "peer-reviewed", or say "conference papers and book chapters"?
6. **Consulting details** (practitioner, board member):
   - how the assessment relates to existing Hearts and Minds work;
   - a typical scope (days at the work, interviews across shifts);
   - multi-site comparison stated up front;
   - who delivers the work;
   - board briefings listed first.
7. **Press and speaking kit** (marketer, board member): 50, 100 and 200-word biographies, a photo, a book description, and a slide-ready chart.
8. **A "start here" paper** for readers who want the argument before February (practitioner suggests SPE-220464-MS).

## C. Waiting on assets (already placeholders)

Most-mentioned before launch: the contact address (four reviewers), the cover and ISBN, retailer links, the mailing list provider with a privacy notice that meets the General Data Protection Regulation (GDPR), the contents list and a sample extract, the hero photograph, and Tim's own paragraph on the author page.

## Would they act?

| Reviewer | Now | What would tip them |
|---|---|---|
| Practitioner | Sign up; read SPE-220464-MS | Hearts and Minds fit, and the scope in time, then an enquiry for two rigs and a shore base |
| Academic | Use References once tidied | Visible engagement with the critics, then pre-order and set as reading |
| Board member | Share with the committee | A contact address and three board-level questions, then a briefing enquiry |
| Marketer | Share internally | Share image, structured data, a working notify route |
| Union officer | Not yet recommend to reps | The pro-union stance shown with substance, and the workforce chapter described |
| Auditor | Fix A2 and A6 before launch | |
