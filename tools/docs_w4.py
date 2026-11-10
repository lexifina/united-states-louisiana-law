"""Writes repo/README.md, LICENSE and jurisdiction.json from corpus.json plus the verified corpus.d parts (wave 4)."""
import json, os, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'world-law'))
sys.path.insert(0, str(HERE.parent / 'gitlaw_common'))
from state_docs import write_docs  # noqa: E402
import publish_marker  # noqa: E402

c = json.loads((HERE / 'corpus.json').read_text('utf-8'))
acts = list(c['acts'])
for p in sorted((HERE / 'corpus.d').glob('*.json')):
    if publish_marker.verified(p):
        acts += json.loads(p.read_text('utf-8')).get('acts', [])
order = {'constitution': 0, 'constitution-ancillaries': 1}


def rank(a):
    s = a['slug']
    if s in order:
        return (order[s], 0, s)
    if s.startswith('civil-code'):
        return (2, ['preliminary', 'book-1', 'book-2', 'book-3', 'book-4'].index(next(k for k in ['preliminary', 'book-1', 'book-2', 'book-3', 'book-4'] if k in s)), s)
    if s.startswith('code-') or s.startswith('childrens'):
        return (3, 0, s)
    return (4, int(s.split('-')[2]), s)


rows = []
for a in sorted(acts, key=rank):
    v = a['versions'][0]
    day = v['from']
    when = 'retrieved 30 October 2026' if day == '2026-10-29' else 'retrieved %d November 2026' % int(day[8:])
    rows.append({'folder': a['slug'], 'title': a['title'] + f" ({len(v['units'])} sections)", 'versions': len(a['versions']),
                 'history': f'One version: the text as the Louisiana State Legislature publishes it, {when}'})
n = sum(len(a['versions'][0]['units']) for a in acts)
write_docs(HERE, {
    'name': 'Louisiana', 'code': 'LA', 'slug': 'united-states-louisiana', 'date': '2026-11-10', 'domain': 'legis-la',
    'publisher': 'the Louisiana State Legislature',
    'acts': rows,
    'build': f'built: Constitution of Louisiana and its Ancillaries, the Revised Statutes, the Civil Code, the Codes of Civil and Criminal Procedure, the Children\'s Code and the Code of Evidence as published on legis.la.gov ({len(acts)} acts, {n} sections), current text only (one version each)',
    'source': ("The text is read from **Louisiana Laws** on <https://legis.la.gov/>, published by the **Louisiana State Legislature**. The site "
               "publishes no robots.txt (404, re-read 10 November 2026). Tables of contents are the site's own form postbacks; each section is one "
               "GET of its `Law.aspx?d=` page, one request at a time and at most two a second. The Legislature notes that the provisions are "
               "provided for information and are not official or authoritative; this repository carries them as published there. Each "
               "section keeps its text and the Act citations that close it. Annotations are not taken. The House, Senate and Joint Rules, "
               "which the same site publishes, are chamber rules and are not taken."),
    'dates': ("- Each act has **one version**: the first build's four acts are dated 29 October 2026, the last full day before their pages "
              "were retrieved on 30 October 2026; every later act is dated the day its pages were retrieved (November 2026). The site prints "
              "no edition date. It is the oldest version available: the Legislature publishes the current text only.\n"
              "- The first commit of each act is credited to the Louisiana State Legislature as \"oldest version available\".\n"
              "- The Act citations in each section are part of the text, not the commit dates."),
    'limits': ("- Any amendment history: past versions are not online.\n"
               "- Any title or code whose pages are not yet all retrieved (see the table above for what is in).\n"
               "- Regulations (the Louisiana Administrative Code) and the chamber rules.\n"
               "- Nothing here is an official publication."),
    'licence': ("The legal text is the law of Louisiana as published by the Louisiana State Legislature at https://legis.la.gov/. "
                "Statutes are not copyrightable (Georgia v. Public.Resource.Org, Inc., 590 U.S. 255 (2020)), and the site states no "
                "copyright claim. The text is republished unaltered in its wording, with credit to the Louisiana State Legislature as its publisher."),
})
readme = HERE / 'repo' / 'README.md'
t = readme.read_text('utf-8')
link = ("Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the law "
        "of Louisiana, United States, which global-law reads at `united-states/louisiana/acts/`.\n\n")
if 'Part of [lexifina/global-law]' not in t:
    t = t.replace('\n\n', '\n\n' + link, 1)
t = t.replace("Nothing else of Louisiana's law is in it yet.", "Titles and codes not listed are not in it yet.")
t = t.replace('**What is in it now (a first build, not complete)**', '**What is in it now**')
t = t.replace('because this first build holds one version of each act', 'because the repository holds one version of each act')
readme.write_text(t, encoding='utf-8', newline='\n')
print(len(rows), 'acts', n, 'sections')
