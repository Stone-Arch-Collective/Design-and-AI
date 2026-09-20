# Instructor key — HW Case B: Oak Street Lift Station

**Do not distribute with the student package.**

## Planted condition

- Bad channel: **PT-107**
- Planted systematic offset: **+4.80 psig**
- Expected standby baseline: **42.00 psig**
- Fictional requirement: WP-LS-3 §2.1, **each channel** within
  ±0.75 psig under the defined standby condition
- PT-107 sample mean: **46.810 psig**
- PT-107 sample standard deviation: **0.061 psig**

The bad channel's readings are tightly grouped, so the channel is **precise but
inaccurate**. The offset is systematic; its small reading-to-reading scatter is
random variation.

## Reproducible results

| Channel | Mean (psig) | Error from 42.00 (psig) | Per-channel result |
|---|---:|---:|---|
| PT-101 | 41.996 | -0.004 | PASS |
| PT-102 | 42.023 | +0.023 | PASS |
| PT-103 | 41.946 | -0.054 | PASS |
| PT-104 | 41.992 | -0.008 | PASS |
| PT-105 | 41.997 | -0.003 | PASS |
| PT-106 | 42.005 | +0.005 | PASS |
| PT-107 | 46.810 | +4.810 | FAIL |
| PT-108 | 42.010 | +0.010 | PASS |

The mean of all 96 observations is **42.597 psig** (FOREMAN rounds
to **42.60 psig**), or
**+0.597 psig** versus the baseline. That numeric
calculation is correct.

The seven unaffected channels average **41.996 psig**. Giving each
channel equal weight dilutes one channel's roughly +4.8 psig bias by a factor of
eight, leaving only about **+0.602 psig** in the grand average.
That falls inside ±0.75 psig even though PT-107 itself fails badly.
FOREMAN applied an array-level average to a per-channel requirement, so its PASS
method and disposition are wrong.

## Buried clue

The technician-notes section of `install_startup_note.md` says a local zero trim
showing +4.8 psi correction was used on PT-107 while its equalization valve was
shut. Students should find this only after examining the data and then returning
to the field record. It supports, but does not replace, the statistical evidence
of systematic error.

## What a good student write-up includes

1. **Requirement:** quotes or paraphrases “each channel,” the 42.00 psig defined
   standby baseline, and the ±0.75 psig limit.
2. **Evidence:** calculates per-channel means and a scatter measure or range;
   identifies PT-107 as tight but high.
3. **Diagnosis:** distinguishes its random scatter from systematic offset and
   uses “precise but inaccurate” correctly.
4. **Judgment:** rejects FOREMAN's PASS even though its arithmetic is correct;
   explains why averaging across channels answers the wrong question.
5. **Action:** holds acceptance, checks PT-107 zero/manifold/configuration
   against a traceable reference, corrects or replaces it, and repeats the
   defined standby test for every channel. Students should not simply delete the
   outlier and proceed.
6. **Decision log:** records the requirement, dataset/version, calculations,
   anomaly, field-note clue, decision owner, hold/retest action, and unresolved
   uncertainty. Diane, not FOREMAN, owns engineering acceptance.

Reasonable uncertainty discussions may mention reference-gauge uncertainty,
resolution, repeatability, stabilization, and whether the ±0.75 psig criterion
is an acceptance limit rather than a statistical confidence interval.

---

Fictional instructional case. Data generated with seed 2010107. Not verified by
a licensed engineer.
