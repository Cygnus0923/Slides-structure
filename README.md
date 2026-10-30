# Installation review

A Claude Code plugin that turns an installation project's GitHub repo into a project review deck with a **fixed structure**.

- **The template decides the slides.** Same eleven slides, same order, every review.
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
| 1. Load template | Reads `templates/installation-review.yaml`: slides, fields, source hints | Skill |
| 2. Scan repo | Searches hinted files, git history and GitHub per slide | `repo-scanner` agent |
| 3. Map to slots | Marks each slide found / partial / missing / stale and writes `coverage.md` | Skill |
| 4. Ask for gaps | One batch of questions, plus overall status to confirm | You |
| 5. Condense | Assertion headlines, one fact per bullet, within limits | Skill |
| 6. Validate | `check_deck.py` for structure, then `deck-validator` agent for facts | Script + agent |

Output goes to `reviews/<YYYY-MM-DD>/deck.md` and `coverage.md` in the project repo. The next review uses that date as its period start.

## The template

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
