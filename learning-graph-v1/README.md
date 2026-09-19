# SEIS 201 learning graph (v0.1 draft, 2026-09-18)

230 concepts, 417 prerequisite edges, one connected graph, longest prerequisite chain 16. 12 concepts assumed on entry, 202 taught by a named session, 16 implied (needed but not taught). Passes: no cycles, no orphans, every prerequisite scheduled no later than the concept that needs it, all labels 32 characters or fewer, no category above 30%.

Built from the syllabus text (Sept 2026 draft, "SEIS 201: TBD") in the McCreary learning-graph layout: `learning-graph.csv` (ConceptID, ConceptLabel, Dependencies pipe-delimited, TaxonomyID), `learning-graph.json` (metadata, groups, nodes, edges), `taxonomy-names.json`, `metadata.json`. Extra files: `concept-schedule.csv` (session, unit, status, prerequisite names), `concept-list.md`, `quality-metrics.md`, `taxonomy-distribution.md`, `syllabus-findings.md`, `graph-viewer.html`.

Format note: built from the published learning-graph-generator description, not from the local MicroSims files, which could not be read (OneDrive unavailable). Check the JSON edge direction and column names against the local viewer before loading. Edges here run from the dependent concept (from) to its prerequisite (to).

Units: 1 = W1-3, 2 = W4-7, 3 = W8-10 (plus proposed W7 code primer), 4 = W11-12, 5 = W13-16. Replaces nothing: the earlier 174-concept summary (`claude/seis201-learning-graph-summary.md`) described a bundle that was never saved, so the two are not comparable one-to-one.

Not done: one-line concept definitions; expert review of dependencies (Dana Miller, Barton Malow, is the named technical validator).
