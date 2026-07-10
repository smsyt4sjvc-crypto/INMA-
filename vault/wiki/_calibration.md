# _calibration — Jake's bias map

> This is the file that lets me disagree with you *usefully* instead of agreeing
> politely. It only works if the map is real and in your words. **You fill this
> in — honestly, in a working session.** I've seeded a few candidate observations
> from our build sessions, clearly marked as *my outside read* — confirm, rewrite,
> or delete them. Nothing here is settled until you say so.

Related: [[_persona]] · [[state]]

## How to fill this (prompts — answer in your own words, under THESIS)
- Where do you *over*-trust? (A tool "uploaded so it works." A contractor who
  talks a good game. A price that feels right without checking fair-market data.)
- Where do you *under*-weight? (Testing on-device. Reading the fine print.
  Following up. Saying no to a job that's a bad fit.)
- What do you talk yourself into? What do you talk yourself out of?
- When you've been burned before, what was the pattern *you* contributed?
- What kind of pushback actually changes your mind vs. bounces off?
- Money and liability: where are you appropriately cautious vs. where does caution
  cost you deals you should take?

## DATA (observed — things I actually saw, dated)
- [2026-07-10] Uploaded offer files to GitHub and assumed they were live; two
  uploads landed as empty commits and one looked "merged into the old file." The
  gap was caught only by checking the folder, not by the upload UI. Source: this
  session's git history.
- [2026-07-10] Caught two real bugs by testing on his actual iPhone that passed in
  the builder (the accept-checkbox; the export hand-off screen). On-device reality
  differed from the assumption. Source: this session.

## THESIS (the bias map — TENTATIVE, confirm or delete)
> These are *my* outside read after a few sessions, not your self-assessment.
> They're here as a starting point to react to. Replace with your real map.
- [2026-07-10] (my read — confirm/delete) Possible **"it shipped = it works"
  optimism**: strong bias to trust that a build/upload succeeded without verifying
  the end state on the real device or in the live folder. Counter-move I should
  make: before we call something done, ask "have you seen it work on your phone /
  in the live folder?"
- [2026-07-10] (my read — confirm/delete) **Builder's enthusiasm**: fast to add
  new tools and features. Usually a strength; the risk is surface area that
  outpaces testing/maintenance. Counter-move: occasionally ask whether a new thing
  earns its keep vs. the last three.
- [2026-07-10] (my read — confirm/delete) **Well-calibrated on money/liability**:
  repeatedly corrected money-flow and GC-liability framing without prompting. This
  reads as a genuine strength, not a bias — flagged so pushback here should be
  *rare* and evidence-heavy; don't invent risk where he's already careful.

## Falsified
- (none yet)
