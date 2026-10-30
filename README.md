# Installation review

A Claude Code plugin that turns an installation project's GitHub repo into a project review deck with a **fixed structure**.

- **The template decides the slides.** Same slides, same order, every review of the same kind.
- **The repo decides the content.** Every bullet is extracted from files, commits, PRs, issues or test reports, and tagged with its source.
- **You fill only the gaps.** Anything the repo can't answer is asked in one batch. Skipped items stay `TBD` instead of being guessed.

## How it works

```
Load fixed template ─► Scan repo ─► Map content to slots ─► Ask user for gaps
                                                                   │
            Fill template ◄─ Validate ◄─ Condense key points ◄─────┘
```

| Step | What happens | Who |
|---|---|---|
| 1. Load template | Reads the chosen file in `templates/`: slides, fields, source hints | Skill |
| 2. Scan repo | Searches hinted files, git history and GitHub per slide | `repo-scanner` agent |
| 3. Map to slots | Marks each slide found / partial / missing / stale and writes `coverage.md` | Skill |
| 4. Ask for gaps | One batch of questions, plus overall status to confirm | You |
| 5. Condense | Assertion headlines, one fact per bullet, within limits | Skill |
| 6. Validate | `check_deck.py` for structure, then `deck-validator` agent for facts | Script + agent |

Output goes to `reviews/<YYYY-MM-DD>/deck.md` and `coverage.md` in the project repo. The next review uses that date as its period start.

## The templates

Three deck types, one YAML each. The skill uses the installation review unless the project's `project.yaml` sets `review_template:`, or you ask for a concept review or an engineering assessment.

### Installation review (default)

For a project being installed: progress against plan.

| # | Slide | Filled from |
|---|---|---|
| S01 | Title | `project.yaml`, README |
| S02 | Executive summary | Derived from S04–S09; status rule Green / Amber / Red |
| S03 | Scope and configuration | `docs/scope.md`, BOM, `config/`, version changes |
| S04 | Milestones | `docs/plan.md`, GitHub milestones |
| S05 | Work completed this period | Commits, merged PRs, closed issues, site logs in the period |
| S06 | Testing and commissioning | `tests/reports/`, FAT / SAT docs, CI runs |
| S07 | Issues and blockers | Issues labelled `blocker`, `bug`, `site-issue` |
| S08 | Risks | `docs/risks.md`, issues labelled `risk` |
| S09 | Decisions needed | Issues labelled `decision-needed`, `docs/decisions.md` |
| S10 | Next steps | Plan, assigned open issues, next milestone |
| S11 | Appendix (optional) | Site photos, report links |

### Concept review

For a project before contract: can we quote it, and what must the customer accept first.

| # | Slide | Filled from |
|---|---|---|
| S01 | Title | `project.yaml`, README |
| S02 | Executive summary | Derived from S05–S13; status from the S08 verdicts |
| S03 | Customer brief | `customer/`, requirements docs, README |
| S04 | What changed (optional) | Previous review, concept docs |
| S05 | Proposed concept | Concept and design docs, BOM |
| S06 | How it works | Concept docs, README |
| S07 | Fit check | Design docs, site survey |
| S08 | Feasibility | `docs/feasibility.md`, issues labelled `feasibility` |
| S09 | Tight constraints (optional) | Feasibility and design docs |
| S10 | Questions for the customer | `docs/questions.md`, issues labelled `question` |
| S11 | Risks | `docs/risks.md`, issues labelled `risk` |
| S12 | Quote impact | `docs/quote.md`, BOM |
| S13 | Decisions needed | Issues labelled `decision-needed`, `docs/decisions.md` |
| S14 | Next steps | Plan, assigned open issues |
| S15 | Appendix (optional) | Drawings, renders, site photos |

### Engineering assessment

For engineering's answer to one customer document, such as an email with new terms: what to agree to now and what to price separately. Give the skill that document as the trigger document.

| # | Slide | Filled from |
|---|---|---|
| S01 | Title | `project.yaml`, README, the trigger document |
| S02 | Design concept | Concept and design docs, with the principles behind them |
| S03 | What changed in the ask | Earlier customer documents and the trigger document, quoted word for word |
| S04 | Bottom line | Derived from S03 and S05–S08; recommendation confirmed by you |
| S05 | Sharpest issue (optional) | The trigger-document item with the widest gap, options side by side |
| S06 | Risks if we accept the terms | The trigger document, `docs/risks.md`, feasibility and quote docs |
| S07 | Technical risks | `docs/risks.md`, design and test docs |
| S08 | Item-by-item answer | One row per trigger-document item: this contract or priced separately |

To change the structure, edit the YAML. See [AGENTS.md](AGENTS.md) for the rules.

## Install

In Claude Code:

```
/plugin marketplace add https://github.com/Cygnus0923/Slides-structure
/plugin install installation-review@installation-review-tools
```

For a private repo, the machine needs GitHub access to it (for example via `gh auth login`).

To try it from a local clone without installing:

```bash
claude --plugin-dir ./plugins/installation-review
```

## Use

From inside a project repo:

```
Prepare the installation review deck for this project
/installation-review:review-deck
Review slides for the Tuas AMR project, period since the last review
```

The GitHub-based slides (milestones, issues, PRs) need the `gh` CLI authenticated, or a connected GitHub tool. Without either, those slots fall into the question batch.

## Getting good coverage

The skill works on any repo, but fills more and asks less when the project repo follows the conventions in [`repo-conventions.md`](plugins/installation-review/skills/review-deck/references/repo-conventions.md): a `project.yaml`, a milestone table in `docs/plan.md`, a risk register, dated site logs, and the four GitHub labels above.

## Rendering slides

`deck.md` is the structured source, not the final slides. Render it with whatever the team uses (a PowerPoint skill, the branded company template, Marp). The renderer may move source tags into speaker notes but must keep slide order, headlines and content.

## Repo layout

See [AGENTS.md](AGENTS.md#what-this-repo-is). An example of the output format is in [`examples/example-deck.md`](examples/example-deck.md).
