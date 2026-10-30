# Example rack scanning — Engineering assessment
review_date: 2026-11-20 · trigger: customer/2026-11-18-email.pdf · template: engineering-assessment v1

<!-- Fictional example for format reference. Not a real project. -->

## [S01] Title
**Headline:** Example rack scanning — Engineering assessment
**Layout:** title
**Status:** filled

- Customer: Example Logistics Pte Ltd [src: project.yaml#L2]
- Informs: the reply to the customer's 18 Nov email [src: user, 2026-11-20]
- Trigger document: email of 2026-11-18, six items [src: customer/2026-11-18-email.pdf]
- Audience: internal, not for the customer [src: user, 2026-11-20]
- Presenter: Engineering team [src: user, 2026-11-20]

## [S02] Design concept
**Headline:** Three units, two bought in, built around parts we already run
**Layout:** two-column
**Status:** filled

- AMR base, bought in: drives the aisles and docks to charge [src: docs/concept.md#L8]
- Telescopic mast, bought in: raises the camera head to 9.2 m [src: docs/concept.md#L9]
- Camera head, custom: 4 barcode cameras and lights [src: docs/concept.md#L10]
- Principle: reuse a base we already run, to limit unknowns [src: docs/concept.md#L30]
- Principle: buy the mast rather than build one, to keep effort on reading labels [src: docs/concept.md#L31]

## [S03] What changed in the ask
**Headline:** The September brief asked for a pilot; the November email asks for handover terms
**Layout:** table
**Status:** filled

| Topic | Earlier document | Trigger document |
|---|---|---|
| Read rate | "at least 99.5%" | "99.9%, binding at handover" [src: customer/2026-09-15-requirements.pdf p3; customer/2026-11-18-email.pdf item 1] |
| Temperature zones | "the −20 °C freezer zone is out of scope" | "include the freezer zone" [src: customer/2026-09-15-requirements.pdf p5; customer/2026-11-18-email.pdf item 2] |
| Throughput | "600 locations per hour" | "600 per hour as an agreed performance requirement" [src: customer/2026-09-15-requirements.pdf p3; customer/2026-11-18-email.pdf item 3] |
| WMS link | "results exported as CSV" | "live integration through the WMS API" [src: customer/2026-09-15-requirements.pdf p4; customer/2026-11-18-email.pdf item 4] |
| Site changes | "layout may change during the project" | "layout changes without additional cost" [src: customer/2026-09-15-requirements.pdf p2; customer/2026-11-18-email.pdf item 5] |
| New in the trigger document | — | "two years of support after warranty" [src: customer/2026-11-18-email.pdf item 6] |

## [S04] Bottom line
**Headline:** Pilot terms are deliverable; handover terms need numbers we don't have yet
**Layout:** summary
**Status:** filled

- Conclusion: the email turns a pilot into a handover, which the current design can't promise yet [src: S03; S06]
- Freezer operation is beyond the cameras and battery we selected [src: S05]
- 99.9% and 600 per hour have no measured basis; nothing has run on site [src: S06; S07]
- Recommendation: agree the pilot now; price handover terms after the pilot's measurements [src: S08; user, 2026-11-20]

**Notes:** "Pilot" means the system running on site with our engineers present. "Handover" means the customer runs it without us, against binding figures. The recommendation assumes the customer accepts a two-step contract.

## [S05] Sharpest issue
**Headline:** The freezer zone needs a different robot, not a configuration change
**Layout:** table
**Status:** filled

| Criterion | Option A: chilled zone only | Option B: add the freezer zone |
|---|---|---|
| What we deliver | Scanning at 2–8 °C, as quoted | Scanning at −20 °C as well [src: docs/feasibility.md#L11; customer/2026-11-18-email.pdf item 2] |
| Who makes the decision | Customer, as in the brief | Customer, with our new design [src: customer/2026-09-15-requirements.pdf p5] |
| What it needs | Cold-rated cameras, already planned | Freezer-rated base, heated cameras, new battery [src: docs/feasibility.md#L30-L32] |
| Risk to us | Priced and planned | A design we have not studied [src: docs/risks.md#L9] |
| Where it was asked | Brief, p5 | Email, item 2 [src: customer/2026-11-18-email.pdf item 2] |
- Recommended position: keep the pilot to the chilled zone; study the freezer zone as a priced option [src: user, 2026-11-20]

## [S06] Risks if we accept the terms
**Headline:** Four terms would bind us to figures and work nobody has priced
**Layout:** table
**Status:** filled

| Risk | Why it is a risk | If we sign it as written |
|---|---|---|
| 99.9% read rate at handover | Best bench result is 99.6% on clean labels | A shortfall on a figure we have never reached [src: customer/2026-11-18-email.pdf item 1; docs/feasibility.md#L22] |
| 600 per hour binding | Design reaches about 550 per hour on paper | A shortfall from day one [src: customer/2026-11-18-email.pdf item 3; docs/feasibility.md#L23] |
| Free layout changes | Site layout is not final | Open-ended rework inside the quoted price [src: customer/2026-11-18-email.pdf item 5; docs/risks.md#L7] |
| Two years of post-warranty support | No support terms with the mast supplier | Support costs nobody has quoted [src: customer/2026-11-18-email.pdf item 6; docs/quote.md#L25] |

## [S07] Technical risks
**Headline:** Three design risks stay whatever we sign; none tested on hardware yet
**Layout:** table
**Status:** filled

| Risk | Why it is a risk | What retires it |
|---|---|---|
| Mast sway at 9 m | Reading needs a still camera head | Trial at full height before the pilot [src: docs/risks.md#L6; issue #15] |
| Condensation on camera windows | Robot docks outside the chilled zone | Heated windows; test a dock inside the zone [src: docs/risks.md#L5] |
| Read rate on damaged labels | Bench tests used clean labels only | Trial on a sample of real damaged labels [src: docs/feasibility.md#L22] |

**Notes:** Nothing in the design has run on site yet.

## [S08] Item-by-item answer
**Headline:** Every email item answered: what the pilot covers, and what we price later
**Layout:** table
**Status:** filled

| Item | This contract | Priced separately |
|---|---|---|
| 1 · Read rate 99.9% | Measure and report the read rate on every run | Binding figure, once the pilot shows it is reachable [src: customer/2026-11-18-email.pdf item 1; user, 2026-11-20] |
| 2 · Freezer zone | Chilled zone only | Freezer study and design [src: customer/2026-11-18-email.pdf item 2; user, 2026-11-20] |
| 3 · 600 per hour | Record locations per hour on every run | Binding figure after the pilot [src: customer/2026-11-18-email.pdf item 3; user, 2026-11-20] |
| 4 · Live WMS API | Define the interface; CSV export stays | Build the live integration [src: customer/2026-11-18-email.pdf item 4; user, 2026-11-20] |
| 5 · Layout changes | Absorb changes to paths and dock position | Re-quote changes to aisle widths or rack heights [src: customer/2026-11-18-email.pdf item 5; user, 2026-11-20] |
| 6 · Post-warranty support | List wear parts and supplier terms | Support quote for the handed-over system [src: customer/2026-11-18-email.pdf item 6; user, 2026-11-20] |
