# SEIS 201 interactive guides (draft v0.1)

Four self-contained HTML files. No login, no network, no data collected. Open in any browser; works offline. Students can also get them by email or LMS file upload.

| File | Covers | Feeds | Questions | Time |
|---|---|---|---|---|
| probability-and-sampling.html | probability, sample vs population, random sampling, sampling variability, standard error, t multiplier | M03, M04, M09, M10 | 18 | ~35 min |
| code-reading-primer.html | variables/types, functions/imports, conditionals/loops, error messages (Python assumed) | async module, before M15 | 18 | ~40 min |
| engineering-reference-cards.html | statics, stress/strain, beam bending, thermal resistance, factor of safety | lab reference cards | 19 | ~35 min |
| optional-concepts.html | calibration, multiple regression, log scale, sensitivity, standard of care, code of ethics, corroborating sources, context window, stale data, tradeoff uncertainty | cut concepts | 20 | ~30 min |

## Completion code
Format: `SEIS201-<GUIDE>-<first-try>of<total>-<checksum>`, e.g. `SEIS201-PROB-09of18-FF4D`.
Students paste it into an LMS assignment. The checksum only catches typos and casual made-up codes. It is honor-system: anyone can share a code, and a student can get every answer right on retries. Reloading resets progress.

To check a code:
```python
def check(code):
    _, g, score, cs = code.split('-')
    first, total = map(int, score.split('of'))
    x = 7
    for c in f"{g}|{first}|{total}": x = (x*31 + ord(c)) % 65521
    return format(x, '04X') == cs
```

## Known limits
- Not reviewed by an engineering or statistics instructor. Formulas and answer keys were script-checked, not expert-checked.
- Code primer assumes Python and pandas; confirm against the course.
- Reference cards are simplified; the lab's own cards win on any conflict.
- "Calibration" is covered in both senses (instrument, confidence); confirm which the syllabus means.
