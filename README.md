# SEIS 201: AI for CE/ME Engineers (drafts)

Course-design work for SEIS 201, University of St. Thomas, Spring 2027 (28 Tue/Thu meetings, 3 credits, 75 minutes). Everything here is a draft. Nothing has been reviewed by an engineering or statistics instructor.

## What is here

| Folder | Contents |
|---|---|
| `learning-graph-v1/` | First learning graph built from the syllabus (230 concepts), McCreary-style CSV/JSON, viewer, syllabus findings |
| `learning-graph-v2/` | Trimmed to fit Spring 2027 (163 concepts, 299 edges, meetings M01-M28), `spring-2027-plan.md`, `definitions.csv` (all 163 defined and reviewed), `graph-viewer.html`, Qwen prompt packet |
| `guides/` | Four self-check guides: probability and sampling, code-reading primer (Python assumed), engineering reference cards, ten optional concepts. Completion code, nothing collected. See `guides/README.md` |
| `vocab-lab/` | `vocab-lab.html`, a single-file vocabulary game (five modes, all 163 terms) |
| `tools/` | Generators. Paths inside point at the original workspace; edit the paths at the top of each script before re-running |

Open each `.html` file directly in a browser. No server, login, or network needed (the graph viewers load vis-network from a CDN).

## Status (paused)

Work is paused for now. Nothing above is final.

## Open items

- Technical review: a licensed engineer should check `definitions.csv` rows 144, 153, 154 (accountability, PE stamp, responsible charge; state-dependent) and the reference cards
- Graph edges and the ten cut concepts have not been validated by an engineer
- Confirm the course programming language (guides assume Python and pandas) and which meaning of "calibration" the syllabus uses
- Registrar approval needed for Exam 2 in the finals slot; exam time for a Tue/Thu section unconfirmed
- Decide whether to restore any cut concepts (buy-back order: calibration, multiple regression, tradeoff uncertainty, standard of care and code of ethics, the rest)
- ENGR 100 content is still unchecked against the assumed-on-entry list
- Vocab Lab feedback so far: "ok but a bit boring." Entry-level concepts (statics, stress and strain, beam bending) are inherently easy to recognize. Ideas not built: short application questions for those five, progress that persists across visits, a story or scenario layer
- Progress in Vocab Lab and the guides resets on reload by design (no storage)

## Method notes

- Definitions: first drafts by a local Qwen model, then reviewed. 98 kept, 54 edited, 11 rewritten (see `ReviewStatus` and `ReviewNote` columns)
- Answer choices in Vocab Lab come from graph neighbors, hand-built look-alike clusters, and shared wording, with 17 hand-listed overlapping pairs kept apart
- Prompt wording that gives an answer away is masked with blanks
