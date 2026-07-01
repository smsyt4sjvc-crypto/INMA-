# data/ — datasets for the brain

Drop CSVs / spreadsheets here (e.g. the macro database). Then in any chat say
**"ingest the macro data"** and I'll pull it from the repo and write the interpreting
wiki note (facts as DATA, the regime read as THESIS).

## Stored
- `jake-bishop-project-memory.csv` — CANONICAL. Full trading-project memory (profile, comm
  style, 11-vector convergence stack, 4-basket + Tier A/B/C portfolio, positions, hedges,
  principles, tools, open decisions). Supersedes earlier partial `portfolio-state` guesses.
  Dated 2026-06-30. Full reconciliation into `wiki/portfolio-state.md` still pending.

## Expected / stored
- `macro_2019_present.csv` — monthly monetary + macro + market series since 2019
  (Fed rates, balance sheet, M2, debt, CPI/PCE, curve, S&P/VIX/dollar/oil/HY spread).
  Built via the ChatGPT prompt in `wiki/data-sourcing-playbook.md`.
  → will be interpreted in `wiki/new-economy-regime.md`.
