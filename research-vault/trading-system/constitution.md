# Trading System — Constitution (FOUNDATION / v0)

Started 2026-07-17 ~11:00am PT. A bounded, rules-enforced volatility-premium harvest for **Jake's own capital
only** (self-directed — no other people's money, ever; that would be RIA territory). **Paper-first.** This doc
is the foundation stone; it grows clause by clause as we build. Sister to [[where-the-edge-is]] (the edge) and
[[market-fragility]] (the stand-down signals). This folder (`trading-system/`) is designed to lift into a
standalone repo later.

> Design order (non-negotiable): **constraints → vehicle → laws → paper → (much later) live.** You design
> AROUND the constraints, not the other way around.

## §0 — ACCOUNT CONSTRAINTS (the foundation; everything is built on these)
- **Broker: Fidelity | Options approval: TIER 1.**
  - **Permitted (Tier 1):** covered calls, buy-writes, rolling covered calls, buying calls/puts (long),
    **selling cash-covered puts (CSPs)**, long straddles/strangles.
  - **Forbidden at Tier 1:** spreads (Tier 2), naked/uncovered writing + short straddles (Tier 3).
    → **Defined-risk is enforced by the tier itself.** The one way to blow up selling vol (naked) is locked
    out for us by the broker. The constraint is a guardrail.
- **Capital: ~$1,000, cash account** (no margin). → one CSP at a time on a ~$5–10 name (strike×100 collateral).
  **Learning/proof vehicle, NOT income** (~$20–60/mo premium). Honesty up front so nobody mistakes it for a paycheck.
- **Fidelity has NO retail order API** → **live execution is MANUAL** (system proposes, Jake clicks). Automated
  testing runs on a separate **Alpaca paper** account. Human-in-the-loop is therefore the *default*, which is safer.

## §1 — THE VEHICLE (what the constraints force, and it's the right tool)
**The regime-gated wheel:**
1. Sell a **cash-secured put** on a liquid, quality, optionable name you'd genuinely be happy to own, at a
   strike you'd accept — **only while price > its 200-day**, **not within ~7 days of earnings**.
2. Collect the premium = the volatility risk premium (the validated edge, single-name expression).
3. If assigned → you own 100 shares → sell **covered calls** above your cost basis → repeat.
- This is the ONLY capital-efficient VRP vehicle at Tier 1 / $1k, and it's defined-risk by construction.
- ⚠️ Callback: the wheel was on the "four dead systems" list — dead as a way to BEAT buy-and-hold in a bull
  (caps upside). It is ALIVE as a **regime-gated premium harvest**. Different job; the discipline is the difference.

## §2 — CLAUSE ONE (the first law — earned, evidenced)
**Harvest vol ONLY above the 200-day. Stand down below it.**
- Evidence ([[where-the-edge-is]] VRP study + decay recheck): the 200-day gate keeps ~87–161% of the income
  while cutting drawdown ~8x (−533 → −68), across FULL / 2010+ / 2019+ eras — and got MORE valuable post-2019.
  It's an **ex-ante, real-time** rule (no lookahead), battle-tested through 2020 & 2022.
- Caveat baked in: the 200-day is LAGGING — a bolt-from-blue crash from ABOVE the line still bites. Size for
  the residual tail; never treat the gate as a force field.

## §3 — HONEST RISKS (the single-name tail vs the index we tested)
- The VRP study was on the INDEX. Single-name vol has a FATTER idiosyncratic tail (earnings gaps, low-priced
  junk can −30% on news). Mitigations become laws: **liquid + quality names only, no near-earnings, above the
  200-day, only names you'd own at the strike.**
- Assignment is not failure — it's the deal. You sold the put because you'd own it. If you wouldn't, don't sell it.

## §4 — BUILD ROADMAP (from the beginning)
1. **§0 constraints** — done (this doc).
2. **CSP name-selection screen** (Colab, token-free): the affordable/liquid/above-200d/no-near-earnings/
   not-junk optionable universe under ~$10, ranked by premium-yield vs risk. ← *next*
3. **Complete the laws** (constitution §5+): position size, max-loss/kill-switch, one-position rule, logging,
   halt flag — as enforceable CODE for the paper engine.
4. **Alpaca paper account**: prove the whole loop (propose → validate → execute → journal) with fake money, months.
5. **Live (Fidelity, manual)**: one CSP at a time, above the 200-day, human-clicks. Graduate size only on a
   clean paper + manual track record.

## §5+ — LAWS AS CODE (to be written)
*(placeholder — the enforceable risk engine: instrument allowlist, max position % , defined-risk-only assert,
daily-loss kill-switch, max open positions, mandatory audit log, phone-flippable global HALT.)*
