# SEIS 201: fitting the course to Spring 2027 (draft plan)

## Bottom line

- Spring 2027 gives **28 Tuesday/Thursday meetings** (Feb 2 to May 13), not 30, because classes start Feb 1 and mid-term plus Easter break runs Mar 22 to 29. Source: St. Thomas 2026-27 undergraduate calendar.
- Assumptions you gave me: 75-minute meetings, 3 credits, Exam 2 moves into the finals slot (May 17-21). Exam 1 stays in class time on Mar 18.
- That leaves **26 teaching meetings**. The syllabus needs 27, plus about 2 sessions of fill-in material for the holes. All of it fits by removing 14 concepts, merging 23, and turning 30 concepts into lab examples (details below).
- Result: 147 concepts taught in class (about 5.7 per meeting, none above 7), 4 in an async module, 9 expected on entry, 3 supplied on lab reference cards.
- The 5.7 per meeting figure is my judgment for a 75-minute session, not something I tested. If you think 7 to 8 is workable, the buy-back list restores content first.

## What is a prerequisite

Holding your earlier decision (no math or programming prerequisite), the prerequisites are engineering only:

- ENGR 100 or equivalent, plus declared CE/ME major (as your earlier analysis recommended). **ENGR 100 content is still unchecked.**
- Expected on entry, all things an engineering first-year should have: algebra, units and dimensional analysis, significant figures, ratios and percentages, reading plots, spreadsheets and CSV files, using a chat assistant, and knowing that engineering codes and standards exist.
- **Not prerequisites, supplied instead:** statics, stress and strain, and beam bending. Each lab hands out a one-page reference card with the formula and a worked answer. I'd also add cards for thermal resistance and factor of safety, which appear in the project options. This matches your earlier flag that the engineering level is unstated.

## How each hole is filled

| Hole in the syllabus | Fix | Where |
|---|---|---|
| Probability | Taught as a 15-minute block | Meeting 3 (Feb 9) |
| Sample versus population | Taught inside descriptive stats | Meeting 4 (Feb 11) |
| Random sampling, sampling variability | Moved into space freed by cutting calibration | Meeting 9 (Mar 2) |
| Standard error, the t multiplier | Taught with confidence intervals; t value read from a table or tool, not derived | Meeting 10 (Mar 4) |
| Code reading (7 concepts) | Compressed to 4 and moved to a self-paced async module, auto-checked, low stakes. Assigned Meeting 12, due before Meeting 15 | Async |
| Frequency (vibration spectrum) | Removed by switching the Week 6 chart example to traffic flow | Meeting 12 |
| Thermal resistance, factor of safety | Lab reference cards, not taught concepts | Labs |

## What was cut, merged, or demoted

- **Cut or optional (14):** model calibration, multiple regression, context window, logarithmic scale, stale data, sensitivity analysis, uncertainty in tradeoff inputs, standard of care, corroborating across sources, engineering code of ethics, and four presentation-skills items (technical communication, presenting verification, stating tool limits, defending choices), which are practiced in the presentations, not taught.
- **Merged (23):** for example, variance into standard deviation, p-value into significance, confounders into spurious correlation, tokens into LLMs. Full list in `disposition-of-v01-concepts.csv`.
- **Lab examples (30):** cylinder strength data, fatigue data, cantilever beam, truss, footing, heat exchanger and similar. They stay as the exercises the syllabus names, but they no longer count as new concepts.
- **Structure change:** the two Week 12 sessions merge into one (research assistant plus design tradeoffs). That is the biggest content compression, and it touches two things the course description promises. Watch it.

## Buy-back order if you get more room

1. Model calibration (Meeting 9), 2. multiple regression (Meeting 8), 3. uncertainty in tradeoff inputs (Meeting 23), 4. standard of care and 5. code of ethics (Meeting 26), 6. sensitivity analysis, 7. corroborating sources, 8. context window, 9. stale data, 10. log scale.

## Risks and open decisions

- **Exam 1 is a 75-minute applied practical.** The syllabus called it a full session. A practical on real data in 75 minutes needs a tighter design, or a slot outside class time.
- **Exam 2 in the finals slot needs registrar approval.** I haven't confirmed the exam time for a Tuesday/Thursday section. It now also comes after Unit 5, so decide whether it covers Units 3 to 5 or 3 and 4 only.
- **The project window shrinks** from about 33 days to 26 if it is assigned Apr 15. Announce the options at Meeting 16 (Apr 1) to get it back to about 40.
- **Meeting 12 has 4 concepts** so it can double as Exam 1 review. That review session replaces the "Semester review" the syllabus put in Week 7 Tuesday.
- **Homework:** 12 assignments still fit, one per week from Meeting 15 on. HW1 to HW6 are unchanged.
- **Nothing is validated by an engineer yet.** The dependency edges and the cut choices need review before this goes into a syllabus.

## Meeting calendar

| Meeting | Date | Topic | Concepts | Unit |
|---|---|---|---|---|
| 1 | Tue Feb 2 | What is AI. Rules versus learned patterns | 6 | 1 |
| 2 | Thu Feb 4 | Why statistics matters. Measurement activity | 6 | 1 |
| 3 | Tue Feb 9 | How LLMs generate answers (+ probability basics) | 7 | 1 |
| 4 | Thu Feb 11 | Descriptive statistics. Measurement lab | 6 | 1 |
| 5 | Tue Feb 16 | Agentic AI | 6 | 1 |
| 6 | Thu Feb 18 | Distributions. Auditing an agent's analysis | 6 | 1 |
| 7 | Tue Feb 23 | Where AI bias comes from | 6 | 2 |
| 8 | Thu Feb 25 | Correlation and regression. Spurious correlation | 6 | 2 |
| 9 | Tue Mar 2 | Overconfidence and false precision (+ sampling) | 5 | 2 |
| 10 | Thu Mar 4 | Confidence intervals and significance | 5 | 2 |
| 11 | Tue Mar 9 | Agentic dashboards | 5 | 2 |
| 12 | Thu Mar 11 | Data visualization. Critiquing AI charts (+ Exam 1 review) | 4 | 2 |
| 13 | Tue Mar 16 | Agentic data pipelines | 6 | 2 |
| 14 | Thu Mar 18 | EXAM 1 (75-minute applied practical) | 0 | 2 |
| 15 | Tue Mar 30 | How AI code generation works | 5 | 3 |
| 16 | Thu Apr 1 | Vibe coding (announce project options) | 5 | 3 |
| 17 | Tue Apr 6 | Agentic coding. AI-written tests | 6 | 3 |
| 18 | Thu Apr 8 | Verifying AI code against known answers | 6 | 3 |
| 19 | Tue Apr 13 | Multi-step agentic debugging | 6 | 3 |
| 20 | Thu Apr 15 | Debugging with AI. Project assigned | 5 | 3 |
| 21 | Tue Apr 20 | Iterative design workflows | 5 | 4 |
| 22 | Thu Apr 22 | Building a calculation or design tool | 5 | 4 |
| 23 | Tue Apr 27 | AI as research assistant and design partner (old W12 merged) | 6 | 4 |
| 24 | Thu Apr 29 | Ethics, bias and risk in autonomous AI | 7 | 5 |
| 25 | Tue May 4 | Verification practices for agentic output | 5 | 5 |
| 26 | Thu May 6 | Safety-critical work. Licensure and responsibility | 5 | 5 |
| 27 | Tue May 11 | Limits of AI (project due) | 6 | 5 |
| 28 | Thu May 13 | Project presentations | 0 | 5 |