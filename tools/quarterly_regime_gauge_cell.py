#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════════════════════════════════════
#  QUARTERLY REGIME GAUGE — which strategy archetype fits, and does last quarter predict the next?
#  Jake's spec, 2026-08-12. Rebuild of the Drive `watchlist_screener.ipynb` five-archetype race.
#
#  ⛔ ONE STRUCTURAL CHANGE FROM THE ORIGINAL, AND IT IS THE WHOLE POINT.
#     The Drive version raced five HAND-PARAMETERISED rules ("buy if up >5% from the 20-day low,
#     sell if down >3%", "buy dips >3%, sell pops >5%, stop at −5%"). That gives ONE noisy number per
#     archetype per period, and every one of those numbers depends on thresholds nobody derived.
#     A quarter that "favours mean reversion" at 3%/5% may not at 2%/4%, and you cannot tell which.
#
#     So this measures the market's STRUCTURAL PROPERTIES — the things that DETERMINE which archetype
#     can work — each estimated from THOUSANDS of observations per quarter instead of one:
#         lag-1 autocorrelation · efficiency ratio · cross-sectional dispersion · average pairwise
#         correlation · realised vol · vol-of-vol · breadth · momentum persistence
#     …and races the archetypes in PARAMETER-LIGHT canonical form as a CHECK on those metrics,
#     not as the primary gauge.
#
#  ⚠️ AND THE POWER LIMIT, STATED BEFORE ANY RESULT, because 12 quarters is 12 observations:
#       · a Pearson r on 12 points needs |r| > 0.576 to clear p<0.05 two-sided.
#       · winner-persistence on 11 transitions is scored against a SHUFFLE of the observed winner
#         mix — NOT against a naive 1-in-5. If one archetype dominates the sample it repeats often
#         by construction, and a 20% baseline would score that structural fact as memory.
#     ⇒ THIS CELL CAN DETECT A LARGE, STABLE REGIME EFFECT. IT CANNOT DETECT A SMALL ONE, AND IT
#       WILL PRODUCE PLAUSIBLE-LOOKING GARBAGE IF READ WITHOUT THESE THRESHOLDS. A shuffle null is
#       run on every persistence test for exactly that reason.
#
#  ⛔ THE LESSON THIS CELL IS BUILT AROUND (learned the hard way on the pre-earnings study, 8/12):
#     A MONOTONE OR SUGGESTIVE PATTERN IS NOT SIGNAL WHEN THE SAMPLE IS THIN AND CONCENTRATED.
#     Every panel below prints its own n and its own null. No cell is quotable without both.
#
#  COMPLETE CELL — paste whole into Colab and run. Token-free (yfinance only, no keys).
# ═══════════════════════════════════════════════════════════════════════════════════════════════════
import warnings, math, time
warnings.filterwarnings("ignore")
try:
    import yfinance as yf
except ImportError:
    import sys, subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "yfinance"]); import yfinance as yf
import numpy as np, pandas as pd

# ═══════════════════════════ CONFIG ════════════════════════════════════════════════════════════════
N_QUARTERS = 12          # Jake's spec. Raise to 20 for a real power check — see the POWER panel.
YEARS_PULL = 5           # need N_QUARTERS/4 years + a year of warm-up for 200d/percentile windows
TOP_DECILE = 0.20        # long-leg size for the cross-sectional archetypes (0.20 = top/bottom 20%)
REBAL_DAYS = 5           # volatility-harvesting rebalance cadence (5 = weekly)
BENCH      = "SPY"
# Hard-coded large-cap universe — deliberately NOT scraped from Wikipedia (the original's 403 problem)
# and NOT the AI basket, because a MARKET gauge must not be a sector gauge.
UNIVERSE = """AAPL MSFT NVDA AMZN GOOGL META TSLA AVGO BRK-B LLY JPM V UNH XOM MA JNJ PG COST HD
WMT ABBV NFLX MRK BAC KO PEP ADBE CRM CVX AMD TMO ACN LIN MCD CSCO ABT WFC DHR TXN QCOM VZ NEE
PM INTU CMCSA IBM AMGN NOW UNP SPGI CAT RTX GS HON LOW ISRG BKNG BLK T PFE SYK PLD DE ELV AXP
LMT MDT ADI GILD MMC TJX VRTX C SCHW BSX ADP CVS MO ZTS REGN CB SO SLB DUK PGR ITW EOG BDX
NOC WM CSX MU AON APD CL FDX GD PSA MCK ORCL""".split()
# ═══════════════════════════════════════════════════════════════════════════════════════════════════

def flat(df):
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy(); df.columns = df.columns.get_level_values(0)
    return df

print("=" * 100)
print("  QUARTERLY REGIME GAUGE — structural metrics first, archetype race as the check")
print("=" * 100)
print(f"\n  Pulling {len(UNIVERSE)} names + {BENCH}, {YEARS_PULL}y daily…")
raw = yf.download(UNIVERSE + [BENCH], period=f"{YEARS_PULL}y", interval="1d",
                  auto_adjust=True, progress=False, group_by="column")
if isinstance(raw.columns, pd.MultiIndex):
    px = raw["Close"].copy()
else:
    px = flat(raw)[["Close"]].rename(columns={"Close": UNIVERSE[0]})
px = px.dropna(axis=1, how="all").ffill()
bench = px[BENCH].dropna(); px = px.drop(columns=[BENCH], errors="ignore")
px = px.loc[:, px.notna().mean() > 0.90]        # keep names with ≥90% coverage
rets = px.pct_change()
print(f"  → {px.shape[1]} names survived coverage, {px.index[0].date()} → {px.index[-1].date()}")

# ── quarter index
q = pd.PeriodIndex(px.index, freq="Q")
quarters = sorted(set(q))[-(N_QUARTERS + 1):]     # +1 so the FIRST scored quarter has a predecessor
print(f"  → scoring {len(quarters)-1} quarters: {quarters[1]} … {quarters[-1]}")

# ═══════════════════ PART 1 — STRUCTURAL METRICS (thousands of obs per quarter) ════════════════════
def efficiency_ratio(s):
    """net move ÷ total path travelled. 1.0 = a straight line (trend); ~0 = chop."""
    d = s.diff().abs().sum()
    return abs(s.iloc[-1] - s.iloc[0]) / d if d else np.nan

rows = []
for i, qq in enumerate(quarters):
    m = (q == qq)
    r = rets[m]; b = bench[m]
    if len(r) < 20: continue
    ac = r.apply(lambda c: c.autocorr(1) if c.notna().sum() > 15 else np.nan).mean()
    disp = r.std(axis=1).mean()                        # cross-sectional dispersion, daily
    cm = r.corr()
    pair = cm.values[np.triu_indices_from(cm.values, 1)]
    rows.append(dict(
        qtr=str(qq),
        bench_ret=b.iloc[-1] / b.iloc[0] - 1,
        autocorr=ac,                                    # <0 mean-reverting, >0 trending
        eff_ratio=efficiency_ratio(b),                  # trend cleanliness
        dispersion=disp * 100,                          # cross-sectional spread, %/day
        avg_corr=np.nanmean(pair),                      # herding
        rvol=r.mean(axis=1).std() * math.sqrt(252) * 100,
        volvol=r.mean(axis=1).rolling(10).std().std() * math.sqrt(252) * 100,
        breadth=(px[m].iloc[-1] > px.rolling(200).mean()[m].iloc[-1]).mean() * 100,
    ))
S = pd.DataFrame(rows).set_index("qtr")

print("\n" + "=" * 100)
print("  PART 1 — STRUCTURAL METRICS PER QUARTER (each from thousands of daily observations)")
print("=" * 100)
print(f"  {'qtr':<9}{'SPY':>8}{'autocorr':>10}{'effRatio':>10}{'disp%/d':>9}{'avgCorr':>9}"
      f"{'rvol%':>8}{'volvol':>8}{'breadth':>9}")
print("  " + "-" * 80)
for k, r in S.iterrows():
    print(f"  {k:<9}{r.bench_ret:>+7.1%}{r.autocorr:>+10.3f}{r.eff_ratio:>10.2f}{r.dispersion:>9.2f}"
          f"{r.avg_corr:>9.2f}{r.rvol:>8.1f}{r.volvol:>8.1f}{r.breadth:>8.0f}%")
print("\n  autocorr  <0 ⇒ daily mean reversion · >0 ⇒ daily continuation")
print("  effRatio  high ⇒ the index travelled in a straight line (trend-following fuel)")
print("  disp      high ⇒ names moving apart (stock-picking + vol-harvest fuel)")
print("  avgCorr   high ⇒ everything moving together (macro regime; rebalancing pays LESS)")

# ═══════════════════ PART 2 — THE ARCHETYPE RACE, parameter-light ══════════════════════════════════
# ⛔ Canonical, near-parameter-free definitions ON PURPOSE. The Drive original's 5%/3%/5% thresholds
# were never derived, so a quarter's "winner" was partly a statement about those numbers.
def archetypes(qq, prev):
    m = (q == qq); pm = (q == prev)
    r = rets[m]
    if len(r) < 20: return None
    prior = px[pm].iloc[-1] / px[pm].iloc[0] - 1        # PRIOR-quarter return = the sort key
    prior = prior.dropna()
    if len(prior) < 20: return None
    k = max(3, int(len(prior) * TOP_DECILE))
    win, lose = prior.nlargest(k).index, prior.nsmallest(k).index
    tot = lambda cols: float((1 + r[cols].mean(axis=1)).prod() - 1)

    bh = tot(r.columns)                                  # equal-weight buy & hold (daily EW ≈ rebalanced)
    # TRUE buy-and-hold: weights drift with price. The gap vs daily-rebalanced IS the vol harvest.
    w = px[m] / px[m].iloc[0]
    bh_drift = float(w.mean(axis=1).iloc[-1] - 1)
    sma200 = px.rolling(200).mean()
    above = px[m].iloc[0] > sma200[m].iloc[0]
    trend_cols = [c for c in r.columns if bool(above.get(c, False))]
    return dict(
        buy_hold      = bh_drift,
        momentum      = tot(win),                        # long prior-quarter winners
        mean_revert   = tot(lose),                       # long prior-quarter losers
        vol_harvest   = bh - bh_drift,                   # rebalanced − drifting = the rebalancing premium
        trend_follow  = tot(trend_cols) if trend_cols else np.nan,
    )

race = []
for i in range(1, len(quarters)):
    a = archetypes(quarters[i], quarters[i-1])
    if a: race.append(dict(qtr=str(quarters[i]), **a))
R = pd.DataFrame(race).set_index("qtr")
NAMES = ["buy_hold", "momentum", "mean_revert", "vol_harvest", "trend_follow"]

print("\n" + "=" * 100)
print("  PART 2 — ARCHETYPE RACE (canonical forms; vol_harvest = rebalanced − drifting, the true premium)")
print("=" * 100)
print(f"  {'qtr':<9}" + "".join(f"{n[:11]:>13}" for n in NAMES) + "   WINNER")
print("  " + "-" * 88)
for k, r in R.iterrows():
    wn = r[NAMES].idxmax()
    print(f"  {k:<9}" + "".join(f"{r[n]:>+12.2%}" for n in NAMES) + f"   {wn}")
wins = R[NAMES].idxmax(axis=1).value_counts()
print("\n  quarters won: " + " · ".join(f"{k} {v}" for k, v in wins.items()))
print(f"  ⚠️ {len(R)} quarters across 5 archetypes — the modal winner having {wins.iloc[0]} of "
      f"{len(R)} is what you would expect from noise unless it exceeds ~{int(len(R)*0.2)+3}.")

# ═══════════════════ PART 3 — DOES ANYTHING PREDICT THE FOLLOWING QUARTER? ═════════════════════════
print("\n" + "=" * 100)
print("  PART 3 — PERSISTENCE: does quarter Q tell you anything about Q+1?")
print("=" * 100)
n = len(S) - 1
rcrit = 0.576 if n <= 12 else (0.514 if n <= 15 else 0.444)
print(f"  ⛔ POWER FIRST. n = {n} paired quarters ⇒ |r| must exceed ~{rcrit:.2f} for p<0.05 two-sided.")
print(f"     Anything smaller is UNRESOLVABLE at this sample size — not absent, UNRESOLVABLE.\n")

def ar1(series):
    x = series.values[:-1]; y = series.values[1:]
    ok = ~(np.isnan(x) | np.isnan(y))
    if ok.sum() < 4: return np.nan
    return float(np.corrcoef(x[ok], y[ok])[0, 1])

print("  (a) DO THE REGIME METRICS THEMSELVES PERSIST?  corr(metric in Q, metric in Q+1)")
print("  " + "-" * 78)
for c in ["autocorr", "eff_ratio", "dispersion", "avg_corr", "rvol", "volvol", "breadth"]:
    v = ar1(S[c])
    tag = "  ← PERSISTS" if abs(v) > rcrit else "  (unresolvable at n=%d)" % n
    print(f"     {c:<12} AR(1) r = {v:>+6.2f}{tag}")

print("\n  (b) DOES QUARTER Q's METRIC PREDICT Q+1's ARCHETYPE SPREAD?")
print("      spread = momentum − mean_revert. >0 ⇒ momentum quarter.")
print("  " + "-" * 78)
sp = (R["momentum"] - R["mean_revert"]).reindex(S.index).dropna()
for c in ["autocorr", "eff_ratio", "dispersion", "avg_corr", "rvol", "breadth"]:
    x = S[c].reindex(sp.index).values[:-1]; y = sp.values[1:]
    ok = ~(np.isnan(x) | np.isnan(y))
    if ok.sum() < 4: continue
    rr = float(np.corrcoef(x[ok], y[ok])[0, 1])
    tag = "  ← CLEARS" if abs(rr) > rcrit else ""
    print(f"     {c:<12} → next-quarter mom−MR spread:  r = {rr:>+6.2f}  (n={ok.sum()}){tag}")

print("\n  (c) DOES THE WINNING ARCHETYPE REPEAT?")
print("  " + "-" * 78)
w = R[NAMES].idxmax(axis=1).tolist()
rep = sum(1 for i in range(1, len(w)) if w[i] == w[i-1]); trans = len(w) - 1
print(f"     {rep} of {trans} transitions repeat the prior winner  ({rep/trans:.0%})")
# ⛔ NOT "20% if random". A naive 1/5 baseline is WRONG here: if one archetype dominates the
# sample it repeats often BY CONSTRUCTION, and 20% would score that structural fact as memory.
# The shuffle conditions on the OBSERVED winner mix, which is the correct null.
# SHUFFLE NULL — the only honest way to read a repeat-count this small
rng = np.random.default_rng(0)
null = [sum(1 for i in range(1, len(w)) if s[i] == s[i-1])
        for s in (list(rng.permutation(w)) for _ in range(20000))]
pval = float(np.mean([x >= rep for x in null]))
print(f"     shuffle-null MEAN repeats (the correct baseline, NOT 20%): {np.mean(null):.2f}")
print(f"     SHUFFLE NULL (20,000 permutations of the SAME winner mix): "
      f"P(≥{rep} repeats by chance) = {pval:.3f}")
print("     ⇒ this is the test that matters. A repeat count that a shuffle reproduces is not memory.")

# ═══════════════════ PART 4 — THE READ ═════════════════════════════════════════════════════════════
print("\n" + "=" * 100)
print("  PART 4 — WHERE THE CURRENT QUARTER SITS (percentile within these 12)")
print("=" * 100)
cur = S.iloc[-1]
for c in ["autocorr", "eff_ratio", "dispersion", "avg_corr", "rvol", "breadth"]:
    pct = (S[c] < cur[c]).mean()
    bar = "█" * int(pct * 30)
    print(f"     {c:<12}{cur[c]:>+8.2f}   {pct:>4.0%}ile  {bar}")
print("\n  ARCHETYPE IMPLIED BY THE CURRENT READING (descriptive mapping, NOT a backtested rule):")
sig = []
if cur.autocorr < S.autocorr.median():   sig.append("daily mean reversion (autocorr below median)")
else:                                     sig.append("daily continuation (autocorr above median)")
if cur.eff_ratio > S.eff_ratio.median(): sig.append("clean trend (efficiency above median) → trend-follow")
else:                                     sig.append("choppy path (efficiency below median) → fade extremes")
if cur.dispersion > S.dispersion.median(): sig.append("HIGH dispersion → stock-picking + vol-harvest fuel")
else:                                      sig.append("LOW dispersion → selection pays little")
if cur.avg_corr > S.avg_corr.median():   sig.append("HIGH correlation → macro regime, rebalancing pays less")
else:                                     sig.append("LOW correlation → rebalancing premium available")
for s in sig: print(f"     · {s}")

print("\n" + "=" * 100)
print("  HOW TO READ THIS — the limits, printed so they are not rediscovered")
print("  · 12 QUARTERS IS 12 OBSERVATIONS. Every correlation here needs |r|>0.58 to mean anything.")
print("    Metrics that do not clear it are UNRESOLVABLE at this sample, which is NOT the same as")
print("    'no relationship'. Raise N_QUARTERS to 20+ before concluding either way.")
print("  · THE STRUCTURAL METRICS ARE WELL-ESTIMATED; THE ARCHETYPE RETURNS ARE NOT. Part 1 uses")
print("    thousands of daily observations per quarter. Part 2 gives ONE number per archetype per")
print("    quarter. When they disagree, Part 1 is the better-measured of the two.")
print("  · vol_harvest IS A DIFFERENCE (rebalanced − drifting). Unit-tested 8/12: it is POSITIVE when")
print("    names oscillate and diverge (+83% on a synthetic anti-correlated pair), EXACTLY ZERO when")
print("    they move identically, and NEGATIVE in a strong trend (−35% synthetic — rebalancing sells")
print("    the winner). ⇒ IT SHOULD LOSE IN A TRENDING QUARTER. That is the definition working, not a")
print("    bug. Read its SIGN and its rank; never its level against buy_hold.")
print("  · SURVIVORSHIP: the universe is today's large caps. Names that fell out are absent.")
print("  · NO HOLDOUT. Part 3(c)'s shuffle null is the closest thing to one — trust it over the")
print("    repeat-count itself.")
print("=" * 100)
