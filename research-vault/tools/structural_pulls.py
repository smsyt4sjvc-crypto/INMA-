# WEEKLY STRUCTURAL PULL — positioning + filings watchlist sweep (manual Colab run, ~5 min)
# Built 2026-07-11. Jake's directive: structural reports/filings > news and shock events.
# NO automation/cron per standing spending rule — run by hand, weekly.
# Cell A: CFTC COT leveraged-fund net positioning (free prime-book proxy; futures, not sectors)
# Cell B: Form 4 tripwire sweep over vault watchlists (3+ filings in 14d -> run form4 detail parser)
# Cell C: short interest snapshot | Cell D: 13F freshness check on tracked managers
import pandas as pd, requests, time
import xml.etree.ElementTree as ET
from datetime import date, timedelta

# ---------------- CELL A ----------------
for mkt, label in [("E-MINI S&P 500", "ES"), ("NASDAQ MINI", "NQ"),
                   ("CRUDE OIL, LIGHT SWEET", "CL"), ("GOLD", "GC")]:
    url = ("https://publicreporting.cftc.gov/resource/gpe5-46if.json"
           f"?$where=contract_market_name like '%25{mkt.replace(' ', '%20')}%25'"
           "&$order=report_date_as_yyyy_mm_dd DESC&$limit=8")
    try:
        d = pd.DataFrame(requests.get(url, timeout=30).json())
        if d.empty: print(f"{label}: no rows"); continue
        d["net_lev"] = d.lev_money_positions_long.astype(float) - d.lev_money_positions_short.astype(float)
        cur, prior = d.net_lev.iloc[0], d.net_lev.iloc[min(4, len(d)-1)]
        print(f"{label}: leveraged funds net {cur:+,.0f} | 4wk ago {prior:+,.0f} | delta {cur-prior:+,.0f}")
    except Exception as e:
        print(f"{label}: {str(e)[:50]}")

# ---------------- CELL B ----------------
EMAIL = "your_email@example.com"
H = {"User-Agent": f"Jake research {EMAIL}"}
WATCH = {
 "semi_grid": ["MU","LRCX","AMAT","NVDA","AMD","AVGO","KLAC","TER","ON","MRVL","MPWR","SMCI","WDC","STX","SNDK"],
 "quiet_health": ["PG","GILD","CME","GD","HIG","EA","FFIV","ULTA","GEHC","CBOE","UHS","WRB","CB","HII","CI"],
 "mold_12": ["VRRM","GTM","DUOL","INSP","EPAM","FRPT","BLKB","AMPH","GPK","ADMA","UPWK","WEN"],
 "bottleneck": ["CLF","VICR","VSH","ENS","VECO","AXTI","POWL","STRL","FIX","TTMI"],
}
cm = requests.get("https://www.sec.gov/files/company_tickers.json", headers=H, timeout=30).json()
cik = {v["ticker"]: str(v["cik_str"]).zfill(10) for v in cm.values()}
SINCE = (date.today() - timedelta(days=14)).isoformat()

def sweep(t):
    c = cik.get(t)
    if not c: return None
    sub = requests.get(f"https://data.sec.gov/submissions/CIK{c}.json", headers=H, timeout=30).json()
    r = sub["filings"]["recent"]; time.sleep(0.12)
    return sum(1 for i in range(len(r["form"])) if r["form"][i] == "4" and r["filingDate"][i] >= SINCE)

for group, names in WATCH.items():
    hits = {t: sweep(t) for t in names}
    flagged = {t: n for t, n in hits.items() if n}
    print(f"{group}: {flagged if flagged else 'no Form 4s in 14d'}")

# ---------------- CELL C ----------------
import yfinance as yf
for t in ["MU","NVDA","GPK","FRPT","DUOL","UPWK","VECO","AXTI","ORCL"]:
    i = yf.Ticker(t).info
    spf = i.get("shortPercentOfFloat"); ss, ssp = i.get("sharesShort"), i.get("sharesShortPriorMonth")
    d = f"{(ss/ssp-1)*100:+.0f}% MoM" if ss and ssp else "n/a"
    print(f"{t}: short {spf*100:.1f}% of float | {d}" if spf else f"{t}: n/a")

# ---------------- CELL D ----------------
MANAGERS = {"Scion (Burry)": "0001649339", "Berkshire": "0001067983", "Appaloosa": "0001656456"}
for name, c in MANAGERS.items():
    sub = requests.get(f"https://data.sec.gov/submissions/CIK{c.zfill(10)}.json", headers=H, timeout=30).json()
    r = sub["filings"]["recent"]; time.sleep(0.12)
    f13 = [(r["filingDate"][i], r["accessionNumber"][i]) for i in range(len(r["form"])) if "13F" in r["form"][i]]
    if f13:
        print(f"{name}: latest 13F {f13[0][0]} https://www.sec.gov/Archives/edgar/data/{int(c)}/{f13[0][1].replace('-','')}")
    else:
        print(f"{name}: none")
