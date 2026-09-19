# ACMEJOB.Ai — semester simulation outline

Draft v0.1 for SEIS 201, Spring 2027. Every lab, guide, exam and project in the course becomes an artifact from one job at one fictional firm. Nothing here is final and none of it has been reviewed by an engineering instructor.

---

## 1. The premise

**ACMEJOB.Ai** is a mid-size Minnesota civil and mechanical engineering firm that rebranded two years ago as an AI-augmented practice. It won the Kinnick County contract partly on that promise: faster assessments, lower fees, same rigor.

The firm's own principal engineer does not believe a word of it.

That contradiction is the engine. Students are hired into the gap between what the firm sold and what the engineering actually requires.

**The project.** The Otter Bend Lift Bridge over the Kinnick River, Otter Bend, Minnesota — built 1962, vertical lift span, now carrying loads it was not designed for. The county has installed strain, temperature and vibration sensors and wants an answer by May: rehabilitate or replace. The structure and the town are invented. Failure modes are drawn from the public engineering literature. **No real collapse, and no real casualty event, is referenced or dramatized.**

A lift bridge is chosen deliberately: the structure serves the CE concepts, the lift machinery (motors, bearings, thermal expansion, fatigue) serves the ME concepts, and the sensor array generates every dataset the course needs.

**The cast — three, and no more.** A fourth character is lore overhead.

| Who | What they are | What they generate |
|---|---|---|
| **Diane Halvorsen, PE** | Principal engineer, 27 years, came in with the merger. Knows every inspector in the county, every contractor's habits, and no statistics at all. Does not trust AI. | The recurring question: *how do you know that's right?* |
| **Wes Tanaka, EIT** | Second-year engineer, split across three projects, genuinely trying. | Late, partial, undocumented handoffs |
| **FOREMAN** | The firm's AI platform. Fast, fluent, confident. Wrong in designed ways about one time in five. | Every error the course teaches students to catch |

FOREMAN is deliberately ungendered — defaulting an AI assistant to a woman's voice is its own tired pattern and this course has no reason to repeat it.

Diane is not a fool and she is not an obstacle. She is right about a third of the time, and wrong in ways that are reasonable. Her resistance to AI deserves to be written with a reason behind it: she has spent 27 years as one of the few women in the room having her work doubted, and not once in those years has she been able to answer a doubt with *the computer said so*. "How do you know?" is not a demand she invented. It is one she survived, and she is asking it of the student the way it was asked of her.

There are two ways to write her badly. As a caricature, which teaches contempt for management. Or as *difficult*, which is the tired trope wearing a hard hat. The guard against both: her critiques are always substantive and grounded in something she actually knows, and she is demanding because the stakes are real — never because of her mood.

---

## 2. The four rules that make it a simulation

**Hours, not a clock.** Each week carries a budget of working hours. Verifying FOREMAN's number costs two; hand-checking it costs four; calling the vendor costs one and a day of waiting. There is always more worth doing than budget to do it. No countdown timers anywhere — a visible clock punishes slow processors and teaches speed instead of judgment. Choosing what to verify *is* the skill.

**The note.** Every submission carries a short *how I know this is right* statement. Diane reads it, or doesn't. A weak note gets bounced back and the bounce costs hours. The required form escalates without announcement: one sentence in February, a structured verification record by May. That is the course's rising rigor, experienced as earned responsibility.

**Diane runs in two modes, and the schedule decides which.** Behind schedule, she is a believer — *the tool answered in ten seconds, send it.* Client watching or something already went wrong, she is a skeptic — *I'm not putting my name on something a robot wrote.* Students eventually spot the pattern, which is its own lesson about how organizations decide. It also means there is no single script: some weeks you defend using the tool, some weeks you defend refusing it.

**The unreliable coworker is the student's past self.** Work handed off in February comes back in April with an error in it, traceable to a week when the student ran out of hours and accepted a number. Wes supplies the ordinary friction; the student's own file supplies the sting. This costs nothing in fairness and everything in memory.

---

## 3. The semester

Meeting numbers and concept assignments follow `seis201-learning-graph-v2/concept-schedule.csv`. Beats below are the story layer; the concepts taught are unchanged.

### Unit 1 — Hired (M01–M06, Feb 2–18)

The student's first three weeks on the job. Diane's bar is low: one sentence of justification is accepted, and it will not be for long.

- **M01** — First day. The platform demo and Diane's orientation contradict each other within an hour. *Rules versus learned patterns* is the argument they're having.
- **M02** — First site data. Eight strain gauges, and one of them was mis-zeroed at install. Nothing in the file says so.
- **M03** — FOREMAN cites a spec section that does not exist. First hallucination, and it is not flagged as one — the student has to go look.
- **M04** — Diane wants the gauge data "in one number." The spread is the interesting part.
- **M05** — FOREMAN runs a multi-step job against the live sensor stream overnight. A threshold alarm fires at 3 a.m.
- **M06** — Was the alarm real or an outlier? Audit the agent's reasoning. **Closing beat: the student hands their gauge spreadsheet to Wes and moves on.** *(This file returns at M25.)*

### Unit 2 — Doubt (M07–M14, Feb 23–Mar 18)

The tool starts being wrong in ways that matter, and the schedule starts slipping, so Diane flips to believer mode exactly when the student most needs her skeptical.

- **M07** — FOREMAN was trained on highway girder bridges. This is a lift bridge with moving machinery. It does not know what it does not know.
- **M08** — It reports a "strong relationship" between air temperature and strain as a structural finding.
- **M09** — Diane: *one number.* FOREMAN: fourteen decimal places. Both are wrong, differently.
- **M10** — Did the deck actually deteriorate since the 2019 inspection, or is the difference noise? The first claim the student has to defend statistically.
- **M11** — FOREMAN drafts a county-facing dashboard and asks to publish it. Human review checkpoint, in the literal sense.
- **M12** — The chart in that report has a truncated y-axis that makes normal decay look catastrophic. The county reads charts, not appendices.
- **M13** — **Wes's handoff arrives.** Two days late, two of four sheets, feet and millimetres mixed in one column, no assumptions documented.
- **M14 — Exam 1, in world.** The county calls: an overweight load permit, decision needed today. FOREMAN says the crossing is fine. Seventy-five minutes, the real file, and a yes or no with reasons.

### Unit 3 — Build (M15–M20, Mar 30–Apr 15)

*Async code primer assigned M12, due before M15 — in world, "you cannot check what you cannot read."*

- **M15** — The student's first FOREMAN-written script. It runs clean and the answer is wrong.
- **M16** — Writing a specification FOREMAN can't misread. Describe, generate, test.
- **M17** — FOREMAN writes tests for its own code. They pass. It is still wrong. This is the single most important hour in the unit.
- **M18** — **Diane opens a desk drawer and hands over the hand-calc cards.** Known-answer, hand calculation, units, order of magnitude. The student now has a weapon and Diane's question finally has a real answer.
- **M19** — A four-step FOREMAN workflow produces a number nobody can explain. Trace it. *(First small callback: one input came from the student's own February file.)*
- **M20** — Root cause versus symptom, with FOREMAN helping debug the thing FOREMAN broke.

### Unit 4 — Own (M21–M23, Apr 20–27)

The student owns the rehab-versus-replace analysis. The team project is this deliverable.

- **M21** — Load cases and a parameter sweep. Over a long session FOREMAN quietly drifts off the stated requirements.
- **M22** — Build the calculation tool the firm will actually reuse. Input validation exists because Wes will use it next.
- **M23** — FOREMAN's literature summary supports the rehab case with a fabricated citation. The tradeoff is real, the evidence is not, and the recommendation is due.

### Unit 5 — Sign (M24–M28 + finals, Apr 29–May 21)

- **M24** — Risk, consequence, and who answers for a decision a tool recommended.
- **M25** — Independent verification of the whole package. **The February spreadsheet surfaces with the error in it.** The student's own name is on the file.
- **M26** — Diane will not stamp what she cannot defend. She asks, flatly, whether AI was used — and what the student says costs them something now and protects them later.
- **M27** — Where the tool simply cannot go: conditions beyond training, the tacit knowledge Diane has and cannot write down, and when not to use AI at all.
- **M28 — County board briefing.** The team presentation, delivered to non-engineers who will act on it.
- **Finals week — Exam 2.** Post-decision review: here is what the firm recommended and here is what the sensors did afterward. Defend the call you made with the information you had. Pairs with *Reflecting on AI Use*.

---

## 4. Where the existing course materials land

Nothing built so far is discarded. Each piece gets an in-world job.

| Asset | In world |
|---|---|
| `vocab-lab.html` | ACMEJOB.Ai onboarding certification — Diane makes every new hire pass it |
| `probability-and-sampling.html` | Training module assigned in week one; feeds M03, M04, M09, M10 |
| `code-reading-primer.html` | Assigned M12, due before M15: you cannot check what you cannot read |
| `engineering-reference-cards.html` | Diane's hand-calc cards, handed over at M18 |
| `optional-concepts.html` | Firm lunch-and-learns, optional |
| Team project | The rehab-versus-replace recommendation |
| Exam 1 (M14) | The overweight permit call |
| Exam 2 (finals) | The post-decision review |
| M28 presentations | The county board briefing |

---

## 5. Grading

**Grade the reasoning and the record. Never the outcome.** A student who made a defensible call on the information they had, and had it go badly, has done the job correctly. This is not a concession to fairness — it is the standard of care, which the course teaches in Unit 5. The rubric and the content agree.

**Diane is not the grader.** If her approval reads as the right answer, students optimize for pleasing her and the simulation collapses into a multiple-choice test with a job title attached. Decouple it visibly: sometimes a strong note gets a poor reception because she is skimming, and sometimes a thin one sails through because she did not read it. The grade comes from the instructor's rubric on the note. Diane's mood is weather.

**One deliberate burn.** At least once, a confident and well-written but wrong justification should succeed with Diane and come back three weeks later. Otherwise students learn that good writing makes a number right.

**Every arc ends with the mask off.** Fifteen minutes where the class compares what they chose and why, and where it is restated that Diane is a character and her opinion is not anyone's grade. Without the debrief this is not a simulation, it is just stress.

---

## 6. What has to get built

**Exists already:** the 163-concept graph and schedule, the four guides, the vocab game, the definitions.

**New, in rough order of value:**

1. **The sensor dataset.** One synthetic but physically plausible time series for the Otter Bend bridge — strain, temperature, vibration, 2019 and 2027 inspection rounds — with the errors deliberately planted: the mis-zeroed gauge, the unit mismatch in Wes's sheets, the temperature correlation, the genuine deterioration signal buried under noise. Everything downstream reads from this one file. **This is the keystone and should be built first.**
2. **FOREMAN's scripted outputs.** Roughly 25 pieces of AI output across the semester, each wrong in a specific designed way tied to a specific concept.
3. **Diane's messages.** Around 30 short notes. Tone matters more than length.
4. **The note template and rubric,** in its four escalating versions.
5. **The hour budget and decision log** — a single page that holds state across the semester, so week 25 can point at week 6.

**Test one week before building fourteen.** Mid-Unit 2 is where the material is richest: M09 or M10, with the hour budget live, one bounce-back from Diane, and the disclosure question. One week tells us whether this sings.

---

## 7. What would break it

- **Grading on outcomes.** Students reverse-engineer the safe path and it becomes the vocab game again — findable by logic instead of knowledge.
- **A caricature boss.** Contempt for management is the wrong lesson and it is easy to teach by accident. The "difficult woman" version of the same mistake is easier still.
- **Lore overhead.** A student who ignores the fiction entirely must still do identical engineering work. If anyone has to remember who Wes is to answer a question, the fiction has grown too heavy.
- **No debrief.** Deliberately frustrating experiences without a mask-off conversation are hazing, not pedagogy.
- **First-run confound.** This is the first delivery of the course. If a week goes badly, an elaborate story layer makes it harder to tell whether the problem was the pedagogy, the content, or the simulation. Argues for the thinnest version that still creates stakes, and for keeping every piece removable.
