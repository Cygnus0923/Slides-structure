# Example rack scanning — Concept review #2
review_date: 2026-10-30 · period: 2026-10-02 → 2026-10-30 · template: concept-review v2

<!-- Fictional example for format reference. Not a real project. -->

## [S01] Title
**Headline:** Example rack scanning — Concept review #2
**Layout:** title
**Status:** filled

- Customer: Example Logistics Pte Ltd [src: project.yaml#L2]
- Concept revision: Rev B [src: docs/concept.md#L1]
- Review #2, 2026-10-30 [src: reviews/2026-10-02/deck.md]
- Audience: internal [src: user, 2026-10-30]
- Presenter: Solutions team [src: user, 2026-10-30]

## [S02] Executive summary
**Headline:** Amber — quotable once the customer accepts two limits
**Layout:** summary
**Status:** filled

- Overall status: Amber — two requirements are Settle with customer, none Not feasible [src: S08]
- The mast falls 0.1 m short of the highest label the survey found [src: S07]
- About 550 locations per hour against the 600 asked [src: S09]
- Top ask: approve taking both limits to the customer before requoting [src: S13]

## [S03] Customer brief
**Headline:** Seven requirements; the survey found one label higher than the brief
**Layout:** bullets
**Status:** filled

- Read pallet labels from 0.3 m to 9.0 m; survey found a 9.3 m label in aisle 14 [src: customer/2026-09-15-requirements.pdf p2; docs/survey-2026-10-08.md#L12]
- Aisles 1.8 m wide [src: customer/2026-09-15-requirements.pdf p2]
- Scan 600 locations per hour [src: customer/2026-09-15-requirements.pdf p3]
- Read rate of at least 99.5% [src: customer/2026-09-15-requirements.pdf p3]
- Runs overnight unattended and docks itself [src: customer/2026-09-15-requirements.pdf p3]
- Works in the 2–8 °C chilled zone [src: customer/2026-09-15-requirements.pdf p4]
- Results exported to the WMS as CSV [src: customer/2026-09-15-requirements.pdf p4]
- Out of scope: the −20 °C freezer zone [src: customer/2026-09-15-requirements.pdf p5]

## [S04] What changed
**Headline:** Rev B swaps the fixed mast for a telescopic one to reach 9 m
**Layout:** table
**Status:** filled

| Unit | Previous revision | This revision |
|---|---|---|
| Mobile base | AMR, 0.75 m wide | No change [src: docs/concept.md#L8] |
| Mast | Fixed, 6.0 m | Telescopic, 9.2 m at full extension [src: docs/concept.md#L9; commit 4c1e7a2] |
| Cameras | 2 barcode cameras | 4 barcode cameras on the mast head [src: docs/concept.md#L10; commit 4c1e7a2] |

**Notes:** Rev A could not reach labels above 6 m, which the brief of 2026-09-15 made a requirement.

## [S05] Proposed concept
**Headline:** Three units, two bought in, one custom mast head
**Layout:** two-column
**Status:** partial

- AMR base, bought in: drives the aisles and docks to charge [src: docs/concept.md#L8]
- Telescopic mast, bought in: raises the camera head to 9.2 m [src: docs/concept.md#L9; design/mast-datasheet.pdf]
- Camera head, custom: 4 barcode cameras and lights [src: docs/concept.md#L10]
- Cold-rated camera model not chosen yet [src: docs/concept.md#L14]

## [S06] How it works
**Headline:** One nightly run covers every aisle, then the robot docks itself
**Layout:** table
**Status:** filled

| Step | What happens | Unit |
|---|---|---|
| 1 | Run starts at the scheduled time | AMR base [src: docs/concept.md#L20] |
| 2 | Drives to the next bay | AMR base [src: docs/concept.md#L21] |
| 3 | Raises the head level by level, reading each label | Mast and camera head [src: docs/concept.md#L22] |
| 4 | Repeats until every aisle is done, then exports CSV | AMR base [src: docs/concept.md#L23] |
| 5 | Returns to the dock and charges | AMR base [src: docs/concept.md#L24] |

## [S07] Fit check
**Headline:** Fits the aisles; the mast is 0.1 m short of the highest label
**Layout:** table
**Status:** filled

| Check | Required | Design or measured | Margin |
|---|---|---|---|
| Highest label | 9.3 m | 9.2 m | −0.1 m [src: docs/survey-2026-10-08.md#L12; design/mast-datasheet.pdf] |
| Aisle width | 1.8 m | 0.75 m robot width | +1.05 m [src: customer/2026-09-15-requirements.pdf p2; docs/concept.md#L8] |
| Lowest label | 0.3 m | 0.25 m lowest camera | +0.05 m [src: customer/2026-09-15-requirements.pdf p2; docs/concept.md#L11] |

## [S08] Feasibility
**Headline:** Five requirements can be priced; two need the customer's agreement
**Layout:** table
**Status:** filled

| Requirement | Verdict | Why |
|---|---|---|
| Labels 0.3–9.0 m | Settle with customer | Aisle 14 has a 9.3 m label; the mast reaches 9.2 m [src: docs/feasibility.md#L6] |
| Aisles 1.8 m | OK | Robot is 0.75 m wide [src: docs/feasibility.md#L7] |
| 600 locations per hour | Settle with customer | Mast travel makes about 550 per hour [src: docs/feasibility.md#L8] |
| Read rate ≥ 99.5% | Work to price | Needs a trial on real labels [src: docs/feasibility.md#L9] |
| Overnight, self-docking | Work to price | Docking is standard; overnight scheduling is new [src: docs/feasibility.md#L10] |
| 2–8 °C chilled zone | Work to price | Cold-rated cameras needed [src: docs/feasibility.md#L11] |
| CSV export to WMS | OK | Existing export module [src: docs/feasibility.md#L12] |

## [S09] Tight constraints
**Headline:** Each location takes 6.5 s against a 6.0 s budget
**Layout:** table
**Status:** filled

| Item | Amount | Basis |
|---|---|---|
| Budget per location at 600 per hour | 6.0 s | 3600 s ÷ 600 [src: customer/2026-09-15-requirements.pdf p3] |
| Drive to next bay | 2.5 s | 2.5 m at 1.0 m/s [src: docs/feasibility.md#L20] |
| Mast move between levels | 2.8 s | Seller's speed, empty [src: design/mast-datasheet.pdf] |
| Read and decode | 1.2 s | Bench test [src: docs/feasibility.md#L22] |
| Total per location | 6.5 s | Sum of the three rows above [src: docs/feasibility.md#L23] |

**Notes:** 3600 s ÷ 6.5 s ≈ 554 locations per hour. Reading while the mast moves would save most of the 1.2 s.

## [S10] Questions for the customer
**Headline:** Three answers decide whether Rev B can be quoted as is
**Layout:** table
**Status:** filled

| Question | Why it matters |
|---|---|
| Can the 9.3 m labels in aisle 14 move down, or be scanned by hand? | Decides the mast height [src: docs/questions.md#L4] |
| Is about 550 locations per hour acceptable? | Decides whether reading on the move is needed [src: docs/questions.md#L5] |
| Which WMS fields go in the CSV? | Decides the export format [src: docs/questions.md#L6] |

## [S11] Risks
**Headline:** Cold-room condensation is the highest risk to the read rate
**Layout:** table
**Status:** partial

| Risk | Level | Mitigation | Owner |
|---|---|---|---|
| Condensation on camera windows after the robot docks outside the chilled zone | High | Heated windows; dock inside the zone | TBD [src: docs/risks.md#L5] |
| Mast sway at full height slows reading | Medium | Trial at 9 m before quoting | Engineering [src: docs/risks.md#L6] |

## [S12] Quote impact
**Headline:** Telescopic mast and two extra cameras added; new total not priced
**Layout:** bullets
**Status:** partial

**Add**
- Telescopic mast [src: docs/quote.md#L8]
- Two more barcode cameras, cold-rated [src: docs/quote.md#L9]
**Remove**
- Fixed 6 m mast [src: docs/quote.md#L12]
**Re-check**
- Engineering hours for reading on the move [src: docs/quote.md#L15]
- New total against the Rev A quote: TBD [src: docs/quote.md#L20]

## [S13] Decisions needed
**Headline:** Approve taking the two limits to the customer
**Layout:** bullets
**Status:** filled

- Take the 9.2 m reach and about 550 per hour to the customer before requoting; needed by 2026-11-06; asked by Sales [src: issue #14]

## [S14] Next steps
**Headline:** Trial the mast at full height and meet the customer before requoting
**Layout:** table
**Status:** partial

| Action | Owner | Due |
|---|---|---|
| Trial mast sway and reading at 9 m | Engineering | 2026-11-13 [src: issue #15] |
| Meet the customer on the two limits | Sales | 2026-11-06 [src: issue #14] |
| Requote Rev B | Sales | TBD [src: docs/plan.md#L9] |

## [S15] Appendix
**Headline:** Rev B drawing, mast datasheet and aisle 14 survey photo
**Layout:** gallery
**Status:** filled

- Rev B side drawing at full mast height [src: design/rev-b-side.png]
- Mast seller's datasheet, internal only [src: design/mast-datasheet.pdf]
- Aisle 14 top label at 9.3 m [src: site/2026-10-08-aisle-14.jpg]
