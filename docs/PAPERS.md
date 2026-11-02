# Adding publications to the Papers page

The Papers page is `research.html`, in the root of this repository. It is plain HTML, so you can edit it directly in the GitHub web editor (open the file, press the pencil icon) or in any text editor. There is no build step: once the change is merged into `main`, GitHub Pages publishes it.

## 1. Find the DOI

Every entry needs a Digital Object Identifier (DOI), the permanent link to the paper.

- **Society of Petroleum Engineers (SPE) papers.** The DOI is `10.2118/` followed by the paper number and its suffix. For SPE-220464-MS it is `10.2118/220464-MS`. Journal papers end in `-PA` instead of `-MS`, for example `10.2118/27846-PA`. Check it on the paper's page in OnePetro (onepetro.org), where the DOI is printed under the title.
- **Journal articles and book chapters.** The DOI is printed on the first page of the article and on the publisher's web page. If you cannot find it, search the title at [search.crossref.org](https://search.crossref.org).
- **Always test the link.** Paste `https://doi.org/` followed by the DOI into a browser. It should open the paper's page. If it says "DOI Not Found", the DOI is wrong or has not been issued yet.

Papers accepted but not yet published may not have a DOI. Add them with the "In press" tag (section 3) and test the DOI again once they appear in OnePetro.

## 2. Find the right theme

The page groups papers into themes. Each theme is a `<section>` with an `id`:

| Theme on the page | `id` |
|---|---|
| Where the ladder comes from | `origins` |
| Structure: why the rungs sit where they do | `structure` |
| Risk space: what the work demands | `risk-space` |
| Skill: competence plus experience | `skill` |
| Barriers and the bowtie | `barriers` |
| Incidents, non-compliance and a fair culture | `learning` |
| Decisions under pressure and emergency response | `decisions` |
| Choosing tools that fit | `tools` |

Search the file for `id="skill"` (or whichever theme) to jump to it. The papers are inside `<ol class="papers">`, oldest first.

## 3. Add the entry

Copy this block, paste it into the theme's `<ol class="papers">` in date order, and fill it in:

```html
            <li>
              <span class="cite-title">Title exactly as published</span>
              <span class="cite-meta">Hudson, T. G. L. &amp; Hudson, P. T. W. (2027). Conference or journal name, place. SPE-123456-MS.</span>
              <a class="doi" href="https://doi.org/10.2118/123456-MS">doi.org/10.2118/123456-MS</a>
            </li>
```

The three lines are:

1. **`cite-title`**: the title exactly as published. Do not expand acronyms or change spelling inside a title, even where the rest of the site would.
2. **`cite-meta`**: authors (surname, initials), year in brackets, where it appeared, and the paper number for SPE papers. Write `&` as `&amp;`. Put journal and book titles in `<i>…</i>`, for example `<i>Safety Science</i>, 45 (6), 697–722`.
3. **`doi`**: the DOI twice, once in `href` with `https://doi.org/` in front, once as the visible text with `doi.org/` in front.

**For a paper not yet published**, add the tag after the title and say "in press" with the year:

```html
              <span class="cite-title">Title exactly as published</span> <span class="badge">In press</span>
              <span class="cite-meta">Hudson, T. G. L. (2027, in press). …</span>
```

When it is published, delete ` <span class="badge">In press</span>` and `, in press`, and test the DOI.

## 4. Update the count

Near the top of the file is the line:

```html
          <p class="eyebrow">30 papers in eight themes</p>
```

Change the number to match.

## 5. Adding a new theme

Only if a paper fits none of the existing themes.

1. Copy a whole theme, from `<section` to `</section>`, and paste it where the new theme belongs.
2. Give it a new `id` (lower case, hyphens, no spaces), a heading in `<h2>`, and a one- or two-sentence introduction in `<p class="group-intro">`. Spell out any acronym in full the first time it appears on the page.
3. The page alternates dark and teal backgrounds. Sections with `class="tint"` are teal. Set the `class="tint"` attributes so that no two neighbouring sections have the same background.
4. Add a link to the theme list near the top, inside `<ul class="theme-list">`:
   ```html
            <li><a href="#new-id">New theme heading</a></li>
   ```
5. Update the count line ("… in nine themes").

## 6. Check before merging

- Open `research.html` in a browser (download it with the `assets` folder, or use the preview of the branch) and check the new entry looks like its neighbours.
- Click the DOI link.
- Rules from [CLAUDE.md](../CLAUDE.md) apply here too: British spelling in the introductions, no unpublished manuscript text, and nothing confidential. A citation of a published or accepted paper is fine.
