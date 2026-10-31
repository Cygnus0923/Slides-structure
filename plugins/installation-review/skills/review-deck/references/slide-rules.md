# Slide rules

How to turn sourced evidence into slide content. The aim is a deck a reviewer can read in under a minute per slide and trust line by line.

## Headlines

Every slide gets a headline that states the slide's conclusion as a full sentence, not a topic label. The slide name (from the template) already says what the slide is about; the headline says what the reviewer should take away.

| Topic label (don't) | Assertion headline (do) |
|---|---|
| Milestones | SAT slipped 6 days; all other milestones on track |
| Issues and blockers | One blocker open: LiDAR mount bracket awaiting RMA |
| Testing | 14 of 16 acceptance tests passed; 2 rescheduled for next visit |

Keep headlines under about 14 words. The headline must be supported by the slide's own content — if the bullets don't prove it, change the headline.

For a slide that is `TBD` or has no change, say so plainly: "No scope change this period", "Decisions: none requested".

## Bullets

- One fact per bullet. If a bullet contains "and" joining two separate facts, split it or drop the weaker one.
- Lead with the outcome, then the detail: "AMR docking accuracy within ±10 mm after tuning", not "Tuned docking parameters, accuracy now ±10 mm".
- Numbers, dates and names over adjectives. "3 of 4 units installed" beats "most units installed".
- Dates in ISO format (2026-10-30). Owners by name or team, never "TBD" unless the user skipped it.
- Stay within the slide's `max_bullets`. When there is more, keep what affects schedule, acceptance or cost; move the rest to speaker notes or the appendix.
- Group work-completed bullets under the template's group names, in the template's order. Leave out empty groups.

## Tables

- Use exactly the template's `columns`, in order.
- One row per item. Put the source tag in the last cell.
- Status cells use: Done, On track, At risk, Late, Blocked, unless the slide's `rule` gives its own values.
- A cell the repo can't fill and the user skipped holds `TBD`.
- Keep each cell to about 15 words. Move the detail to the speaker notes.

## Source tags

Every bullet and every table row ends with a source tag. See `output-formats.md` for the syntax. Prefer the most specific reference available: a line range over a file, a commit or PR number over "git log".

When several sources support one line, list the strongest one or two, not all of them.

## Speaker notes

Notes are optional. Use them for context the presenter should say but the slide shouldn't show: the reason behind a slip, detail behind a summary number, or which sources were stale and confirmed by the user.

## Summary slide (`when_missing: derive`)

Write it last: the executive summary in the review templates, the decision slide in the engineering assessment. Include what the template's fields ask for:

1. Overall status (Green / Amber / Red), when the template has a `status_rule`, with one line stating which part of the rule applied.
2. Up to three key messages, or the conclusion, each an assertion taken from a filled slide, tagged with that slide's id. A conclusion names the common cause behind the slides it summarises; a count ("six terms can't be agreed") is not a conclusion.
3. The top ask or the decision asked, taken from the slide the template names. If that slide has nothing, write "No decisions requested this review".

Don't introduce anything here that isn't already on another slide, except lines the template's rule says come from the user (such as deal risk).

## Writing for a business reader

The engineering assessment is read by whoever signs. Write so they don't need to ask what a word means:

- Every risk ends in money, time or a payment stage. If the amount isn't known, write `TBD` and say "exposure unknown"; don't write "not fully understood", "cannot bound" or "unpriced" on their own.
- Spell out internal labels (revision names, test numbers, wiki page names) or move them to the notes.
- An undefined term in a contested item ("cycle", "minor", "continuous", "handover") gets the definition we propose, and that definition becomes something we ask the customer to agree.
- Say what the customer gets before what we decline. "Measured cycle times from every trial run" beats "No binding cycle time".

## Judgment slides (`judgment: true`)

Write the confirmed version only. Put the reasoning and its sources in the speaker notes, and say what the judgment assumes. When the user changed your draft, the line is tagged `[src: user, <date>]` alongside the evidence.
