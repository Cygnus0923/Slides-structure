# Example rack scanning — Engineering assessment
review_date: 2026-11-20 · trigger: customer/2026-11-18-email.pdf · template: engineering-assessment v1

<!-- Fictional example for format reference. Not a real project. -->

## [S01] Title
**Headline:** Example rack scanning — Engineering assessment
**Layout:** title
**Status:** partial

- Informs: whether to sign the customer's 18 Nov terms, and our reply [src: user, 2026-11-20]
- Trigger document: Example Logistics email of 2026-11-18, six items [src: customer/2026-11-18-email.pdf]
- Our last offer: quotation of 2026-10-02 [src: customer/2026-10-02-quotation.pdf]
- Audience: internal; presenter: Engineering team [src: user, 2026-11-20]
- Contract value: S$ 480,000 [src: customer/2026-10-02-quotation.pdf p6]
- LD: 0.5% of contract value per week late, all LD capped at 10% [src: customer/2026-10-02-quotation.pdf p7]
- Payment stages: 30% at order, 50% at delivery, 20% at acceptance [src: customer/2026-10-02-quotation.pdf p6]
- Decision needed by: 2026-11-25 [src: user, 2026-11-20]
- Numbers we don't have: liability cap; LD rate for a read-rate shortfall [src: customer/2026-10-02-quotation.pdf; customer/2026-11-18-email.pdf item 1]

## [S02] Design concept
**Headline:** Built from parts we already run, so we can promise what we have measured
**Layout:** two-column
**Status:** filled

**Principles**
- Reuse a base we already run, to limit unknowns [src: docs/concept.md#L30]
- Buy the mast rather than build one, to keep effort on reading labels [src: docs/concept.md#L31]
**Units**
- AMR base, bought in: drives the aisles and docks to charge [src: docs/concept.md#L8]
- Telescopic mast, bought in: raises the camera head to 9.2 m [src: docs/concept.md#L9]
- Camera head, custom: 4 barcode cameras and lights [src: docs/concept.md#L10]

## [S03] What changed in the ask
**Headline:** Targets become binding figures, and excluded work moves into scope
**Layout:** table
**Status:** filled

| Topic | Earlier document | Trigger document | Effect |
|---|---|---|---|
| Read rate | "at least 99.5%" | "99.9%, binding at handover" | target → binding [src: customer/2026-09-15-requirements.pdf p3; customer/2026-11-18-email.pdf item 1] |
| Temperature zones | "the −20 °C freezer zone is out of scope" | "include the freezer zone" | excluded → in scope [src: customer/2026-09-15-requirements.pdf p5; customer/2026-11-18-email.pdf item 2] |
| Throughput | "600 locations per hour" | "an agreed performance requirement" | target → binding [src: customer/2026-09-15-requirements.pdf p3; customer/2026-11-18-email.pdf item 3] |
| WMS link | "results exported as CSV" | "can the link be a live API?" | question [src: customer/2026-09-15-requirements.pdf p4; customer/2026-11-18-email.pdf item 4] |
| Site changes | "layout may change during the project" | "without additional cost" | excluded → in scope [src: customer/2026-09-15-requirements.pdf p2; customer/2026-11-18-email.pdf item 5] |
| New in the trigger document | — | "two years of support after warranty" | new [src: customer/2026-11-18-email.pdf item 6] |

## [S04] Decision
**Headline:** Sign the pilot now; make figures binding once the pilot has measured them
**Layout:** summary
**Status:** filled

- Conclusion: the email turns a pilot into a handover, binding us to figures nobody has measured [src: S03; S06]

| Option | What we sign | Exposure | Deal risk | What the customer hears |
|---|---|---|---|---|
| Sign as written | All six items as asked | LD up to S$ 48,000, plus unpriced freezer work | Lowest | "Yes to everything" [src: S06; user, 2026-11-20] |
| Sign with our counter-offers | Pilot terms; figures binding once measured | LD only on figures we have measured | Kickoff may slip 2 weeks | "Measured figures first, then binding ones" [src: S06; S08; user, 2026-11-20] |
| Hold the kickoff | Nothing until terms agree | None | Customer may go to tender | "We need the terms settled first" [src: user, 2026-11-20] |

- Decision asked: sign with our counter-offers [src: user, 2026-11-20]
- What we tell the customer: you get a working system on site and the measured figures to set binding targets on [src: S08; user, 2026-11-20]
- Decision needed by: 2026-11-25 [src: user, 2026-11-20]

**Notes:** "Pilot" means the system running on site with our engineers present. "Handover" means the customer runs it without us, against binding figures. S$ 48,000 is the 10% LD cap on S$ 480,000.

## [S05] Sharpest issue
**Headline:** The freezer zone moves an unstudied design risk onto us
**Layout:** table
**Status:** filled

| Criterion | Option A: chilled zone only | Option B: add the freezer zone |
|---|---|---|
| What the customer gets | Scanning at 2–8 °C, as quoted | Scanning at −20 °C as well [src: customer/2026-11-18-email.pdf item 2] |
| Who carries the risk | Shared, on a priced design | Us, on a design not yet studied [src: docs/risks.md#L9] |
| What it needs | Cold-rated cameras, already planned | Freezer-rated base, heated cameras, new battery [src: docs/feasibility.md#L30-L32] |
| Exposure | None beyond the quote | Unpriced work, TBD [src: S06] |
| Where it was asked | Brief, p5 | Email, item 2 [src: customer/2026-09-15-requirements.pdf p5; customer/2026-11-18-email.pdf item 2] |
- Recommended: Option A, with a priced freezer study once the customer confirms the freezer aisle count [src: user, 2026-11-20]

## [S06] Exposure if we sign as written
**Headline:** Two binding figures carry LD up to S$ 48,000; two terms add unpriced work
**Layout:** table
**Status:** partial

| Term | Why we'd miss it | What it triggers | Exposure |
|---|---|---|---|
| 99.9% read rate at handover (item 1) | Best bench result is 99.6%, clean labels only | LD | Up to S$ 48,000 cap [src: customer/2026-11-18-email.pdf item 1; docs/feasibility.md#L22; S01] |
| 600 per hour, binding (item 3) | Design reaches about 550 per hour on paper | LD | Within the same cap [src: customer/2026-11-18-email.pdf item 3; docs/feasibility.md#L23] |
| Freezer zone in scope (item 2) | Needs a freezer-rated base and heated cameras | Unpriced work | TBD, exposure unknown [src: customer/2026-11-18-email.pdf item 2; docs/feasibility.md#L30] |
| Layout changes at no cost (item 5) | Site layout is not final | Rework | TBD, exposure unknown [src: customer/2026-11-18-email.pdf item 5; docs/risks.md#L7] |

## [S07] Evidence behind the gaps
**Headline:** Our best read rate is measured; throughput and freezer work are not
**Layout:** table
**Status:** partial

| Contested term | Asked | Best we have now | Basis | What closes it |
|---|---|---|---|---|
| Read rate | 99.9% | 99.6% on clean labels | measured | Trial on damaged labels by 2026-12-15 [src: docs/feasibility.md#L22; issue #16] |
| Throughput | 600 per hour | About 550 per hour | estimate | Timed run at full mast height, TBD [src: docs/feasibility.md#L23] |
| Freezer zone | Operation at −20 °C | Not studied | untested | Freezer study, TBD [src: docs/feasibility.md#L30] |

**Notes:** Design risks not tied to a contested term: mast sway at 9 m (docs/risks.md#L6) and condensation on camera windows (docs/risks.md#L5).

## [S08] Counter-offer per item
**Headline:** Every item answered: two given, three traded for measured figures, one held
**Layout:** table
**Status:** filled

| Item | Kind | Our offer | Stance | Path to yes |
|---|---|---|---|---|
| 1 · Read rate 99.9% | Demand | Measure and report the read rate on every pilot run | Trade | Binding at the measured rate after the pilot; you supply 200 damaged labels [src: customer/2026-11-18-email.pdf item 1; user, 2026-11-20] |
| 2 · Freezer zone | Demand | Scan the chilled zone in the pilot; quote a freezer study | Hold | Study priced by 2026-12-20 once you confirm the freezer aisle count [src: customer/2026-11-18-email.pdf item 2; user, 2026-11-20] |
| 3 · 600 per hour | Demand | Record locations per hour on every run | Trade | Binding after the pilot, measured bay to bay [src: customer/2026-11-18-email.pdf item 3; user, 2026-11-20] |
| 4 · Live WMS API | Question | Get CSV from day one, and a live API after the pilot | Give | — [src: customer/2026-11-18-email.pdf item 4; user, 2026-11-20] |
| 5 · Layout changes | Demand | Move paths and the dock at no cost | Trade | Rack height or aisle width changes re-quoted; layout frozen by 2027-01-15 [src: customer/2026-11-18-email.pdf item 5; user, 2026-11-20] |
| 6 · Post-warranty support | Quote request | Receive a two-year support quote with the reply | Give | — [src: customer/2026-11-18-email.pdf item 6; user, 2026-11-20] |

**Notes:** Fallback if the customer refuses item 1's trade: binding at 99.5%, the brief's original figure (user, 2026-11-20).
