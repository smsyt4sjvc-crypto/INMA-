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
