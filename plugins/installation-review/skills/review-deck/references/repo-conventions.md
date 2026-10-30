# Project repo conventions

The skill works on any repo, but it fills more of the deck — and asks fewer questions — when the project repo follows this layout. When a scan comes back thin, use this file to tell the user which file or label would have answered the gap.

## Layout

```
<project-repo>/
├── project.yaml            Project metadata and source overrides (see below)
├── README.md               Overview: customer, site, what is being installed
├── docs/
│   ├── scope.md            Platforms, payloads, network, software stack
│   ├── bom.md              Bill of materials (or bom.csv / bom.xlsx)
│   ├── plan.md             Milestone table: Milestone | Planned | Actual / forecast | Status
│   ├── risks.md            Risk register: Risk | Likelihood | Impact | Mitigation | Owner
│   ├── decisions.md        Open and closed decisions, with who asked and needed-by date
│   ├── site-logs/          One file per site visit: YYYY-MM-DD.md
│   └── test/               FAT / SAT / acceptance procedures and results
├── tests/reports/          Generated test reports
├── config/                 Robot, network and software configuration
├── media/                  Site photos, named YYYY-MM-DD_<what>.jpg
└── reviews/
    └── YYYY-MM-DD/         Written by this skill: deck.md, coverage.md
```

## project.yaml

```yaml
project: Example AMR deployment
customer: Example Logistics Pte Ltd
site: Warehouse B, Tuas
team: [Alice (PM), Ben (integration)]
platforms:
  - model: <robot model>
    qty: 4
review_template: installation-review.yaml   # optional; a file in the skill's templates/
sources:                                    # optional; overrides template source hints
  S04: { files: [docs/schedule.md] }
  S06: { files: ["qa/results/**"] }
```

## GitHub labels

| Label | Feeds slide |
|---|---|
| `blocker` | S07 Issues and blockers |
| `site-issue` | S07 Issues and blockers |
| `risk` | S08 Risks |
| `decision-needed` | S09 Decisions needed |

Assign an owner and a milestone or due date to open issues; S07 and S10 read them.

## Concept-stage repos

Before contract, the concept review template reads these instead of a plan and test reports. Set `review_template: concept-review.yaml` in `project.yaml`.

| File or label | Feeds slide |
|---|---|
| `customer/` (brief, requirements, dated file names) | S03 Customer brief |
| `docs/concept.md` (units, operating cycle) | S05 Proposed concept, S06 How it works |
| `docs/feasibility.md`: Requirement · Verdict · Why | S08 Feasibility, S09 Tight constraints |
| `docs/questions.md`, issues labelled `question` | S10 Questions for the customer |
| `docs/quote.md` (Add · Remove · Re-check, prices) | S12 Quote impact |

Write feasibility verdicts down in the repo. The skill never assigns one, so without that file every verdict goes into the question batch.

## Customer documents

Save each customer document in `customer/` with a dated name, such as `customer/2026-11-18-email.pdf`, and keep its own item numbering. The engineering assessment compares the newest one (the trigger document) against the earlier ones, and quotes both by item number.

## Review anchors

Each review is saved in `reviews/YYYY-MM-DD/`. Optionally tag the commit as `review/YYYY-MM-DD`. The next review uses the newest of these as its period start, so the "work completed" slide covers exactly the time since the last review.
