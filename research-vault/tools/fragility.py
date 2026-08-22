#!/usr/bin/env python3
"""
fragility.py -- reads data/fragility/series/*.csv, scores each indicator against
ITS OWN history, and prints the dashboard. Also writes latest.json for the HTML
generator.

SCORING PHILOSOPHY (this is the part that can be wrong, so it is stated)
-----------------------------------------------------------------------
NO ABSOLUTE THRESHOLDS. Jake's own rule for swap spreads -- "don't use an
arbitrary X bps = crisis, regulation and issuance move the equilibrium" --
is applied to EVERY series here. Each indicator is scored two ways against
its own trailing 3 years:

  LEVEL   percentile rank of today's value
  RATE    percentile rank of the trailing 20-observation CHANGE

Status combines them, and RATE is weighted to fire first, because Jake's
transmission chain is a statement about SEQUENCE, not about levels.

  critical  level >=95th AND rate >=80th      (high and still accelerating)
  serious   level >=90th OR  rate >=95th
  warning   level >=75th OR  rate >=85th
  calm      otherwise

INVERTED series (bank C&I loans, deposits) are scored on 13-observation
percent change only, flipped -- for those, CONTRACTION is the stress.

STALENESS IS A FIRST-CLASS OUTPUT. A weekly series is not late at 6 days;
a daily series is late at 6 days. Each row carries its own expected cadence
and says so. A stale number that looks calm is the most dangerous cell on
any dashboard.
"""
import csv, json, os, sys
from datetime import date, datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(ROOT, "data", "fragility")
SER  = os.path.join(OUT, "series")

# key: (label, chart#, stage, unit, scale, cadence_days, inverted, note)
IND = {
 "ccc_oas":   ("CCC & lower OAS",              1, 1, "bp",   100, 4,  0, "the weakest borrowers"),
 "hy_oas":    ("High-yield OAS",               1, 1, "bp",   100, 4,  0, "general junk conditions"),
 "ccc_hy_gap":("CCC minus HY quality gap",     1, 1, "bp",   100, 4,  0, "CCC breaking underneath the index"),
 "bbb_oas":   ("BBB OAS",                      2, 2, "bp",   100, 4,  0, "junk problem -> corporate problem"),
 "ig_oas":    ("Investment-grade OAS",         2, 2, "bp",   100, 4,  0, "systemic corporate repricing"),
 "cp_spread": ("A2/P2 minus AA CP 90d",        8, 3, "bp",     1, 4,  0, "short-term unsecured corporate money"),
 "move":      ("MOVE index",                   4, 4, "pts",    1, 4,  0, "implied Treasury vol -- the collateral"),
 "rvol10":    ("10Y realized vol (PROXY)",     4, 4, "bp ann", 1, 4,  0, "MOVE proxy, realized not implied"),
 "dgs30":     ("30Y Treasury yield",           4, 4, "%",      1, 4,  0, "dangerous when rising WITH vol"),
 "pd_ust":    ("Dealer UST net position",      9, 5, "$mm",    1, 10, 0, "are dealers getting stuffed"),
 "pd_ftd":    ("Dealer UST fails to deliver",  9, 5, "$mm",    1, 10, 0, "settlement plumbing"),
 "pd_ftr":    ("Dealer UST fails to receive",  9, 5, "$mm",    1, 10, 0, "settlement plumbing"),
 "sofr_iorb": ("SOFR minus IORB",              7, 6, "bp",     1, 4,  0, "overnight secured funding"),
 "repo_ops":  ("Fed repo ops accepted",        7, 6, "$B",     1, 4,  0, "SRF take-up = plumbing tightening"),
 "ci_loans":  ("H.8 C&I loans",               10, 7, "$B",     1, 40, 1, "stress entering the bank channel"),
 "deposits":  ("H.8 bank deposits",           10, 7, "$B",     1, 10, 1, "falling deposits + falling C&I is ugly"),
 "vix":       ("VIX",                          0, 0, "pts",    1, 4,  0, "context only -- not a chain stage"),
}
STAGES = {
 1: "Low-quality credit (CCC/HY)",
 2: "Investment grade (BBB/IG)",
 3: "Corporate short-term funding (CP)",
 4: "Rates volatility / the collateral",
 5: "Dealers & Treasury absorption",
 6: "Repo & money-market plumbing",
 7: "Bank credit channel",
}
# Series whose LEVEL trends structurally -- a level percentile on these is an
# artifact of the trend, not a stress reading. The 30Y sits at the 99th
# percentile of 3 years because yields ROSE, not because today is stressed;
# dealer positions sit high because ISSUANCE is high. For these, status comes
# from RATE OF CHANGE ONLY. This is Jake's own swap-spread rule generalised:
# no arbitrary level threshold, watch for dislocation from the recent range.
DETREND = {"dgs30", "pd_ust", "pd_ftd", "pd_ftr", "ci_loans", "deposits"}

RANK = {"calm": 0, "warning": 1, "serious": 2, "critical": 3}
ICON = {"calm": "OK", "warning": "!", "serious": "!!", "critical": "!!!"}

def load(key):
    p = os.path.join(SER, f"{key}.csv")
    if not os.path.exists(p): return []
    out = []
    with open(p) as fh:
        for r in csv.DictReader(fh):
            try: out.append((r["date"], float(r["value"])))
            except (ValueError, TypeError): pass
    return out

def pctrank(xs, v):
    if not xs: return None
    return 100.0 * sum(1 for x in xs if x <= v) / len(xs)

def score(key, s):
    label, chart, stage, unit, scale, cadence, inv, note = IND[key]
    if len(s) < 30: return None
    cut = (date.today() - timedelta(days=365 * 3)).isoformat()
    hist = [(d, v) for d, v in s if d >= cut] or s
    vals = [v * scale for _, v in hist]
    last_d, last_v = s[-1][0], s[-1][1] * scale

    def chg(n):
        return (last_v - s[-1-n][1] * scale) if len(s) > n else None
    d1, d5, d20 = chg(1), chg(5), chg(20)

    if inv:
        # stress = CONTRACTION. Score 13-obs % change, flipped.
        pc = [100.0*(hist[i][1]-hist[i-13][1])/abs(hist[i-13][1])
              for i in range(13, len(hist)) if hist[i-13][1]]
        cur = (100.0*(s[-1][1]-s[-14][1])/abs(s[-14][1])) if len(s) > 14 and s[-14][1] else None
        lvl_p = None
        rate_p = (100 - pctrank(pc, cur)) if cur is not None else None
    else:
        lvl_p = pctrank(vals, last_v)
        ch = [vals[i]-vals[i-20] for i in range(20, len(vals))]
        rate_p = pctrank(ch, d20) if d20 is not None else None

    st = "calm"
    R = rate_p or 0
    if key in DETREND or inv:
        L = None                       # level says nothing; rate is the signal
        if   R >= 97: st = "critical"
        elif R >= 90: st = "serious"
        elif R >= 80: st = "warning"
    else:
        L = lvl_p or 0
        if   L >= 95 and R >= 80: st = "critical"
        elif L >= 90 or  R >= 95: st = "serious"
        elif L >= 75 or  R >= 85: st = "warning"

    age = (date.today() - datetime.strptime(last_d, "%Y-%m-%d").date()).days
    return {"key": key, "label": label, "chart": chart, "stage": stage,
            "unit": unit, "note": note, "inverted": bool(inv),
            "date": last_d, "value": round(last_v, 4),
            "d1": d1 and round(d1, 3), "d5": d5 and round(d5, 3),
            "d20": d20 and round(d20, 3),
            "level_pct": (None if (key in DETREND or inv) else
                          (lvl_p and round(lvl_p, 1))),
            "detrended": key in DETREND or bool(inv),
            "rate_pct": rate_p and round(rate_p, 1),
            "status": st, "n": len(s), "age_days": age,
            "stale": age > cadence,
            "spark": [round(v, 4) for v in vals[-120:]]}

def main():
    rows = [r for r in (score(k, load(k)) for k in IND) if r]
    meta = {}
    mp = os.path.join(OUT, "raw_meta.json")
    if os.path.exists(mp): meta = json.load(open(mp))

    # ladder: worst status per chain stage
    ladder = []
    for sn in sorted(STAGES):
        rs = [r for r in rows if r["stage"] == sn]
        worst = max((r["status"] for r in rs), key=lambda x: RANK[x]) if rs else "calm"
        ladder.append({"stage": sn, "name": STAGES[sn], "status": worst,
                       "n": len(rs), "lit": RANK[worst] >= 1})

    lit = [l for l in ladder if l["lit"]]
    if not lit:
        verdict = "NO STAGE LIT -- no evidence of a credit crack in the public data."
    elif len(lit) == 1:
        verdict = (f"ONE STAGE LIT (stage {lit[0]['stage']}: {lit[0]['name']}). "
                   "Localised repricing, not a chain.")
    else:
        verdict = (f"{len(lit)} STAGES LIT: " +
                   " -> ".join(f"{l['stage']}" for l in lit) +
                   ". Check whether they lit IN ORDER -- sequence is the signal.")

    payload = {"generated": datetime.now().astimezone().isoformat(timespec="seconds"),
               "verdict": verdict, "ladder": ladder, "rows": rows,
               "gaps": meta.get("gaps", []), "feed_errors": meta.get("errors", []),
               "stages": STAGES}
    with open(os.path.join(OUT, "latest.json"), "w") as fh:
        json.dump(payload, fh, indent=1)

    # ---- terminal view
    W = 96
    print("=" * W)
    print("  CREDIT / DEBT FRAGILITY DASHBOARD".ljust(70) + payload["generated"][:16])
    print("=" * W)
    print("\n  TRANSMISSION LADDER  (stress migrates downward; SEQUENCE is the signal)")
    for l in ladder:
        bar = "#" * RANK[l["status"]] if RANK[l["status"]] else "."
        print(f"   {l['stage']}  [{bar:<3}] {ICON[l['status']]:<4}"
              f" {l['name']:<38} ({l['n']} series)")
    print(f"\n  >> {verdict}\n")
    print(f"  {'indicator':<30}{'value':>11} {'unit':<8}{'chg1p':>10}{'chg20p':>11}"
          f"{'lvl%':>6}{'rate%':>7}  status")
    print("  (chg is in OBSERVATIONS not days -- weekly series: 1p = 1 week)")
    print("  " + "-" * (W - 4))
    cur = None
    for r in sorted(rows, key=lambda x: (x["stage"] or 99, -RANK[x["status"]])):
        if r["stage"] != cur:
            cur = r["stage"]
            print(f"  -- stage {cur}: {STAGES.get(cur,'context')}")
        f = lambda v: ("--" if v is None else (f"{v:+,.0f}" if abs(v) >= 1000 else f"{v:+,.2f}"))
        lvl = "  -" if r["level_pct"] is None else f"{r['level_pct']:.0f}"
        flag = "  STALE" if r["stale"] else ""
        print(f"  {r['label']:<30}{r['value']:>11,.2f} {r['unit']:<8}"
              f"{f(r['d1']):>10}{f(r['d20']):>11}"
              f"{lvl:>6}"
              f"{(r['rate_pct'] if r['rate_pct'] is not None else 0):>7.0f}"
              f"  {ICON[r['status']]:<4}{r['status']}{flag}")
    if payload["gaps"]:
        print(f"\n  KNOWN GAPS -- these charts are NOT in the data above:")
        for g in payload["gaps"]:
            print(f"   [{g['status']}] chart {g['chart']}: {g['name']}")
    if payload["feed_errors"]:
        print(f"\n  FEED ERRORS: {[e['key'] for e in payload['feed_errors']]}")
    print()

if __name__ == "__main__":
    main()
