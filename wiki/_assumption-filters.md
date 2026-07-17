# _assumption-filters — the pre-flight for any thesis going load-bearing

Standing methodology note (set 2026-07-15, Jake's proposal). Sits with [[_persona]], [[_calibration]],
and the CLAUDE.md standing rules. Purpose: a small set of well-known reasoning "laws" run against the
vault's own assumptions before a thesis is promoted to load-bearing. NOT applied uniformly — used where
it BITES (applying all of them to everything is itself a Hick's Law violation).

> Firewall: this note is METHOD (how we check ourselves), not DATA or market THESIS.

## The four that catch THIS vault's specific biases — run these first
1. **Goodhart's Law** (a measure that becomes a target stops being a good measure).
   - Bites: our metrics-as-triggers. The moment "cover ratio <2x", the fragility-score, a POC line, or a
     trigger-threshold becomes a *target to watch*, it can decouple from the underlying risk — or get
     gamed by actors who know it's the watched line. Trust a metric only until someone optimizes against it.
   - Also explains the bear's self-referential-capex point: "AI capex" became the *signal* of seriousness,
     so it stopped *measuring* real end-demand (spend to signal, not because ROI justifies).
2. **Hanlon's Razor** (don't assume malice/design when self-interest, muddle, or incompetence explains it).
   - Bites: the vault's INTENT bias. "Debasement machinery", "weaponized against retail", "coordinated
     China buildout", "he'll inflate anyhow" — the language keeps sliding to a *plan*. Usually it's a
     thousand uncoordinated actors each dodging the recession on their own watch. Intent-attribution makes
     a thesis feel more certain than it is. (We logged the political corollary; keep the LANGUAGE honest.)
3. **Occam's Razor** (simplest explanation that fits the facts usually wins).
   - Bites: our multi-leg-mechanism habit (three-leg squeeze, the pincer, denominator-migration). Ask if
     "expensive + concentrated + cyclical → corrects and recovers" predicts as well with fewer moving parts.
     The elaborate version usually has a leg that breaks. (Jake's "two sides of one coin" = Occam in action.)
4. **Chesterton's Fence** (don't remove a rule until you understand why it exists).
   - Bites: "this time is different" / "historical precedence will be retired." The fence is the DENOMINATOR
     (price→return). Understand WHY it stands (human behavior, invariant across every revolution) before
     tearing it down because the tech is new. The vault's most seductive temptation; this is its guardrail.

## Standing thumb on the clock
- **Hofstadter's Law** (takes longer than expected, even accounting for that): apply to EVERY timing claim.
  The compression/resolution outlasts even the bear's dated estimate. When sequencing is the crux, bet "longer."

## Situational (use when relevant, not by default)
- **Hick's Law** (more choices → slower decisions): the behavioral catch. The "four dead systems" day was
  this; the fix is reducing the choice set (own-and-hold). Watch for it in strategy-churn and in a 40-note
  vault inducing paralysis.
- **Pareto (80/20)**: pruning tool — ~80% of the decision-signal lives in ~20% of the notes (crux,
  compression-thesis, denominator, fragility triggers). Use to keep the spine visible.
- **Dunning-Kruger**: the "I can know anything instantly" trap ([[how-to-get-paid]]) — feeling expert
  everywhere. Watch for confidence outrunning skill in a domain.
- **Parkinson / Peter / Brooks**: lower fit for market theses. Brooks + Hofstadter do bite the buildout-
  timing (more capex/GPUs ≠ productivity arrives faster). Parkinson bites the research process (work
  expands to fill time → produce decisions, not just notes).

## The rule
Before a thesis goes load-bearing (spine-level, or sized into the book): run it past **Goodhart, Hanlon,
Occam, Chesterton**, with **Hofstadter** on any timing claim. If it survives those four, it's earned its
weight. If it only survives by assuming a plan (Hanlon), a watched metric (Goodhart), an elaborate
mechanism (Occam), or a retired fence (Chesterton) — flag it and downgrade its confidence.

## Reading the feeds — narrative diffusion tiers (Jake, 2026-07-17)
News prices in TIERS, each moving at a different time. Where a headline SITS tells you how late it is:
1. **Mechanism tier** — bond desks watching bid-to-cover, FCF/maturity-wall modelers. Prices FIRST, in flows.
2. **Deep-press tier** — FT/Bloomberg/WSJ long-reads (depreciation, circular financing). Prices second.
3. **Retail-wire tier** — the Morning-Bid vibe line ("AI spending concerns returning to the fore"), hung on
   the most liquid, easiest-to-narrate SYMBOL (7/17: TSMC — a *foreign supplier*, the pick-and-shovel proxy,
   not the American spenders or their debt). Prices LAST. Retail sells the symbol; it can't see the plumbing.
- **Edge lives in the GAP between tiers**, and DECAYS the moment the vibe hits the retail wire. "Reuters
  caught up to us" reads as *early* but means *the crowd is now on it* = a more crowded place to stand.
- **The discipline: trade the MECHANISM, not the vibe.** Retail wire = sentiment turned; the bond
  market/next issuance = whether it's JUSTIFIED. They decouple:
  - **vibe without mechanism** (retail scared, bonds still clear, capex guides up) → *fadeable* fear.
  - **mechanism without vibe** (a Mag7 deal fails to clear / capex guided DOWN while retail's asleep) → the
    dangerous one; respect it.
- **7/17 state:** retail has the vibe; mechanism has NOT confirmed (TSMC 77% + guides up; <2x-cover bonds
  still *clearing*). Vibe running ahead of plumbing = fade setup, not respect setup — *until the plumbing
  catches up.* **Tripwire to watch = the next big Mag7 debt issuance and its bid-to-cover** (the thing retail
  can't see). Links: [[market-fragility]] (Slok cover-ratio), [[compression-thesis]] (razor), [[how-to-get-paid]].
