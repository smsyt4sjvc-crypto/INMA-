#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════════════════════════════
#  F19 — SHELL vs FIT-OUT: dating the buildout with a SERIES instead of an adjective
#
#  The flag (ai-capex-cycle.md:L2076, registered 2026-08-05, never run until now):
#    "WHERE IN THE CYCLE IS THE BUILDOUT? If the shells were built 2024-25 and 2026 is the
#     fill, data-center CONSTRUCTION spending should be DECELERATING while electrical-
#     equipment and semiconductor ORDERS ACCELERATE. A clean divergence DATES the buildout."
#
#  Commissioned by Jake 2026-08-11 to test his own claim that the buildout is "in its
#  adolescence at best." Adolescence is unfalsifiable in real time. THIS IS NOT:
#     SHELL phase   → construction accelerating, orders lagging        (early)
#     FIT-OUT phase → construction decelerating, orders accelerating   (mid/late)
#     BOTH ROLLING  → construction AND orders decelerating             (over)
#     BOTH RISING   → genuinely early, capacity not yet poured         (earliest)
#
#  ⚠️ THE SERIES IDs ARE PROBED AT RUNTIME, NOT ASSUMED. FRED was unreachable from the
#  container this was written in, so rather than ship guessed IDs the cell tries a candidate
#  list, prints exactly what resolved, and builds from that. If a leg finds nothing it says
#  so loudly instead of drawing a chart from half the data.
#
#  COMPLETE CELL — paste the whole thing into Colab and run. Tier 0: free, keyless, no tokens.
# ═══════════════════════════════════════════════════════════════════════════════════════════
import io, urllib.request, warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

warnings.filterwarnings("ignore")

# ═══════════════════════════ CONFIG ═════════════════════════════════════════════════════════
START   = "2015-01-01"    # long enough to see a prior cycle, not just this one
SMOOTH  = 3               # months of smoothing on the growth lines (M3/C30 are noisy)
# ════════════════════════════════════════════════════════════════════════════════════════════

UA = {"User-Agent": "Mozilla/5.0"}

# ── Candidate FRED IDs per leg. Ordered best-guess first; the probe keeps ALL that resolve.
CANDIDATES = {
    "CONSTRUCTION — data centre (the shell leg, most specific first)": [
        ("TLDCCONS",  "Total construction: data center"),
        ("PRDCCONS",  "Private construction: data center"),
        ("TLOFCONS",  "Total construction: office (data centres sit inside this)"),
        ("PROFCONS",  "Private construction: office"),
        ("OFFCONS",   "Construction: office"),
        ("TLCOMCONS", "Total construction: commercial"),
        ("PNRESCONS", "Private nonresidential construction (fallback aggregate)"),
        ("TLPRVCONS", "Total private construction (fallback aggregate)"),
        ("TTLCONS",   "Total construction (last-resort aggregate)"),
    ],
    "ORDERS — computers & electronics (the fit-out leg)": [
        ("A34SNO",   "New orders: computers & electronic products (NAICS 334)"),
        ("A34SVS",   "Shipments: computers & electronic products"),
        ("NEWORDER", "New orders: nondefense capital goods ex aircraft"),
        ("AMTMNO",   "New orders: total manufacturing"),
        ("UMTMNO",   "New orders: total manufacturing (unfilled/alt)"),
    ],
    "ORDERS — electrical equipment (the power/gear leg)": [
        ("A35SNO", "New orders: electrical equipment, appliances & components (NAICS 335)"),
        ("A35SVS", "Shipments: electrical equipment"),
        ("A31SNO", "New orders: primary metals (adjacent input)"),
    ],
}

def fred(sid, timeout=45):
    """Keyless FRED pull. Tries the graph CSV then the raw text endpoint."""
    for url, kind in ((f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}", "csv"),
                      (f"https://fred.stlouisfed.org/data/{sid}.txt", "txt")):
        try:
            raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA),
                                         timeout=timeout).read().decode()
        except Exception:
            continue
        try:
            if kind == "csv":
                df = pd.read_csv(io.StringIO(raw))
                df.columns = ["date", "value"]
                df["value"] = pd.to_numeric(df["value"], errors="coerce")
                s = df.dropna().set_index(pd.to_datetime(df.dropna()["date"]))["value"]
            else:
                rows = [l.split() for l in raw.strip().split("\n") if l[:4].isdigit()]
                s = pd.Series({pd.Timestamp(r[0]): float(r[1]) for r in rows
                               if r[1] not in (".", "")})
            s = s[~s.index.duplicated()].sort_index()
            if len(s) > 24:
                return s
        except Exception:
            continue
    return None

print("=" * 94)
print("  F19 — SHELL vs FIT-OUT.  Probing FRED for the resolver series (no API key needed)")
print("=" * 94)

found = {}
for leg, cands in CANDIDATES.items():
    print(f"\n── {leg}")
    hits = []
    for sid, label in cands:
        s = fred(sid)
        if s is None:
            print(f"   ✗ {sid:<10} —")
            continue
        s = s[s.index >= START]
        if len(s) < 24:
            print(f"   ✗ {sid:<10} resolved but too short after {START}")
            continue
        print(f"   ✓ {sid:<10} {s.index[0].date()} → {s.index[-1].date()}  "
              f"n={len(s):<4} last={s.iloc[-1]:,.0f}   {label}")
        hits.append((sid, label, s))
    if hits:
        found[leg] = hits
    else:
        print(f"   ⚠️ NOTHING RESOLVED FOR THIS LEG — the chart below will be incomplete.")
        print(f"      Check the series IDs on fred.stlouisfed.org and add them to CANDIDATES.")

if not found:
    raise SystemExit("\n⛔ No series resolved at all. FRED unreachable or every ID is wrong — "
                     "nothing is charted, because half a chart here would be worse than none.")

# ── pick the most specific resolved series per leg (first hit = best guess)
picked = {leg: hits[0] for leg, hits in found.items()}
print("\n" + "=" * 94)
print("  USING (most specific resolved series per leg):")
for leg, (sid, label, s) in picked.items():
    print(f"   {leg.split('—')[0].strip():<14} {sid:<10} {label}")
print("  ⚠️ If a leg fell back to an AGGREGATE (total private / total manufacturing), the")
print("     divergence test is DILUTED — an aggregate contains the other leg inside it.")
print("=" * 94)

# ══════════════════════════════ THE F19 TEST ════════════════════════════════════════════════
def growth(s, months=12):
    s = s.resample("MS").last().interpolate(limit_area="inside")
    return (s / s.shift(months) - 1) * 100

def ann3(s):
    s = s.resample("MS").last().interpolate(limit_area="inside")
    return ((s / s.shift(3)) ** 4 - 1) * 100

print("\n  THE TEST — is each leg ACCELERATING or DECELERATING?")
print(f"  {'leg':<16}{'level':>14}{'YoY %':>9}{'3m ann %':>11}{'YoY 6m ago':>12}{'  direction'}")
print("  " + "─" * 88)
rows = {}
for leg, (sid, label, s) in picked.items():
    g, a = growth(s), ann3(s)
    g_now = g.dropna().iloc[-1] if g.notna().any() else np.nan
    g_old = g.dropna().iloc[-7] if g.notna().sum() > 7 else np.nan
    a_now = a.dropna().iloc[-1] if a.notna().any() else np.nan
    dirn = ("ACCELERATING" if g_now > g_old + 0.5 else
            "decelerating" if g_now < g_old - 0.5 else "flat")
    short = leg.split("—")[0].strip() + ("/dc" if "data" in label else "")
    rows[leg] = dict(g=g, a=a, s=s, sid=sid, label=label, g_now=g_now, g_old=g_old, dirn=dirn)
    print(f"  {short:<16}{s.iloc[-1]:>14,.0f}{g_now:>9.1f}{a_now:>11.1f}{g_old:>12.1f}"
          f"   {dirn}")

con_key = next((k for k in rows if k.startswith("CONSTRUCTION")), None)
ord_key = next((k for k in rows if "computers" in k), None)
print("\n  " + "─" * 88)
if con_key and ord_key:
    c, o = rows[con_key], rows[ord_key]
    spread = (o["g"] - c["g"]).dropna()
    print(f"  SPREAD (orders YoY − construction YoY): {spread.iloc[-1]:+.1f}pp now  ·  "
          f"{spread.iloc[-7]:+.1f}pp six months ago  ·  {spread.iloc[-13]:+.1f}pp a year ago"
          if len(spread) > 13 else f"  SPREAD: {spread.iloc[-1]:+.1f}pp")
    # ⚠️ THE VERDICT KEYS OFF GROWTH LEVELS AND THE SPREAD, *NOT* 6-MONTH ACCELERATION.
    # Earlier draft used each leg's accel and mislabelled a regime that changed >6m ago as
    # "both rolling over" while the spread sat at +12pp of obvious fit-out. Caught by the
    # synthetic test. Acceleration only fires during the TRANSITION; the spread persists.
    cg, og, sp_now = c["g_now"], o["g_now"], spread.iloc[-1]
    verdict = (
        "BOTH ROLLING OVER → the cycle is not early on either leg" if cg < 0 and og < 0 else
        "FIT-OUT → shells are done, the fill is running" if sp_now > 3 and og > 0 else
        "SHELL → still pouring concrete, the fill has not started" if sp_now < -3 and cg > 0 else
        "BOTH RISING TOGETHER → genuinely early, or the legs are not separable in this data")
    print(f"  ⇒ CONFIGURATION READS: {verdict}")
    print(f"     (construction {cg:+.1f}% YoY · orders {og:+.1f}% YoY · spread {sp_now:+.1f}pp)")
    if c["dirn"] != "flat" or o["dirn"] != "flat":
        print(f"     6m acceleration, secondary: construction {c['dirn']} · orders {o['dirn']}")

    # ── THE FAST LINE. A 12-month YoY CANNOT SEE A TURN YOUNGER THAN ~6 MONTHS: 9 of its 12
    # months are still the old regime. The synthetic test proved this — a 3-month-old, obvious
    # fit-out turn read as "both rising together." So run the same spread on 3m-annualised
    # growth and report DISAGREEMENT as its own finding rather than picking a winner.
    sp_fast = (o["a"] - c["a"]).dropna()
    if len(sp_fast):
        f_now = sp_fast.iloc[-1]
        print(f"\n     FAST LINE (3m annualised): spread {f_now:+.1f}pp vs YoY {sp_now:+.1f}pp")
        if abs(f_now - sp_now) > 6 and np.sign(f_now) != np.sign(sp_now):
            print(f"     ⚠️⚠️ THE TWO HORIZONS DISAGREE IN SIGN — that is the signature of a TURN")
            print(f"        IN PROGRESS that the YoY has not absorbed yet. The 3m leads; the YoY")
            print(f"        confirms in ~6 months. Treat the verdict above as STALE and watch this.")
        elif abs(f_now - sp_now) > 6:
            print(f"     ⚠️ Same sign, different magnitude — the phase is INTENSIFYING if |3m| >"
                  f" |YoY|, fading if smaller. Here: "
                  f"{'intensifying' if abs(f_now) > abs(sp_now) else 'fading'}.")
        else:
            print(f"     Both horizons agree — the reading is stable, not a fresh turn.")
    print("  ⚠️ This DESCRIBES the two series. It is not a top-call or a timing claim —")
    print("     per the vault's WARNING-vs-TRIGGER rule, a phase reading shades odds and")
    print("     times nothing. What it kills is the ADJECTIVE, in both directions.")
else:
    print("  ⚠️ Cannot compute the spread — one leg did not resolve. Verdict withheld.")

# ═══════════════════════════════════ CHARTS ═════════════════════════════════════════════════
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.25,
                     "axes.spines.top": False, "axes.spines.right": False})
COL = {"CONSTRUCTION": "#b45309", "ORDERS — computers": "#2563eb", "ORDERS — electrical": "#059669"}
def col(leg):
    for k, v in COL.items():
        if leg.startswith(k[:12]):
            return v
    return "#666"

fig, ax = plt.subplots(3, 1, figsize=(12, 11), dpi=110)

for leg, r in rows.items():
    s = r["s"].resample("MS").last()
    ax[0].plot(s.index, s / s.dropna().iloc[0] * 100, lw=2.3, color=col(leg),
               label=f'{leg.split("—")[0].strip()} [{r["sid"]}]')
ax[0].axhline(100, color="#111", lw=0.8, alpha=0.4)
ax[0].set_title(f"LEVELS, indexed to {START[:7]} = 100", fontsize=12.5, weight="bold", loc="left")
ax[0].legend(frameon=False, fontsize=9.5)
ax[0].set_ylabel("index")

for leg, r in rows.items():
    g = r["g"].rolling(SMOOTH).mean()
    ax[1].plot(g.index, g.values, lw=2.3, color=col(leg),
               label=f'{leg.split("—")[0].strip()}  ({r["g_now"]:+.1f}% YoY)')
ax[1].axhline(0, color="#111", lw=0.9)
ax[1].yaxis.set_major_formatter(mtick.PercentFormatter())
ax[1].set_title(f"YoY GROWTH ({SMOOTH}m smoothed) — THE F19 TEST: does construction roll while "
                f"orders accelerate?", fontsize=12.5, weight="bold", loc="left")
ax[1].legend(frameon=False, fontsize=9.5)
ax[1].set_ylabel("YoY")

if con_key and ord_key:
    sp = (rows[ord_key]["g"] - rows[con_key]["g"]).rolling(SMOOTH).mean().dropna()
    ax[2].plot(sp.index, sp.values, lw=2.4, color="#7c3aed")
    ax[2].fill_between(sp.index, sp.values, 0, where=sp.values > 0, color="#7c3aed", alpha=0.14)
    ax[2].fill_between(sp.index, sp.values, 0, where=sp.values < 0, color="#b45309", alpha=0.14)
    ax[2].axhline(0, color="#111", lw=0.9)
    ax[2].yaxis.set_major_formatter(mtick.PercentFormatter())
    ax[2].set_title("SPREAD: orders YoY − construction YoY.  "
                    "PURPLE (>0) = fit-out leading · BROWN (<0) = shell leading",
                    fontsize=12.5, weight="bold", loc="left")
    ax[2].set_ylabel("pp")
else:
    ax[2].text(0.5, 0.5, "spread unavailable — a leg did not resolve",
               ha="center", va="center", fontsize=12, color="#b45309")
    ax[2].set_axis_off()
plt.tight_layout(); plt.show()

print("\n" + "=" * 94)
print("  READING NOTES")
print("  · A DIVERGENCE dates the buildout; a co-movement does not. If both legs move")
print("    together the test is silent — say so rather than reading a phase into noise.")
print("  · Census C30 construction is revised HARD. Read the trend, never the last point.")
print("  · If the construction leg fell back to an office/commercial/private aggregate, data")
print("    centres are a minority of it and the signal is diluted toward zero — i.e. the test")
print("    gets HARDER to pass, not easier. A divergence that survives dilution is stronger.")
print("  · Orders are NOMINAL. Part of any acceleration is the price inflation the vault has")
print("    logged in the supply chain (5-25% PCB assembly, 15-45% bare boards). Volume growth")
print("    is SMALLER than these lines. ⬜ deflating them is the next refinement.")
print("=" * 94)
