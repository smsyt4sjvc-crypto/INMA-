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
| **5** | **AI supplier orders** | does the revenue actually arrive at the sellers? | NVDA DC revenue, memory contracts, backlog, order intake | [[metered-compute]] · [[memory-regime-question]] · [[compression-thesis]] · [[etched-inference-challenger]] | **NVDA DC +92% vs cloud +40-48%. STILL ACCELERATING.** |

## ⛔ AMENDMENT 2026-08-18 — STAGE 3 "RATIONING" NEEDS A QUALIFIER
**Etched raised $700M at +104% in 26 DAYS** ([[etched-inference-challenger]]) while this table calls
stage 3 **RATIONING**. ⇒ **Both are true because they are different markets: rationing describes DEBT
AGAINST DEPRECIATING GPU COLLATERAL; Etched is EQUITY IN THE THING THAT WOULD DEPRECIATE IT.**
⇒ **Capital is not scarce — it is repricing WHICH SIDE of the inference trade to be on.** **Read that
way the Etched raise CONFIRMS stage-3 stress rather than contradicting it.**
⇒ **Stage 5 also gains a second failure mode the original table missed: the incumbent's orders can hold
while a NEW ENTRANT takes the seat.** Stage 5 is now measured from both sides.

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

## ⛔⛔ AMENDMENT 2026-08-19 ~10:05am PDT — **TWO STRUCTURAL HOLES, AND THE SECOND IS THE MORE IMPORTANT: (a) STAGE 4 IS NOT ONE NUMBER — PART OF IT IS 15-25 YEAR TAKE-OR-PAY CONTRACT, NOT A CANCELLABLE CAPEX GUIDE; (b) STAGE 3 HAS A FUNDING CHANNEL THIS CHAIN HAS BEEN BLIND TO — REGULATED UTILITY RATE BASE**
Source: Jake's compiled research, *"Where the Data-Center Power Money Is Going — U.S. 2026"*, 2026-08-19
→ `raw/2026-08-19-dc-power-money/brief.md`. Gate: POWER(13), CAPEX(12), CHAIN(2); **full-text sweep found
NO multi-token hits — genuinely new territory for the map.**
⚠️ **ARTIFACT TEST: a COMPILED SECONDARY document with per-claim attributions (Talen, AEP, Chevron, Entergy,
Evergy, Oracle, Bloom, GE Vernova, IEA…). I verified NONE of it independently. Every figure below is
REPORTED. Most are checkable in 8-Ks and PUC dockets; that is the fetch, and it is not done.**

### THE HOLE IN STAGE 4 — the instrument list misses the hardest part of the stage
- **This table's stage-4 instruments are "capex guides, off-balance-sheet commitments, useful life, project
  phases."** ⇒ **ALL OF THOSE ARE THINGS A HYPERSCALER CAN REVISE.** ⇒ **The document shows a large and
  growing share of stage-4 spending is instead a SIGNED ELECTRIC SERVICE AGREEMENT OR PPA OF 15-25 YEARS
  WITH A NAMED COUNTERPARTY, MINIMUM-PAYMENT FLOORS, COLLATERAL AND TERMINATION CHARGES.**
- **THE HARDEST REPORTED NUMBER IN THE WHOLE DOCUMENT: EVERGY'S LARGE-LOAD STRUCTURE — CUSTOMERS
  RESPONSIBLE FOR MINIMUM PAYMENTS COVERING AT LEAST 80% OF CONTRACTED CAPACITY, PLUS COLLATERAL AND
  TERMINATION CHARGES**, across ESAs with Google (×2), Meta and Beale ≈ **2.5 GW aggregate signed peak load**
  by Q1 2026. **⚠️ EVERGY DOES NOT APPEAR ANYWHERE IN THIS VAULT BEFORE TODAY.**
- **Same shape elsewhere:** Oracle pays **100%** of energy costs at the DTE Stargate site incl. storage,
  transmission and dedicated substation · Equinix bears **100%** of the Central Georgia co-op's cost of
  service incl. new generation, HV substation and two transmission lines · Google pays DTE the **full cost**
  of generation, storage, transmission and distribution.
- ⇒ **★★★★★★ STAGE 4 THEREFORE SPLITS INTO A CANCELLABLE HALF (capex guides, project phases) AND A
  CONTRACTED HALF (ESAs/PPAs with minimums). THIS TABLE'S "INTACT — SO FAR" READS THE CANCELLABLE HALF
  ONLY.** ⇒ **The contracted half does not have a "so far." It has a term.** *(Analysis.)*

### THE HOLE IN STAGE 3 — and this is the one that changes the chain's headline
- **Stage 3 asks "will anyone actually FUND it, and on what terms?" and its instruments are all PRIVATE:
  deal placement, SPV/ABS terms, RVGs, the Bermuda bid. Current state: RATIONING.**
- ⇒ **⛔ THE DOCUMENT EXHIBITS A FOURTH CHANNEL THAT BYPASSES ALL OF THEM: A REGULATED UTILITY WITH A
  PUC-APPROVED LARGE-LOAD CONTRACT FINANCES THE GENERATION THROUGH ITS OWN RATE BASE, AT UTILITY COST OF
  CAPITAL, WITH COST RECOVERY.** **Entergy's Meta-driven plan alone: seven new CCGTs >5.2 GW, ~240 miles of
  500-kV, storage at three sites, nuclear uprates, up to 2.5 GW of new renewables — structured so Meta bears
  the cost of serving its load.** **DTE: ~1.4 GW for Oracle plus 1.0 GW for Google through Dec-2047.**
- ⇒ **★★★★★★ THAT IS THE CHEAPEST CAPITAL IN THE ENTIRE SYSTEM AND THIS CHAIN COULD NOT SEE IT, BECAUSE
  STAGE 3 WAS BUILT LOOKING ONLY AT PRIVATE CREDIT AND SECURITISATION.** ⇒ **"RATIONING" MAY BE TRUE OF THE
  CHANNEL THE VAULT WAS WATCHING AND FALSE OF THE SYSTEM.** ⇒ **This is the same class of error as the 8/18
  Etched amendment above — the stage was measured on one market and generalised to the stage.**
  ⚠️ **NOT a claim that stage 3 is fine: regulated financing is SLOW, capacity-limited and PUC-gated. It is a
  claim that the chain's stage-3 instrument set is INCOMPLETE.** *(Analysis.)*

### ⇒ THE CHAIN GAINS A NODE: STAGE 4b — THE POWER COUNTERPARTY
| # | stage | the question | primary instrument | note |
|---|---|---|---|---|
| **4b** | **Power counterparty (utility / generator / powered landlord)** | who holds the CONTRACTUAL CLAIM on the hyperscaler's cash flow, and who then spends it? | ESAs, large-load tariffs, PPAs, PUC dockets, minimum-payment & termination terms, customer-funded substation/transmission filings | [[power-scarcity-equities]] · [[power-not-petroleum]] |
- **★★★★★ THE POINT OF THE NODE, IN ONE LINE THE DOCUMENT GETS EXACTLY RIGHT: THE UTILITY/GENERATOR HAS A
  CLAIM ON THE *HYPERSCALER'S CASH FLOW*; THE EQUIPMENT MAKER HAS A CLAIM ON THE *UTILITY'S CAPEX*.**
  ⇒ **Two different credits, two different durations, two different failure modes — and stage 5 was
  measuring only the second.** *(Analysis.)*
- **★★★★★★ AND IT INDEPENDENTLY RE-DERIVES THE VAULT'S OWN 2000 FINDING FROM CONTRACT STRUCTURE RATHER
  THAN FROM PRICE HISTORY, WHICH IS THE CORROBORATION STANDARD.** `ai-capex-cycle:L2717`: ***"BACKLOG IS NOT
  DURATION. A signed PPA or a 20-year lease is duration; an order book is a queue of cancellable
  intentions"*** — **contracted-revenue owners (Crown Castle) grew through the 2000 bust; order-book
  installers (Quanta, Dycom) fell with the equipment makers.** ⇒ **That note assigned utilities/REITs to the
  Crown Castle side and GEV to the Quanta side FROM 2000 PRICES. This document reaches the same split FROM
  2026 CONTRACT TERMS.** ⇒ **And it grades GEV's position on its own ladder: ~116 GW of gas backlog **PLUS
  SLOT RESERVATIONS** — and a slot reservation is a RESERVATION, not an order.** *(Analysis.)*
- **⇒ ★★★★★ THE RISK REALLOCATION, WHICH IS THE TRADE-RELEVANT OUTPUT: IF THE AI CAPEX CYCLE DISAPPOINTS,
  THE LOSS DOES NOT LAND FIRST ON THE UTILITY — IT IS PROTECTED BY MINIMUMS, COLLATERAL AND TERMINATION
  CHARGES. IT LANDS ON THE HYPERSCALER (which still owes) AND ON THE EQUIPMENT MAKER (whose orders were
  placed against utility capex that can be deferred).** ⇒ **That INVERTS the intuitive "utilities are the
  bubble beta" read.** *(Analysis.)*

### ⛔ AND A HOUSEKEEPING HAZARD THE COLLISION CHECK JUST EXPOSED — DO NOT DOUBLE-COUNT THE GIGAWATTS
- **The document's warning: one campus can carry a utility-service contract + a renewable PPA + a nuclear
  contract + storage + fuel cells + backup gensets AT ONCE. Those MW DO NOT ADD.** **A 1 GW site drawing
  from DTE while Google signs matching renewable PPAs is not 2 GW of load.** **Correct unit: CRITICAL IT
  LOAD / PEAK CAMPUS LOAD first, then ask which resources physically SERVE vs financially MATCH it.**
- ⇒ **⚠️ THIS VAULT IS EXPOSED TO EXACTLY THIS. Today's collision check found "5 GW" on 12 lines and
  "800 MW" on 9, across notes that were never reconciled against one another.** 🚩 **A GW audit is now owed,
  and it is the same class as the 8/13 SPR 100× error: a number reused without checking its unit.**

### 📌 REGISTERED
1. 🚩🚩🚩 **VERIFY THE EVERGY 80% MINIMUM FROM PRIMARY** (10-Q/10-K or the Kansas/Missouri large-load tariff).
   **It is the single most load-bearing reported fact here and the vault has zero prior Evergy coverage.**
2. 🚩🚩🚩 **GW AUDIT ACROSS THE VAULT** — reconcile every GW/MW figure to critical-IT-load vs contracted
   supply vs financially-matched. **Same discipline as the post-SPR magnitude audit.**
3. 🚩🚩 **ADD STAGE 4b INSTRUMENTS TO THE ROUTINE:** PUC docket filings, ESAs, customer-funded
   substation/transmission filings. **These lead 8-Ks; the document's own claim is that the leading
   indicator sits in a commission docket, not in an earnings release.**
4. 🚩 **STAGE-3 RE-TEST: what share of announced AI power capex is being funded through REGULATED RATE BASE
   vs private credit/ABS?** **If the regulated share is large, "RATIONING" is a channel finding, not a
   system finding, and the chain's headline needs restating.**
**Links:** [[power-scarcity-equities]] · [[power-not-petroleum]] · [[ai-capex-cycle]] · [[ai-financing-fragility]] · [[buildout-bottleneck-map]]
