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
