# CEPI — Capex → Earnings → Price Intensity

A measure the **user invented** to gauge AI-capex fragility. Related: [[ai-capex-cycle]],
[[market-fragility]], [[fragility-engine]].

> Firewall: DATA = what the measure literally computes + observed inputs. THESIS = what a
> given CEPI reading is claimed to *mean*. The construct itself is the user's idea, not an
> established/consensus metric — flag it as such wherever cited.

## DATA (definition — what it computes)
- Universe treated as one "sector": Mag-7 + MU + ORCL (NVDA, MSFT, GOOGL, AMZN, META, AAPL,
  AVGO, MU, ORCL).
- Inputs per name (annual, current-cycle): capex, net income, revenue, price.
- Core ratios:
  - **Air gap** = (sector capex YoY growth) − (sector earnings YoY growth). >0 = capex
    outrunning earnings.
  - **Intensity** = sector capex / sector net income.
- Data source for current cycle: **yfinance annual** financials (clean). EDGAR quarterly is
  the higher-resolution upgrade but has XBRL tagging inconsistencies (YTD-vs-discrete,
  company-specific tags) — see ⚠️ below.

## ⚠️ artifact notes (do not treat as clean)
- EDGAR quarterly pull gave ORCL intensity 2.82, AMZN/NVDA empty, capex/revenue distorted —
  cause was per-company XBRL tagging (some report discrete 3-month, some YTD cumulative).
  CEPI for the *current* cycle was therefore pivoted to yfinance annual. EDGAR only for the
  harder multi-year cloud-era baseline, and only with tag normalization.

## THESIS (interpretation — NOT fact)
- *(user's thesis)* Capex growing faster than the earnings it's supposed to produce (positive,
  widening air gap) is the tell of a late-stage capex bubble; price is discounting returns
  that the cash flows don't yet support. When intensity is high AND price is at highs, the
  setup is fragile.
- *(analysis)* CEPI is a *leading* lobe of [[fragility-engine]] because fundamentals lead
  price — weight it heavily, but it is a bespoke construct, not a validated factor. Treat its
  output as a structured opinion, not a reading off an instrument.

## Sources
- User's v2 memo (CEPI framework). Session EDGAR/yfinance pulls, 2026-H1.

---

## 2026-08-07 ~1:55pm PDT — ★★★ CEPI GETS AN INSTRUMENT: `tools/cepi_tracker_cell.py` (Jake's spec: *"take capex:earnings… scale down and create a running E/C ratio"*)

**THE HONEST ANSWER TO "CAN WE REASONABLY RIGHT NOW": THE FRAMEWORK YES, THE NUMBER NO — AND THE CELL
PROVES IT BY PRINTING ITS OWN COVERAGE.** Seeded with everything the vault holds, the tracker returns
**ONE company-quarter (SPCX 2026Q2) filling 1 of 4 ratio cells.** Not a series — a seed. *(This note
had a thesis and no instrument for six weeks; it now has the instrument and a measured data gap.)*

### THE DESIGN — why FOUR ratios, not one (analysis)
- **E/C = net income ÷ capex** — Jake's ask; GAAP profit per dollar of capex.
- **★ OCF/C = operating cash flow ÷ capex — THE LINE THAT MATTERS. Below 1.00 the buildout is NOT
  self-funded** (FCF<0 ⟺ OCF/C<1). **The vault already has this firing at the aggregate: Alphabet's
  first negative-FCF quarter since its 2004 IPO, and the GS chart's five-hyperscaler combined negative.**
- **C/R = capex ÷ revenue** — intensity. Vault comparators: **SPCX 2.35x · ORCL ~1.0x · MSFT ~0.7x.**
- **DA/C = D&A ÷ capex** — the CATCH-UP ratio.
- **★★★ THE TRAP E/C ALONE WALKS INTO, AND WHY DA/C IS MANDATORY: earnings are AFTER depreciation, so
  as the 2024-26 wave depreciates, E/C falls for TWO reasons at once — capex UP and earnings DOWN.
  DA/C separates them: rising DA/C = the old capex hitting the P&L (mechanical, expected); FLAT DA/C
  with falling E/C = earnings deteriorating for a REAL reason.** **That is the difference between a
  depreciation wave and a demand problem, and E/C alone cannot see it.** *(Analysis.)*
- **⚠️ AND THE MEASUREMENT TRAP: headline "capex" from a press release often EXCLUDES FINANCE-LEASE
  ADDITIONS — where much AI infrastructure sits.** Use the **cash-flow-statement line + the lease
  footnote.** *(The vault caught exactly this once: MSFT $196.6B stale vs $329.1B actual — a $132B gap
  inside one number.)*
- **⚠️ WHAT THE RATIO IS AND IS NOT: capex spent in 2026 produces earnings in 2028-2030, so a
  CONTEMPORANEOUS E/C is NOT a return-on-investment measure.** It measures **how much current profit is
  being consumed by forward bets** — which is exactly the CEPI question ("is price discounting returns
  the cash flows don't support"), but it must never be described as ROI.

### 🚩 THE FETCH THAT TURNS THE SEED INTO A SERIES — per company, per quarter, from the 10-Q
**MSFT · GOOGL · AMZN · META · ORCL** (+ SPCX's missing lines), **2026Q1 and 2026Q2** to start:
1. **Revenue** · 2. **Capex** = *purchases of property & equipment* (cash flow statement) **PLUS
finance-lease additions** (state them separately) · 3. **Net income (GAAP)** · 4. **Operating cash
flow** · 5. **D&A** · 6. *(optional)* **remaining performance obligations / purchase commitments.**
**Six lines × 5 companies × 2 quarters = 60 numbers, and the series exists.**

**Links:** [[ai-capex-cycle]] · [[ai-financing-fragility]] · [[fragility-engine]] · [[compression-thesis]] ·
[[new-economy-regime]] (the 8/7 productivity entry — the macro-side version of the same question)
