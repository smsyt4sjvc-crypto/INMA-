# transmission-chain — THE SPINE: risk-free rate → AI supplier orders, in five stages

> **Jake, 2026-08-18:** *"Treasuries → hyperscaler CDS/bond spreads → bank/private-credit appetite →
> hyperscaler capex commitments → AI supplier orders. // Hierarchy. Each should have its own running
> timeline. From the beginning of our data so we have a running log."*
>
> **THIS IS A CAUSAL ORDER, NOT A TOPIC LIST.** Each stage prices the one below it. A move at stage 1
> only matters to stage 5 if it survives the intervening stages — and the vault's job is to say WHERE a
> shock is currently sitting, and whether it has propagated or died. **Read the stages in order.**

Related: every stage note below · [[market-fragility]] · [[portfolio-state]] · [[new-economy-regime]]

---

## THE CHAIN — stage, question, instrument, note, current state

| # | stage | the question it answers | primary instrument | note | as of 2026-08-18 |
|---|---|---|---|---|---|
| **1** | **Treasuries** | what does risk-free duration cost? | Treasury par curve; 2s30s; auction internals | [[rates-board]] | **30Y 5.31% (Treasury, primary), 2s30s +112bp = 48th pctile. TIGHTENING.** |
| **2** | **Hyperscaler CDS / bond spreads** | what does the AI complex pay OVER risk-free? | 5Y CDS; new-issue concession; OAS | [[hyperscaler-credit]] | **NVDA 5Y CDS ~40 → 80.33bp since late May. DOUBLED. TIGHTENING.** |
| **3** | **Bank / private-credit appetite** | will anyone actually FUND it, and on what terms? | deal placement, SPV/ABS terms, RVGs, insurance/Bermuda bid | [[ai-financing-fragility]] · [[balance-sheet-board]] | **$500B announced to unstick STALLED deals; issuers ASKED TO WAIT; Ohio wrap restructured $250B blanket → $105B residual-value. RATIONING.** |
| **4** | **Hyperscaler capex commitments** | does the spending plan change? | capex guides, off-balance-sheet commitments, useful life, project phases | [[ai-capex-cycle]] · [[cepi]] | **Not yet cut. $3T off-B/S commitments; META make-whole with ZERO liability booked. INTACT — so far.** |
| **5** | **AI supplier orders** | does the revenue actually arrive at the sellers? | NVDA DC revenue, memory contracts, backlog, order intake | [[metered-compute]] · [[memory-regime-question]] · [[compression-thesis]] | **NVDA DC +92% vs cloud +40-48%. STILL ACCELERATING.** |

## ★★★ THE READING THIS ORDERING PRODUCES, AND IT IS THE POINT
- **★★★★★★ THE SHOCK IS CURRENTLY SITTING AT STAGES 1-3 AND HAS NOT REACHED 4-5.** **Rates are
  repricing, the complex's own credit has doubled, and the funding market is rationing rather than
  pricing — while capex plans are unchanged and supplier revenue is still accelerating.** ⇒ **That gap
  IS the trade and it is also the risk: stages 4-5 are the LAGGING half, and everything bullish about
  the AI complex is measured there.** *(Analysis. This is what a hierarchy buys you that a topic list
  does not.)*
- **⭐⭐⭐ AND THE BLOOMBERG US FINANCIAL CONDITIONS INDEX SAYS THE OPPOSITE OF STAGES 1-3, WHICH IS THE
  MOST INTERESTING CONTRADICTION ON THE BOARD TODAY.** Jake's chart: **FCI is near the TOP of its
  1990-2026 range (~+0.5 to +1) — i.e. conditions are LOOSE**, with the historic drawdowns marked
  (Gulf War ≈ −4 · LTCM ≈ −3.5 · GFC ≈ −13.5 · S&P downgrade ≈ −3.5 · Covid ≈ −7).
  ⇒ **An AGGREGATE index reads loose while two of its own components (long rates, AI-complex credit)
  are tightening hard.** ⇒ **Either the tightening is too narrow to move the aggregate — in which case
  it is an AI-COMPLEX event, not a macro one — or the FCI is being held up by equity levels and vol
  that lag credit.** **⬜ NOT SETTLED, and it is the sharpest open question the chain raises.**
  🚩 **FETCH: the FCI's component decomposition. An index is not evidence until you know which leg
  moved it.** *(Analysis.)*
- **⚠️ THE CHAIN IS A HYPOTHESIS ABOUT CAUSALITY, AND THE VAULT HAS NOT TESTED IT.** **Stated plainly so
  it does not harden by repetition: no lead-lag study has been run on these five stages.** **The
  ordering is economically reasonable and matches the 2026 sequence so far — it is NOT yet a measured
  relationship.** 🚩 **The test: does stage N move before stage N+1, on the vault's own dated record?**
  ⇒ **`wiki/_timelines/_chain.md` now makes that testable — it is the whole chain in one chronology.**

## 📌 HOW THIS IS MAINTAINED (so it does not rot)
- **Every stage note carries its own ⏱ TIMELINE block** (`tools/timeline_header.py`), so opening any
  stage gives its running log from the beginning.
- **`wiki/_timelines/_chain.md` is the MERGED CHAIN LOG** — all five stages in one chronology, each line
  tagged with its stage number, oldest first. **That is the "running log from the beginning of our
  data" Jake asked for.** Rebuild: `python3 tools/timeline_header.py --chain`.
- **Router key `CHAIN`** points any transmission/propagation inbound here.
- **⛔ When a new datapoint lands, file it to ITS STAGE — not here.** This note holds the ORDER and the
  current state of each link; the evidence lives in the stage notes. **A spine that accumulates detail
  stops being a spine.**

---
_Created 2026-08-18 on Jake's hierarchy spec._
