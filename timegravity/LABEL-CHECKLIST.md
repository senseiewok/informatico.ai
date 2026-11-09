# Label checklist · Time & Gravity (T)

The lint (`tools/check_timegravity_labels.py`) checks mechanics: rows, dates, collaborations, DOIs, label sequences. It
cannot read physics. A person decides the label with this checklist before a page ships (aviation-style: tick every
line, in order; a "no" stops at that line). Record the date and the initials of the checker in the pull request body.

## For every claim span

1. **Is it a claim at all?** Transitions, questions and definitions carry no span. If the sentence would still be true
   with the evidence removed, it is not a claim.
2. **Can a reader find the number in the source?** Every quantity in the span appears in the cited paper's abstract,
   a table, or a numbered result. If it comes from a secondary source, cite the secondary source as a `review` row.
3. **Does the span cite every row it leans on?** A number that needs two papers cites two rows.
4. **Decide the label, from the top down:**
   - **MEASURED** — at least two independent collaborations (different institutions, different apparatus), each with a
     peer-reviewed DOI, both older than the 24-month replication window, measured *the same quantity*. An internal
     repeat by the same collaboration is one collaboration.
   - **BOUND** — the result is an exclusion limit (an upper bound, a null result with a confidence level). Never write it
     as if the excluded thing were measured.
   - **DERIVED** — follows by mathematics from a named parent MEASURED row; the derivation row (a paper or a review)
     is cited too. If any step needs an assumption the parent does not cover, say so in the text.
   - **SINGLE RESULT** — one collaboration, or any peer-reviewed row inside the replication window, however good.
   - **PROPOSED** — a proposal, or any preprint. A preprint never rises above this.
   - **OPEN** — a question the field has not closed, anchored to a review or survey row that says so.
5. **Does the text say what the label means?** The first time a label appears on a page, one clause explains it.
6. **Would the claim survive the Scite column?** If the cited row shows more `contrasting` than `supporting`
   citations, read three of the contrasting statements on the Scite report before keeping the label; note the outcome
   in the ledger row's `note`. The counts are `[observed: Scite ML citation classification]`, never a verdict.

## For every page

7. The fixed boundary line is present, unchanged, in both languages.
8. The hub-only sentence does not appear (the lint checks the exact phrase; you check paraphrases).
9. "What would change this page" names at least one observation that would make a MEASURED or DERIVED claim false,
   and says the page would be withdrawn or rewritten, not relabelled.
10. The AI-contribution line names any AI system that contributed to a cited result and the human who checked it,
    or states that none did.
11. The page ends with exactly one open question, and the map on the hub names the page that takes it up.
12. The es-MX twin was read in Spanish by a person, not only diffed.

## For every ledger row

13. `review_by` is at most 24 months out for rows inside the replication window and at most 36 months for others.
14. `collaboration` names who did the work, not the journal.
15. `kind` is `press` for nothing; press rows do not enter the ledger.
