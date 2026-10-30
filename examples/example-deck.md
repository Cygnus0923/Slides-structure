# Example AMR deployment — Installation review #3
review_date: 2026-10-30 · period: 2026-10-16 → 2026-10-30 · template: installation-review v1

<!-- Fictional example for format reference. Not a real project. -->

## [S01] Title
**Headline:** Example AMR deployment — Installation review #3
**Layout:** title
**Status:** filled

- Customer: Example Logistics Pte Ltd [src: project.yaml#L2]
- Site: Warehouse B [src: project.yaml#L3]
- Review period: 2026-10-16 → 2026-10-30 [src: reviews/2026-10-16/deck.md]
- Presenter: Integration team [src: user, 2026-10-30]

## [S02] Executive summary
**Headline:** Amber — SAT slipped 6 days on a bracket RMA; install otherwise complete
**Layout:** summary
**Status:** filled

- Overall status: Amber — one milestone slipped ≤ 7 days, blocker has owner and ETA [src: S04; S07]
- All 4 AMRs installed and docking within tolerance [src: S05]
- 14 of 16 acceptance tests passed; 2 moved to next visit [src: S06]
- Top ask: approve weekend access for the SAT re-run [src: S09]

## [S03] Scope and configuration
**Headline:** No scope change; navigation stack updated to v2.4.1
**Layout:** two-column
**Status:** filled

- Platforms: 4 × AMR, 1 × charging dock per unit [src: project.yaml#L5-L8]
- Software: navigation stack v2.4.1 (was v2.3.0) [src: commit 3f2a9c1]
- Changes since last review: version bump only [src: commit 3f2a9c1]

## [S04] Milestones
**Headline:** SAT slipped 6 days; all other milestones on track
**Layout:** table
**Status:** filled

| Milestone | Planned | Actual / forecast | Status |
|---|---|---|---|
| FAT | 2026-09-12 | 2026-09-12 | Done [src: docs/plan.md#L8] |
| Installation | 2026-10-24 | 2026-10-23 | Done [src: docs/plan.md#L9; PR #47] |
| SAT | 2026-10-20 | 2026-10-26 | Late [src: milestone "SAT"; issue #52] |
| Handover | 2026-11-13 | 2026-11-13 | On track [src: docs/plan.md#L11] |

**Notes:** SAT slip traced to the LiDAR bracket RMA in issue #52.

## [S05] Work completed this period
**Headline:** All four units installed and tuned; operator training delivered
**Layout:** bullets
**Status:** filled

**Hardware installation**
- 4 of 4 AMRs mounted and commissioned on site [src: docs/site-logs/2026-10-23.md]
**Software and integration**
- WMS task interface live in staging [src: PR #47]
**Configuration and tuning**
- Docking accuracy within ±10 mm after tuning [src: tests/reports/docking-2026-10-24.md#L5]
**Documentation and training**
- Operator training delivered to 6 staff [src: docs/site-logs/2026-10-28.md#L3]

## [S06] Testing and commissioning
**Headline:** 14 of 16 acceptance tests passed; 2 rescheduled
**Layout:** table
**Status:** filled

| Test | Result | Date | Note |
|---|---|---|---|
| Acceptance suite | 14/16 pass | 2026-10-27 | 2 blocked by bracket [src: tests/reports/sat-2026-10-27.md] |

## [S07] Issues and blockers
**Headline:** One blocker open: LiDAR bracket awaiting RMA, due 2026-11-04
**Layout:** table
**Status:** filled

| Issue | Impact | Owner | ETA |
|---|---|---|---|
| LiDAR bracket cracked on unit 3 | Blocks 2 SAT tests | Integration team | 2026-11-04 [src: issue #52; user, 2026-10-30] |

## [S08] Risks
**Headline:** Spare-part lead time is the main schedule risk
**Layout:** table
**Status:** filled

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Spare lead time > 2 weeks | Medium | Handover slip | Hold 1 spare bracket on site | PM [src: docs/risks.md#L4] |

## [S09] Decisions needed
**Headline:** One decision: weekend site access for SAT re-run
**Layout:** bullets
**Status:** filled

- Approve weekend access on 2026-11-07 for SAT re-run; requested by PM [src: issue #55]

## [S10] Next steps
**Headline:** Re-run SAT after RMA, then prepare handover pack
**Layout:** table
**Status:** filled

| Action | Owner | Due |
|---|---|---|
| Fit replacement bracket | Integration team | 2026-11-05 [src: issue #52] |
| Re-run 2 SAT tests | Integration team | 2026-11-07 [src: milestone "SAT"] |
| Handover documentation | PM | 2026-11-12 [src: docs/plan.md#L11] |
