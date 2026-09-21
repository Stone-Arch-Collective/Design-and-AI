# SEIS 201 M10 — Did it get worse?

**Status: OLI CLOUD HARD-REVIEW PASS · revised M10 SAY · folded 2026-09-21**

## Story Spine

1. Diane Halvorsen, PE asks a yes/no: did the Otter Bend deck get worse since 2019?
2. FOREMAN claims strain under the test truck is up about 6%, “deterioration confirmed,” p = 0.04, so “96% chance the deck has deteriorated.”
3. Students open `coupons.csv` and `loadtest_2019_2027.csv`. They build a coupon confidence interval with a t-table, then compute eight paired load-test differences and the 95% and 99% confidence intervals.
4. Diane Halvorsen, PE is in BELIEVER mode. She wants a clean yes or no for the county. Students must decide what the intervals actually say.
5. The 95% interval for the mean paired difference just excludes zero; the 99% interval includes zero. The change is probably small—how sure can the team be?
6. Wes Tanaka, EIT is quietly checking why FOREMAN’s “confirmed” language does not match what the coupons show.
7. Light close: eyes outside the project team will soon be on Otter Bend health. No dashboard score, tile, or publish decision is named here.

## Student Hunt

Open the coupon and 2019/2027 load-test files. Build the coupon interval from the t-table. Compute the eight paired differences. Find the 95% and 99% intervals for the mean paired difference. Does either interval include zero? What would you tell Diane Halvorsen, PE if she demanded yes or no right now? Do not invent a dashboard score.

## Instructor Reveal

Open only after the hunt. FOREMAN’s designed error is treating p = 0.04 as a 96% chance the claim is true and treating “significant” as if the change were confirmed and large. That is wrong on purpose. Teach must establish the opposite before Reveal: p is not P(claim true), and significant does not mean confirmed or large. The coupons and paired differences show a borderline, small-looking shift—not a slam-dunk “confirmed deterioration.” Wes Tanaka, EIT’s quiet check supplies later liability color; he does not co-solve the student hunt.

## SAY Beats

### Inbox · 10 minutes

- Diane Halvorsen, PE: “Otter Bend deck—worse since 2019? Yes or no. County wants an answer.”
- FOREMAN: “Mean strain under test truck +6%. Deterioration confirmed. p = 0.04 → 96% chance the deck has deteriorated.”
- Wes Tanaka, EIT, side thread: “I’m looking at the coupon pairs again. Don’t hang the whole story on that one line.”

### Teach · 25 minutes

- “A p-value is not the probability that a claim is true. FOREMAN’s ‘96% chance’ line is the misconception you must reject.”
- “Statistically significant does not mean confirmed, and it does not mean large. Those are separate claims requiring separate evidence.”
- “Standard error estimates how much a sample mean would vary from sample to sample. It is not the spread of the individual readings.”
- “For a small sample, the t multiplier reflects both the confidence level and the degrees of freedom. A higher confidence level requires a larger multiplier and a wider interval.”
- “If zero is outside the 95% interval but inside the 99% interval, the evidence is borderline, not a slam-dunk.”

### Lab · 30 minutes

- “Open `coupons.csv`. Build the interval for the coupon mean using the t-table. Show degrees of freedom and the critical t.”
- “Open `loadtest_2019_2027.csv`. For each of the eight matched locations, calculate 2027 minus 2019. The observations for this analysis are the eight paired differences.”
- “Report the 95% and 99% intervals for the mean paired difference. Mark whether each includes zero.”
- “Now answer Diane Halvorsen, PE’s yes-or-no demand without deleting the uncertainty.”

### Note · 10 minutes

- “Write Note version 2: claim, check, result. Include the mean change and an interval.”
- “HW5 is the confidence interval on mean daily peak strain from the feed.”
- “HW3 callback: if duplicate timestamps were not removed, the sample appears larger than it is and the interval comes out too narrow. Say why in one sentence on the HW5 sheet.”
- Notebook line: “p ≠ P(claim true); significant ≠ confirmed ≠ large.”

### Closing · 5 minutes

- “The 95% interval just excludes zero; the 99% interval includes it. The honest answer is probably a small real change, with the level of confidence stated.”
- “Eyes outside this project team will soon be on the Otter Bend health record. Preserve the uncertainty now. The public-facing fight belongs later.”

## Spoiler Guard

- No M11 tile score, numeric health score, publish-dashboard interface, or approve-to-publish beat.
- Diane Halvorsen, PE stays in BELIEVER mode and wants yes/no.
- Students discover the interval story.
- FOREMAN’s p-to-probability misuse is identified as false during Teach and exposed as its designed error at Reveal.
- Wes Tanaka, EIT does not co-solve on the student deck.
- No Exam 1 scenario details.

## Pack Wiring

- Hand-in: **HW5** = confidence interval on mean daily peak strain from the feed.
- **HW3 callback** = skipped duplicate-timestamp cleaning → interval too narrow.
- Assets: `coupons.csv`, `loadtest_2019_2027.csv`, and a t-table.
- Do not start M11 scaffolding from this pack.
