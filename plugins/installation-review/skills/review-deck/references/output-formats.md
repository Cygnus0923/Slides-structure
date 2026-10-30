# Output formats

Both files go in `reviews/<YYYY-MM-DD>/` in the project repo. `scripts/check_deck.py` parses `deck.md`, so follow the format exactly.

## Source tags

A source tag goes at the end of every bullet and in the last cell of every table row:

| Source | Tag |
|---|---|
| File, whole | `[src: docs/plan.md]` |
| File, lines | `[src: docs/plan.md#L12-L30]` |
| Commit | `[src: commit 3f2a9c1]` |
| Pull request / issue | `[src: PR #48]` · `[src: issue #52]` |
| GitHub milestone | `[src: milestone "SAT"]` |
| CI run | `[src: CI run 1182]` |
| Item in a customer document | `[src: customer/2026-10-23-email.pdf item 6]` |
| User answer | `[src: user, 2026-10-30]` |
| Another slide (summary slide only) | `[src: S04]` |

Two sources: `[src: issue #52; docs/risks.md#L4]`.

## deck.md

```markdown
# <Project> — Installation review #<n>
review_date: 2026-10-30 · period: 2026-10-16 → 2026-10-30 · template: installation-review v1

## [S01] Title
**Headline:** <deck title>
**Layout:** title
**Status:** filled

- Customer: <name> [src: project.yaml]
- Site: <site> [src: project.yaml]

## [S04] Milestones
**Headline:** SAT slipped 6 days; all other milestones on track
**Layout:** table
**Status:** filled

| Milestone | Planned | Actual / forecast | Status |
|---|---|---|---|
| FAT | 2026-09-12 | 2026-09-12 | Done [src: docs/plan.md#L8] |
| SAT | 2026-10-20 | 2026-10-26 | Late [src: milestone "SAT"; issue #52] |

**Notes:** Slip caused by bracket RMA (issue #52).
```

Rules the checker enforces:

- Slide headers are `## [<id>] <name>` with the template's id and name, in the template's order. Optional slides may be absent; nothing else may.
- Each slide has `**Headline:**`, `**Layout:**` and `**Status:**` lines. Status is `filled`, `partial` or `tbd`.
- Every bullet (`- `) and every table body row in the content ends with a `[src: ...]` tag, unless its text is exactly `TBD`.
- A `tbd` slide contains at least one `TBD` line.
- Bullets plus table rows do not exceed the slide's `max_bullets`. Group headings, such as `**Hardware installation**` or `**Add**`, are bold lines, not bullets, and don't count.
- Everything after `**Notes:**` is speaker notes and is not checked.

## coverage.md

```markdown
# Coverage — <Project> review #<n> (2026-10-30)
period: 2026-10-16 → 2026-10-30

| Slide | Status | Sources used | Gaps / notes |
|---|---|---|---|
| S01 Title | found | project.yaml | — |
| S04 Milestones | stale | docs/plan.md (last changed 2026-09-30) | User confirmed dates still valid |
| S07 Issues and blockers | partial | issue #52 | Owner and ETA from user |
| S09 Decisions needed | missing | — | User: none this review |

## Answers from the user
- S07 issue #52 owner: <name>, ETA 2026-11-04 → suggest adding to the issue
- S08 new risk: <text> → suggest adding to docs/risks.md

## Not reachable
- GitHub milestones (gh CLI not authenticated)
```
