# Louisiana: law history in git

The statute law of Louisiana as a git repository: one file per section, committed with the official publisher named as author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of Louisiana (1974) (337 sections) | 1 | One version: the text as the Louisiana State Legislature publishes it, retrieved 30 October 2026 |
| `rs-title-12-corporations-and-associations/` | Louisiana Revised Statutes, Title 12: Corporations and Associations (924 sections) | 1 | One version: the text as the Louisiana State Legislature publishes it, retrieved 30 October 2026 |
| `rs-title-14-criminal-law/` | Louisiana Revised Statutes, Title 14: Criminal Law (730 sections) | 1 | One version: the text as the Louisiana State Legislature publishes it, retrieved 30 October 2026 |
| `civil-code-book-2-things/` | Louisiana Civil Code, Book II: Things and the Different Modifications of Ownership (arts. 448-818) (377 sections) | 1 | One version: the text as the Louisiana State Legislature publishes it, retrieved 30 October 2026 |

Nothing else of Louisiana's law is in it yet.

## Where the text comes from

The text is read from **Louisiana Laws** on <https://legis.la.gov/>, published by the **Louisiana State Legislature**. The Legislature notes that the provisions are provided for information and are not official or authoritative; this repository carries them as published there. Each section keeps its text and the Act citations that close it. Annotations are not taken.

## Dates

- Each act has **one version**, dated 29 October 2026, the last full day before the pages were retrieved on 30 October 2026 (the site prints no edition date, and no commit is dated ahead of the build). It is the oldest version available: the Legislature publishes the current text only.
- The first commit of each act is credited to the Louisiana State Legislature as "oldest version available".
- The Act citations in each section are part of the text, not the commit dates.

## What it does not show

- Any amendment history: past versions are not online.
- The rest of the Revised Statutes, the other Civil Code books, the procedure codes, the Children's Code and regulations.
- Nothing here is an official publication.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- Each source file is identified by its sha256, in `data/versions.json`.

## What "author" means

Each commit is authored by the publisher (the Louisiana State Legislature) because this first build holds one version of each act, the oldest version available. The committer is always Lexifina.
