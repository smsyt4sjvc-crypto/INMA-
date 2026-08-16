#!/usr/bin/env python3
# =============================================================================
#  DURABLE-VALUE SCREEN — a POINT-IN-TIME backtest of "cheap, but for a good reason"
#  Built 2026-08-15, rebuilt 2026-08-16 after three EPS bugs. Paste and run.
#
#  THE QUESTION
#  ------------
#  A low price-to-earnings (P/E) ratio has two very different causes:
#    (a) the price is depressed and the earnings are normal   -> possibly cheap
#    (b) the EARNINGS are temporarily inflated and the price is normal -> a TRAP
#  Case (b) is the whole argument at single-stock scale: a cyclical at peak
#  earnings prints its LOWEST multiple exactly when it is most expensive.
#
#  Jake's spec as filters: low P/E, where BOTH the P and the E sit in
#  historically tolerated ranges -- not where one of them is doing all the work.
#  No quarter of crazy earnings, no pulled-forward depreciation, no acquisition
#  eating the earnings. Good balance sheet. Price above its 50- and 200-day
#  moving averages (that is what excludes the falling knife).
#
#  ⛔ THE TWO THINGS THAT WOULD INVALIDATE THIS, STATED UP FRONT
#  -------------------------------------------------------------
#  1. LOOK-AHEAD BIAS. Using today's fundamentals for a 2021 screen is cheating.
#     FIXED: every EDGAR fact carries a `filed` date and this script uses ONLY
#     facts filed BEFORE the formation date. That is real point-in-time.
#  2. SURVIVORSHIP BIAS. The universe is TODAY'S index. Every company that went
#     bankrupt, got acquired, or shrank out of the index between 2021 and now is
#     missing -- and those are disproportionately the failures.
#     NOT FIXED. It biases every return in this script UPWARD, including the
#     benchmark. Read the SPREAD vs the benchmark, never the absolute return.
#
#  WHY THE CONTROL GROUP IS THE POINT: the script runs the screen WITH and
#  WITHOUT the durability filter. If durable-E cheap beats naive cheap, the
#  filter is doing work. If it does not, the idea is wrong and we say so.
#
#  ⛔⛔ THE THREE EPS BUGS THIS FILE EXISTS TO KILL (found 2026-08-16, all in
#  one hand-check of five names -- the run BEFORE this one was unreportable)
#  ---------------------------------------------------------------------------
#  A. QUARTERLY FACTS WEARING ANNUAL CLOTHES. Valero's 10-K tags its quarterly
#     EPS footnote with form="10-K". Keying on `end` alone lets Q4-2019 (end
#     2019-12-31, val 2.58) silently OVERWRITE FY-2019 (same end, val 5.84).
#     VLO's "annual EPS history" printed as [2.58, -4.54, 3.07, -1.14, -0.88]:
#     five CONSECUTIVE QUARTERS masquerading as five YEARS. Chevron's 10-K does
#     not tag quarterly data, so Chevron looked fine.
#     ⇒ THE BUG WAS COMPANY-DEPENDENT. Spot-checking one name could not find it.
#  B. YEAR-TO-DATE MIXED WITH DISCRETE QUARTERS. A Q2 10-Q carries BOTH the
#     3-month figure and the 6-month figure, and `fp` says "Q2" for both.
#     Summing four rows off the `fp` label mixes bases and double-counts.
#  C. THE STRUCTURAL ONE: Q4 DISCRETE EPS IS NEVER IN A 10-Q. It exists only in
#     the 10-K, and only for filers that tag it. So "sum four 10-Q quarters" can
#     NEVER build a trailing twelve months that spans a fiscal year-end. That is
#     not patchable by filtering forms.
#
#  ⇒ THE FIX, AND IT IS THE ONLY CONSTRUCTION THAT WORKS ON WHAT EDGAR ACTUALLY
#    PUBLISHES: classify every fact by the SPAN BETWEEN ITS start AND end DATES,
#    never by its form or fp label. Then build the trailing twelve months by
#    ARITHMETIC ON CUMULATIVE PERIODS:
#
#        TTM = latest FY annual
#            + current-FY cumulative through period P
#            - prior-FY cumulative through the SAME period P
#
#    Verified by hand against the raw facts, formation 2021-08-16:
#      CVX  -2.96 + 2.32 - (-2.51) = +1.87  -> P/E 54.0   (was: nan)
#      VLO  -3.50 + (-1.34) - (-1.48) = -3.36 -> loss     (was: P/E 109.4)
#    Both are RIGHT, and both correctly DROP OUT of a cheapness screen. The old
#    code showed Valero as a 109x "value" name.
# =============================================================================

import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from statistics import median

# ----------------------------------------------------------------- PARAMETERS
FORMATION = "2021-08-16"      # 5 years back
HOLD_END  = "2026-08-14"      # last completed session
SEC_UA    = {"User-Agent": "INMA Research contact@example.com"}   # SEC requires a real UA
YF_UA     = {"User-Agent": "Mozilla/5.0"}

PE_MAX          = 15.0    # "low P/E"
DURABLE_LO      = 0.70    # TTM EPS must be >= 0.70x the multi-year median  (not collapsed)
DURABLE_HI      = 1.60    # ...and <= 1.60x                                  (not a spike)
MIN_YEARS       = 4       # need this many annual EPS prints for a median to mean anything
MAX_DEBT_EQUITY = 1.50    # balance sheet
MIN_CURRENT     = 1.00    # current ratio
REQUIRE_SMA     = True    # price above BOTH the 50d and 200d at formation
MAX_TTM_STALE   = 200     # days: a TTM built from a bare annual older than this is unusable

CACHE = os.environ.get("DVS_CACHE", "/tmp/dvs_cache")

# ------------------------------------------------------------------- PLUMBING
def _get(url, headers, tries=3, pause=0.35):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=45) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as e:
            if e.code in (404, 403):
                return None
            time.sleep(pause * (i + 1))
        except Exception:
            time.sleep(pause * (i + 1))
    return None


def _cached(key, fn):
    """EDGAR companyfacts blobs run to tens of megabytes. Cache them so a
    re-run after a parameter change costs no network and no SEC goodwill."""
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, key + ".json")
    if os.path.exists(path):
        try:
            with open(path) as fh:
                return json.load(fh)
        except Exception:
            pass
    d = fn()
    if d is not None:
        try:
            with open(path, "w") as fh:
                json.dump(d, fh)
        except Exception:
            pass
    return d


def sp500_tickers():
    """Ticker -> CIK. ⚠️ NOT point-in-time -- see the survivorship note."""
    d = _cached("_tickers", lambda: _get("https://www.sec.gov/files/company_tickers.json", SEC_UA))
    if not d:
        return {}
    return {v["ticker"]: str(v["cik_str"]).zfill(10) for v in d.values()}


def prices(ticker):
    """Daily closes AND the split history.

    ⛔ THE BUG THIS EXISTS TO KILL, caught on the first smoke test: Yahoo's
    closes are SPLIT-ADJUSTED BACKWARDS. EDGAR's EPS is AS-REPORTED at the time
    and is NOT. Divide one by the other and a stock that later split 10:1 shows
    a P/E ten times too low. The smoke test printed NVDA at 2.6x and GOOGL at
    1.7x in Aug-2021 -- both nonsense, both caused by exactly this.

    So: return the adjusted series AND the AS-TRADED price, which is the only
    thing comparable to a filed EPS.
    """
    def fetch():
        return _get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
                    f"?range=10y&interval=1d&events=split", YF_UA)
    d = _cached("px_" + ticker.replace("/", "_"), fetch)
    try:
        r = d["chart"]["result"][0]
        splits = []
        for s in (r.get("events", {}).get("splits") or {}).values():
            splits.append((datetime.fromtimestamp(s["date"], timezone.utc).strftime("%Y-%m-%d"),
                           s["numerator"] / s["denominator"]))
        splits.sort()
        out = []
        for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]):
            if c is None:
                continue
            dt = datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%d")
            f = 1.0                                     # cumulative factor of splits AFTER this date
            for sd, ratio in splits:
                if sd > dt:
                    f *= ratio
            out.append((dt, c, c * f))                  # (date, adjusted, AS-TRADED)
        return out
    except Exception:
        return []


def px_on(series, date, traded=False):
    """Last close on or before `date`.
    traded=False -> split-ADJUSTED (use for RETURNS, which must be adjusted).
    traded=True  -> AS-TRADED     (use for the P/E, which must match filed EPS)."""
    i = 2 if traded else 1
    prior = [row[i] for row in series if row[0] <= date]
    return prior[-1] if prior else None


def sma(series, date, n):
    """SMA on the ADJUSTED series -- a split must not create a fake trend break."""
    prior = [row[1] for row in series if row[0] <= date]
    return sum(prior[-n:]) / n if len(prior) >= n else None


def edgar_facts(cik):
    return _cached("cf_" + cik,
                   lambda: _get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", SEC_UA))


def splits_of(ticker):
    """Split events (date, ratio) from the same cached Yahoo blob the prices use."""
    def fetch():
        return _get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
                    f"?range=10y&interval=1d&events=split", YF_UA)
    d = _cached("px_" + ticker.replace("/", "_"), fetch)
    try:
        ev = (d["chart"]["result"][0].get("events", {}).get("splits") or {}).values()
        out = [(datetime.fromtimestamp(s["date"], timezone.utc).strftime("%Y-%m-%d"),
                s["numerator"] / s["denominator"]) for s in ev]
        return sorted(out)
    except Exception:
        return []


# ------------------------------------------------------- THE EPS LAYER (rebuilt)
def _days(a, b):
    return (datetime.fromisoformat(b) - datetime.fromisoformat(a)).days


def eps_facts(facts, asof, splits=()):
    """Every diluted-EPS fact FILED STRICTLY BEFORE `asof`, tagged with the true
    length of the period it covers, and restated onto ONE share basis.

    The `filed` filter is the line that makes the whole backtest honest -- drop
    it and you are fitting on data nobody had.
    The `span` field is the line that makes the EPS honest -- see bugs A/B/C.

    ⛔ BUG D, THE SPLIT BUG A SECOND TIME, INSIDE THE EPS HISTORY ITSELF.
    EDGAR restates comparatives for a split only in filings made AFTER it, so a
    single company's history is MIXED-BASIS. Apple's annual list came back as
        [9.22, 8.31, 9.21, 2.98, 2.97, 3.28]
    -- the first three pre-split as-reported, the next two EDGAR's post-split
    restatements of 11.91 and 11.89 (the 4:1 of Aug-2020). The MEDIAN of that
    list is not a number about anything, and the median is what the durability
    ratio divides by.

    ⇒ Adjust each fact by the splits that fell between ITS OWN `filed` DATE and
      the formation date -- the exact mirror of how the price series is adjusted
      by the splits after each price date. A fact filed after a split already
      reflects it; a fact filed before it does not. Everything then sits on the
      basis in effect AT FORMATION, which is the basis of the as-traded price.
      Apple becomes [2.31, 2.08, 2.30, 2.98, 2.97, 3.28] -- one basis, and its
      durability goes 0.88 -> 1.94, correctly reading 2021 as a SPIKE.
    """
    us = facts.get("facts", {}).get("us-gaap", {})
    node = us.get("EarningsPerShareDiluted") or us.get("EarningsPerShareBasicAndDiluted")
    if not node:
        return []
    rows = []
    for u in node.get("units", {}).get("USD/shares", []):
        if not u.get("filed") or u["filed"] >= asof or u.get("val") is None or not u.get("start"):
            continue
        f = 1.0
        for sd, ratio in splits:                # splits between the filing and formation
            if u["filed"] < sd <= asof:
                f *= ratio
        rows.append(dict(start=u["start"], end=u["end"], val=u["val"] / f,
                         raw=u["val"], adj=f, filed=u["filed"], form=u.get("form", ""),
                         span=_days(u["start"], u["end"])))
    rows.sort(key=lambda r: (r["end"], r["filed"]))
    return rows


def _dedupe(rows):
    """Latest FILING wins for a given (start, end) -- that is a restatement,
    and the point-in-time investor would have seen the restated number."""
    by = {}
    for r in rows:
        by[(r["start"], r["end"])] = r
    return sorted(by.values(), key=lambda r: r["end"])


def annual_eps(facts, asof, splits=()):
    """Annual diluted EPS history, selected BY SPAN (340-400 days), never by form.

    ⛔ Selecting by form="10-K" is what produced VLO's five-quarters-as-five-years
    (bug A). A 10-K contains quarterly facts too; a fiscal year is 365 days long
    and that is the only reliable signal in the data."""
    return _dedupe([r for r in eps_facts(facts, asof, splits) if 340 <= r["span"] <= 400])


def ttm_eps(facts, asof, splits=()):
    """Trailing twelve months diluted EPS, point-in-time.

    Builds EVERY construction that the data supports and returns THE FRESHEST --
    not the first one that happens to work:
      cum:    latest FY + current-FY-to-date - prior-FY-to-same-date.
              The only method that spans a fiscal year-end, because Q4 discrete
              EPS is never published in a 10-Q (bug C).
      4q:     four consecutive discrete quarters, verified consecutive BY DATE
              (each start within 5 days of the prior end, total span 350-380).
              Not by counting rows off an `fp` label (bug B).
      annual: the bare latest fiscal year.

    ⚠️ WHY FRESHEST, NOT A FIXED LADDER: Procter & Gamble has a June year-end and
    filed its FY2021 10-K on 2021-08-05, eleven days before formation. A ladder
    that tries `cum` first finds no post-year-end quarter yet, falls through to
    `4q`, and returns a window ending 31-MAR -- 138 days stale -- when a 47-day-old
    full fiscal year was sitting right there. Freshest-wins fixes every fiscal
    calendar at once instead of special-casing them.

    Returns (ttm, annual_list, method, stale_days).
    """
    rows = eps_facts(facts, asof, splits)
    ann = annual_eps(facts, asof, splits)
    hist = [a["val"] for a in ann]
    if not rows:
        return None, [], "none", None
    cands = []

    # ---- cumulative arithmetic
    if ann:
        fy = ann[-1]
        cum = [r for r in rows if 80 <= r["span"] <= 290 and r["start"] > fy["end"]]
        if cum:
            cur = max(cum, key=lambda r: (r["end"], r["filed"]))
            prev = [r for r in rows
                    if abs(r["span"] - cur["span"]) <= 6
                    and 350 <= _days(r["start"], cur["start"]) <= 380]
            if prev:
                p = max(prev, key=lambda r: r["filed"])
                cands.append((_days(cur["end"], asof), fy["val"] + cur["val"] - p["val"], "cum"))

    # ---- four consecutive discrete quarters
    q = _dedupe([r for r in rows if 80 <= r["span"] <= 100])
    if len(q) >= 4:
        w = q[-4:]
        if (all(abs(_days(w[i]["end"], w[i + 1]["start"])) <= 5 for i in range(3))
                and 350 <= _days(w[0]["start"], w[-1]["end"]) <= 380):
            cands.append((_days(w[-1]["end"], asof), sum(x["val"] for x in w), "4q"))

    # ---- the bare latest fiscal year
    if ann:
        cands.append((_days(ann[-1]["end"], asof), ann[-1]["val"], "annual"))

    if not cands:
        return None, hist, "none", None
    stale, val, method = min(cands, key=lambda c: c[0])
    return val, hist, method, stale


def instant(facts, tags, asof):
    """Latest balance-sheet value as of a date, point-in-time. Balance-sheet
    facts are INSTANTS: they carry an `end` and no `start`."""
    us = facts.get("facts", {}).get("us-gaap", {})
    for tag in tags:
        node = us.get(tag)
        if not node:
            continue
        for unit in ("USD",):
            rows = [u for u in node.get("units", {}).get(unit, [])
                    if u.get("filed") and u["filed"] < asof and u.get("val") is not None
                    and not u.get("start")]
            if rows:
                rows.sort(key=lambda r: (r["end"], r["filed"]))
                return rows[-1]["val"]
    return None


# --------------------------------------------------------------- THE SCREEN
GATES = ["no price", "no facts", "no EPS", "TTM stale", "TTM<=0", "too few years"]


def evaluate(ticker, cik, funnel):
    px = prices(ticker)
    if len(px) < 300:
        funnel["no price"] += 1
        return None
    p0  = px_on(px, FORMATION)                # adjusted -> for the RETURN
    p1  = px_on(px, HOLD_END)
    p0t = px_on(px, FORMATION, traded=True)   # as-traded -> for the P/E
    if not p0 or not p1 or not p0t:
        funnel["no price"] += 1
        return None

    facts = edgar_facts(cik)
    if not facts:
        funnel["no facts"] += 1
        return None

    ttm, ann, method, stale = ttm_eps(facts, FORMATION, splits_of(ticker))
    if ttm is None:
        funnel["no EPS"] += 1
        return None
    if stale is not None and stale > MAX_TTM_STALE:
        funnel["TTM stale"] += 1
        return None
    if ttm <= 0:
        funnel["TTM<=0"] += 1
        return None
    if len(ann) < MIN_YEARS:
        funnel["too few years"] += 1
        return None

    pe  = p0t / ttm                              # AS-TRADED price over AS-FILED EPS
    med = median(ann[-6:])                       # multi-year normal
    if not med or med <= 0:
        funnel["too few years"] += 1
        return None
    durability = ttm / med

    eq  = instant(facts, ["StockholdersEquity"], FORMATION)
    lia = instant(facts, ["Liabilities"], FORMATION)
    if lia is None:
        # many filers never tag `Liabilities`; derive it rather than let the
        # balance-sheet gate silently pass on a missing value
        tot = instant(facts, ["LiabilitiesAndStockholdersEquity", "Assets"], FORMATION)
        if tot is not None and eq is not None:
            lia = tot - eq
    ca = instant(facts, ["AssetsCurrent"], FORMATION)
    cl = instant(facts, ["LiabilitiesCurrent"], FORMATION)
    de = (lia / eq) if (eq and eq > 0 and lia is not None) else None
    cr = (ca / cl) if (cl and cl > 0 and ca is not None) else None

    s50, s200 = sma(px, FORMATION, 50), sma(px, FORMATION, 200)

    # 3-year EPS CAGR off the ANNUAL prints.
    # ⚠️ Guarded on BOTH endpoints being positive: Python returns a COMPLEX
    # number for a negative float raised to 1/3, which then raised TypeError
    # inside the caller's try/except and SILENTLY DROPPED the name.
    growth = None
    if len(ann) >= 4 and ann[-4] > 0 and ann[-1] > 0:
        growth = (ann[-1] / ann[-4]) ** (1 / 3) - 1
    g_ttm = None
    if len(ann) >= 4 and ann[-4] > 0:
        g_ttm = (ttm / ann[-4]) ** (1 / 3) - 1        # ttm is >0 by the gate above

    return dict(
        ticker=ticker, pe=pe, ttm=ttm, med=med, durability=durability, method=method,
        stale=stale, de=de, cr=cr,
        above50=(s50 is not None and p0 > s50),
        above200=(s200 is not None and p0 > s200),
        no_loss=all(e > 0 for e in ann[-3:]), growth=growth, g_ttm=g_ttm,
        ann=ann, p0=p0t, p1=p1, ret=(p1 / p0 - 1),
    )


CUTS = ["P/E", "prior loss", "SMA", "D/E", "current", "growth", "durability"]


def passes(r, use_durability, cuts=None):
    def cut(name):
        if cuts is not None:
            cuts[name] += 1
        return False
    if r["pe"] > PE_MAX:                                     return cut("P/E")
    if not r["no_loss"]:                                     return cut("prior loss")
    if REQUIRE_SMA and not (r["above50"] and r["above200"]): return cut("SMA")
    if r["de"] is not None and r["de"] > MAX_DEBT_EQUITY:    return cut("D/E")
    if r["cr"] is not None and r["cr"] < MIN_CURRENT:        return cut("current")
    if r["growth"] is None or r["growth"] <= 0:              return cut("growth")
    if use_durability and not (DURABLE_LO <= r["durability"] <= DURABLE_HI):
        return cut("durability")
    return True


# --------------------------------------------------------------------- VERIFY
VERIFY = ["CVX", "VLO", "MPC", "GM", "F", "JNJ", "PG", "CSCO", "MU", "AAPL"]


def verify():
    """Print the full workings for known names. ⛔ THIS MODE IS NOT OPTIONAL --
    the previous version of this file produced a complete, plausible, WRONG
    result set, and the only thing that caught it was reading ten numbers by hand."""
    cikmap = sp500_tickers()
    print("=" * 96)
    print("  HAND-VERIFY — EPS construction at formation", FORMATION)
    print("=" * 96)
    print(f"  {'tkr':<6}{'as-traded':>10}{'TTM EPS':>9}{'P/E':>8}{'method':>8}{'stale':>7}"
          f"{'splt':>6}{'dur':>7}  annual EPS history (oldest -> newest)")
    for t in VERIFY:
        cik = cikmap.get(t)
        if not cik:
            print(f"  {t:<6}  no CIK")
            continue
        facts, px = edgar_facts(cik), prices(t)
        if not facts or not px:
            print(f"  {t:<6}  no data")
            continue
        sp = [s for s in splits_of(t) if s[0] <= FORMATION]
        ttm, ann, method, stale = ttm_eps(facts, FORMATION, splits_of(t))
        p0t = px_on(px, FORMATION, traded=True)
        pe = (p0t / ttm) if (ttm and ttm > 0) else float("nan")
        med = median(ann[-6:]) if ann else None
        dur = (ttm / med) if (ttm and med and med > 0) else float("nan")
        print(f"  {t:<6}{p0t:>10.2f}{(ttm if ttm else float('nan')):>9.2f}{pe:>8.1f}"
              f"{method:>8}{(stale if stale is not None else -1):>7}"
              f"{(f'{len(sp)}' if sp else '-'):>6}{dur:>7.2f}  "
              f"{[round(a, 2) for a in ann[-6:]]}")
        time.sleep(0.1)
    print("\n  TWO THINGS TO READ, and they are the two bugs that got through before:")
    print("  1. The annual history must be YEARS, not quarters. Consecutive small")
    print("     numbers of quarterly magnitude = bug A is back.")
    print("  2. It must be ONE SHARE BASIS. A step-change of exactly the split ratio")
    print("     partway along the list (splt column non-zero) = bug D is back.")


# ----------------------------------------------------------------------- MAIN
def main(limit=None):
    print("=" * 96)
    print("  DURABLE-VALUE SCREEN — point-in-time, formation", FORMATION, "-> hold to", HOLD_END)
    print("=" * 96)
    print("  ⚠️ SURVIVORSHIP: universe is TODAY'S listed set. Companies that failed or")
    print("     were acquired since 2021 are ABSENT. Every return here is biased UP.")
    print("     READ THE SPREAD vs SPY, NEVER THE ABSOLUTE NUMBER.")
    print("  ✓ LOOK-AHEAD: every fundamental is filtered on EDGAR's `filed` date.")
    print("  ✓ EPS periods are classified by DATE SPAN, never by form/fp label.\n")

    spx = prices("SPY")
    b0, b1 = px_on(spx, FORMATION), px_on(spx, HOLD_END)
    bench = b1 / b0 - 1
    print(f"  SPY {b0:.2f} -> {b1:.2f} = {bench:+.1%} over the window (price only, no dividends)\n")

    tickers = UNIVERSE[:limit] if limit else UNIVERSE
    cikmap = sp500_tickers()
    funnel = {k: 0 for k in GATES}
    funnel["no CIK"] = 0
    rows = []
    for i, t in enumerate(tickers, 1):
        cik = cikmap.get(t)
        if not cik:
            funnel["no CIK"] += 1
            continue
        try:
            r = evaluate(t, cik, funnel)
        except Exception as exc:                       # noqa: BLE001
            print(f"    ⚠️ {t}: {type(exc).__name__} {exc}")
            r = None
        if r:
            rows.append(r)
        if i % 40 == 0:
            print(f"    ...{i}/{len(tickers)} processed, {len(rows)} with usable data")
        time.sleep(0.05)

    print(f"\n  UNIVERSE {len(tickers)} -> USABLE {len(rows)}")
    print("  dropped: " + " · ".join(f"{k} {v}" for k, v in funnel.items() if v))
    meth = {}
    for r in rows:
        meth[r["method"]] = meth.get(r["method"], 0) + 1
    print("  TTM method: " + " · ".join(f"{k} {v}" for k, v in sorted(meth.items())))

    results = {}
    for label, use_dur in (("NAIVE CHEAP (no durability filter)", False),
                           ("DURABLE CHEAP (Jake's full spec)", True)):
        cuts = {k: 0 for k in CUTS}
        sel = [r for r in rows if passes(r, use_dur, cuts)]
        print("\n" + "-" * 96)
        print(f"  {label}   n={len(sel)}")
        print("    cut by: " + " · ".join(f"{k} {v}" for k, v in cuts.items() if v))
        if not sel:
            print("    no names passed")
            continue
        rets = [r["ret"] for r in sel]
        avg, med_r = sum(rets) / len(rets), median(rets)
        win = sum(1 for x in rets if x > bench) / len(rets)
        results[label] = (avg, med_r, win, len(sel))
        print(f"    mean {avg:+.1%} · median {med_r:+.1%} · vs SPY {bench:+.1%} "
              f"· spread {avg-bench:+.1%} · beat-rate {win:.0%}")
        print(f"    {'tkr':<7}{'P/E':>7}{'dur':>7}{'D/E':>7}{'g3y':>8}{'5y return':>11}")
        for r in sorted(sel, key=lambda x: -x["ret"]):
            print(f"    {r['ticker']:<7}{r['pe']:>7.1f}{r['durability']:>7.2f}"
                  f"{(r['de'] if r['de'] else 0):>7.2f}{r['growth']:>7.1%}{r['ret']:>+11.1%}")

    print("\n" + "=" * 96)
    print("  THE COMPARISON IS THE RESULT. If DURABLE does not beat NAIVE, the")
    print("  durability filter is not doing work and the idea is wrong — say so.")
    print("=" * 96)
    return results


UNIVERSE = """AAPL MSFT NVDA AMZN GOOGL META AVGO TSLA BRK-B JPM LLY V UNH XOM MA COST HD PG
JNJ WMT NFLX BAC CRM ORCL MRK ABBV CVX AMD KO PEP ADBE TMO LIN CSCO ACN MCD ABT PM DHR
WFC TXN VZ INTU IBM CAT GE QCOM NOW DIS AMGN NEE CMCSA PFE UNP RTX SPGI AXP LOW HON T
COP ELV BKNG SYK BLK VRTX PLD MDT ADP GILD MU SBUX LMT TJX MMC ADI CVS SCHW REGN CI BSX
ETN ZTS MO CB SO BA DE PGR AMT ANET FI ITW SLB DUK NKE EOG APD SHW BDX WM MCK CME TGT
MPC ICE PSX EMR NOC MCO CSX PNC AON APH ORLY GD MSI USB HCA VLO FCX MAR NSC F GM AZO
ROP AJG TDG TRV PCAR CTAS PSA AEP CPRT WELL SRE MET DXCM O KMB AIG D EW PRU ALL EXC
GIS DOW HLT KMI JCI ODFL IDXX SYY RSG A OTIS AME CMI HSY PPG STZ FAST YUM VRSK EA
KR CTSH GWW ED IQV WMB XEL DD ROK GLW EFX AVB CHTR VICI EBAY MTD DVN HIG WEC ANSS
KEYS FTV ES CDW TSCO ULTA HPQ PPL AWK BKR NUE STT LYB VTR DTE MLM VMC EIX HPE""".split()

# ------------------------------------------------------------------ ENTRY POINT
# Colab-safe: in a notebook sys.argv carries the kernel's connection-file path,
# so a bare int(sys.argv[1]) raises ValueError before a single line of the screen
# runs. Parse defensively and ignore anything that is not a number.
if __name__ == "__main__":
    _lim = None
    for _a in sys.argv[1:]:
        if _a.lstrip("-").isdigit():
            _lim = int(_a.lstrip("-"))
    verify()                      # ⛔ ALWAYS. The previous version of this file produced a
    print()                       #    complete, plausible, WRONG result set, and the only
    main(limit=_lim)              #    thing that caught it was reading ten numbers by hand.
