# How this repository was made (Louisiana)

This file is written by the build on 2026-11-10, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Louisiana Laws (Louisiana State Legislature) | <https://legis.la.gov/legis/Laws.aspx> | 2026-10-30 | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020). legis.la.gov states no copyright claim; it notes that the provisions "are provided for informational purposes" and are not official or authoritative. Only the text of each provision is taken. |
| Louisiana Laws (Louisiana State Legislature), wave 4 | <https://legis.la.gov/legis/LawSearch.aspx> | 2026-11-10 | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020); legis.la.gov states no copyright claim. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of Louisiana (1974) | 1 | 2026-10-29 to 2026-10-29 |
| `rs-title-12-corporations-and-associations` | Louisiana Revised Statutes, Title 12: Corporations and Associations | 1 | 2026-10-29 to 2026-10-29 |
| `rs-title-14-criminal-law` | Louisiana Revised Statutes, Title 14: Criminal Law | 1 | 2026-10-29 to 2026-10-29 |
| `civil-code-book-2-things` | Louisiana Civil Code, Book II: Things and the Different Modifications of Ownership (arts. 448-818) | 1 | 2026-10-29 to 2026-10-29 |
| `constitution-ancillaries` | Louisiana Constitution Ancillaries | 1 | 2026-11-10 to 2026-11-10 |
| `civil-code-preliminary-title` | Louisiana Civil Code, Preliminary Title (arts. 1-23) | 1 | 2026-11-10 to 2026-11-10 |
| `civil-code-book-1-persons` | Louisiana Civil Code, Book I: Of Persons (arts. 24-447) | 1 | 2026-11-10 to 2026-11-10 |
| `civil-code-book-3-acquiring-things` | Louisiana Civil Code, Book III: Of the Different Modes of Acquiring the Ownership of Things (arts. 870-3514, 3550-3556) | 1 | 2026-11-10 to 2026-11-10 |
| `civil-code-book-4-conflict-of-laws` | Louisiana Civil Code, Book IV: Conflict of Laws (arts. 3515-3549) | 1 | 2026-11-10 to 2026-11-10 |

The build made 9 commits:

| Commits | Kind |
| ---: | --- |
| 9 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-10.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 9 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: La. R.S. 24:4: an act takes effect on August 1 of the year of a regular session unless it says otherwise; this first build holds only the current text, dated by the day before retrieval https://legis.la.gov/legis/Laws_Toc.aspx?folder=75&level=Parent

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `a466a3fffc69232ffa7cb867cbdd22d249e6d892491f37ef29912d75e77b449d` (4947412 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `3024ff164c261807dfc4d5b7b1b4a2cde4357da1`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- First build: the Constitution, Revised Statutes Titles 12 and 14 and Civil Code articles 448 to 818 only, as retrieved on 2026-10-30. Each act has one version, credited to the publisher as the oldest version available.
- The version is dated 2026-10-29, the last full day before retrieval, so that no commit is dated ahead of the build; the site prints no edition date.
- Civil Code Book II is taken as articles 448 to 818 (the articles between Civil Code 448 and the one before 870, the first of Book III).
- Each section keeps the Act citations (source note) that close it; no annotations are taken.
- Wave 4 (2026-11-10): every other Revised Statutes title, the Constitution Ancillaries, the rest of the Civil Code, the Codes of Civil and Criminal Procedure, the Children's Code and the Code of Evidence, one act each (the Civil Code by book), read like the first build. The House, Senate and Joint Rules are not taken: they are chamber rules, not law.
- Each wave 4 act has one version, the text published now, dated by the day its pages were retrieved (the site prints no edition date), credited to the publisher as the oldest version available.
- Civil Code books are split by article number: Preliminary Title 1-23, Book I 24-447, Book III 870-3514 and 3550-3556 (Title XXV follows Book IV in the numbering), Book IV 3515-3549.
- Civil Code articles 819, 823 and 856 are left out: each is only the line that articles 819-822, 823-855 and 856-869 were repealed in 1977, printed after Book II (which this repository holds as articles 448-818).

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
