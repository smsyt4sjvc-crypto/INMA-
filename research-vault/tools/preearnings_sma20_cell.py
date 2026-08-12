#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════════════════════════════════════
#  PRE-EARNINGS 20-SMA SUPPRESSION STUDY — Jake's spec, 2026-08-12
#
#  THE IDEA (his words): "check companies that trade below (even daily low if it closes above) the
#  20 SMA at least 70% of the 45 trading days leading up to earnings. If after 30 days from the
#  45 day mark (15 days before earnings) it's traded under 70% we buy it then and through earnings.
#  Only in our 2nd order universe and if implied volatility is elevated. Sweep the volatility
#  threshold from normal to high so we can see results without rejecting too many."
#
#  FORMALISED:
#    · MEASURE window  = trading days [E−45, E−15)   ← 30 bars, ends the day we decide
#    · DAY CONDITION   = Low < SMA20  (a TOUCH counts even if the close is back above — his spec)
#    · TRIGGER         = suppressed_fraction ≥ 70%   (swept 50→90, because a fixed 70 is a guess)
#    · ENTRY           = close of E−15               (the last bar of the measure window)
#    · EXIT            = close of E+1                (through the print; E+0/E+3/E+5 also reported)
#    · UNIVERSE        = the 23-name 2nd-order basket, wiki/ai-infra-allocation-map.md:L161
#    · VOL GATE        = swept, and n IS PRINTED AT EVERY LEVEL so the rejection cost is visible
#
#  ⛔ THE ONE THING YOU MUST READ BEFORE TRUSTING A NUMBER — THE IV SUBSTITUTION.
#     There is NO free source of HISTORICAL implied volatility. yfinance serves the CURRENT option
#     chain only. So a backtest gated on "IV was elevated back then" cannot be built at tier 0.
#     What this cell does instead, explicitly:
#       · BACKTEST  gates on REALISED-vol percentile (20d RV ranked in its own trailing 252d).
#       · LIVE SCREEN gates on ATM IV ÷ RV20 from the real chain — "are options rich vs what this
#         stock actually does", which is the better reading of "elevated" anyway.
#     ⚠️ RV IS NOT IV. The gap between them IS the volatility risk premium — an entire vault thread
#     ([[bull-bear-ledger]] VRP studies). RV says what the stock DID; IV says what the market EXPECTS.
#     For a LONG-SHARES trade through a print, "expected big move" is the intended signal, and that is
#     the half RV cannot see. Treat every backtest row below as the RV-proxy version of the idea.
#
#  ⚠️ AND THE STRUCTURAL LIMIT, STATED UP FRONT: there is NO HOLDOUT here, and two thresholds are
#     swept. Any single best cell in these tables is selected by the same data that scored it. The
#     durable output is the SHAPE across the sweep + the CONTROL legs, never the best cell.
#
#  COMPLETE CELL — paste whole into Colab and run. Token-free (yfinance only, no keys).
# ═══════════════════════════════════════════════════════════════════════════════════════════════════
import warnings, time, math
warnings.filterwarnings("ignore")
try:
    import yfinance as yf
except ImportError:
    import sys, subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "yfinance"])
    import yfinance as yf
import numpy as np, pandas as pd

# ═══════════════════════════ CONFIG ═══════════════════════════════════════════════════════════════
# The 2nd-order capex basket — wiki/ai-infra-allocation-map.md:L161 (Jake's 7/31 construction).
# ⚠️ EWY is DROPPED: it is an ETF and has no earnings date, so it cannot enter an earnings study.
UNIVERSE = ["NVDA","AVGO","TSM","INTC","AMD","MU","GFS","ARM",      # compute silicon 35.5%
            "IREN","CRWV","NBIS",                                    # neocloud 13.5%
            "AMAT","LRCX",                                           # semicap 9.0%
            "COHR","LITE",                                           # optical 8.5%
            "QRVO","SWKS",                                           # RF/handset 7.0%
            "ORCL","TXN","RNW","RIVN","MP"]                          # + hyperscaler/analog/power/EV/materials

LOOKBACK_START = 45      # window opens this many trading days before earnings
ENTRY_OFFSET   = 15      # window closes / we enter this many trading days before earnings
SMA_LEN        = 20
TOUCH_MODE     = True    # True = Low < SMA20 (Jake's spec). False = Close < SMA20 (stricter).
# ⚠️ ONE GENUINE AMBIGUITY IN THE SPEC, EXPOSED RATHER THAN BURIED. "30 days from the 45 day mark"
# spans E−45 → E−15. That is 30 bars EXCLUSIVE of the decision bar, or 31 INCLUSIVE of it. Both are
# defensible: at the E−15 close you already know that bar's low, so counting it is legitimate.
# It only matters at the boundary — 70% is 21/30 but 22/31 (21/31 = 67.7% would fail). Flip and
# compare; if the result moves on this, the result was the boundary, not the setup.
INCLUDE_ENTRY_BAR = False
YEARS          = 6       # price history to pull
EXIT_OFFSETS   = [0, 1, 3, 5]   # trading days after the earnings date; 1 is the headline
SUPPRESS_SWEEP = [0.50, 0.60, 0.70, 0.80, 0.90]     # his 70% is the middle of this
VOL_SWEEP      = [0.0, 0.20, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]   # RV-percentile floor; 0 = no gate
BENCH          = "SPY"
PAUSE          = 0.4     # be polite to Yahoo; raise if you get rate-limited
# ══════════════════════════════════════════════════════════════════════════════════════════════════

def flat(df):
    """yf.download returns MultiIndex columns for some calls and not others. This is the single
    most common breakage in this whole notebook folder — 4 of the archived notebooks die on it."""
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy(); df.columns = df.columns.get_level_values(0)
    return df

def load_px(tkr, years=YEARS):
    try:
        df = yf.download(tkr, period=f"{years}y", interval="1d",
                         auto_adjust=True, progress=False, threads=False)
    except Exception as e:
        return None, f"download failed: {type(e).__name__}"
    if df is None or len(df) == 0:
        return None, "no rows returned"
    df = flat(df).dropna(subset=["Close"])
    if len(df) < 300:
        return None, f"only {len(df)} bars"
    df["SMA20"] = df["Close"].rolling(SMA_LEN).mean()
    r = df["Close"].pct_change()
    df["RV20"] = r.rolling(20).std() * math.sqrt(252)
    # RV percentile = where today's 20d realised vol sits in its OWN trailing year. Self-referential
    # on purpose: "elevated for THIS name", not elevated vs the market.
    df["RVpct"] = df["RV20"].rolling(252).rank(pct=True)
    return df, None

def load_earnings(tkr):
    """Past earnings dates. yfinance coverage is SHALLOW and uneven — this is the binding constraint
    on sample size, so the coverage is reported rather than hidden."""
    try:
        ed = yf.Ticker(tkr).get_earnings_dates(limit=60)
    except Exception as e:
        return [], f"{type(e).__name__}"
    if ed is None or len(ed) == 0:
        return [], "none returned"
    idx = pd.to_datetime(ed.index)
    try: idx = idx.tz_localize(None)
    except Exception:
        try: idx = idx.tz_convert(None)
        except Exception: pass
    today = pd.Timestamp.today().normalize()
    return sorted([d.normalize() for d in idx if d.normalize() < today]), None

def suppressed_fraction(df, i_e):
    """Fraction of the MEASURE window whose LOW pierced the 20-SMA.
    Window = [i_e-45, i_e-15) → exactly 30 bars, ending on the entry bar (exclusive)."""
    lo = i_e - LOOKBACK_START
    hi = i_e - ENTRY_OFFSET + (1 if INCLUDE_ENTRY_BAR else 0)
    if lo < SMA_LEN + 1 or hi <= lo:
        return None, 0
    w = df.iloc[lo:hi]
    if w["SMA20"].isna().any():
        return None, 0
    below = (w["Low"] < w["SMA20"]) if TOUCH_MODE else (w["Close"] < w["SMA20"])
    return float(below.mean()), len(w)

def build_events():
    rows, notes = [], []
    bench, berr = load_px(BENCH)
    if berr:
        raise SystemExit(f"⛔ {BENCH} failed ({berr}) — no benchmark leg means no interpretable result.")
    print(f"  {'ticker':<7}{'bars':>7}{'earnings':>10}{'usable':>8}   note")
    print("  " + "-" * 74)
    for t in UNIVERSE:
        df, err = load_px(t)
        time.sleep(PAUSE)
        if err:
            print(f"  {t:<7}{'—':>7}{'—':>10}{'—':>8}   ⛔ {err}"); notes.append((t, err)); continue
        eds, eerr = load_earnings(t)
        time.sleep(PAUSE)
        if eerr or not eds:
            print(f"  {t:<7}{len(df):>7}{'—':>10}{'—':>8}   ⛔ earnings: {eerr or 'empty'}")
            notes.append((t, f"earnings {eerr}")); continue
        used = 0
        for e in eds:
            pos = df.index.searchsorted(e)
            if pos <= 0 or pos >= len(df): continue
            i_e = int(pos)
            frac, n = suppressed_fraction(df, i_e)
            if frac is None: continue
            i_entry = i_e - ENTRY_OFFSET
            if i_entry < 0 or i_e + max(EXIT_OFFSETS) >= len(df): continue
            entry_px = float(df["Close"].iloc[i_entry])
            rvp = df["RVpct"].iloc[i_entry]
            rvp = float(rvp) if pd.notna(rvp) else np.nan
            rec = dict(ticker=t, edate=df.index[i_e], entry_date=df.index[i_entry],
                       frac=frac, rvpct=rvp, entry=entry_px)
            for k in EXIT_OFFSETS:
                px = float(df["Close"].iloc[i_e + k])
                rec[f"ret_{k}"] = px / entry_px - 1.0
                # benchmark over the IDENTICAL calendar span — the leg the archived backtests omit
                try:
                    b0 = float(bench["Close"].asof(df.index[i_entry]))
                    b1 = float(bench["Close"].asof(df.index[i_e + k]))
                    rec[f"spy_{k}"] = b1 / b0 - 1.0
                except Exception:
                    rec[f"spy_{k}"] = np.nan
                rec[f"alpha_{k}"] = rec[f"ret_{k}"] - rec[f"spy_{k}"]
            rows.append(rec); used += 1
        print(f"  {t:<7}{len(df):>7}{len(eds):>10}{used:>8}")
    return pd.DataFrame(rows), notes

def stat_block(d, k=1):
    if len(d) == 0: return None
    r, a = d[f"ret_{k}"], d[f"alpha_{k}"]
    return dict(n=len(d), win=(r > 0).mean(), mean=r.mean(), med=r.median(),
                amean=a.mean(), amed=a.median(), beat=(a > 0).mean(), sd=r.std())

def line(lab, s):
    if s is None or s["n"] == 0:
        return f"  {lab:<26}{'—  no events':>12}"
    return (f"  {lab:<26}{s['n']:>5}  win {s['win']:>5.0%}  mean {s['mean']:>+7.2%}  "
            f"med {s['med']:>+7.2%}  α-mean {s['amean']:>+7.2%}  beat-SPY {s['beat']:>5.0%}")

print("=" * 100)
print("  PRE-EARNINGS 20-SMA SUPPRESSION — 2nd-order basket")
print(f"  measure [E−{LOOKBACK_START}, E−{ENTRY_OFFSET}) = {LOOKBACK_START-ENTRY_OFFSET} bars · "
      f"{'LOW touches' if TOUCH_MODE else 'CLOSE below'} SMA{SMA_LEN} · enter E−{ENTRY_OFFSET} close")
print("=" * 100)
print("\n  COVERAGE — read this before any result. Thin coverage is the binding constraint.\n")
ev, notes = build_events()

if len(ev) == 0:
    raise SystemExit("\n⛔ No usable events. Almost always yfinance earnings coverage — check the ⛔ rows.")

print(f"\n  → {len(ev)} usable earnings events across {ev.ticker.nunique()} names, "
      f"{ev.edate.min().date()} → {ev.edate.max().date()}")

# ── the suppression distribution: is 70% rare, or is it most of the sample?
print("\n" + "=" * 100)
print("  WHERE DOES THE 70% BAR ACTUALLY SIT? (distribution of the suppressed fraction)")
print("=" * 100)
q = ev["frac"].quantile([.1,.25,.5,.75,.9])
print("  deciles: " + "  ".join(f"p{int(k*100)}={v:.0%}" for k, v in q.items()))
for th in SUPPRESS_SWEEP:
    n = (ev["frac"] >= th).sum()
    print(f"     ≥{th:.0%} suppressed: {n:>4} events ({n/len(ev):>4.0%} of sample)  {'█'*int(40*n/len(ev))}")

# ── the headline table: BOTH sweeps, with n printed everywhere
print("\n" + "=" * 100)
print(f"  THE SWEEP — entry E−{ENTRY_OFFSET} → exit E+1.  n IS SHOWN AT EVERY CELL ON PURPOSE:")
print("  a gate that rejects its way to a good number is the failure mode, not the result.")
print("=" * 100)
for th in SUPPRESS_SWEEP:
    trig = ev[ev["frac"] >= th]
    print(f"\n  ── suppressed ≥ {th:.0%}   ({len(trig)} events before the vol gate)")
    if len(trig) == 0:
        print("     none"); continue
    for vg in VOL_SWEEP:
        sub = trig if vg == 0 else trig[trig["rvpct"] >= vg]
        lab = "no vol gate" if vg == 0 else f"RV pctile ≥ {vg:.0%}"
        print(line(lab, stat_block(sub, 1)))

# ── THE CONTROLS. Without these the table above is unreadable.
print("\n" + "=" * 100)
print("  CONTROL LEGS — the comparison the result actually needs")
print("=" * 100)
base = ev[ev["frac"] < 0.70]
trig70 = ev[ev["frac"] >= 0.70]
print(line("ALL events (universe)", stat_block(ev, 1)))
print(line("TRIGGERED (≥70%)", stat_block(trig70, 1)))
print(line("NOT triggered (<70%)", stat_block(base, 1)))
if len(trig70) > 1 and len(base) > 1:
    d = trig70["ret_1"].mean() - base["ret_1"].mean()
    sp = math.sqrt(trig70["ret_1"].var()/len(trig70) + base["ret_1"].var()/len(base))
    print(f"\n  triggered − not-triggered = {d:+.2%}   t ≈ {d/sp if sp else float('nan'):+.2f}")
    print("  ⚠️ |t| < 2 on a sample this size is noise. Say so out loud rather than reading the sign.")

# ── holding-horizon shape
print("\n" + "=" * 100)
print("  HOLD HORIZON — is 'through earnings' the right exit, or is the move before/after the print?")
print("=" * 100)
for k in EXIT_OFFSETS:
    s = stat_block(trig70, k)
    print(line(f"triggered ≥70%, exit E+{k}", s))

# ── per-name, so one ticker's run cannot masquerade as an effect
print("\n" + "=" * 100)
print("  PER-NAME (triggered ≥70%) — concentration check")
print("=" * 100)
if len(trig70):
    g = trig70.groupby("ticker")["ret_1"].agg(["count","mean","median"]).sort_values("mean", ascending=False)
    for t, r in g.iterrows():
        print(f"     {t:<7} n={int(r['count']):>3}  mean {r['mean']:>+7.2%}  med {r['median']:>+7.2%}")
    top = g["mean"].idxmax()
    ex = trig70[trig70.ticker != top]
    print(f"\n  drop the best name ({top}): " + (line("", stat_block(ex, 1)).strip() or "—"))
    print("  If the effect dies when one name leaves, it was that name — not the setup.")

# ── LIVE SCREEN, with REAL implied vol (the thing the backtest could not use)
print("\n" + "=" * 100)
print("  LIVE — who is in the setup NOW, with ACTUAL implied vol from the chain")
print("  IV/RV > 1 = options priced above what the stock has been doing = 'elevated' in the sense")
print("  that matters. This is the real gate; the backtest above only had the RV half of it.")
print("=" * 100)
def atm_iv(tkr, spot):
    try:
        tk = yf.Ticker(tkr); exps = tk.options
        if not exps: return np.nan, None
        exp = exps[0]
        for e in exps:   # first expiry at least a week out
            if (pd.Timestamp(e) - pd.Timestamp.today()).days >= 7: exp = e; break
        ch = tk.option_chain(exp)
        cs = ch.calls.dropna(subset=["impliedVolatility"])
        if len(cs) == 0: return np.nan, exp
        k = (cs["strike"] - spot).abs().idxmin()
        return float(cs.loc[k, "impliedVolatility"]), exp
    except Exception:
        return np.nan, None

print(f"  {'tkr':<6}{'days→ER':>9}{'suppress%':>11}{'RVpct':>8}{'RV20':>8}{'ATM IV':>9}{'IV/RV':>8}  status")
print("  " + "-" * 84)
for t in UNIVERSE:
    df, err = load_px(t, years=2)
    if err: continue
    eds, _ = load_earnings(t)
    try:
        nxt = yf.Ticker(t).calendar
        nd = None
        if isinstance(nxt, dict) and nxt.get("Earnings Date"):
            nd = pd.Timestamp(sorted(nxt["Earnings Date"])[0])
        elif hasattr(nxt, "loc") and "Earnings Date" in getattr(nxt, "index", []):
            nd = pd.Timestamp(nxt.loc["Earnings Date"][0])
    except Exception:
        nd = None
    time.sleep(PAUSE)
    if nd is None: continue
    dte = int(np.busday_count(pd.Timestamp.today().date(), nd.date()))
    if not (0 < dte <= LOOKBACK_START): continue
    i_e = len(df) + dte                      # projected bar index of the print
    lo, hi = i_e - LOOKBACK_START, min(len(df), i_e - ENTRY_OFFSET)
    lo = max(lo, 0)
    if hi <= lo: continue
    w = df.iloc[lo:hi]
    below = (w["Low"] < w["SMA20"]) if TOUCH_MODE else (w["Close"] < w["SMA20"])
    frac = float(below.mean())
    spot = float(df["Close"].iloc[-1]); rv = float(df["RV20"].iloc[-1])
    rvp = df["RVpct"].iloc[-1]; rvp = float(rvp) if pd.notna(rvp) else np.nan
    iv, _ = atm_iv(t, spot); time.sleep(PAUSE)
    ratio = iv / rv if (rv and not np.isnan(iv)) else np.nan
    st = "SETUP" if frac >= 0.70 else ("watch" if frac >= 0.55 else "")
    if st == "SETUP" and not np.isnan(ratio) and ratio < 1.0: st = "SETUP (IV not rich)"
    print(f"  {t:<6}{dte:>9}{frac:>10.0%}{rvp:>8.0%}{rv:>8.0%}"
          f"{(f'{iv:.0%}' if not np.isnan(iv) else '—'):>9}"
          f"{(f'{ratio:.2f}' if not np.isnan(ratio) else '—'):>8}  {st}")
    if dte > ENTRY_OFFSET:
        print(f"         ↑ window still OPEN — decision bar is E−{ENTRY_OFFSET}, "
              f"{dte-ENTRY_OFFSET} trading days away. This % can still move.")

print("\n" + "=" * 100)
print("  HOW TO READ THIS — the limits, stated so they are not rediscovered later")
print("  · NO HOLDOUT, TWO SWEPT AXES. The best cell in the sweep was chosen by the data that scored")
print("    it. Read the SHAPE (does it improve monotonically with the gate?) and the CONTROL legs.")
print("    A gate that only looks good at one threshold with n=6 is a coincidence with a label.")
print("  · THE BACKTEST'S VOL GATE IS REALISED VOL, NOT IMPLIED. There is no free historical IV.")
print("    RV says what the stock DID; IV says what the market EXPECTS — and 'expects a big move' is")
print("    the actual thesis. The live table above is the only place real IV appears.")
print("  · SURVIVORSHIP: the universe is today's basket. Every name survived to today by construction.")
print("  · THE SETUP IS NEARLY A DOWNTREND DEFINITION. 'Below its 20-SMA 70% of 30 days' selects")
print("    beaten-down names almost tautologically, so this tests ONE specific claim: that the")
print("    earnings print reverses them. The not-triggered control is what separates the two.")
print("  · EARNINGS COVERAGE from yfinance is shallow and uneven; several names here IPO'd recently")
print("    (CRWV, NBIS, ARM, IREN). Sample size, not signal strength, is the binding constraint.")
print("=" * 100)
