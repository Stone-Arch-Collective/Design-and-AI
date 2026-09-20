# SEIS 201 Simulation Plan: ACMEJOB.Ai and the Otter Bend Lift Bridge

Draft v0.2, 2026-09-19, Shannon Seaver. Exported copy. The live, editable version is the Claude doc at https://claude.ai/code/artifact/32916372-255d-40c1-ba75-2eb22e8ae848. Supersedes nothing: `acmejob-semester-outline.md` (v0.1) remains the story source; this adds the knowledge-graph match, the mechanics numbers, and Unit 1 and 2 meeting detail.

## What this is

This is a draft plan to run SEIS 201 (Spring 2027, 28 Tuesday/Thursday meetings) as one continuous job at a fictional engineering firm, instead of 28 unconnected examples. The syllabus topics, the order, the exams and the grading weights do not change. What changes is that every lab, dataset and exam comes from the same bridge and the same project file.

- **What it covers.** All 163 concepts in the course knowledge graph are assigned to a meeting and a story beat. Units 1 and 2 (meetings 1 to 14, through Exam 1) are planned meeting by meeting. Units 3 to 5 are mapped at outline level.
- **Why do it this way.** The skill the course description promises is judgment about AI output: when to trust it, when to check it, and how to show the check. A student only practices that when a wrong number has a cost later. A running project makes week 3 matter in week 13.
- **What it is not.** It is not a game layered over the content. A student who ignores the story does the same engineering and statistics work as one who follows it.
- **Status.** Draft. No engineer or statistics instructor has reviewed the bridge, the data design or the concept order. The open slots for department input are listed in their own section below.

## The simulation in one page

Students are hired as junior engineers at ACMEJOB.Ai, a mid-size Minnesota civil and mechanical firm that sold a county on AI-assisted bridge assessment. The firm's own principal engineer does not trust the AI. Students work in the gap between what was sold and what the engineering requires.

**The project.** The Otter Bend Lift Bridge over the Kinnick River: built 1962, vertical lift span, carrying loads it was not designed for. Kinnick County has installed strain, temperature and vibration sensors and wants an answer by May: rehabilitate or replace. The bridge, town and county are invented. Failure modes come from public engineering literature. No real collapse or casualty event is referenced.

**Why a lift bridge.** One structure carries both majors, and its sensors produce every dataset the course needs.

| Side | What the bridge supplies | Syllabus examples it absorbs |
| --- | --- | --- |
| Civil | Deck, girders, towers, piers, concrete cores, load rating, traffic counts | Load rating check, deck deterioration model, concrete cylinder strength, concrete mix regression, traffic volume, structural health monitoring feed |
| Mechanical | Lift motors, gearbox, sheave bearings, counterweight ropes, thermal expansion at the span locks | Machined part measurement, gear tooth dimensions, fatigue test data, fatigue life prediction, yield strength coupons, vibration data |

**The cast: three, and no more.**

| Who | What they are | What they generate |
| --- | --- | --- |
| Diane Halvorsen, PE | Principal engineer, 27 years. Knows every inspector and contractor in the county, and no statistics. Does not trust AI. | The recurring question: how do you know that is right? |
| Wes Tanaka, EIT | Second-year engineer split across three projects. Trying. | Late, partial, undocumented handoffs |
| FOREMAN | The firm's AI platform. Fast, fluent, confident. Wrong in designed ways about one time in five. Ungendered on purpose. | Every error the course teaches students to catch |

Diane is written as right about a third of the time and wrong in reasonable ways. Her critiques are always substantive. She is demanding because the stakes are real, never because of mood. Writing her as a caricature or as "difficult" would teach contempt for management, which is the wrong lesson.

## Semester map: meetings, graph concepts and story beats

Every meeting keeps its syllabus topic and its knowledge-graph concepts; the story beat is the wrapper. Concept numbers are the ConceptID values in `concept-schedule.csv` (version 2 of the graph, 163 concepts). Concepts 1 to 12 are entry knowledge: nine assumed, three (statics, stress and strain, beam bending) supplied on reference cards.

### Unit 1: Hired (meetings 1 to 6, Feb 2 to 18). How AI works, and describing data

Diane's bar is low. One sentence of justification is accepted. It will not be for long.

| Mtg | Date | Syllabus topic | Concepts | Story beat |
| --- | --- | --- | --- | --- |
| M01 | Tue Feb 2 | What is AI. Rules versus learned patterns | 13-18 (6) | First day. FOREMAN's demo and Diane's orientation contradict each other within the hour. |
| M02 | Thu Feb 4 | Why statistics matters. Measurement activity | 19-24 (6) | Diane makes new hires measure a part by hand before touching sensor data. Then the first site file: eight strain gauges, one mis-zeroed. |
| M03 | Tue Feb 9 | How LLMs generate answers, plus probability basics | 25-31 (7) | FOREMAN summarizes a design standard and cites a section that does not exist. Nothing flags it. |
| M04 | Thu Feb 11 | Descriptive statistics. Measurement lab | 32-37 (6) | Deck core strengths come back from the lab. Diane wants one number. The spread is the finding. |
| M05 | Tue Feb 16 | Agentic AI | 38-43 (6) | FOREMAN runs a multi-step job on the live sensor feed overnight. A threshold alarm fires at 3 a.m. |
| M06 | Thu Feb 18 | Distributions. Auditing an agent's analysis | 44-49 (6) | Was the alarm real? FOREMAN's summary assumed the wrong distribution. Student hands the gauge file to Wes. |

### Unit 2: Doubt (meetings 7 to 14, Feb 23 to Mar 18). Judging AI and data claims

The tool starts being wrong in ways that matter. The schedule slips, so Diane flips to believing the tool exactly when the student needs her skeptical.

| Mtg | Date | Syllabus topic | Concepts | Story beat |
| --- | --- | --- | --- | --- |
| M07 | Tue Feb 23 | Where AI bias comes from | 50-55 (6) | FOREMAN's damage model was trained on highway girder bridges in warm states. This is a lift bridge in Minnesota. |
| M08 | Thu Feb 25 | Correlation and regression. Spurious correlation | 56-61 (6) | FOREMAN reports strain rising month over month as structural damage. It is spring. |
| M09 | Tue Mar 2 | Overconfidence and false precision, plus sampling | 62-66 (5) | Remaining fatigue life reported to the single cycle. And the cores were drilled where access was easy. |
| M10 | Thu Mar 4 | Confidence intervals and significance | 67-71 (5) | Did the deck get worse since 2019, or is the difference noise? First claim the student defends statistically. |
| M11 | Tue Mar 9 | Agentic dashboards | 72-76 (5) | FOREMAN builds a county-facing dashboard and asks permission to publish it. |
| M12 | Thu Mar 11 | Data visualization. Critiquing AI charts, plus Exam 1 review | 77-80 (4) | A truncated axis makes normal variation look like failure. The county reads charts, not appendices. |
| M13 | Tue Mar 16 | Agentic data pipelines | 81-86 (6) | Wes's handoff arrives: two days late, feet and millimetres in one column, nothing documented. |
| M14 | Thu Mar 18 | Exam 1, 75-minute applied practical | none new | The county calls about an overweight load permit. FOREMAN says yes. Decide today, with reasons. |

Async module (assigned M12, due before M15): code-reading primer, concepts 87-90 (4). In world: you cannot check what you cannot read.

### Unit 3: Build (meetings 15 to 20, Mar 30 to Apr 15). AI-assisted coding and verification

| Mtg | Date | Syllabus topic | Concepts | Story beat |
| --- | --- | --- | --- | --- |
| M15 | Tue Mar 30 | How AI code generation works | 91-95 (5) | The student's first FOREMAN-written script runs clean and the answer is wrong. |
| M16 | Thu Apr 1 | Vibe coding. Project options announced | 96-100 (5) | Writing a specification FOREMAN cannot misread. |
| M17 | Tue Apr 6 | Agentic coding. AI-written tests | 101-106 (6) | FOREMAN writes tests for its own code. They pass. It is still wrong. |
| M18 | Thu Apr 8 | Verifying AI code against known answers | 107-112 (6) | Diane hands over her hand-calculation cards. Her question finally has a real answer. |
| M19 | Tue Apr 13 | Multi-step agentic debugging | 113-118 (6) | A four-step workflow gives a number nobody can explain. One input came from the student's February file. |
| M20 | Thu Apr 15 | Debugging with AI. Project assigned | 119-123 (5) | Root cause versus symptom, with FOREMAN helping debug what FOREMAN broke. |

### Unit 4: Own (meetings 21 to 23, Apr 20 to 27). Building tools and research with AI

The team project is the rehabilitate-or-replace analysis.

| Mtg | Date | Syllabus topic | Concepts | Story beat |
| --- | --- | --- | --- | --- |
| M21 | Tue Apr 20 | Iterative design workflows | 124-128 (5) | Load cases and a parameter sweep. Over a long session FOREMAN drifts off the stated requirements. |
| M22 | Thu Apr 22 | Building a calculation or design tool | 129-133 (5) | Build the tool the firm will reuse. Input validation exists because Wes uses it next. |
| M23 | Tue Apr 27 | AI as research assistant and design partner | 134-139 (6) | FOREMAN's literature summary supports rehabilitation with a fabricated citation. The recommendation is due. |

### Unit 5: Sign (meetings 24 to 28 and finals, Apr 29 to May 21). Responsibility, verification and limits

| Mtg | Date | Syllabus topic | Concepts | Story beat |
| --- | --- | --- | --- | --- |
| M24 | Thu Apr 29 | Ethics, bias and risk in autonomous AI | 140-146 (7) | Who answers for a decision a tool recommended. |
| M25 | Tue May 4 | Verification practices for agentic output | 147-151 (5) | Independent check of the whole package. The February file surfaces with the student's name on it. |
| M26 | Thu May 6 | Safety-critical work. Licensure and responsibility | 152-156 (5) | Diane will not stamp what she cannot defend. She asks whether AI was used. |
| M27 | Tue May 11 | Limits of AI. Project due | 157-162 (6) | Where the tool cannot go: conditions beyond training, and what Diane knows but cannot write down. |
| M28 | Thu May 13 | Project presentations | none new | County board briefing, delivered to non-engineers who will act on it. |
| Finals | May 17-21 | Exam 2 and reflection | 163 (1) | Post-decision review: what the firm recommended, and what the sensors did afterward. |

## Coverage check

All 163 concepts land somewhere: 12 on entry, 146 in a class meeting, 4 in the async module and 1 in the finals reflection. No meeting carries more than 7 new concepts. Counts were checked by script against `concept-schedule.csv`, and every meeting's concept numbers run in one unbroken block.

| Unit | Meetings | Concepts | Of which gap-fills the syllabus did not schedule |
| --- | --- | --- | --- |
| Entry | before M01 | 12 | 3 supplied on reference cards |
| 1 Hired | M01-M06 | 37 | 2 (probability basics, sample versus population) |
| 2 Doubt | M07-M14 | 37 | 4 (random sampling, sampling variability, standard error, the t multiplier) |
| 3 Build | M15-M20 plus async | 37 | 4 async (code reading) |
| 4 Own | M21-M23 | 16 | 0 |
| 5 Sign | M24-M28 plus finals | 24 | 0 |

One thing the map exposes. The graph's verification strand has 20 concepts, but only 2 of them fall in Units 1 and 2; 12 arrive in Unit 3. The simulation asks for a "how I know this is right" note from week one. So in Units 1 and 2 the note may only demand checks already taught by that date: compare against the source (M03), look at the spread (M04), check units (entry knowledge). The formal toolkit arrives at M18, and the story treats that as the moment Diane's question gets a real answer.

## Mechanics: the four rules that make it a simulation

Four rules turn a themed course into a simulation: a budget of hours, a required note, a boss with two modes, and old work that comes back. All numbers below are starting values to be tuned in a one-week pilot, not tested ones.

### Rule 1. Hours, not a clock

Each week the student has **10 project hours** on a fictional timesheet to spend on that week's homework. These are story hours, not real homework time. There is always more worth checking than hours to check it. Choosing what to verify is the skill. There are no countdown timers anywhere: a visible clock rewards speed, and the course is teaching judgment.

| Action | Cost in project hours |
| --- | --- |
| Accept FOREMAN's output as delivered | 0 |
| Spot-check one value against the source | 1 |
| Verify the full output against the source or the data | 2 |
| Recompute independently by hand or spreadsheet | 4 |
| Ask Wes | 1, and the answer arrives next meeting |
| Call the lab or the sensor vendor | 1, and the answer arrives next meeting |
| Redo a note Diane bounced | 2 |

Class time is the same for everyone and is not budgeted. The budget applies to the weekly homework (HW1 to HW6 in Units 1 and 2), where each student chooses differently.

### Rule 2. The note

Every submission carries a short "how I know this is right" statement. The instructor grades it against a rubric. The required form escalates without announcement, and never asks for a check the course has not yet taught.

| Version | When | Required form |
| --- | --- | --- |
| 1 | Unit 1 | One sentence: what I checked it against. |
| 2 | Unit 2 | Three lines: the claim, the check, what the check showed. Includes a number with its spread or interval once M10 has happened. |
| 3 | Units 3 and 4 | Adds a check that does not depend on the tool that produced the answer, and a line for what was not checked. |
| 4 | Unit 5 | Full verification record: checklist, assumptions, who checked, what tool was used and where, traceable to files. |

### Rule 3. Diane runs in two modes, and the schedule decides which

Behind schedule, she believes the tool: it answered in ten seconds, send it. When the client is watching or something already went wrong, she is a skeptic: I am not putting my name on something a robot wrote. Some weeks the student defends using the tool, some weeks defends refusing it. Students eventually spot the pattern, which is its own lesson about how organizations decide.

| Meetings | Diane's mode | Why |
| --- | --- | --- |
| M01-M04 | Skeptic, low bar | New hire. She asks the question but accepts one sentence. |
| M05-M06 | Skeptic, sharper | The 3 a.m. alarm went out under the firm's name. |
| M07-M10 | Believer | The county moved the interim report up. Schedule is slipping. |
| M11-M12 | Skeptic | The dashboard and charts are going to the county. |
| M13 | Believer | Wes is late and the pipeline has to run tonight. |
| M14 | Unreachable | She is on a site visit. The permit call is the student's alone, so her opinion cannot be mistaken for the exam's answer. |

### Rule 4. The unreliable coworker is the student's past self

The student keeps a one-page **decision log**: week, item, action chosen, hours spent, and a running list of what was accepted unverified. Units 1 and 2 plant three latent problems, and ten hours a week is not enough to chase all of them. Whatever the student skipped comes back later with their name on the file.

| Planted | What it is | Returns |
| --- | --- | --- |
| M02 / HW1 | Strain gauge G6 mis-zeroed at install. Every reading offset by a constant. | M19 (an input to the four-step workflow), M25 |
| M05 / HW3 | A block of duplicated timestamps in the overnight feed. Makes the sample look larger than it is. | M10 (interval too narrow), M25 |
| M13 lab | Feet and millimetres mixed in one column of Wes's sheet. | M21 (load cases), M25 |

Fairness rules for callbacks:

- A callback costs project hours and requires a written correction. It never costs grade points for the original week.
- A student who caught all three still gets a callback: Wes edited their clean file after the handoff.
- Exam 1 starts everyone from the same clean exam file. Earlier choices do not carry in.

### The debrief rule

Every unit ends with 15 minutes with the mask off. The class compares what they chose to verify and why. The instructor restates that Diane is a character and her opinion is nobody's grade. Without the debrief, a deliberately frustrating experience is just stress.

## The Otter Bend project file

One synthetic but physically plausible project file feeds every lab, homework and exam in Units 1 and 2. It is the first thing to build, because every meeting below reads from it. None of it exists yet.

| File | Contents | First used |
| --- | --- | --- |
| `gauges_install.csv` | Eight strain gauges, repeated no-load readings from install day | M02 |
| `cores_2027.csv` | About 24 deck core compressive strengths, with drill location | M04, M09 |
| `feed.csv` | Strain, temperature and vibration every 10 minutes from Feb 1, growing weekly | M05 onward |
| `traffic_counts.csv` | Hourly vehicle counts by class | M06, M12 |
| `loadtest_2019_2027.csv` | Test-truck strain at the same 8 locations, both years | M10 |
| `coupons.csv` | Yield strength from 6 steel coupons cut from a replaced member | M10 |
| `weather_station.csv` | County airport hourly weather | M08, M13 |
| `wes_handoff.xlsx` | Two of four promised sheets | M13 |
| FOREMAN outputs | About 12 scripted AI outputs for Units 1 and 2, each wrong in one designed way | every meeting |

**What is planted, and what each plant teaches.**

| Planted in the data | Where | Concept it teaches |
| --- | --- | --- |
| Gauge G6 offset by a constant | `gauges_install.csv` | Systematic error and accuracy (22) |
| Readings reported past the gauge's resolution | `gauges_install.csv` | Instrument resolution (24) |
| Core strengths with a wide spread around an acceptable mean | `cores_2027.csv` | Coefficient of variation (35), uncertainty from spread (37) |
| All cores drilled from the shoulder, where access was easy | `cores_2027.csv` | Representative sample (52), random sampling (65) |
| Peak strains right-skewed, because a few heavy trucks dominate | `feed.csv` | Skewed distribution (47), outliers (48) |
| One block of duplicated timestamps | `feed.csv` | Data cleaning (84), and an interval that comes out too narrow (69) |
| Strain climbing from February to May with air temperature | `feed.csv` | Spurious correlation (61), correlation versus causation (60) |
| A small real increase in test-truck strain since 2019 | `loadtest_2019_2027.csv` | Confidence interval (69), confidence level (70), significance (71) |
| Feet and millimetres in one column, two sheets missing | `wes_handoff.xlsx` | Unit and format mismatch (83), missing and bad data (85) |

The real deterioration signal is sized on purpose: the 95% interval on the mean change just excludes zero, and the 99% interval includes it. The honest answer is "probably a small real change", and students have to say how sure.

Working values an engineer needs to check before the file is generated: live-load strain in the range of tens to a few hundred microstrain, steel thermal strain near 12 microstrain per degree C, core strengths of 4,000 to 6,000 psi with a coefficient of variation of 10 to 15 percent. These are my starting assumptions, not verified design values.

## Unit 1 detail: Hired (M01 to M06)

Unit 1 teaches how AI produces answers and how to describe a set of measurements, in 37 concepts over six meetings. By M06 the student has met all three characters, handled four project files, and caught FOREMAN being wrong three different ways.

**Every meeting runs the same 75 minutes:** 10 minutes on what arrived in the inbox, 25 minutes of teaching, 30 minutes of lab on the project file, 10 minutes to write the note and close.

**FOREMAN is scripted.** Its outputs are documents written in advance, so every student sees the same designed error and it can be graded. Students also use a real AI assistant live in labs. Which one depends on what St. Thomas licenses for students, which is an open question.

### M01, Tue Feb 2. First day

- **Concepts (6):** artificial intelligence, rule-based systems, machine learning, training data, learned patterns, rules versus learned patterns.
- **Syllabus example carried:** rule-based load rating check versus a learned model that predicts deck deterioration from inspection photos. Used as written.
- **In the inbox:** FOREMAN's onboarding demo rates deck condition from photos in seconds. Diane's orientation memo says a load rating is a formula, and she signs nothing she cannot trace.
- **Students get:** Diane's one-page load rating sheet, with a simplified rating factor. Six inspection photos with FOREMAN's condition ratings.
- **In class:** work the rating formula by hand for one girder. Then sort eight firm tasks into rules, learned patterns, or either, and say what you would need to see to trust each.
- **FOREMAN's designed error:** none. It is right today, and cannot say why. Diane's formula can say why, and cannot read a photo. That is the argument of the course.
- **Hand in:** note version 1, one sentence.
- **Diane:** skeptic, low bar.

### M02, Thu Feb 4. Measure something with your own hands

- **Concepts (6):** measurement and why it matters, repeated measurements, range of readings, systematic error and accuracy, uncertainty propagation, instrument resolution.
- **Syllabus example carried:** repeated measurements of a machined part dimension. Used as written, hands on, with calipers.
- **In the inbox:** Diane: nobody here touches sensor data until they have measured a part and disagreed with themselves.
- **Students get:** a machined pin standing in for a lift sheave pin, calipers, and `gauges_install.csv`.
- **In class:** each student measures the pin five times. Pool the class readings, find the range, then propagate the uncertainty into a cross-section area. Then open the gauge file and look for the gauge that disagrees with the other seven by a constant.
- **FOREMAN's designed error:** averages all eight gauges into one no-load value, which hides G6's offset, and reports it to six decimal places from a gauge that resolves one microstrain.
- **Hand in:** HW1, the no-load reading for each gauge with its uncertainty. Ten project hours. Checking every gauge against the install sheet costs more than the budget allows alongside the rest.
- **Diane:** skeptic, low bar.

### M03, Tue Feb 9. The section that does not exist

- **Concepts (7):** large language models and tokens, probability basics, next-token prediction, sampling and temperature, prompts, hallucination, checking output against source.
- **Syllabus example carried:** have an LLM summarize a section of a design standard, then check it against the actual text. Used as written.
- **In the inbox:** FOREMAN's summary of the inspection requirements for movable bridge machinery, with section numbers. One section it cites does not exist. Nothing flags it.
- **Students get:** FOREMAN's summary and the real excerpt of the standard.
- **In class:** 15 minutes on probability as weighted dice. Students run one prompt five times in a live assistant and tally how the answers differ. Then check FOREMAN's summary line by line against the source.
- **FOREMAN's designed error:** one fabricated section number, and one real section paraphrased with a "shall" turned into a "should".
- **Hand in:** note version 1. HW2 assigned.
- **Diane:** skeptic. She has never heard the word hallucination and does not need it: "So it made it up."

### M04, Thu Feb 11. One number

- **Concepts (6):** data sets and variables, mean, variance and standard deviation, coefficient of variation, sample versus population, uncertainty from spread.
- **Syllabus example carried:** concrete cylinder compressive strength data. Here they are cores drilled from the Otter Bend deck. Gear tooth dimensions from the lift gearbox are the mechanical alternative.
- **In the inbox:** the lab results are back. Diane: give me one number for the deck.
- **Students get:** `cores_2027.csv`.
- **In class:** compute mean, standard deviation and coefficient of variation in a spreadsheet. Count how many cores fall below the specified strength. Discuss what 24 cores can say about a whole deck.
- **FOREMAN's designed error:** reports the mean, notes it exceeds the specified strength, and concludes the deck concrete is adequate. It never mentions that several individual cores fall below.
- **Hand in:** HW2, a three-sentence answer to Diane that gives her the one number and the reason one number is not enough.
- **Diane:** skeptic, low bar. She is wrong to want one number and right that a client needs a short answer.

### M05, Tue Feb 16. The 3 a.m. alarm

- **Concepts (6):** AI agent, tool use, multi-step planning, agent action loop, sensor data stream, threshold check.
- **Syllabus example carried:** an agent pulls readings from a structural health monitoring feed, checks a threshold and drafts an inspection flag. Used as written.
- **In the inbox:** FOREMAN ran overnight against the live feed. At 3:07 a.m. it drafted a flag to the county: threshold exceeded, recommend immediate closure.
- **Students get:** FOREMAN's step-by-step run log and the first two weeks of `feed.csv`.
- **In class:** mark every line of the run log as plan, tool call, observation or decision. Find the threshold check and notice it is a rule, in the M01 sense, sitting inside a learned system.
- **FOREMAN's designed error:** it escalated on a single reading, with no repeat check and no look at the neighbouring gauges, and wrote "recommend closure" when the data supported "look at this".
- **Hand in:** note version 1. HW3 assigned: the feed file, which contains the block of duplicated timestamps.
- **Diane:** skeptic, sharper. The draft nearly went out under the firm's name.

### M06, Thu Feb 18. Real, or an outlier?

- **Concepts (6):** distribution, histogram, normal distribution, skewed distribution, outliers, auditing an agent's analysis.
- **Syllabus example carried:** audit an agent's summary of traffic volume counts or fatigue data for a distribution it described incorrectly. Used as written, with traffic counts.
- **In the inbox:** after Diane's reaction, FOREMAN reverses itself. Its new analysis says peak strain is normally distributed, the 3 a.m. reading is a five-sigma event, and it should be discarded as a sensor fault.
- **Students get:** FOREMAN's analysis, `feed.csv`, `traffic_counts.csv`.
- **In class:** build the histogram of daily peak strain. It is right-skewed, because a few heavy trucks dominate. The 3 a.m. reading lines up with a heavy vehicle in the traffic file. It was a real truck.
- **FOREMAN's designed error:** it assumed a normal distribution for skewed data, and so threw away a real event. On Tuesday it overreacted, on Thursday it overcorrected. An outlier is not automatically an error.
- **Closing beat:** the student hands the gauge spreadsheet to Wes and moves on. That file comes back in April and May. The 3 a.m. truck comes back as Exam 1.
- **Hand in:** HW3, an audit of FOREMAN's analysis.
- **Last 15 minutes:** Unit 1 debrief, mask off. What did you choose to verify, and what did you let go?

## Unit 2 detail: Doubt (M07 to M14)

Unit 2 teaches students to judge a claim, whether it comes from an AI or from data, in 37 concepts over seven teaching meetings and Exam 1. The county moves its interim report up, so Diane starts believing the tool exactly when it starts being wrong in ways that matter. Note version 2 applies from M07: the claim, the check, what the check showed.

### M07, Tue Feb 23. It does not know what it does not know

- **Concepts (6):** AI bias, training data bias, representative sample, distribution shift, out-of-domain use, training coverage gap.
- **Syllabus example carried:** a damage detection model trained mostly on one bridge type or climate region. Used as written.
- **In the inbox:** FOREMAN's damage report on the towers and machinery room: no significant defects, high confidence. Attached is the vendor's one-page training summary.
- **Students get:** the report, the training summary, 12 photos.
- **In class:** read the training summary. It is almost all highway girder bridges from warm states, and no movable bridges. List what Otter Bend has that the training data never saw: lift machinery, freeze and thaw, road salt.
- **FOREMAN's designed error:** it rates machinery room photos with the same confidence as girder photos. It was never trained on anything like them and gives no sign of that.
- **Side beat:** Wes submits a polished memo accepting the machinery rating. Diane passes it without reading closely. It comes back at M13. This is the course's one deliberate burn, and it happens to Wes, not to a student.
- **Hand in:** note version 2 only. HW4 remains parked until M08.
- **Diane:** believer. "It looked at 400 photos in a minute. Give me a reason not to use it." The student has to defend refusing the tool.

### M08, Thu Feb 25. It is spring

- **Concepts (6):** scatter plot, correlation coefficient, linear regression, R-squared, correlation versus causation, spurious correlation.
- **Syllabus example carried:** a real regression set against a spurious one tied to a seasonal trend. The real one here is strain against temperature. Concrete strength against mix variables is the alternative data set. Lift motor noise against season is the mechanical parallel, close to the syllabus wording.
- **In the inbox:** FOREMAN: midspan strain has risen steadily since February 1, R-squared 0.87 against date, indicating progressive structural deterioration.
- **Students get:** `feed.csv`, `weather_station.csv`.
- **In class:** plot strain against date, then strain against air temperature. Fit both lines in a spreadsheet. Temperature drives both the calendar trend and the strain. Steel expands when it warms. Students name the mechanism, not just the pattern.
- **FOREMAN's designed error:** it read a seasonal temperature effect as damage, and offered a high R-squared as proof of cause.
- **Hand in:** note version 2. HW4 is assigned here: a temperature-corrected strain trend and a two-line reply to FOREMAN's claim.
- **Diane:** believer. "0.87 sounds high. Put it in the report."

### M09, Tue Mar 2. To the single cycle

- **Concepts (5):** AI overconfidence, false precision, statistical basis for a claim, random sampling, sampling variability.
- **Syllabus example carried:** a model reports a precise remaining fatigue life in cycles with no statistical basis for the precision. Used as written, on a sheave shaft in the lift machinery.
- **In the inbox:** FOREMAN: remaining fatigue life 41,872,316 cycles. Diane: just give me one number. Both are wrong, differently.
- **Students get:** FOREMAN's estimate, a small fatigue test data set with its scatter, and a spreadsheet of 200 simulated core strengths.
- **In class:** ask what data could support eight significant figures. Then each student draws a random sample of 8 from the 200 cores and the class compares sample means. That spread is sampling variability, seen by hand. Then go back to the real cores: every one was drilled from the shoulder, where access was easy.
- **FOREMAN's designed error:** precision far beyond what scattered fatigue data can support, stated with no range.
- **Hand in:** note version 2.
- **Diane:** believer.

### M10, Thu Mar 4. Did it get worse?

- **Concepts (5):** standard error, the t multiplier, confidence interval, confidence level, significance and p-values.
- **Syllabus example carried:** a confidence interval on yield strength from a small sample of test coupons. Used as written as the warm-up, with 6 coupons.
- **In the inbox:** Diane: did the deck get worse since 2019, yes or no? FOREMAN: strain under the test truck is up 6 percent, deterioration confirmed, p = 0.04, so there is a 96 percent chance the deck has deteriorated.
- **Students get:** `coupons.csv`, `loadtest_2019_2027.csv`.
- **In class:** build the coupon interval together, with the t value read from a table. Then take the eight same-location differences between 2019 and 2027 and build the interval on the mean change. At 95 percent it just excludes zero. At 99 percent it does not.
- **FOREMAN's designed error:** it reads a p-value as the probability the claim is true, and treats "significant" as "confirmed" and "large".
- **Hand in:** HW5, an interval on mean daily peak strain from the feed. First callback: anyone who did not remove the duplicated timestamps in HW3 gets an interval that is too narrow.
- **Diane:** believer. She wants yes or no. The honest answer is "probably, by a small amount, and here is how sure".

### M11, Tue Mar 9. Permission to publish

- **Concepts (5):** dashboard and metrics, time series data, agent-built report, agent autonomy, human review checkpoint.
- **Syllabus example carried:** an agent assembles a dashboard tracking bridge vibration data. Used as written.
- **In the inbox:** FOREMAN has built a county-facing dashboard overnight and asks for approval to publish.
- **Students get:** the five-tile dashboard and a review form.
- **In class:** the student is the human review checkpoint, literally. For each tile: approve, fix, or pull, with a reason.
- **FOREMAN's designed error:** one tile shows a "structural health score" of 87 out of 100 with no definition. Another shows the raw strain trend from M08 with a red "worsening" arrow.
- **Hand in:** the completed review form, with note version 2.
- **Diane:** skeptic again. The county will see this.

### M12, Thu Mar 11. The county reads charts, not appendices

- **Concepts (4):** chart type selection, axis scales and baselines, misleading charts, critiquing AI-generated charts.
- **Syllabus example carried:** critique an AI-generated chart of traffic flow for misleading axes. Used as written. The vibration spectrum option is dropped because frequency is not taught.
- **In the inbox:** FOREMAN's chart pack for the interim report.
- **In class:** find the truncated axis that makes ordinary variation look like failure, and the pie chart used for hourly traffic. Redraw both. Last 25 minutes: Exam 1 review.
- **FOREMAN's designed error:** a truncated y-axis, and a chart type that does not match the data.
- **Hand in:** HW6, the two redrawn charts. The async code-reading primer is assigned, due before M15.
- **Diane:** skeptic.

### M13, Tue Mar 16. Wes's handoff

- **Concepts (6):** data pipeline, data ingestion, unit and format mismatch, data cleaning, missing and bad data, errors through a pipeline.
- **Syllabus example carried:** a pipeline pulls weather station and sensor data, cleans it, and feeds a simple model. Used as written. The simple model is the M08 temperature correction.
- **In the inbox:** Wes's handoff, two days late: two of four sheets, feet and millimetres in one column, no assumptions written down. Also, the mechanical inspector found bearing wear that FOREMAN rated as fine at M07. Wes's memo is back on Diane's desk.
- **Students get:** `wes_handoff.xlsx` and FOREMAN's pipeline log.
- **In class:** trace one value through the pipeline from ingestion to output. Find where rows with missing temperatures were dropped without a word, and where millimetres were read as feet. Show how the error grows at each step.
- **FOREMAN's designed error:** silent ingestion. It never stops to ask.
- **Hand in:** note version 2. There is not enough lab time to check all four columns. Students choose, and log what they left unchecked.
- **Diane:** believer. The pipeline has to run tonight.
- **Last 15 minutes:** Unit 2 debrief, mask off.

### M14, Thu Mar 18. Exam 1: the overweight permit

- **Concepts:** none new. It draws on Units 1 and 2.
- **The call:** the county needs a decision today on an overweight load permit for a night crossing. FOREMAN says the crossing is fine. Diane is on a site visit and cannot be reached.
- **Students get:** one clean exam file, the same for everyone, built from files they have already worked with. FOREMAN's recommendation with one chart.
- **The work, in 75 minutes:** check one of FOREMAN's claims against its source. Describe the relevant strain data with a spread, not just a mean. Scale the test-truck strain to the permit load by ratio, with an interval. Name one flaw in FOREMAN's chart. Answer yes, yes with conditions, or no, and write note version 2.
- **Grading:** the reasoning and the record. "Yes with conditions" and "no" are both defensible. The grade does not depend on which one the student picks.
- **Syllabus match:** an applied practical built around a dataset introduced earlier in the course. 20 percent of the grade, unchanged.

## Where the department's engineering suggestions plug in

Each meeting has one engineering example, and any of them can be swapped without touching the concepts or the story, as long as the replacement produces data with the same shape. These are the slots where department input changes the most.

| Slot | What is there now | What a replacement has to supply |
| --- | --- | --- |
| The structure itself | A 1962 vertical lift bridge | One asset with a civil side, a mechanical side, and sensors. If the department prefers a different structure or a plant, the beats survive; the project file is rebuilt. |
| M01 | Simplified load rating factor | A short rule-based check a first-year can do by hand |
| M02 | Caliper measurements of a machined pin | Any part or beam deflection students can measure five times each in class |
| M03 | Inspection requirements for movable bridge machinery | A standard section students can legally read in full. Which standards does the library license? |
| M04 | Deck core strengths. Gear tooth dimensions as the mechanical option | About 20 to 30 measurements of one quantity against a specified value |
| M06 | Peak strain and traffic counts | A right-skewed data set where the extreme values are real |
| M08 | Strain against temperature. Concrete mix as the alternative | Two variables with a physical cause, and one trend with a hidden seasonal driver |
| M09 | Fatigue life of a sheave shaft | A quantity with wide natural scatter that tools tend to report too precisely |
| M10 | Steel coupons and a paired load test | A small sample, 6 to 10 values, and a before-and-after comparison |
| M14 Exam 1 | Overweight load permit | A same-day yes-or-no decision that rests on data students already know |
| Units 3 to 5 | Beam deflection, truss, wall heat transfer, footing, heat exchanger, as the syllabus lists | Known-answer problems with a closed-form solution to check code against. These units are mapped but not detailed, so they are the cheapest place to add department examples. |

Mechanical balance is the thing to watch. Units 1 and 2 as drafted lean civil: seven of the thirteen teaching meetings use structural data (M01, M04, M05, M06, M08, M10, M13), three use machinery (M02, M07, M09), three are neutral (M03, M11, M12). If the department wants it closer to even, M04, M08 and M10 each have a mechanical alternative ready to promote.

## Grading

The syllabus weights do not change: homework 25 percent, Exam 1 20 percent, Exam 2 20 percent, project 25 percent, reflection 5 percent, participation 5 percent. The simulation changes what the work looks like, not what it is worth.

- **Grade the reasoning and the record, never the outcome.** A student who made a defensible call on the information they had, and had it go badly, did the job correctly. That is the standard of care the course teaches in Unit 5, so the rubric and the content agree.
- **Diane is not the grader.** If her approval reads as the right answer, students optimize for pleasing her and the simulation collapses into a quiz with a job title. Sometimes a strong note gets a poor reception because she is skimming. The grade comes from the instructor's rubric on the note.
- **Hours are not points.** The hour budget shapes what students choose to check. Running out of hours never lowers a grade.
- **One deliberate burn, and it lands on Wes.** A confident, well-written, wrong memo succeeds with Diane at M07 and comes back at M13. Students see that good writing does not make a number right, without being set up to fail themselves.
- **Anyone can ignore the story.** A student who never learns who Wes is still does identical engineering and statistics work and is graded the same way.

## Risks, open decisions, and what needs an engineer

The biggest risk is that this is the first run of a new course, and a story layer makes it harder to tell whether a bad week was the content, the teaching, or the simulation. The answer is to keep every mechanic removable and to pilot one week before building fourteen.

### What would break it

| Priority | Risk | Guard |
| --- | --- | --- |
| P0 | First-run confound: cannot tell what failed | Every mechanic can be dropped mid-semester without changing a lab. Pilot M10 with the hour budget live before building the rest. |
| P0 | Unreviewed engineering | Nothing here has been checked by an engineer. The bridge, the working values and the exam scenario all need review before data is generated. |
| P1 | Grading on outcomes | Rubric scores the note and the record only. Exam 1 accepts more than one answer. |
| P1 | Diane as caricature | Her critiques are always substantive. Her messages get a read from someone outside the project before use. |
| P1 | Story overhead | No graded question depends on remembering the fiction. |
| P1 | No debrief | 15 minutes, mask off, at the end of every unit. M06 and M13 already carry 6 concepts each, so those are the tightest sessions in the plan. |
| P2 | Hour budget adds bookkeeping | One page per student. If it costs more than five minutes a week, it goes. |

### Decisions that are open

- **Where this plan departs from the written syllabus.** Spring 2027 has 28 meetings, not 30. Exam 2 moves from week 13 to finals week, which needs registrar approval. The two week-12 sessions merge into one. The vibration spectrum example is dropped. Fourteen concepts were cut or made optional to fit. The department should see these as changes, not discover them.
- **Which AI assistant students use live.** Depends on what St. Thomas licenses for students.
- **Which standard students read at M03.** Depends on library access.
- **Programming language for Unit 3: decided.** Python, written by vibe coding. Students describe what they need, the AI generates the code, and students read, run and test it. They are not taught to write Python from a blank file, which is why the async primer teaches code reading only.
- **Exam 1 in 75 minutes.** Five tasks is tight. It needs a timed dry run with someone who has not seen the file.
- **ENGR 100 content** has still not been checked against the list of entry knowledge.

### What needs an engineer's eyes

- [ ] Is a 1962 vertical lift bridge with strain, temperature and vibration sensors a believable assessment project?
- [ ] The simplified load rating formula at M01.
- [ ] Working values for strain, thermal strain and core strength in the project file.
- [ ] Scaling test-truck strain to a permit load by ratio on Exam 1: acceptable simplification, or misleading?
- [ ] Fatigue scatter at M09: is the sheave shaft a fair example?
- [ ] Definitions of accountability, the PE stamp and responsible charge (concepts 144, 153, 154), which vary by state.
- [ ] The prerequisite edges in the knowledge graph.

## Build list, in order

The first class is Tuesday, February 2, 2027. Nothing below is built. What exists today is the 163-concept graph and schedule, the definitions, four self-check guides and the vocabulary game.

| Order | Item | Size for Units 1 and 2 | Depends on |
| --- | --- | --- | --- |
| 1 | Department feedback folded in | The structure and the example slots locked | Monday's meeting |
| 2 | Engineer review of working values and the exam scenario | One sitting | 1 |
| 3 | Project file generator | 8 data files, errors planted by script so they can be regenerated | 2 |
| 4 | One-week pilot of M10 with the hour budget live | 3 to 5 volunteer testers | 3 |
| 5 | FOREMAN's scripted outputs | About 12 documents | 3 |
| 6 | Diane's messages and Wes's handoff | About 15 short notes, 1 workbook | 5 |
| 7 | Note template and rubric, versions 1 and 2. Decision log page | 3 one-page documents | 4 |
| 8 | HW1 to HW6 and Exam 1, with a timed dry run | 6 assignments, 1 exam | 5, 7 |
| 9 | Units 3 to 5 detailed to the same level as this document | 14 meetings | 4 |

Existing materials keep a job in the story: the vocabulary game is the firm's onboarding certification, the probability guide is a week-one training module, the code-reading primer is the async module due before M15, the reference cards are what Diane hands over at M18, and the optional concepts are lunch-and-learns.
