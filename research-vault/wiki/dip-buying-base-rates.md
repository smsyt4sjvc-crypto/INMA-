# Dip-Buying Base Rates — the ruler for adding on weakness

Three empirical studies built 2026-07-23 (~7:34pm PT) to answer Jake's live question: *"should I add SPY/QQQ if it
dips further?"* Two are **war-tape** base rates (this war only); one is a **regime-general** drawdown ruler. Companion to
[[buying-at-highs]], [[seeing-vs-predicting]], [[detachment-bid]]; feeds [[portfolio-state]] and [[war-board]].

> Firewall: DATA = the computed numbers (source = Yahoo v8 chart pulls, dated below). THESIS = the reads, labeled.
> Method (to REGRADE): Yahoo v8 chart via curl; SPY / ^GSPC / ^NDX daily; war window from **2026-03-02** (war day-1,
> = today−144d); down-day threshold ≤ −0.80% close-to-close; forward returns close-to-close. Re-run to extend the sample.

---

## STUDY 1 — After a war ≥0.80% one-day SPX drop (DATA, SPY, since 2026-03-02)
- **n = 14** down days ≤ −0.80% (13 with a next day to grade; the 14th = 2026-07-23 itself).
- **Next day:** 6/13 UP = **46%** · avg **+0.17%** · median −0.05% · best +1.70% / worst −1.71%.
- **3 trading days forward:** 8/13 up = **62%**; but only **5/13 (38%) cleared +0.7%**; winners were FAT (+3.34%, +4.05%).
- **Renewed-campaign subset (since 7/11):** only 7/17 (−0.99%) graded → next day **−0.16%**, 3-day **+0.55%** (did NOT bounce).
### THESIS
- *(no bounce edge)* Next-day after a war down day is a **coin flip** (46% up, ~0 avg). "It fell so it'll bounce" is NOT
  in the data. On the 3-day horizon it's a **~38%-hit, fat-right-tail lottery** — most windows drift/chop, the few that rip
  pay big. A long call monetizes the tail; it does NOT get favorable odds. Confirms [[seeing-vs-predicting]]: magnitude yes,
  sign no. The recent hot-phase down day (7/17) did not reward the dip-buyer.

## STUDY 2 — War weekends (DATA, SPY, 21 weekends since 2026-03-02)
- **Fri-close → Mon-open GAP:** 12/21 UP = **57%** · avg +0.24% · median +0.09% · best +1.46% / worst −1.06%.
- **Fri-close → Mon-CLOSE (weekend + Mon session):** 14/21 UP = **67%** · avg **+0.38%** · median +0.23% · best +1.76% / worst −0.77%.
- **Skew:** 6/21 weekends gapped **≥ +0.7%** vs only **2/21 ≤ −0.7%** → big up-gaps outnumber big down-gaps **3-to-1**.
- **⚠️ Hot-phase caveat:** the two weekends INSIDE the renewed campaign both closed RED through Monday —
  **7/10→7/13 = −0.77%**, **7/17→7/20 = −0.16%** (gapped +0.5% then faded). The bullish stats are front-loaded in calm Mar–Jun.
### THESIS
- *(weekend = least-bad long window, but you still need the catalyst)* War weekends carried a real up-bias + favorable
  up-skew + contained downside — the calendar is NOT against a long. BUT the **median weekend (~+0.1–0.2%) doesn't cover a
  ~+0.7% option breakeven**, and the last two *hot-phase* weekends punished the long. The edge is the de-escalation
  **catalyst**, not the calendar. Absent the catalyst, it's a slow bleed.

## STUDY 3 — Drawdown-from-ATH ruler (DATA, ^GSPC + ^NDX, 2020→2026-07-23)
| Episode | S&P 500 | Nasdaq-100 |
|---|---|---|
| 2020 COVID | **−33.9%** (3386 2/19→2237 3/23) | **−28.0%** (9719→6994) |
| 2023 dip (Aug–Oct) | **−14.2%** (vs 4797 ATH → 4117) | **−14.9%** (vs 16573 ATH → 14110) |
| 2025 tariffs (Apr) | **−18.9%** (6144 2/19→4983 4/8) | **−22.9%** (22176→17090) |
| **Median of the 3** | **−18.9%** | **−22.9%** |
| *(if "2023" = 2022 bear low)* | *−25.4%* (→3577 10/12/22) | *−35.6%* (→10679 12/28/22) |
| **NOW (off 6/2/2026 ATH)** | **−2.6%** (7610→7408) | **−7.2%** (30661→28455) |
### THESIS
- *(we're at a wobble, not a correction)* −2.6% SPX / −7.2% NDX = **one-fifth to one-tenth** the depth of the last three
  real entries (shallowest −14%, median ~−19%/−23%, deepest −34%). "Further" has almost always meant **a lot** further →
  if scaling in on weakness, keep powder **staged**; don't spend it at −3%. The current dip is the appetizer.
- *(but don't over-wait — [[buying-at-highs]])* Deep dips are RARE; most dips resolve shallow and the tape grinds up.
  Holding cash for −19% risks missing the melt-up. Disciplined shape = a **LADDER**: small/none here, more at −7/−10%,
  the big tranche reserved for the −15%+ washouts that were the generational entries.
- *(SPY vs QQQ beta is NOT symmetric on the way down)* Rate/tech-driven selloffs (2022, 2025) hit **NDX harder** (−36%,
  −23% vs SPX −25%, −19%); the real-economy crash (COVID 2020) hit **SPX harder** (−34% vs −28%, tech was the haven).
  → In an AI-financing/rate-driven dip, **QQQ = deeper discount + bigger hit**; in an oil/war/real-economy shock, SPX catches
  down too. Match the vehicle to which shock brings the dip.

---
## Falsifier / regrade triggers
- STUDY 1/2 small-sample (war n small) — re-run to extend; a bounce edge could emerge or the coin-flip could firm up.
- STUDY 3 is the durable one (multi-cycle). Update "NOW" each session Jake asks; if SPX/NDX push to a new ATH the
  drawdown resets to 0 and the ladder resets.
- Book context at build: +2 SPY @ 738.46, names (VG/CRCL/LLY/NOW) held indefinite, rest SPAXX (cash = the dry powder this
  ruler is sizing). See [[portfolio-state]].

## 2026-07-30 ~4:20pm PT — APPLIED: "I just need 2%, that's not uncommon" (Jake) — the base rates, against the claim
- **THE MATH IS HIS.** SPY 741.69, Dec-745 put marked $26.11, cost $33.3667, 141 days left, IV ~15.6%.
  **Breakeven TODAY = SPY 726.82 = −2.01%.** (The −4.05% figure I quoted is the **EXPIRY** breakeven, SPY
  711.63, and only binds if held to December. **With 141 days of extrinsic on it, he needs 2%. He is right.**)
- **★★ AND THE VEGA MAKES HIS CASE BETTER THAN HE ARGUED IT.** Vega $182/pt:

  | SPY move | IV +0 | IV +3 | IV +6 | IV +10 |
  |---|---|---|---|---|
  | **−2%** | **+$724** | +$1,261 | **+$1,798** | +$2,516 |
  | −5% | +$2,049 | +$2,537 | +$3,037 | +$3,714 |

  **−2% with a 6-point IV pop is +$1,798 — it does not merely recover the loss, it clears the $3,337 basis.**
  **~60% of a shock payoff is the VOL leg, not the spot leg.** ⇒ **The position needs VIOLENCE, not
  direction.** A grinding −2% over three weeks pays ~$724 less ~$150 of theta; a violent −2% in one session
  with vol bid pays 2.5×. **That distinction is the whole trade and it is not what "I need 2%" describes.**
- **⛔ THE COUNTER IS IN HIS OWN ACCOUNT, 48 HOURS OLD.** `SPY 740.40 → 729.46 (−1.48%) → 741.69 (+1.68%)`;
  `put 27.16 → 34.16 → 26.11`. **He ALREADY GOT the shock day. It paid +$700 and was gone in 24 hours; the
  round trip netted −$105.** **He does not need a 2% move — he needs a 2% move that STICKS, or an exit taken
  INTO it.** *(Descriptive: the payoff here is governed by exit discipline, not by the forecast. He was up
  $700 on the thesis working.)*
- **STUDY 1 recall (war down-days):** *"most windows drift/chop; the few that rip pay big... magnitude yes,
  sign no."* **Chop is the enemy of a long option in either direction.** **STUDY 2 (war weekends): 67% UP
  Fri→Mon close, big up-gaps outnumber big down-gaps 3-to-1** — though **both hot-phase weekends closed RED**,
  which is the one base rate on Jake's side.
- **STUDY 3 update:** ATH 7610 (6/2/26); SPX ≈ **7417** now = **−2.5%**. His 2% takes it to −4.5% — **still
  inside "wobble," a quarter of the −18.9% median real correction.** Cuts both ways: shallow moves are common
  (his point), *and* nothing about the current tape says a real correction has begun (mine).

## 2026-07-31 ~5:20pm PDT — ★★★ MOVEMENT-CAPTURE SCREEN, RUN 1 (Jake's Colab, 34 names, 2015→)
`tools/movement_capture_screen_cell.py`. Dip = **≥8% off a 63d high**, transition-measured, 21d cooloff.

- **⛔ FIRST: A BUG IN MY CELL INVALIDATES THE `rec%` / `r*` / `score` COLUMNS.** The reclaim loop started at
  the **TRIGGER DAY**, so a name 8% off its high but **still ABOVE its 20-SMA** logged *"reclaimed, lag 0."*
  **It filtered nothing — rec% came back 100% on 29 of 34 names, lag 0 on six** (IREN, NBIS, RIVN, AMD, ARM,
  MP). **[[deep-value-reclaim]] requires BELOW the 20-SMA first, THEN a cross back above.** **Patched: events
  that never go below are now EXCLUDED. Re-run required.** ✓ **The `e*` columns never touch the SMA and are
  UNAFFECTED — everything below rests on those.**

### ★★★ THE HEADLINE, AND IT INVERTS A FOLK RULE — DO NOT BUY THE MEGACAP-LEADER DIP
| name | n | e21 | e63 | HEAT |
|---|---|---|---|---|
| **NVDA** | **53** | **−3.0** | **−3.6** | −5.4 |
| AVGO | 44 | −1.2 | −1.6 | −4.3 |
| TSM | 41 | −1.1 | −0.9 | −3.8 |
| SWKS | 46 | −2.2 | −1.9 | −6.5 |
| COHR | 47 | +0.2 | **−4.4** | −6.5 |
**NVDA is NEGATIVE at EVERY horizon on n=53.** ⇒ **Buying NVDA dips has UNDERPERFORMED simply holding NVDA.**
Mechanism: **its drift is so strong that the dip-conditional return is WORSE than the unconditional one** —
the dip is not an opportunity, it is a sample of the name's bad days. **"Buy the leader on weakness" is
measurably wrong here, n=53.**

### THE USABLE RANKING — EDGE PER UNIT OF HEAT (n≥19; HEAT = median worst 21d drawdown after entry)
| tkr | n | e63 | HEAT | e63/HEAT |
|---|---|---|---|---|
| **AMAT** | 46 | **+8.8** | **−2.4** | **3.67** |
| **IWM** | 33 | +2.8 | −0.9 | **3.11** |
| **SPY** | 19 | +3.6 | −1.2 | **3.00** |
| XLK | 35 | +3.7 | −2.3 | 1.61 |
| SMH | 37 | +3.9 | −2.6 | 1.50 |
| LRCX | 53 | +4.2 | −3.1 | 1.35 |
- **★★ AMAT IS THE STANDOUT: +8.8% edge at 63d on n=46 with only −2.4% HEAT.** Best in the table by a wide
  margin, **and it is already a 5% basket position.** **LRCX (4%) is the same cluster.** ⇒ **SEMICAP EQUIPMENT
  beats the megacaps it sells to, on dip-buying, decisively.**
- **★ IWM and SPY: small edge, almost NO heat.** The low-drama expression — and **SPY only gives 1.6 dips/yr**,
  so the opportunity rate is the binding constraint, not the edge.
- **⚠️ THE TOP OF THE `score` COLUMN IS A TRAP.** IREN scored 3.30 on **n=14, 119% vol, −10.3% HEAT**; NBIS on
  **n=8**. **Both used the BROKEN r21, and survivorship hits the neoclouds hardest — the ones that FAILED are
  not in the sample at all.** **Lottery tickets, not strategies.**
- **📌 FOR THE 90-DAY PLAN: HEAT IS THE SIZING INPUT.** At $1,037/name, **AMAT's −2.4% HEAT = sit through
  −$25**; **MP's −9.0% = −$93**; **IREN's −10.3% = −$107.** *Size for the heat, not the entry.*

## 2026-07-31 ~5:45pm PDT — ★★★ RUN 2 (filter fixed): the reclaim filter HURTS the best names, and the EV collides with the theta bill

### ★★★ FINDING 1 — THE FILTER IS A TRADE OF RETURN FOR SAFETY, AND THE **LAG** COLUMN TELLS YOU WHICH
| tkr | n | lag | e63 | r63 | Δ |
|---|---|---|---|---|---|
| **AMD** | 53 | 13 | +1.2 | **+5.1** | **+3.9** |
| **INTC** | 46 | 11 | +2.3 | **+4.8** | **+2.5** |
| QQQ | 27 | 11 | +2.2 | +3.9 | +1.7 |
| **LRCX** | 53 | 9 | **+4.2** | +1.6 | **−2.6** |
| **QRVO** | 45 | 10 | +3.9 | +0.3 | −3.6 |
| **AMAT** | 46 | **6** | **+8.8** | +4.1 | **−4.7** |
**The filter CUTS AMAT's edge — the best in the table — IN HALF. It QUADRUPLES AMD's and DOUBLES INTC's.**
**MECHANISM: waiting for the reclaim means entering LATER and HIGHER. On a name that SNAPS BACK you forfeit
the move; on a name that GRINDS you dodge the knife.**
⇒ **DECISION RULE, and the lag is the selector: LAG ≤9d → BUY THE DIP DIRECTLY. LAG ≥12d → WAIT FOR THE
RECLAIM.** Fast: **AMAT(6), AVGO(8), LLY(9), LRCX(9), NVDA(6)**. Slow: **AMD(13), MU(12), XLK(12), ORCL(12),
COHR(12), SWKS(12), ARM(12), IREN(17)**.
- **★★ THIS REFINES [[deep-value-reclaim]], IT DOES NOT CONTRADICT IT.** That note measured the filter at
  **PORTFOLIO** level: *"+3 points of CAGR while CUTTING VOL NEARLY IN HALF."* **Per NAME it is not uniform —
  it buys safety with return, and whether the trade is worth it is READABLE FROM THE LAG.** The portfolio
  result and the per-name result are both true; the vault only had the first.
- *(and rec% is still ~94-100% everywhere even after the fix — so the reclaim is near-UNIVERSAL after an 8%
  dip. It is therefore a **TIMING device, not a selector**. It never told you WHICH name; it tells you WHEN.)*

### FINDING 2 — 90 DAYS BUYS YOU ABOUT **FOUR SETUPS**
AMAT 0.99 · LRCX 1.13 · MU 1.16 · SMH 0.79 = **4.07 expected entries.**
⇒ **This is not an active-trading plan. It is WAIT-AND-STRIKE with long idle stretches. Budget patience,
not screen time.** *(HEAT at $1,037/name: AMAT −$25 · LRCX −$32 · SMH −$27 · MU −$65.)*

### ⛔⛔ FINDING 3 — THE DECISIVE ONE: THE DIP EDGE DOES NOT COVER THE OPTION CARRY
**All four firing once at $1,037 and capturing their full e63 edge = `+$226` on $4,148 = `+5.4%`/90d.**
**The theta bill on "half into long options" = `−$1,805`.**
⇒ **THE OPTION SLEEVE'S CARRY IS 8× THE DIP SLEEVE'S ENTIRE EXPECTED EDGE.**
- **★★★ AND NO AMOUNT OF DIP-BUYING AT THIS ACCOUNT SIZE FIXES IT.** Deploying the **whole** $7,262 at the same
  rate yields ~**$392** — still a fifth of the carry. **The problem is not the strategy. It is that the option
  position is LARGE RELATIVE TO THE BOOK** (the Dec put alone is **19%** of $12,766; adding another $1,800
  makes decaying instruments **~33%**).
- **⇒ THE REFRAME: THESE ARE NOT TWO HALVES OF ONE PLAN. THEY ARE TWO INDEPENDENT BETS WITH OPPOSITE CARRY.**
  **Sleeve A (dip capture): ~$4,148, ~+5%/90d, low heat, 4 setups — this is the EDGE.**
  **Sleeve B (the put): $2,410 committed, −$720 carry, pays only below SPY 711.63 — this is a WAGER.**
  **Adding to B doubles the carry without touching the edge.** *(Descriptive, rule 7: this is the arithmetic,
  not an instruction. Jake has already said B is a deliberate, accepted risk.)*
- **⚠️ EVERY REASON +5.4% IS TOO HIGH:** edge is over each name's OWN base rate · **survivorship — the failures
  are absent** · assumes all four caught and held 63d · overlapping windows ⇒ optimistic t-stats.

### THE SHORTLIST, FROM MEASUREMENT
**AMAT** — best in table: **e63 +8.8, HEAT −2.4, n=46, 4 dips/yr, lag 6 ⇒ BUY DIRECT, DO NOT WAIT.**
Already a 5% basket position. **LRCX** (+4.2, lag 9, direct) · **MU** (+4.9, lag 12 ⇒ wait for reclaim, HEAT
−6.3 so size smaller) · **SMH/XLK** (ETF expression, lowest heat).
**AVOID on measurement: NVDA (−3.6, n=53), AVGO, TSM, SWKS, COHR, MP, ARM.**
