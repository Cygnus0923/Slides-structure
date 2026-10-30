# AGENTS.md

Instructions for any AI agent working with this repository, either **running** the review workflow on a project or **maintaining** the skill itself.

## What this repo is

A Claude Code plugin marketplace containing one plugin, `installation-review`. The plugin builds a project review deck for a robot installation project by reading that project's GitHub repo and filling a fixed template. Every point comes from the repo or from the user; nothing is invented.

```
.claude-plugin/marketplace.json         marketplace listing
plugins/installation-review/
├── .claude-plugin/plugin.json          plugin manifest (name, version)
├── agents/
│   ├── repo-scanner.md                 finds evidence, read-only
│   └── deck-validator.md               fact-checks the finished deck, read-only
└── skills/review-deck/
    ├── SKILL.md                        the workflow
    ├── templates/                      THE fixed slide structures, one YAML per review type
    ├── references/                     slide rules, output formats, repo conventions
    └── scripts/check_deck.py           structural validator
examples/example-deck.md                fictional installation review deck
examples/example-concept-deck.md        fictional concept review deck
```

## Roles when running a review

| Role | Who | Does | Never |
|---|---|---|---|
| Orchestrator | The main session running the `review-deck` skill | Loads the template, maps evidence to slots, asks the user once, condenses, writes `deck.md` and `coverage.md`, runs the checks | Adds, drops or reorders slides; writes a line without a source |
| `repo-scanner` | Subagent | Searches the project repo, git history and GitHub for each slot's evidence and returns an evidence index | Summarises, judges or edits anything |
| `deck-validator` | Subagent | Opens every source tag and checks the claim, dates, numbers, headlines and status rule | Edits the deck |
| User | The engineer preparing the review | Fills gaps the repo can't answer, confirms overall status and key messages | — |

If the subagents aren't available (for example outside Claude Code), the orchestrator does the scan and the validation itself, following the same agent files.

## Ground rules for every agent

1. **The template is the structure.** Slide ids, names and order come from the chosen file in `templates/` and nothing else.
2. **Extract, don't invent.** Every bullet and table row carries a `[src: ...]` tag pointing at a file, commit, PR, issue, milestone, CI run or user answer.
3. **Ask once.** Gaps and judgments to confirm go to the user in a single batch.
4. **Read-only on the project.** Scanning never changes the project repo or GitHub. The only write is the new `reviews/<date>/` folder.
5. **Unknown stays unknown.** A gap the user skips is `TBD` on the slide, not a guess.

## Rules for maintaining this repo

- **Changing the slide structure** means editing the template's YAML in `templates/`, then bumping its `version` and the plugin `version` in `plugin.json`. Update that template's example deck to match and make sure it still passes the checker.
- **Adding a template** for another project type: add a new YAML file in `templates/` with the same keys, and a fictional example deck in `examples/`. Projects select it with `review_template:` in their `project.yaml`. Don't fork `SKILL.md` for it.
- **Changing the deck format** means changing `references/output-formats.md` and `scripts/check_deck.py` together.
- Keep `SKILL.md` under about 300 lines. Detail belongs in `references/`.
- Before committing, run:

```bash
claude plugin validate .
python plugins/installation-review/skills/review-deck/scripts/check_deck.py \
  examples/example-deck.md \
  --template plugins/installation-review/skills/review-deck/templates/installation-review.yaml
python plugins/installation-review/skills/review-deck/scripts/check_deck.py \
  examples/example-concept-deck.md \
  --template plugins/installation-review/skills/review-deck/templates/concept-review.yaml
```

- To try local changes without installing: `claude --plugin-dir ./plugins/installation-review`.
