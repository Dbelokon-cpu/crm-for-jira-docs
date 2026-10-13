# CRM for Jira: Documentation

Public documentation, privacy policy and security policy for the CRM for Jira app by Vudia. The app's source code lives in a separate, private repository; this one holds only the user-facing docs.

## How the site is made

The pages are generated from content fragments, so every page shares one navigation, one stylesheet and one layout.

```
src/*.html        content, one fragment per page (edit these)
tools/build.py    builds the pages (Python 3, standard library only)
assets/           style.css, site.js (search, nav), search-index.json (generated)
*.html in root    generated pages, committed, because GitHub Pages serves the repo as-is
```

To change the docs:

1. Edit or add a fragment in `src/`. It starts with one metadata line, then the body (no `<h1>`; the title comes from the metadata):
   `<!--meta {"title": "Deals", "desc": "One-sentence summary shown under the title and in search."} -->`
2. A new page must also be added to the `NAV` list in `tools/build.py`.
3. Run `python3 tools/build.py` and commit the source **and** the generated pages.

The build fails on a link to a page that does not exist or to a section (`page.html#anchor`) that is missing, so broken internal links are caught before publishing.

## Structure

Start (overview, quick start) · Concepts (pipeline, records) · Guides (leads, deals, contacts and companies, products, tasks, search and filters, bulk and CSV, dashboard, reports, activities, settings, Jira links) · Reference (limits, permissions, glossary) · Help (troubleshooting, FAQ, what's new) · Policies (privacy, security). One worked example, the *Northwind Traders* sale, runs through the pages so numbers can be followed from page to page.

When the app changes behaviour, update the matching page, the troubleshooting entry if the symptom changes, and add a line to `src/changelog.html`.
