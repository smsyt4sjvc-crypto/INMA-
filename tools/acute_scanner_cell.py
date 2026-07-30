
# ============================================================================
#  ACUTE SCANNER — 10-hour window, 78 vault keywords / 10 threads, source-tiered
#  Prints: (1) INDEX prices  (2) MAG 7 alone  (3) MEMORY alone
#          (4) keyword HITS ONLY, financial outlets first, buzz last.
#  Prints NOTHING for a tier with no hits. No padding. Token-free.
# ============================================================================
import subprocess, sys, re, io, time, urllib.request
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
try:
    import yfinance as yf
except Exception:
    subprocess.run([sys.executable,'-m','pip','install','-q','yfinance']); import yfinance as yf

HOURS  = 10                       # <-- the window. change to 6 / 24 as needed
PER_TIER_CAP = 40                 # safety cap so a bad feed can't wall you
UA = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
NOW = datetime.now(timezone.utc)
CUT = NOW - timedelta(hours=HOURS)

# ---------------------------------------------------------------- PRICES
INDEX = [('^GSPC','S&P 500'), ('^NDX','Nasdaq 100'), ('^RUT','Russell 2000'),
         ('SOXX','SOXX semis'), ('SMH','SMH semis'), ('^VIX','VIX'),
         ('^TNX','US 10Y'), ('^TYX','US 30Y'), ('DX-Y.NYB','DXY'),
         ('CL=F','WTI'), ('BZ=F','Brent'), ('GC=F','Gold'), ('TLT','TLT 20y+')]
MAG7  = [('AAPL','Apple'), ('MSFT','Microsoft'), ('GOOGL','Alphabet'), ('AMZN','Amazon'),
         ('META','Meta'), ('NVDA','Nvidia'), ('TSLA','Tesla')]
MEM   = [('MU','Micron'), ('SNDK','SanDisk'), ('STX','Seagate'), ('WDC','WestDigital'),
         ('005930.KS','Samsung Elec'), ('000660.KS','SK hynix'), ('TSM','TSMC'), ('AVGO','Broadcom')]

def px_block(title, rows):
    print(f'\n### {title}')
    print(f'  {"":13}{"last":>12}{"chg%":>9}{"BASE":>12}   as of')
    tick = [t for t,_ in rows]
    try:
        df = yf.download(tick, period='5d', progress=False, auto_adjust=True, threads=True)['Close']
    except Exception as e:
        print(f'  !! price fetch failed: {e}'); return
    if hasattr(df,'to_frame') and not hasattr(df,'columns'): df = df.to_frame(tick[0])
    for t, lab in rows:
        try:
            s = df[t].dropna()
            if len(s) < 2: print(f'  {lab:13}   -- n/a'); continue
            last, base = float(s.iloc[-1]), float(s.iloc[-2])
            print(f'  {lab:13}{last:>12,.2f}{(last/base-1)*100:>+9.2f}{base:>12,.2f}   {s.index[-1].date()}')
        except Exception:
            print(f'  {lab:13}   -- n/a')
    print('  (chg% is vs the BASE column = prior session close. Compare PRICES across runs.)')

# ---------------------------------------------------------------- KEYWORDS
# ~45 terms, thread-tagged. \b-anchored so short acronyms don't false-match
# (SPR must not hit "spread", CDS must not hit "CDSL", etc).
THREADS = {
 'MEMORY':    ['dram','hbm','nand','cxmt','micron','hynix','sandisk','memory price','memory chip'],
 'SEMIS':     ['wafer','foundr','lithograph','advanced packaging','chip capex'],
 'CAPEX':     ['capex','capital expenditure','data center','data centre','hyperscaler',
               'off-balance','uncommenced','not commenced','depreciation'],
 'FINANCING': ['credit default','cds','private credit','bdc','spv','neocloud','coreweave',
               'nebius','free cash flow','bond sale','off balance sheet'],
 'POWER':     ['pjm','curtail','grid emergency','turbine','interconnection','smr',
               'behind-the-meter'],
 'WAR/OIL':   ['hormuz','qeshm','tanker','houthi','irgc','abqaiq','jazan','transit fee',
               'war risk','crack spread','refiner','lng'],
 'INVENTORY': ['spr','cushing','strategic petroleum','crude draw','crude build','tank bottoms'],
 'FED':       ['warsh','term premium','forward guidance','steepen','core cpi','supply shock','dissent'],
 'MODEL-ECON':['open-weight','open weight','routing layer','per-token','inference cost','agentic'],
 'KOREA':     ['kospi','circuit breaker','de-gross','degross','leveraged etf','margin call'],
}
# TWO KEYWORD CLASSES — this distinction is the whole gate and it was WRONG on first build.
# STRICT: short acronyms where a suffix creates a false positive. \bKWs?\b only.
#   spr must NOT match "spread"; cds must NOT match "CDSL"; dram must NOT match "drama".
# STEM: everything else gets up to 3 trailing chars, because headlines use plurals and
#   verb forms far more than base forms — "data centerS", "steepenS", "tankerS", "refinerIES".
#   Anchoring those with a hard \b silently drops most real hits. (Caught by the offline
#   unit test below; 3 of 14 cases failed before this fix.)
STRICT = {'spr','cds','bdc','spv','hbm','pjm','smr','irgc','dram','nand','lng'}
def _pat(k):
    return re.compile(r'\b'+re.escape(k)+(r's?\b' if k in STRICT else r'\w{0,3}\b'), re.I)
PATS = {th: [_pat(k) for k in ks] for th, ks in THREADS.items()}
NKEY = sum(len(v) for v in THREADS.values())

def tags(text):
    return [th for th, ps in PATS.items() if any(p.search(text) for p in ps)]

# ---------------------------------------------------------------- FEEDS BY TIER
# CNBC: the search.cnbc.com/combinedcms endpoint returns a 682-byte error page with ZERO items.
# Verified working format is /id/<ID>/device/rss/rss.html (30 items each, fresh dates).
CNBC = 'https://www.cnbc.com/id/{}/device/rss/rss.html'
GN   = 'https://news.google.com/rss/search?q={}&hl=en-US&gl=US&ceid=US:en'
YF   = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s={}&region=US&lang=en-US'

TIERS = [
 ('T1  FINANCIAL WIRE  (least partisan — read these first)', [
   ('MW-top',    'https://feeds.content.dowjones.io/public/rss/mw_topstories'),
   ('MW-bulletins','https://feeds.content.dowjones.io/public/rss/mw_bulletins'),
   # MW-marketpulse DROPPED: live-tested 30 items whose newest pubDate was Jul-2025.
   # Dead/static feed, not a parser bug — the dates really are a year old.
   ('CNBC-mkts', CNBC.format('20910258')),
   ('CNBC-fin',  CNBC.format('10000664')),
   ('SeekAlpha', 'https://seekingalpha.com/market_currents.xml'),
   ('Reuters-biz',GN.format('site:reuters.com+when:1d')),
   ('Bloomberg', GN.format('site:bloomberg.com+when:1d')),
   ('WSJ',       GN.format('site:wsj.com+when:1d')),
   ('FT',        GN.format('site:ft.com+when:1d')),
   ('YF:MU',     YF.format('MU')),
   ('YF:NVDA',   YF.format('NVDA')),
   ('YF:MSFT',   YF.format('MSFT')),
   ('YF:META',   YF.format('META')),
 ]),
 ('T2  NETWORKS + GOOGLE  (broad, mixed reliability)', [
   ('CNBC-top',  CNBC.format('100003114')),
   ('ABC-money', 'https://abcnews.go.com/abcnews/moneyheadlines'),
   ('ABC-intl',  'https://abcnews.go.com/abcnews/internationalheadlines'),
   ('GN-business','https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=en-US&gl=US&ceid=US:en'),
   ('GN-world',  'https://news.google.com/rss/headlines/section/topic/WORLD?hl=en-US&gl=US&ceid=US:en'),
   ('GN-hormuz', GN.format('Hormuz+OR+Qeshm+OR+tanker+when:1d')),
   ('GN-memory', GN.format('DRAM+OR+HBM+OR+CXMT+OR+memory+chip+when:1d')),
   ('GN-capex',  GN.format('hyperscaler+capex+OR+data+center+capex+when:1d')),
   ('GN-grid',   GN.format('PJM+OR+grid+curtail+data+center+when:1d')),
 ]),
 ('T3  FAST / OPINIONATED  (speed over neutrality — verify before weighting)', [
   ('ZeroHedge', 'https://cms.zerohedge.com/fullrss2.xml'),
   ('Fox-biz',   'https://moxie.foxbusiness.com/google-publisher/markets.xml'),
 ]),
]

# FEED HEALTH, live-tested from this container 2026-07-29 ~10:50pm PT (fresh = within 10h):
#   T1  MW-top 10/10 · MW-bulletins 10/9 · SeekAlpha 7/7 (newest 2m) · Reuters 100/41 ·
#       Bloomberg 100/38 · WSJ 100/39 · FT 100/31 · YF:MU 20/11 · YF:NVDA 20/20 · CNBC 30 each
#   T2  ABC-money 25/7 · ABC-intl 25/4 · GN-business 26/17 · GN-world 34/13 ·
#       GN-hormuz 100/47 (newest 12m) · GN-memory 100/10
#   T3  ZeroHedge 25/20 · Fox-biz 25/1 (low yield, kept for coverage)
# The Google-News site: queries for Reuters/Bloomberg/WSJ/FT are the T1 backbone — 31-41 fresh
# items each — because those outlets' own RSS is discontinued or paywalled.

def parse(name, url):
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20).read()
    except Exception as e:
        return None, f'{name}: fetch failed ({type(e).__name__})'
    txt = raw.decode('utf-8', 'replace')
    out = []
    for m in re.finditer(r'<item[ >](.*?)</item>', txt, re.S|re.I):
        blk = m.group(1)
        def grab(tag):
            g = re.search(rf'<{tag}[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</{tag}>', blk, re.S|re.I)
            return re.sub(r'<[^>]+>','', g.group(1)).strip() if g else ''
        title = grab('title')
        if not title: continue
        dt = None
        for tag in ('pubDate','updated','published','dc:date'):
            d = grab(tag)
            if d:
                try: dt = parsedate_to_datetime(d)
                except Exception:
                    try: dt = datetime.fromisoformat(d.replace('Z','+00:00'))
                    except Exception: dt = None
                if dt: break
        if dt is None: continue
        if dt.tzinfo is None: dt = dt.replace(tzinfo=timezone.utc)
        out.append((dt, title, grab('description')[:200], grab('link')))
    return out, None

print('='*74)
print(f'  ACUTE SCANNER — last {HOURS}h  |  {NKEY} keywords / {len(THREADS)} threads')
print(f'  run {NOW:%Y-%m-%d %H:%M} UTC   cutoff {CUT:%Y-%m-%d %H:%M} UTC')
print('='*74)

px_block('INDEX / MACRO', INDEX)
px_block('MAG 7 (independent)', MAG7)
px_block('MEMORY COMPLEX (independent)', MEM)

print('\n'+'='*74); print(f'  KEYWORD HITS ONLY — last {HOURS}h, financial tier first'); print('='*74)

seen, problems, grand = set(), [], 0
for tier_name, feeds in TIERS:
    hits = []
    for name, url in feeds:
        items, err = parse(name, url)
        if err: problems.append(err); continue
        for dt, title, desc, link in items:
            if dt < CUT: continue
            k = re.sub(r'[^a-z0-9]','', title.lower())[:60]
            if k in seen: continue
            th = tags(title+' '+desc)
            if not th: continue          # <-- the gate: direct keyword hit or it does not print
            seen.add(k); hits.append((dt, name, th, title, link))
    print(f'\n{"="*74}\n{tier_name}\n{"="*74}')
    if not hits:
        print('  no keyword hits in this tier.')
        continue
    hits.sort(key=lambda x: x[0], reverse=True)
    for dt, name, th, title, link in hits[:PER_TIER_CAP]:
        age = (NOW-dt).total_seconds()/60
        agestr = f'{age:.0f}m' if age < 90 else f'{age/60:.1f}h'
        print(f'\n[{agestr:>5}] {name:<12} {"|".join(th)}')
        print(f'        {title[:150]}')
        if link: print(f'        {link[:110]}')
    grand += len(hits)
    if len(hits) > PER_TIER_CAP:
        print(f'\n  ...{len(hits)-PER_TIER_CAP} more in this tier (capped at {PER_TIER_CAP}).')

print('\n'+'='*74)
print(f'  TOTAL KEYWORD HITS: {grand}   (a low number is a real signal, not a broken scanner)')
if problems:
    print('  feed problems (missing coverage, not errors in the hits above):')
    for p in problems: print(f'    - {p}')
print('='*74)
