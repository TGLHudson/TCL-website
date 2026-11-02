# thecultureladder.com: proposal and first build

2 November 2026. Draft for Tim's review. Nothing here is live until GitHub Pages is switched on and the domain is pointed at it.

## 1. What the site has to do

Three jobs, in this order of weight:

1. **Make the case for the book** and turn interest into pre-orders, then orders.
2. **Turn readers into consulting enquiries**, handed to Hudson Global Consulting (hudsonglobalconsulting.com), which stays the firm's main site.
3. **Keep a list of interested readers** so that publication day reaches people who already asked to hear.

thecultureladder.com is the book's home and the front door to the consulting. hudsonglobalconsulting.com stays the company site. Every consulting call to action on this site points there or to a shared enquiry route.

## 2. What sites in the same space do

I could not load the sites directly from this session (its network policy blocks them), so this is from search results and general knowledge of the field. Worth a direct look before the visual identity is fixed:

| Site | What it does well | What to take |
|---|---|---|
| Todd Conklin (Pre-Accident Investigation podcast) | The podcast is the hub; books and speaking hang off a body of free, regular work. | A reason to come back. A short notes or articles page later would do the same job. |
| Sidney Dekker / Safety Differently | Ideas first, books listed plainly, a community around a named movement. | Give the idea a name people repeat. "Fit, not height" or "the floor" could carry that. |
| Energy Institute, Hearts and Minds | Tools presented as a practical kit, with the ladder at the centre. | Credit the programme and the ladder's history; position the book as the theory under a tool people already use. |
| The Fearless Organization (Amy Edmondson) | Book, then a diagnostic (the Scan), then certified practitioners: a clear ladder from reading to buying. | The same ladder here: book, then a culture fit assessment, then consulting. |
| ProAct Safety / Shawn Galloway | Book page with retailers and formats, priced public workshops, speaking page with testimonials, weekly podcast. | A proper book page (formats, retailers, bulk orders) and a speaking page for event organisers. |

The pattern across all of them: one big idea stated plainly on the home page, the book as proof of that idea, and a short, visible route from the idea to paid work. The weaker sites bury the idea under services lists and stock photographs of hard hats.

## 3. Recommendations

- **Lead with the argument, not the author.** The home page opens on the book's claim and the fit picture. The author page carries the credentials.
- **One original picture does the work.** The site draws its own version of the fit chart (risk along the bottom, culture up the side, the floor and the band). It is drawn in code, so it is sharp at any size, works in dark mode and adds no weight. The book's own figures stay out of this public repository until CRC Press clears them.
- **A restrained identity.** Deep navy, warm paper and one ochre accent for action and for "the floor". A book serif for reading, a plain sans for labels. No stock photography. The real cover replaces the placeholder as soon as CRC Press releases it.
- **Honest placeholders.** Endorsements, client names, formats, ISBN and pre-order links are marked as placeholders, never invented.
- **Credit the ladder's origin** on the home page footer, the book page and the author page.

## 4. Technical choice

**Plain HTML and CSS, served by GitHub Pages from the `main` branch.** No framework, no build step, no JavaScript.

Reasons: five pages do not need a framework; anyone can edit a page in the GitHub web editor; pages load fast and work for screen readers and without scripts; nothing to keep up to date. Fonts are system fonts, so no visitor data goes to a font service, which keeps the site simpler under the General Data Protection Regulation (GDPR).

The cost: the header and footer are repeated in every page, so a menu change means editing six files. If the site grows past about ten pages, or gains a notes or articles section, move to **Eleventy**, a small static site generator that keeps the same HTML and adds shared templates. GitHub Pages can build it with a short GitHub Actions workflow.

## 5. What is in this first build

| File | Purpose |
|---|---|
| `index.html` | Home: the claim, the fit chart, the four questions, consulting teaser, praise (placeholder), mailing list |
| `book.html` | The argument, the five rungs, who it is for, contents (placeholder), pre-order (placeholder) |
| `consulting.html` | Proposed services, how engagements run, call to action |
| `author.html` | Biography, the ladder's origin, publications and speaking |
| `contact.html` | Enquiry routes and mailing list |
| `404.html` | Not-found page |
| `assets/site.css` | All styles, with colour tokens and dark mode |
| `assets/favicon.svg` | Ladder icon |
| `CNAME`, `robots.txt`, `sitemap.xml`, `.nojekyll` | Domain and search engine housekeeping |

Placeholders show on the page as striped boxes headed "Placeholder", so nothing unfinished can be mistaken for content.

## 6. Decisions needed from Tim

1. **Consulting services.** The six services on the consulting page are my outline from the book and the brief. Which are real, what are they called, and is there a fixed-scope entry offer (a one-day assessment, for example)?
2. **Contact route.** A role address on this domain, a form service, or send everything to hudsonglobalconsulting.com?
3. **Mailing list provider.** Buttondown or MailerLite both work with a plain HTML form and have European data options.
4. **Cover and author photograph.** When CRC Press releases the cover, and whether a photograph is wanted at all.
5. **Endorsements.** Who has read the manuscript and would give a line.
6. **Pre-order links.** CRC Press page first, then which retailers.
7. **Analytics.** None, or a cookie-free counter such as Plausible or GoatCounter.

## 7. Going live

1. Merge this branch into `main`.
2. In the repository settings, under Pages, choose "Deploy from a branch", `main`, folder `/ (root)`.
3. At the domain registrar, point `thecultureladder.com` at GitHub Pages: four `A` records for the apex (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153) and a `CNAME` record for `www` pointing to `tglhudson.github.io`.
4. Back in Pages settings, tick "Enforce HTTPS" once the certificate is issued.

## 8. Voice notes for Tim's pass

The copy is drafted to the voice guide and house style (British spelling, no spaced dashes, no redefinition pairs, acronyms spelled out once per page). It still needs your ear. Places where the voice was unclear to me:

- **Home page hero.** "For twenty years organisations have asked how far up the ladder they have climbed." Is twenty years right for public use, or "more than two decades" as the book has it?
- **The Deepwater Horizon paragraph on the home page.** Written fresh from the public record, but it follows the book's opening closely. Keep it as the site's way in, or save the scene for the book and open on the claim?
- **"Fit points both ways."** Taken from the book's own phrasing. Fine as a short public line, or keep it for the book?
- **The author page.** The second paragraph turns the brief's stance into prose ("Safety is the condition of being able to do it again"). It needs a paragraph only you can write: how you came to the work.
- **Origin of the ladder.** The author page says your father developed the five stages "from Ron Westrum's three cultures". Should James Reason be named as well, as the book's Introduction does?
- **First name.** The author page uses "Tim Hudson" in the biography and "T. G. L. Hudson" everywhere else. Which do you want in public?
- **CRC Press.** The house rule says spell out acronyms; CRC Press is a trade name and is left as it is.
