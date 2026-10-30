---
name: review-deck
description: Build a project review slide deck for a robot installation or deployment project by reading the project's GitHub repo and filling a fixed review template. Every point is extracted from the repo and traced to its source, and the user is asked only for the slots the repo cannot fill. Use this whenever someone wants a project review, installation review, deployment status deck, milestone or progress review, "review slides for <project>", or asks to summarise a project repo into slides for a meeting, even if they don't mention a template.
---

# Installation review deck

Turn an installation project repo into a review deck with a fixed structure. Three things decide what ends up in the deck, and they never swap roles:

- **The template** decides which slides exist and in what order (`templates/installation-review.yaml`).
- **The repo** decides what goes on them.
- **The user** fills only what the repo can't, and confirms judgments such as overall status.

This skill extracts and condenses. It does not author. A review deck is used as a record of where the project stood, so a confident-sounding bullet with nothing behind it does more harm than an honest "TBD".

## Ground rules

1. **The structure is fixed.** Use every slide in the template, in order, with the template's ids and names. Never add, merge, split or rename slides. An `optional: true` slide may be left out only when it has no content.
2. **Extract, don't invent.** Every bullet, table row, number, date and owner comes from a repo source or from the user's answer, and carries a source tag (format below). If you can't point at a source, it doesn't go on the slide.
3. **Ask once.** Collect every gap and every judgment that needs confirming, then ask in a single batch. Don't stop at each slide.
4. **Judgments are proposals.** Overall status, headlines and the executive summary are derived by you. Show the reasoning and let the user confirm or change them in the same batch.
5. **Never overwrite a past review.** Each review is written to its own dated folder.

## Inputs

| Input | Default | If unknown |
|---|---|---|
| Project repo | Current working directory | Ask for a path or GitHub URL. Clone read-only. |
| Review date | Today | — |
| Review period start | Date of the previous review: the newest `reviews/<YYYY-MM-DD>/` folder or `review/<YYYY-MM-DD>` git tag | Ask (part of the batch, not a separate question) |
| Review number | Previous review number + 1 | Ask |
| Template | `templates/installation-review.yaml` in this skill, unless `project.yaml` sets `review_template:` to another file in `templates/` | — |

The project repo may contain a `project.yaml` with metadata and `sources:` overrides. Read it first if it exists. `references/repo-conventions.md` describes the layout this skill expects and works best with.

## Workflow

### Step 1 — Load the template

Read the template file. For each slide, note its `fields` or `columns`, `sources`, `keywords`, `fresh`, `when_missing`, `max_bullets` and any `rule`. Apply `project.yaml` source overrides on top.

### Step 2 — Scan the repo

If the `repo-scanner` subagent is available, delegate to it: pass the repo path, the review period and the slide list with source hints. It returns an evidence index. Otherwise do the scan yourself, following the same procedure:

1. For each slide, look in the hinted `sources` first.
2. If those are empty, fall back to a keyword search across text files, honouring the template's `skip` list. Robotics repos often contain bags, point clouds and meshes; never open them.
3. For `git` sources, use read-only commands such as `git log --since=<start> --until=<date>`, `git diff <ref>..HEAD -- <paths>`.
4. For `github` sources, use the `gh` CLI if it is authenticated (`gh issue list`, `gh pr list --state merged`, `gh api repos/{owner}/{repo}/milestones`), or a connected GitHub tool. If neither is available, record the slide's GitHub sources as "not reachable" so the gap batch can ask for them.
5. Record each finding with its source reference and date. Don't summarise yet.

Reading "the entire repo" is the fallback, not the plan. The hints keep the context on what the deck needs.

### Step 3 — Map evidence to slots

Give every slide a coverage status:

- **found**: enough sourced content to fill the slide.
- **partial**: some fields or columns have no source (for example, a blocker with no owner).
- **missing**: nothing found.
- **stale**: for `fresh: true` slides, the newest source predates the review period start. The content may still be right, but it needs the user's confirmation.

Write the coverage report in the format in `references/output-formats.md`. Executive summary (S02) is `derive`: leave it until Step 5.

### Step 4 — Ask for gaps in one batch

Build one message that covers, slide by slide:

- each missing, partial or stale item: what is needed, and where you looked;
- each proposed judgment to confirm: overall status with the rule that produced it, and the three key messages.

Keep each question short and answerable. Use a structured question tool if the environment has one. If the user skips an item, mark it `TBD` on the slide. Don't fill it with a guess.

Tag the user's answers as `[src: user, <review date>]`. After the review, suggest where each answer belongs in the repo (for example "add this to docs/risks.md") so the next review finds it there.

### Step 5 — Condense

Fill each slide following `references/slide-rules.md`. In short: assertion headlines, one fact per bullet, numbers and dates over adjectives, named owners, within `max_bullets`. Keep what is decision-relevant; put supporting detail in the speaker notes or the appendix. Write S02 last, from the filled slides only, citing the slide each message comes from (for example `[src: S04]`).

### Step 6 — Validate and write

1. Write `deck.md` and `coverage.md` to `reviews/<review date>/` in the project repo. If the folder already exists, stop and ask; don't overwrite.
2. Run the structural check from the skill directory:
   `python scripts/check_deck.py <repo>/reviews/<date>/deck.md --template templates/installation-review.yaml`
   It checks slide order, ids, headlines, statuses, bullet limits and that every content line has a source tag. Fix every error and re-run until it passes.
3. If the `deck-validator` subagent is available, run it for the semantic check: does each source actually support its claim? Fix what it flags.
4. Report back briefly: the output path, coverage per slide (found / partial / TBD), and the open TBD items.

## Output

`deck.md` is the structured source of the deck, in the format defined in `references/output-formats.md`. Turning it into slides is a separate step: hand it to whichever renderer the team uses (a PowerPoint skill, a branded company template, Marp). The renderer may move source tags into the speaker notes, but it must not change slide order, headlines or content.

## Reference files

- `templates/installation-review.yaml`: the fixed structure. Read in Step 1.
- `references/slide-rules.md`: how to write headlines, bullets and tables. Read in Step 5.
- `references/output-formats.md`: `deck.md` and `coverage.md` formats, and the source tag syntax. Read before writing either file.
- `references/repo-conventions.md`: the project repo layout this skill expects. Read when a scan finds little, to tell the user what to add.
- `scripts/check_deck.py`: structural validator. Run in Step 6.
