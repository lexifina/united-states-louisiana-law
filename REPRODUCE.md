# How this repository was made (Louisiana)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Louisiana Laws (Louisiana State Legislature) | <https://legis.la.gov/legis/Laws.aspx> | 2026-10-30 | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020). legis.la.gov states no copyright claim; it notes that the provisions "are provided for informational purposes" and are not official or authoritative. Only the text of each provision is taken. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of Louisiana (1974) | 1 | 2026-10-29 to 2026-10-29 |
| `rs-title-12-corporations-and-associations` | Louisiana Revised Statutes, Title 12: Corporations and Associations | 1 | 2026-10-29 to 2026-10-29 |
| `rs-title-14-criminal-law` | Louisiana Revised Statutes, Title 14: Criminal Law | 1 | 2026-10-29 to 2026-10-29 |
| `civil-code-book-2-things` | Louisiana Civil Code, Book II: Things and the Different Modifications of Ownership (arts. 448-818) | 1 | 2026-10-29 to 2026-10-29 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: La. R.S. 24:4: an act takes effect on August 1 of the year of a regular session unless it says otherwise; this first build holds only the current text, dated by the day before retrieval https://legis.la.gov/legis/Laws_Toc.aspx?folder=75&level=Parent

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `bf3efdcaaae1f6de04be80afbfb72478c1a687769dc74e070929daa52ec0d8e7` (3676482 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- First build: the Constitution, Revised Statutes Titles 12 and 14 and Civil Code articles 448 to 818 only, as retrieved on 2026-10-30. Each act has one version, credited to the publisher as the oldest version available.
- The version is dated 2026-10-29, the last full day before retrieval, so that no commit is dated ahead of the build; the site prints no edition date.
- Civil Code Book II is taken as articles 448 to 818 (the articles between Civil Code 448 and the one before 870, the first of Book III).
- Each section keeps the Act citations (source note) that close it; no annotations are taken.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
