#!/usr/bin/env python3
"""Builds the documentation site: src/*.html fragments -> pages in the repo root.

Run from the repository root:  python3 tools/build.py
No dependencies beyond the standard library. The generated pages are committed,
because GitHub Pages serves the repository as-is.

A fragment starts with one line of metadata:
    <!--meta {"title": "...", "desc": "one-sentence summary"} -->
followed by the page body (no <h1>: the template draws it from the title).
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

SITE = "CRM for Jira"
NAV = [
    ("Start", [("index", "Overview"), ("quick-start", "Quick start")]),
    ("Concepts", [("pipeline", "Leads, deals and the pipeline"), ("records", "Records, notes and timeline")]),
    ("Guides", [
        ("leads", "Leads"), ("deals", "Deals"), ("contacts-companies", "Contacts and companies"),
        ("products", "Products"), ("tasks", "Tasks"), ("finding", "Search, filters and saved views"),
        ("bulk-csv", "Bulk actions, import and export"), ("dashboard", "Dashboard"), ("reports", "Reports"),
        ("activities", "Activities"), ("settings", "Settings"), ("jira", "Linking to Jira and sharing records"),
    ]),
    ("Reference", [("limits", "Limits and behaviour"), ("permissions", "Permissions and access"), ("glossary", "Glossary")]),
    ("Help", [("troubleshooting", "Troubleshooting"), ("faq", "FAQ and support"), ("changelog", "What's new")]),
    ("Policies", [("privacy", "Privacy policy"), ("security", "Security policy")]),
]
ORDER = [slug for _, items in NAV for slug, _ in items]
LABEL = {slug: label for _, items in NAV for slug, label in items}
GROUP = {slug: g for g, items in NAV for slug, _ in items}

LOGO = '<img src="assets/icon.svg" width="30" height="30" alt="" aria-hidden="true">'

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="icon" href="assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<div class="shell">
  <aside class="side">
    <a class="brand" href="index.html">
      <div class="brand-mark">{logo}</div>
      <div><div class="brand-name">CRM FOR JIRA</div><div class="brand-sub">Documentation · by Vudia</div></div>
    </a>
    <div class="search">
      <input id="q" type="search" placeholder="Search the docs" aria-label="Search the documentation" autocomplete="off">
      <div class="search-results" id="results" hidden></div>
    </div>
    <details class="nav-wrap" open>
      <summary>Menu</summary>
      <nav class="toc" aria-label="Documentation">
{nav}
      </nav>
    </details>
    <div class="meta-card">
      <div class="meta-row"><span class="meta-label">Platform</span><div class="meta-value">Atlassian Forge · Jira Cloud</div></div>
      <div class="meta-row"><span class="meta-label">Support</span><div class="meta-value"><a href="mailto:info@vudia.site">info@vudia.site</a></div></div>
    </div>
  </aside>

  <main id="content">
    <div class="crumb">{crumb}</div>
    <h1>{title}</h1>
    <p class="subtitle">{desc}</p>
{body}
{pagenav}
    <div class="colophon">CRM for Jira is built on Atlassian Forge and runs entirely on Atlassian's infrastructure. Questions or corrections: <a href="mailto:info@vudia.site">info@vudia.site</a>.</div>
  </main>

  <nav class="toc-right" aria-label="On this page">
{toc}
  </nav>
</div>
<script src="assets/site.js"></script>
</body>
</html>
"""


def slugify(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-") or "section"


def add_ids(body):
    """Give every h2/h3 an id (unique per page) and a hover anchor link."""
    seen = set(re.findall(r'id="([^"]+)"', body))

    def repl(m):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        found = re.search(r'id="([^"]+)"', attrs)
        if found:
            hid = found.group(1)
        else:
            base = slugify(inner)
            hid, n = base, 2
            while hid in seen:
                hid, n = f"{base}-{n}", n + 1
            seen.add(hid)
            attrs = f'{attrs} id="{hid}"'
        return f'<{tag}{attrs}>{inner}<a class="h-anchor" href="#{hid}" aria-label="Link to this section">#</a></{tag}>'

    return re.sub(r"<(h[23])([^>]*)>(.*?)</\1>", repl, body, flags=re.S)


def toc_for(body):
    items = re.findall(r'<h2[^>]*id="([^"]+)"[^>]*>(.*?)<a class="h-anchor"', body, flags=re.S)
    if len(items) < 2:
        return ""
    links = "\n".join(f'    <a href="#{i}">{html.unescape(re.sub(r"<[^>]+>", "", t)).strip()}</a>' for i, t in items)
    return f"    <p>On this page</p>\n{links}"


def plain(body):
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    return re.sub(r"\s+", " ", html.unescape(body)).strip()


def nav_html(current):
    out = []
    for group, items in NAV:
        out.append(f'        <span class="toc-group-label">{group}</span>')
        for slug, label in items:
            cur = ' aria-current="page"' if slug == current else ""
            out.append(f'        <a href="{slug}.html"{cur}>{html.escape(label)}</a>')
    return "\n".join(out)


def pagenav(slug):
    i = ORDER.index(slug)
    prev = f'<a class="prev" href="{ORDER[i-1]}.html"><small>Previous</small>{html.escape(LABEL[ORDER[i-1]])}</a>' if i > 0 else ""
    nxt = f'<a class="next" href="{ORDER[i+1]}.html"><small>Next</small>{html.escape(LABEL[ORDER[i+1]])}</a>' if i < len(ORDER) - 1 else ""
    return f'    <div class="pagenav">{prev}{nxt}</div>' if prev or nxt else ""


def main():
    search, problems = [], []
    ids, links = {}, []
    for slug in ORDER:
        path = SRC / f"{slug}.html"
        if not path.exists():
            problems.append(f"missing source: src/{slug}.html")
            continue
        text = path.read_text(encoding="utf-8")
        m = re.match(r"\s*<!--meta\s*(\{.*?\})\s*-->\s*", text, flags=re.S)
        if not m:
            problems.append(f"src/{slug}.html: no <!--meta {{...}}--> header")
            continue
        meta = json.loads(m.group(1))
        body = add_ids(text[m.end():].strip("\n"))
        title = meta["title"]
        crumb = f'<a href="index.html">Docs</a> / {GROUP[slug]}' if slug != "index" else "Documentation"
        page = TEMPLATE.format(
            page_title=html.escape(f"{title} · {SITE} documentation" if slug != "index" else f"{SITE} documentation"),
            desc=html.escape(meta["desc"], quote=True), logo=LOGO, nav=nav_html(slug), crumb=crumb,
            title=html.escape(title), body="\n".join("    " + l if l.strip() else l for l in body.split("\n")),
            pagenav=pagenav(slug), toc=toc_for(body),
        )
        (ROOT / f"{slug}.html").write_text(page, encoding="utf-8")
        headings = " ".join(html.unescape(re.sub(r"<[^>]+>|#$", "", h)) for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body, flags=re.S))
        search.append({"url": f"{slug}.html", "title": title, "headings": headings, "text": plain(body)})

        # Broken internal links are a build error, not a surprise for a reader.
        ids[slug] = set(re.findall(r'id="([^"]+)"', body))
        for href, anchor in re.findall(r'href="([^"#:]+\.html)(?:#([^"]*))?"', body):
            if href.removesuffix(".html") not in ORDER:
                problems.append(f"src/{slug}.html: link to unknown page {href}")
            else:
                links.append((slug, href.removesuffix(".html"), anchor))
        for anchor in re.findall(r'href="#([^"]+)"', body):
            links.append((slug, slug, anchor))

    for src_slug, target, anchor in links:
        if anchor and anchor not in ids.get(target, set()):
            problems.append(f"src/{src_slug}.html: link to #{anchor} but {target}.html has no such section")

    # The 404 page uses the same shell.
    page404 = TEMPLATE.format(
        page_title=f"Page not found · {SITE} documentation", desc="This page does not exist.", logo=LOGO,
        nav=nav_html(""), crumb="Documentation", title="Page not found",
        body='    <p>That page does not exist or has moved. Try the <a href="index.html">overview</a> or search the docs.</p>',
        pagenav="", toc="")
    (ROOT / "404.html").write_text(page404, encoding="utf-8")

    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "search-index.json").write_text(json.dumps(search, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)
    print(f"built {len(search)} pages")


if __name__ == "__main__":
    main()
