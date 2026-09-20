# ACMEJOB.Ai

## Oak Street Lift Station — instrument installation / startup note

**Client:** Westfield Public Works  
**Work order:** OSL-28-0916  
**Date:** 2028-09-16  
**Prepared by:** Wes Tanaka, EIT  
**Reviewed by:** Pending Diane Halvorsen, PE  
**Status:** Field draft — not PE-verified

### Purpose and standby condition

Eight pressure transducers, PT-101 through PT-108, were installed on the common
force-main / wet-well discharge header. Startup observations were recorded with
both pumps off, discharge isolation valves seated, and the instrument manifold
equalization valves open. The header was allowed to settle for ten minutes.

The expected pressure in this defined standby condition is 42.00 psig.
Fictional project specification WP-LS-3 §2.1 states:

> Under the defined no-flow standby condition, each discharge-pressure channel
> shall read within ±0.75 psig of the expected baseline before acceptance.

### Field checklist

| Item | Field entry |
|---|---|
| Tag and cable labels | PT-101 through PT-108 matched PLC inputs AI-01 through AI-08. |
| Manifold position | Equalization valves marked open at data capture. |
| Loop power | 24 VDC supply steady; no PLC diagnostic flags. |
| Reference | Header test gauge showed 42.0 psig after settling. |
| Weather / access | Indoor dry well, 21 °C; access clear. |
| Data capture | Twelve rounds at 30-second spacing exported for FOREMAN review. |

### Technician notes

- PT-103 conduit label was replaced after the original sleeve tore.
- AI-05 took one extra scan to appear after the PLC rack restart.
- During the earlier point-to-point check, PT-107 would not settle while its
  equalization valve was shut. J.M. used the local zero trim (+4.8 psi shown
  as the correction) to finish PLC scaling; the valve was then reopened.
  Revisit after lunch if startup timing permits.
- Temporary test leads were removed from the terminal cabinet.
- No leakage was visible at the impulse tubing fittings.

### Handoff

FOREMAN v4.2 was asked to evaluate the exported standby readings against
WP-LS-3 §2.1. Diane's engineering acceptance and signature remain outstanding.

---

**SCHEMATIC / INSTRUCTIONAL DATA ONLY.** Westfield Public Works, Oak Street Lift
Station, WP-LS-3, and all measurements are fictional. This field draft is not
verified by a licensed engineer and is not suitable for construction, operation,
or public-safety decisions.
