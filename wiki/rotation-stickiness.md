# Rotation Stickiness — when a tech→defensive rotation persists vs snaps back

The framework for judging whether a "money leaving tech, into defense/gold/healthcare" day is
the start of a regime or a 48-hour flush. Built 2026-07-03 off the candle-scan below.
Related: [[market-fragility]], [[concentration]], [[new-economy-regime]], [[detachment-bid]],
[[live-flow-trackers]], [[portfolio-state]].

> Firewall: DATA = the scan + observable base rates. THESIS = the stickiness model (analysis).

## DATA — the triggering scan (2026-07-03, candle scan, `tools/flow_trackers.py`-style)
- **Clean one-way de-risking day.** Sector roll-up (avg % move): Defense **+4.7**, Gold **+3.7**,
  Health **+3.0**, Staples **+3.0** at the TOP; Semis **−4.2**, AIinfra **−4.7**, Power **−1.1** at the BOTTOM.
- **Conviction confirmed by close-location:** greens closed at/near highs (Defense/Health/Staples
  clsLoc ~0.95–1.00 = bought all day); reds closed at/near lows (MRVL 0.21, NBIS 0.28, META 0.08,
  TSLA 0.10 = sold all day, no dip-buying). Directional, not chop.
- **Volume caveat:** rvol mostly ~1.0 (normal, not a panic spike) → orderly de-risking, not capitulation.
  ⚠️ MRVL −9.8% on rvol **0.6** (below-avg volume) = thin/gappy, trust that specific size less.
- **Base rates (observable history):** sharp-tech-down/defensive-up days occur many times per bull
  market; the majority resolve as V-bounces within 1–3 weeks (e.g. 2018-Q4 flushed then fully
  recovered; 2023–24 wobbles same). The minority that mark true tops (2000, 2007, 2022) → defensives
  led for quarters-to-years. Day-1 looks identical in both.

## ⚠️ Correction to prior read (firewall rule 4 — wrong reads stay)
- **2026-07-02/03 WebSearch sector read was YTD-lagged and wrong for the current tape.** It reported
  Healthcare *weakening*, Defense *underperforming*, Energy/Industrials/Materials *leading* (reflation).
  The bottoms-up candle scan says the **opposite**: Defense/Gold/Health/Staples leading, Energy/Indu
  middling, Semis/AIinfra dumping (**risk-off**, not reflation). The tape beat the search — same
  "go to the source" lesson as the ChatGPT stale-macro catch. Weight direct scans over search for *current* momentum.

## THESIS (the stickiness model — NOT fact)
- *(analysis, the core model)* **Valuation sets the DEPTH. Catalyst + Fed set the TIMING & stickiness.
  Concentration sets the TAIL.** Overvaluation only says how far it *can* fall — never that it starts now
  or persists. The rotation itself isn't sticky; the **earnings deceleration under it** is.
- *(analysis)* Stickiness lives on the **funding side** (tech bleeding), not the destination side
  (defensives ripping). In an over-owned, concentrated regime the unwind self-feeds (crowded exit →
  CTA/passive de-gross → [[concentration]] / Vector 11) → tech downside has a mechanical tail even if
  the defensive upside is modest.
- *(calibration — the side Jake under-weights)* "Usually sticky" **overstates the base rate.** On any
  single day, mean-reversion/bounce is the majority outcome; P(sticky) is LOW unconditionally, HIGH only
  *conditional on a real top* — and you cannot tell which from the rotation alone. One clean day ≠ regime.
- *(analysis — why THIS one has better-than-base odds)* Three stickiness conditions are unusually present:
  1. **Real catalyst** (Meta capex cut / compute-crack / memory+H100 pricing — [[ai-capex-cycle]]) — earnings
     decel is the ingredient that turns flush→regime. Present, not proven.
  2. **Hawkish Fed = no put** ([[new-economy-regime]], Warsh) — removes the #1 killer of defensive rotations
     (Fed blinks → tech V-bounces). Biggest structural point in favor.
  3. **Record concentration** — the mechanical tail is loaded.
  → Conditional, not confirmed. **The confirm is the leading-indicator set, not today's candles:** H100
  rental, DDR5 pricing, Aug-28 QCEW, next earnings guides. Roll → sticks. Hold + Fed dovish hint → flush.
- *(analysis — persistence ranking of the destinations)* **Gold is the stickiest leg** (real rates /
  debasement / CB buying = structural, multi-quarter, not positioning; rarely reverses in days).
  Defense & healthcare give more back on a tech bounce. If weighting which defensive *holds*: gold > defense/health.

## Book implication (descriptive, not advice — [[portfolio-state]])
- Jake's heavy sleeve (Semis: MU/MRVL/NVDA-adj; AIinfra: NBIS/CRWV) **is the funding source** — bottom of
  the scan. SPY Dec puts favored by exactly this tape. LLY (Health) on the right side today.
- ⚠️ **Power sleeve traded as AI-beta, not defensive** (Power −1.1, SMR −3.8 closed at low) — GEV/VST/OKLO/SMR
  correlated to the thing cracking, NOT hedged against it. Contradicts the "utilities improving" search read.

## Update 2026-07-07 — the rotation reached the SECOND RANK (evidence FOR sticky)
- *(DATA — Jake's Colab, 1-day moves)* Chips: SMH **−5.71**, MU **−7.65**, MRVL **−9.63**, AVGO −2.77,
  **NVDA only −1.75** (flagship defended; the basket destroyed). Healthcare: **GILD +4.38**, JNJ +3.77,
  LLY +2.99, REGN +2.78, **CI +2.46, UHS +2.32 — the cheap LAGGARDS beating XLV (+2.04)**.
- *(THESIS)* July-3 was liquid-first (ISRG/ABBV/JNJ ran, laggards sat). Today the [[quiet-health-screen]]
  value laggards (CI/UHS, both negative 52w) outperformed the sector ETF = flow working past the front of
  the line → **rotation-with-legs signature, not a 48h flush.** First second-rank entry in the sticky column.
- *(chips composition)* Pain concentrated in memory (MU) + custom-ASIC (MRVL — the AVGO/MediaTek margin-war
  repricing) while NVDA holds = the second-liners derate first, exactly as the [[ai-capex-cycle]] Stage-1.5
  read predicted.
- ⚠️ Still one day + one prior scan. Falsifier live: chips V-bounce this week + CI/UHS give it back = July-1 redux.

## Falsifiers (what kills the sticky read)
- Tech V-bounces within 1–3 weeks on no fundamental change → it was a flush (base-rate outcome).
- Fed hints at a cut → rotation likely ends (removes condition #2).
- H100 rental / DDR5 pricing hold firm + earnings guides don't cut → no earnings decel → flush.

## Sources
- Candle scan 2026-07-03 (`tools/flow_trackers.py`); session discussion 2026-07-03.

## Update 2026-07-10 — record tech insider BUYING (against-the-bear ledger, honest entry)
- *(DATA — Kobeissi/SentimenTrader chart, Jake image)* **28 XLK executives bought own stock on the open
  market in 6 months = highest on record** (prior record 25 in 2011 — a wobble insiders correctly bought;
  early-2025: 5). Doubled since Jan 2026. Paired with Jake's observation: SOXX fund INFLOWS last week.
- *(THESIS)* Two independent accumulation signals through the derate = real weight on the flush-not-regime
  side, alongside the V-bounce falsifier and the median line. Insider open-market buying has one explanation.
- ⚠️ Caveats: chart shows buyer COUNT, not net dollars (tech insiders sell on autopilot — no sell ratio
  shown); no buyer identity (buys cluster in FALLEN names — could be intra-tech value signal, not AI-core
  endorsement); no size split. → Jake running the Form-4 pull on the 24-name semi basket (OpenInsider cell)
  to answer the sharp version: are MU/AMD/semicap insiders buying or selling through the crack? LRCX/KLAC/
  AMAT insider direction = adversarial test of the scanner puts. TSM/ASML/ASX exempt (no Form 4s).

## Update 2026-07-10 PM — the semi Form-4 grid RESOLVES the insider puzzle (searches, verified)
- *(DATA, verified via WebSearch)* Semi-basket insider activity ~90d: **MU: all selling, zero buys — CEO
  Mehrotra $32.8M (June 26, day after the ATH), EVP $43.4M (Jul 1, 10b5-1), director sales. LRCX: director
  $39.1M over two days (Jun 11-12). AMAT: CTO 35k shares (Jun 15-16). NVDA/AVGO/MU/PLTR aggregate: ~$13B
  net insider sales trailing 3yr [Fool]. ZERO open-market purchases found across the 24.** Coverage: MU/
  LRCX/AMAT direct + aggregate; rest pending Jake's Colab Form-4 cell. Sells cluster Jun-11→Jul-1 (at the
  top), nothing found post-crash (blackouts + won't sell the hole).
- *(THESIS — the reconciliation)* The Kobeissi record XLK buying is real AND not in semis: XLK's 28 buyers
  ≈ the fallen software/legacy names (MSFT-19% class) = intra-tech VALUE accumulation. Semi insiders (the
  AI order books) distributed $100M+ at the June highs. **Record SOXX inflows + pundit-driven bounce (Tom
  Lee 7/9: AMD +7, INTC +5) + insider distribution = the textbook bag-holder pattern.**
- *(ledger fix)* The 7/10 "against the bear" entry SPLITS by sector: insider buying supports the fallen-
  tech value trade (= the quiet-health/GOOGL side); insider selling supports semi-complex caution (= the
  puts side). Both halves of Jake's book get insider sponsorship; the contradicted trade = the SOXX dip-buy
  he already declined. Vindicates compiling the index off the inflows.
- Watch: fresh Form-4 sells INTO the current bounce (post-7/8) = insiders using the rally as a second exit
  = final confirmation. Jake's 24-name Colab pull completes the grid.
- *(mechanics + the one-line summary, 2026-07-10)* Insider sales are PERSONAL money (can't fund capex/
  buybacks — those come from operating cash + debt). The real linkage runs the other way: active buyback
  programs = the corporate treasury providing the bid insiders sell into (check MU's 10-Q repurchase line,
  same filing as the prepayments tell). **The signal: corporately ALL-IN, personally DE-RISKED** — record
  capex guides + "shortage to 2027" publicly, while the officers' own money exits at the ATH; and not one
  open-market buy across 24 companies at prices they call a supercycle. Watch what they do with their own
  money, not what they guide with yours (Burry's public-commitment-bias, purest form). Caveat: 10b5-1
  mechanics make any single sale meaningless; the absence of buys is the tell.
- *(where the sale proceeds GO — the visibility map, 2026-07-10)* Personal portfolios are unreported: Form
  4s exist only where someone is an insider (no filing when a semi CEO buys GLD/treasuries/another sector's
  stock as a passive holder). Partial windows: (1) their Form 4s at OTHER companies (EDGAR searches by
  reporting-owner name across all issuers); (2) 13Fs ~never (family offices exempt); (3) **the aggregate
  shadow = the flow data already tracked: record $7.95T MMFs + gold bid = the class-level destination —
  the semi officers are effectively running Jake's book** (sell the complex at highs, sit in yield, wait);
  (4) the class-level revealed preference = the market-wide CLUSTER-BUY screen (3+ insiders buying own
  stock, rolled up by industry — openinsider latest-cluster-buys cell) → expect buys clustering in fallen
  value sectors and a void at the AI complex = the insider version of the rotation, market-wide.
- *(2026-07-10 — the market-wide cluster-buy map, Jake's run)* 40 recent cluster buys: **AI complex = a
  VOID** (zero semis/neoclouds/megacap tech). Where insider personal money IS going: **Pharma $101M** (#2
  industry = the quiet-health thesis co-signed), **energy throughout** (MTDR, EXE, DINO, KYN, YPF, PAM),
  fallen consumer value (KMX **5 insiders**, LOVE, VRA, FUN, MBC), financials (12-insider bank cluster,
  RYAN 5, HLNE), and two buildout-adjacent: **ACM (3, engineering services)** + **ADSK (4, $2.2M — the
  design-software layer, BSY's neighbor)**. Haircuts: strip CEFs (12/40 = mechanical NAV-arb), PSUS ($70M
  Ackman seeding) and LILA ($140M Malone control-buying) = plumbing not sentiment; the AI void is partly
  BASE RATE (megacap insiders never cluster-buy at highs) — the signal is the ASYMMETRY (pharma/energy/
  consumer execs buying own dips vs semi execs selling $100M at own highs). TSM row anomalous ($74 vs $434
  tape; FPIs don't file Form 4s) — quarantined. Tension logged: KMX 5-insider buy = a consumer-credit
  confidence vote AGAINST the Hollow Bottom's auto-lending read (small, honest entry).
- *(⚠️ CORRECTION 2026-07-10 — Jake's, supersedes the KMX read above)* **KMX 5-insider buying CONFIRMS the
  Hollow Bottom rather than cutting against it: CarMax = the trade-down landing pad** (the automotive ULTA).
  DATA (verified): avg new-car transaction ~$50K, avg financed $44,156, record **$777/mo** payment, **20.3%
  of new-car buyers paying $1,000+/mo** (ATH), 7-yr loans climbing; used avg $531/mo — the $246/mo gap =
  the forced-migration mechanism. Refinements: (1) KMX owns CarMax Auto Finance (subprime-adjacent) → the
  insider buys only pay in the **squeeze-but-not-collapse** world = the same grind-not-crack shape as Jake's
  GPT reframe — the auto-credit insiders are on his side of flush-vs-collapse; (2) the silicon thread runs
  through the windshield: cars = datacenters on wheels (automakers are named DRAM-suit victims) — the same
  memory extraction that put $150 on an Xbox holds cars at $50K → the trade-down IS the buildout's cost
  transmitting to households, one hop removed. Wrinkle: used PRICES fell 2% YoY (off-lease supply) = demand
  hasn't firmed used pricing yet — fine, arguably better for KMX units/margins.

## 2026-07-11 — GS Prime book: the hedge-fund layer prints (Jake paste)
- DATA (as-reported, GS prime brokerage weekly): Semis & Semi Equip = most net-BOUGHT subsector this
  week, but heavily net SOLD past month. Semi net exposure: **6.8% (Jan 2026) → 14% record (early June)
  → 10.3% now** of total US net exposure on the Prime book.
- Clarified for the record: HFs = hedge funds (prime-brokerage flow), a separate layer from insiders
  (Form 4, personal money) — three positioning layers now visible on the same sector.
- *(THESIS — the distribution chain in time order)* (1) INSIDERS sold first: zero buys/$100M+ sells at
  the June ATHs (the 24-name grid). (2) HEDGE FUNDS second: 14→10.3% in ~5 weeks. (3) RETAIL arriving
  last: presidential MU posts to Truth Social this week. Smart→fast→slow = distribution texture, not
  accumulation. Caveats: this week's HF net buying = a real V-bounce vote, and 10.3% is still ~1.5x the
  January weight — trimmed, not out; room to re-add OR keep unwinding.
- *(test link)* Bears on the [[quiet-health-screen]] basket-vs-SPY benchmark: HFs just re-bought chips.
  Chips re-sold into this bounce while the basket holds → rotation sticky; V-bounce holds → base rate
  wins. The next 2 weekly GS Prime prints = the scoreboard.
