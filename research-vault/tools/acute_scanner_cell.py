
# ============================================================================
#  ACUTE SCANNER — 10-hour window, vault keywords / threads, source-tiered
#  Prints: (1) INDEX prices  (2) MAG 7 alone  (3) MEMORY alone
#          (4) keyword HITS ONLY, financial outlets first, buzz last
#          (5) PRIORITY FOLLOW-UP QUEUE — hits grouped by the OPEN VAULT FLAG they
#              could close, paywalled primary wires marked [GET], with full links.
#  Two gates: keywords say ON-TOPIC; the flag registry says WORTH READING.
#  Prints NOTHING for a tier with no hits. No padding. Token-free.
# ============================================================================
import subprocess, sys, re, io, time, textwrap, urllib.request
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
try:
    import yfinance as yf
except Exception:
    subprocess.run([sys.executable,'-m','pip','install','-q','yfinance']); import yfinance as yf

HOURS  = 10                       # <-- the DISPLAY window for the hit tiers
# The FLAG window is deliberately WIDER than the display window. An open question does not
# age out because the news cycle did: on run 3 the two PRI-1 flags (F1 MSFT leases, F2 the
# Goldman/Blue Owl deals) showed "no candidate" purely because their evidence had scrolled
# past 10h. The highest-priority questions were the ones the window hid. Feeds using
# Google's when:1d cap out around 24h regardless; this takes whatever the others still hold.
FLAG_HOURS = 30
PER_TIER_CAP = 40                 # safety cap so a bad feed can't wall you
UA = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
NOW = datetime.now(timezone.utc)
CUT = NOW - timedelta(hours=HOURS)
FCUT= NOW - timedelta(hours=FLAG_HOURS)

# ---------------------------------------------------------------- PRICES
INDEX = [('^GSPC','S&P 500'), ('^NDX','Nasdaq 100'), ('^RUT','Russell 2000'),
         ('SOXX','SOXX semis'), ('SMH','SMH semis'), ('^VIX','VIX'),
         ('^TNX','US 10Y'), ('^TYX','US 30Y'), ('DX-Y.NYB','DXY'),
         ('CL=F','WTI'), ('BZ=F','Brent'), ('GC=F','Gold'), ('TLT','TLT 20y+')]
MAG7  = [('AAPL','Apple'), ('MSFT','Microsoft'), ('GOOGL','Alphabet'), ('AMZN','Amazon'),
         ('META','Meta'), ('NVDA','Nvidia'), ('TSLA','Tesla')]
MEM   = [('MU','Micron'), ('SNDK','SanDisk'), ('STX','Seagate'), ('WDC','WestDigital'),
         ('005930.KS','Samsung Elec'), ('000660.KS','SK hynix'), ('TSM','TSMC'), ('AVGO','Broadcom')]


# ── EVENT CLUSTERING — added 8/2 after Jake caught me presenting a ZeroHedge re-report of a
#    Truth Social post HE HAD ALREADY PASTED as fresh corroboration. The run printed 95 HITS;
#    it carried ~15-18 DISTINCT EVENTS. The Hormuz block alone was ~50 headlines over ~9 things.
#    ⛔ THE DEFECT: the scanner counted SYNDICATION as SIGNAL. Forty outlets reprinting one
#    statement is one datum, not forty — and a big hit-count READS as high signal, which is the
#    opposite of true. war-board.md L572 already registered the rule: "if this is the same story
#    resurfacing it is NOT NEW INFORMATION." The scanner had no way to apply it.
STOP = set("""the a an of of to in on for and or at by from with as is are was be been says say said
after over amid new more than that this it its us u.s. reuters bloomberg report reports news will would
could may might near into out up down but not no yes he she they his her their who what when where why
live day update breaking exclusive""".split())
def _stem(w):
    for suf in ("'s", "ies", "ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 4: return w[:-len(suf)]
    return w
def _toks(t):
    import re as _re
    return {_stem(x) for x in _re.findall(r"[a-z0-9']+", t.lower())
            if x not in STOP and len(x) > 2}
def cluster_hits(hits, thresh=0.60, minshare=3):
    """Group same-EVENT headlines. CONTAINMENT (inter / smaller set), not Jaccard --
       headlines vary wildly in length and Jaccard punishes long-vs-short pairs, which is
       exactly the wire-vs-aggregator case we need to catch."""
    out = []
    for h in hits:
        tk = _toks(h[3]); placed = False
        for rep, dupes, rtk in out:
            inter = len(tk & rtk)
            if inter >= minshare and inter / max(1, min(len(tk), len(rtk))) >= thresh:
                dupes.append(h); rtk |= tk          # widen the cluster as members join
                placed = True; break
        if not placed:
            out.append((h, [], set(tk)))
    return [(r, d) for r, d, _ in out]

def px_block(title, rows):
    print(f'\n### {title}')
    print(f'  {"":13}{"last":>12}{"chg%":>9}{"BASE":>12}   as of')
    tick = [t for t,_ in rows]; moves = []
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
            ch = (last/base-1)*100; moves.append((lab, ch))
            print(f'  {lab:13}{last:>12,.2f}{ch:>+9.2f}{base:>12,.2f}   {s.index[-1].date()}')
        except Exception:
            print(f'  {lab:13}   -- n/a')
    print('  (chg% is vs the BASE column = prior session close. Compare PRICES across runs.)')
    _price_alarms(title, moves)

# ── PRICE ALARMS — added 8/1 after the scanner printed SK hynix +29.95% (0.05pp off the
#    KRX daily limit) next to Micron -5.90% and raised NOTHING. Every alarm below is
#    PRICE-ONLY. The keyword tier could not have caught it: the KOREA thread's words are
#    kospi/circuit breaker/de-gross/margin call, and the wire said "SK Hynix Surged 30% in
#    South Korea." A limit-up is not a vocabulary event.
#    ⇒ THE GAP WAS STRUCTURAL: the scanner held prices and headlines in the same run and
#      NEVER CROSSED THEM. A move can be the story even when no headline says so.
LIMIT_UP = {'Samsung Elec': 30.0, 'SK hynix': 30.0}      # KRX daily price limit, +/-30%
def _price_alarms(title, moves):
    if not moves: return
    out = []
    for lab, ch in moves:
        lim = LIMIT_UP.get(lab)
        if lim and abs(ch) >= lim - 0.5:
            out.append(f'!! {lab} {ch:+.2f}% — WITHIN 0.5pp OF THE {lim:.0f}% DAILY LIMIT. '
                       f'A limit move is a FLOW event until proven fundamental. Check the ADR: '
                       f'if it disagrees, the local move is positioning, not news.')
        elif abs(ch) >= 10:
            out.append(f'!! {lab} {ch:+.2f}% — DOUBLE-DIGIT SINGLE SESSION on a mega-cap. '
                       f'Confirm it is not a split/dividend/currency artifact BEFORE reading it.')
    hi, lo = max(moves, key=lambda x: x[1]), min(moves, key=lambda x: x[1])
    spread = hi[1] - lo[1]
    if spread >= 15:
        out.append(f'!! DISPERSION {spread:.1f}pp INSIDE ONE BLOCK — {hi[0]} {hi[1]:+.2f}% vs '
                   f'{lo[0]} {lo[1]:+.2f}%. Same industry moving opposite is a SORT, not a drift: '
                   f'name the axis it sorted on before reading any single name.')
    if out:
        print(f'  {"-"*72}')
        for o in out: print(f'  {o}')

# ---------------------------------------------------------------- FRONT END
# Yahoo has no clean 2Y ticker (^FVX=5Y, ^IRX=13wk), so the 2Y comes from FRED.
# THIS IS NOT DECORATION: the 2Y is the registered KILL SWITCH on the Fed-hike
# call (predictions/2026-07-30-fed-hike-before-december.md). The scanner ran a
# full window on 7/31 WITHOUT it, which is the one number the call turns on.
#   2Y RISING while the 30Y stalls  = BEAR FLATTENING = the market pricing hikes
#   2Y FALLING while the 30Y rises  = inflation-TOLERANCE steepening (the 7/29 read)
def front_end_block():
    import urllib.request, io as _io
    print('\n### FRONT END / CURVE  (FRED — the Fed-call kill switch)')
    out = {}
    for sid in ('DGS2', 'DGS10', 'DGS30'):
        try:
            raw = urllib.request.urlopen(
                f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}', timeout=25).read().decode()
            d = pd.read_csv(_io.StringIO(raw)); d.columns = ['date', sid]
            d[sid] = pd.to_numeric(d[sid], errors='coerce')
            d = d.dropna()
            out[sid] = (float(d[sid].iloc[-1]), float(d[sid].iloc[-2]), d['date'].iloc[-1])
        except Exception as e:
            print(f'  {sid:13}   -- FRED fetch failed ({type(e).__name__})')
    if not out:
        print('  !! front end unavailable — the Fed kill switch CANNOT be read this run'); return
    print(f'  {"":13}{"last":>12}{"chg bp":>9}{"BASE":>12}   as of')
    for sid, lab in (('DGS2','US 2Y'), ('DGS10','US 10Y (FRED)'), ('DGS30','US 30Y (FRED)')):
        if sid in out:
            l, b, dt = out[sid]
            print(f'  {lab:13}{l:>12.2f}{(l-b)*100:>+9.0f}{b:>12.2f}   {dt}')
    if 'DGS2' in out and 'DGS30' in out:
        l2, b2, _ = out['DGS2']; l30, b30, _ = out['DGS30']
        sp, spb = l30 - l2, b30 - b2
        print(f'  {"2s30s":13}{sp:>+12.2f}{(sp-spb)*100:>+9.0f}{spb:>+12.2f}')
        d2, d30 = (l2-b2)*100, (l30-b30)*100
        if   d2 > 0 and d30 <= d2: verdict = 'BEAR FLATTENING — front end leading = market pricing HIKES'
        elif d2 < 0 and d30 > 0:   verdict = 'inflation-TOLERANCE steepening — 2Y down, long end up'
        elif d2 > 0 and d30 > d2:  verdict = 'bear steepening — long end leading'
        else:                      verdict = 'no clean signal this session'
        print(f'  -> {verdict}')
    print('  (FRED lags ~1 session vs the Yahoo quotes above. Compare LEVELS, not timestamps.)')

# ---------------------------------------------------------------- KEYWORDS
# ~45 terms, thread-tagged. \b-anchored so short acronyms don't false-match
# (SPR must not hit "spread", CDS must not hit "CDSL", etc).
# ═══════════════ THREAD MAP BEGIN — single source of truth ═══════════════
# The router EXECS this block as real Python (sentinel-delimited), so comments and
# apostrophes are safe — the 8/8 regex-parser bug class is structurally dead.
# DESIGN (rebuilt 2026-08-08 after FIVE gaps in one day, #13-#17):
#   Every thread carries THREE vocabulary layers, because each missed for a different reason:
#   1. CONCEPTS  — what the thread is about        (the original map had only these)
#   2. ENTITIES  — proper nouns: tickers, companies, people, places, models, agencies
#                  (gaps #13/#14/#15/#16: materials, robotics policy, model names, alliances)
#   3. MEASURES  — the data vocabulary that REPORTS on the thread: series names, assessors,
#                  ratio/flow words (gap #17: flows/positioning; gap #12: earnings quality)
#   Layers are merged per-list (the matcher is flat); the discipline is in AUTHORING:
#   when adding a thread, fill all three layers or say why one is empty.
#   Duplicates ACROSS threads are fine — a hit can legitimately tag two threads.
#   Gap history stays here as comments; it is the map's calibration record.
THREADS = {
 # ── MEMORY ──
 'MEMORY':    ['dram','hbm','nand','memory price','memory chip','chip shortage',
               'cxmt','micron','hynix','sk hynix','samsung','sandisk','sndk','kioxia',
               'western digital','wdc',
               'contract price','spot price','bit growth','wafer input'],
 # ── SEMIS ──
 'SEMIS':     ['wafer','foundr','lithograph','advanced packaging','chip capex',
               'tsmc','asml','nvidia','nvda','amd','broadcom','avgo','intel','qualcomm',
               'rubin','blackwell','h100','h200','gb200','cowos'],
 # gap #13 (2026-08-08): rare-earth/magnet/humanoid had NO thread; duplicate note filed.
 # gap #14 (2026-08-08): robotics POLICY vocabulary (fcc, import ban, producer names).
 'MATERIALS': ['rare earth','rare-earth','magnet','ndfeb','ndpr','neodymium','dysprosium',
               'terbium','praseodymium','critical mineral','permanent magnet','mgoe',
               'humanoid','actuator','reducer','robotics','physical ai','motion control',
               'robot dog','quadruped','embodied',
               'harmonic drive','nabtesco','mp materials','lynas','vulcan elements',
               'reelement','niron','tuopu','sanhua','inovance','unitree','agibot','ubtech',
               'figure ai','optimus','noveon','vacuumschmelze','energy fuels','ucore',
               'arafura','niocorp','serra verde','torngat','pensana','traxys','nidec',
               'solvay','shanghai metals','smm',
               'fcc','import ban','import control','entity list','section 232',
               'price floor','offtake','fob china','book-to-bill','order intake'],
 # gap #11 (8/5): filer names. gap #12 (8/8): earnings-quality measures.
 'CAPEX':     ['capex','capital expenditure','data center','data centre','hyperscaler',
               'off-balance','uncommenced','not commenced','depreciation','useful life',
               'useful-life','finance lease','self-funding',
               'spacex','spcx','starlink','microsoft','msft','alphabet','googl','google',
               'amazon','amzn','meta','oracle','orcl','openai','anthropic','stargate','xai',
               'unrealized','unrealised','mark-to-market','marked up','equity investment',
               'equity securities','earnings quality','net margin','earnings beat',
               'operating cash flow','free cash flow','net income'],
 'FINANCING': ['credit default','cds','private credit','bdc','spv','neocloud','coreweave',
               'nebius','bond sale','off balance sheet','vendor financing',
               'lockup','lock-up','tender offer','share unlock','secondary sale','follow-on',
               'blue owl','apollo','blackstone','ares','oaktree','diameter','valor','obdc',
               'ig spread','high yield','spread widen','non-accrual','downgrade','issuance',
               'trs','total return swap','13f','situational awareness','aschenbrenner',
               'coatue','citadel','prime brokerage','prime book','swap position'],
 'POWER':     ['pjm','curtail','grid emergency','turbine','interconnection','smr',
               'behind-the-meter','ofgem','grid access','connection queue','commitment fee',
               'wolfspeed','silicon carbide','empower semiconductor','ionic digital',
               'grid operator','transmission','substation','ratepayer','moratorium',
               'nuclear','reactor','criticality','part 57','nrc',
               'avista','spokane','oklo','westinghouse','vistra','constellation','nextera',
               'ge vernova','ercot','caiso','datacenter power','megawatt','gigawatt'],
 # gap #18 (2026-08-09): Western-hemisphere replacement-barrel vocabulary — a Venezuela-imports
 # paste weak-matched ALLIANCE(1)* while demand-destruction held the +1.6M b/d offset line and the
 # China-routing prior. The oil map covered the DISRUPTED side, never the REPLACEMENT side.
 'WAR/OIL':   ['hormuz','qeshm','tanker','houthi','irgc','abqaiq','jazan','transit fee',
               'war risk','crack spread','refiner','lng',
               'iran','oman','majlis','fars','aramco','opec','brent','wti','kharg',
               'corridor','flag state','insurance premium',
               'venezuela','pdvsa','chevron','merey','heavy sour','heavy crude','guyana',
               'gulf coast','official selling price','crude import','import license'],
 'BLACK SEA': ['cpc','caspian pipeline','novorossiysk','tengiz','kashagan','karachaganak',
               'kazakh','kazakhstan','black sea','primorsk','ust-luga','druzhba','ceyhan'],
 'INVENTORY': ['spr','cushing','strategic petroleum','crude draw','crude build','tank bottoms',
               'eia','api inventory','days of supply'],
 # GAP #10 (8/5): the call's own subject. Entities + auction/liquidity measures added 8/8.
 'FED':       ['warsh','term premium','forward guidance','steepen','core cpi','supply shock',
               'dissent','rate hike','rate cut','rate pause','rate decision','fomc','fed funds','raise rate','cut rate','the fed',
               'fedwatch','hike odds','basis point','powell','hawkish','dovish','fed meeting',
               'rate expectations',
               'hammack','kashkari','waller','bostic','goolsbee','jefferson','bowman','daly',
               'treasury auction','30y auction','auction tail','bid-to-cover','indirect',
               'reserve balances','reverse repo','rrp','qt','tic data','dot plot','sep'],
 # gap #17 (8/8): measurement vocabulary — flows/positioning. NOT the proper-noun defect.
 'FLOWS':     ['fund flow','inflow','outflow','epfr','allocation','net buying','net selling',
               'retail flow','institutional flow','positioning','percentile','exposure',
               'de-gross','cta','systematic','risk parity','buyback','short interest',
               'put/call','skew','sentiment','aaii','bull-bear','cash levels',
               'fund manager survey','bofa','hartnett','record inflow','annualized'],
 # gap #15 (8/8): model NAMES + usage-share measures.
 'MODEL-ECON':['open-weight','open weight','routing layer','per-token','inference cost','agentic',
               'deepseek','qwen','kimi','glm','minimax','tencent','hunyuan','xiaomi','mimo',
               'llama','mistral','nemotron','gpt-5','gpt5','gemini','claude','grok','astra',
               'openrouter','leaderboard','token usage','token share','token volume',
               'market share','usage share','model ranking','trillion tokens'],
 'FX/CARRY':  ['yen','jpy','usd/jpy','usdjpy','boj','bank of japan','carry trade','repatriation',
               'currency intervention','fx intervention','fx reserves','ministry of finance',
               'dxy','dollar index','ueda','mof','kanda','jgb','japan sold','tic shows'],
 'AI-POLICY': ['export control','entity list','blacklist','huawei','huang','jensen',
               'chip ban','chip export','tech transfer','sovereign ai','ai regulation',
               'ai policy','diffusion rule','deregulat','preempt','smic','state ai law',
               'executive order','white house','ai framework','voluntary framework',
               'model evaluation','capabilities testing','pre-release','frontier model',
               'ai safety','ai executive','classified threshold','trusted partner',
               'ai act','model access','safety institute','nist ai','red team'],
 'KOREA':     ['kospi','kosdaq','circuit breaker','de-gross','degross','leveraged etf',
               'margin call','south korea','limit up','limit-up','daily limit','krx','korea'],
 'LABOR':     ['payroll','jolts','job openings','unemployment','jobless','nonfarm',
               'hires','quits rate','layoffs','labor market','labour market','wage growth',
               'initial claims','continuing claims','adp employment',
               'bls','household survey','participation rate','multiple jobholders',
               'full-time','part-time','productivity','unit labor cost'],
 'MUNITIONS': ['atacms','tomahawk','munition','stockpile','prsm','precision strike',
               'defense production act','missile inventory','replenish','ordnance',
               'supplemental appropriation','arms sale','patriot','interceptor','thaad'],
 # gap #16 (8/8): alliances had no vocabulary — war was reachable only via weapons/oil/theatres.
 'ALLIANCE':  ['defense pact','defence pact','mutual defense','mutual defence','collective defense',
               'collective defence','article 5','joint defence','joint defense','security guarantee',
               'saudi','pakistan','turkey','turkiye','erdogan','bin salman','sharif','mecca',
               'riyadh','islamabad','ankara','nato','treaty','accession','mjda'],
 'LEVANT':    ['lebanon','hezbollah','israel','litani','leviathan','karish','rome talks',
               'framework agreement','ceasefire','idf','beirut','northern front'],
 'TOKEN-ECON':['token cost','token price','per token','tokens per','inference cost',
               'api pricing','price per million','intelligence per watt','tokens per watt',
               'token expenditure','compute cost','gpu rental','jevons','price war',
               'inference revenue','cost per task',
               'custom chip','in-house chip','custom silicon','asic','tpu','trainium',
               'co-design','custom accelerator',
               'silicon data','sdllmtk','cheaperinference'],
}

# THREAD -> ORIGINATING VAULT NOTE. Every hit routes BACK to the note it came from.
ROUTE = {
 'MEMORY':    'memory-regime-question / compression-thesis',
 'SEMIS':     'ai-infra-allocation-map / buildout-bottleneck-map',
 'MATERIALS': 'buildout-bottleneck-map (the magnet chokepoint, 8/4 + 8/8) / physical-ai-hardware-stack (actuators/reducers) / war-board',
 'CAPEX':     'ai-capex-cycle / cepi',
 'FINANCING': 'ai-financing-fragility',
 'POWER':     'buildout-bottleneck-map / power-not-petroleum / nuclear',
 'WAR/OIL':   'demand-destruction / war-board / oil-value-chain',
 'BLACK SEA': 'demand-destruction (CPC/Kazakh outage) / oil-value-chain',
 'INVENTORY': 'demand-destruction (SPR clock)',
 'FED':       'new-economy-regime / market-fragility / predictions (the registered hike call)',
 'FLOWS':     'market-fragility (the 7/22 gearing frame + 8/8 record tech inflows) / detachment-bid / portfolio-state',
 'MODEL-ECON':'metered-compute / compression-thesis',
 'FX/CARRY':  'ai-financing-fragility (yen-carry corners the Fed, L491) / market-fragility / new-economy-regime',
 'AI-POLICY': 'ai-financing-fragility (blacklist timeline, F17 risk stack) / metered-compute (the NVDA letter, the council) / ai-capex-cycle (advisory council) / compression-thesis (two-bloc)',
 'KOREA':     'market-fragility (leverage cascade)',
 'LABOR':     'predictions/2026-07-30-fed-hike (the registered Friday trigger) / new-economy-regime',
 'MUNITIONS': 'war/war-board (escalation ceiling, the A-vs-C fork) / ai-capex-cycle (defense-AI crowding)',
 'ALLIANCE':  'war/war-board (MJDA 8/8 — verified; Article 5 language vs Article 5 capability) / demand-destruction / oil-value-chain',
 'LEVANT':    'war/war-board (talks-while-shooting; MoU Article 1 broke via Lebanon -- portfolio-state L143)',
 'TOKEN-ECON':'metered-compute (the Jevons/elasticity-1 test) / compression-thesis / cepi',
}
# ═══════════════ THREAD MAP END ═══════════════

# TWO KEYWORD CLASSES — this distinction is the whole gate and it was WRONG on first build.
# STRICT: short acronyms where a suffix creates a false positive. \bKWs?\b only.
#   spr must NOT match "spread"; cds must NOT match "CDSL"; dram must NOT match "drama".
# STEM: everything else gets up to 3 trailing chars, because headlines use plurals and
#   verb forms far more than base forms. (3 of 14 offline unit-test cases failed before this fix.)
STRICT = {'spr','cds','bdc','spv','hbm','pjm','smr','irgc','dram','nand','lng','cpc','smic',
          'yen','jpy','boj','dxy','ueda','mof','qt','sep','bls','nrc','smm','eia','rrp','mjda',
          'wti','glm','tpu','fcc','krx','idf','trs','13f'}
def _pat(k):
    return re.compile(r'\b'+re.escape(k)+(r's?\b' if k in STRICT else r'\w{0,3}\b'), re.I)
PATS = {th: [_pat(k) for k in ks] for th, ks in THREADS.items()}
NKEY = sum(len(v) for v in THREADS.values())

def tags(text):
    return [th for th, ps in PATS.items() if any(p.search(text) for p in ps)]

# ═══════════════════════════════════════════════════════════════════════════════
# OPEN FLAGS REGISTRY — the second gate, and the more important one.
#
# The keyword gate answers "is this ON-TOPIC". That is not the same question as
# "is this WORTH READING". A headline earns a follow-up only if it can CLOSE
# something the vault has registered as UNRESOLVED (⚠️) or LOGGED AS WRONG (⛔).
#
# Every entry below is a real, dated, open item from a vault note. `q` states what
# would actually resolve it — not the topic, the MISSING FACT. `pat` detects a
# candidate resolver. Retire an entry the moment it closes; a stale registry
# manufactures false urgency.
# ═══════════════════════════════════════════════════════════════════════════════
WATCH = [
 dict(id='F1', pri=1, note='ai-capex-cycle',        since='07-29',
      q='Is MSFT $130B new leases a SUBSET of the $329.1B uncommenced total, or ADDITIVE? '
        'A quarter that created a third of the off-balance-sheet obligation is a rate, not a stock.',
      pat=r'(lease|uncommenced|off.balance|329|130 ?b|\$130)'),
 dict(id='F2', pri=1, note='ai-financing-fragility', since='07-29',
      q='SPREAD, TENOR and TAKE-UP on the Goldman $5.4B MSFT-tied and Blue Owl $5.9B deals. '
        'Size alone supports neither containment nor cascade. Primary prices MARGINAL risk.',
      pat=r'(goldman|blue owl|data cent\w* (debt|loan|financ)|private credit|syndicat|spv)'),
 dict(id='F3', pri=1, note='memory-regime-question', since='07-28',
      q='The CXMT fork: glut vs politically walled out. Is the Senate action a LETTER or a BILL? '
        'A letter is noise; an enforcement mechanism is the wall. Second, COMMERCIAL evidence on '
        'the same fork: buyers signing multi-year supply deals are pre-committing AGAINST Chinese '
        'supply filling the gap — money at stake rather than votes.',
      pat=r'(cxmt|chinese memory|apple.*(memory|chip)|senator|export control|entity list|'
            r'long.?term supply|supply (deal|agreement)|multi.?year (supply|contract))'),
 dict(id='F4', pri=1, note='demand-destruction',     since='07-30',
      q='CPC/Kazakh loading status AFTER the 7/30 re-attack. Force majeure? August loading program? '
        'THE VAULT MISSED THIS THEATRE FOR ELEVEN DAYS — treat every CPC item as priority until caught up.',
      pat=r'(cpc|caspian|novorossiysk|tengiz|kashagan|kazakh|force majeure)'),
 dict(id='F5', pri=2, note='demand-destruction',     since='07-30',
      q='Are QatarEnergy\'s 33 US cargoes SPOT or TERM? Spot bridges weeks; term prices permanence. '
        'This is the cleanest available test of the structural-vs-episodic branch.',
      pat=r'(qatarenergy|qatar.*(lng|cargo)|33 cargo|term contract|spot cargo)'),
 dict(id='F6', pri=2, note='new-economy-regime',     since='07-30',
      q='The actual dissent COUNT and the 1970 comparison set. I retracted a 56-year record because '
        'it was engineered — intent revises meaning, not magnitude.',
      pat=r'(dissent|1970|fomc vote|voted against)'),
 dict(id='F7', pri=2, note='buildout-bottleneck-map', since='07-29',
      q='Ofgem commitment fee LEVEL, and is it REFUNDABLE on commencement? A refundable deposit is '
        'anti-squatting; a non-refundable fee is a real price on the optionality MSFT was rewarded for.',
      pat=r'(ofgem|commitment fee|connection queue|grid access|interconnect)'),
 dict(id='F8', pri=2, note='ai-financing-fragility',  since='07-29',
      q='The neocloud NAMED CASUALTY. Five sessions of double-digit drawdown, still nobody named. '
        'Absence is the strongest datum in the containment case — until it is not.',
      pat=r'(coreweave|nebius|neocloud|crusoe|lambda|default|covenant|going concern|missed payment)'),
 dict(id='F9', pri=3, note='memory-regime-question', since='07-30',
      q='SK hynix Q2 miss MAGNITUDE, and Micron CEO sale size + 10b5-1 status. A CEO sale without '
        'size, plan status and prior cadence is not evidence.',
      pat=r'(hynix.{0,40}(miss|consensus|target|guidance|shortfall)|10b5|mehrotra|(insider|ceo).{0,20}(sold|sale|selling))'),
 # F11 CLOSED 07-30: cap SPX -2.32% MTD vs EW SPX +1.39% -- inversion confirmed, and the
 # EW-vs-cap test returned the OPPOSITE sign from my prediction (damage is in the mega-caps,
 # not the crowded tail). Replaced by the live containment trigger, which is now a PRICE.
 dict(id='F11',pri=1, note='market-fragility',       since='07-30',
      q='CONTAINMENT KILL SWITCH: does RSP close below 212.77 (the 2026-06-30 close, -2.3% from '
        'the 07-28 ATH) while NDX keeps falling? That is the average S&P stock giving back all of '
        'July -- rotation has become a broad de-rate. Currently 215.73, -1.37% away.',
      pat=r'(equal.?weight|equal.?weighted|breadth|rotation|rotat\w+ out|average stock|rsp\b|advance.decline)'),
 dict(id='F13',pri=1, note='demand-destruction',      since='07-30',
      q='THE CRUX: is China\'s 40%%+ import cut (~4.4 mb/d, larger than every supply loss combined) a\n        SUSPENSION or a STRUCTURAL SHIFT? Reversible = reserve draws, coal switching, deferred buying.\n        Irreversible = EV substitution. Nobody has published the split. Watch the July/August import\n        bounce, Chinese gasoline demand vs EV penetration, and reserve levels.',
      pat=r'(china.{0,30}(import|crude|demand|purchas|refin|reserve|stockpil)|chinese (crude|oil|buyer|demand)|teapot|kpler|vortexa|sinopec|unipec|spr refill)'),
 dict(id='F12',pri=1, note='demand-destruction',      since='07-30',
      q='Saudi Q2 GDP: is GASTAT\'s oil -24.7%% y/y or q/q SA? And does Saudi ABANDON its ~1 mb/d\n        cut to defend volume? An oil economy down ~25%% with non-oil at +0.9%% is fiscal pressure to\n        stop cutting -- the crude BEAR case, and the vault runs only the war-premium side.',
      pat=r'(saudi|gastat|aramco|opec|quota|production cut|market share|yanbu|east.?west pipeline)'),
 dict(id='F10',pri=3, note='ai-capex-cycle',         since='07-30',
      q='Zhongji InnoLight break SIZE and terms, and whether other AI-supply-chain deals are pulled. '
        'One broken debut is a datum; a second is a primary-market regime.',
      pat=r'(innolight|zhongji|(ipo|debut|listing|offering).{0,40}(tumbl|slump|break|below|flop|pull|postpon|withdraw|price[ds] at))'),
]
WPATS = [(w, re.compile(w['pat'], re.I)) for w in WATCH]

# Brands Jake can open behind a paywall — these get marked [GET] in the follow-up queue,
# because a fetchable primary source outranks a free paraphrase of it. (The Axios/Pacing
# error was built entirely on a one-sentence paraphrase of a document I could have read.)
GETTABLE = ('reuters', 'wsj', 'wall street journal', 'bloomberg', 'ft', 'financial times')

def flags(text):
    return [w for w, p in WPATS if p.search(text)]

def brand(title, src):
    if src: return src
    m = re.search(r' [-–] ([^-–]{2,40})$', title)
    return m.group(1).strip() if m else ''

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
  # Second theatre. Do NOT fold this into GN-hormuz: a Hormuz-scoped query ranks Hormuz
  # results and buried an 1.8 mb/d Black Sea outage for eleven days. One feed per theatre.
  ('GN-blacksea', GN.format('CPC+OR+Novorossiysk+OR+Tengiz+OR+Kazakh+oil+export+when:1d')),
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
        out.append((dt, title, grab('description')[:200], grab('link'), grab('source')))
    return out, None

print('='*74)
print(f'  ACUTE SCANNER — last {HOURS}h  |  {NKEY} keywords / {len(THREADS)} threads')
print(f'  run {NOW:%Y-%m-%d %H:%M} UTC   cutoff {CUT:%Y-%m-%d %H:%M} UTC')
print('='*74)

px_block('INDEX / MACRO', INDEX)
front_end_block()
px_block('MAG 7 (independent)', MAG7)
px_block('MEMORY COMPLEX (independent)', MEM)

print('\n'+'='*74); print(f'  KEYWORD HITS ONLY — last {HOURS}h, financial tier first'); print('='*74)

seen, problems, grand, QUEUE = set(), [], 0, []
distinct = 0
for tier_idx, (tier_name, feeds) in enumerate(TIERS):
    hits = []
    for name, url in feeds:
        items, err = parse(name, url)
        if err: problems.append(err); continue
        for dt, title, desc, link, src in items:
            if dt < FCUT: continue       # widest window anything is considered in
            k = re.sub(r'[^a-z0-9]','', title.lower())[:60]
            if k in seen: continue
            th = tags(title+' '+desc)
            if not th: continue          # <-- the gate: direct keyword hit or it does not print
            seen.add(k)
            fl = flags(title+' '+desc)   # <-- the SECOND gate: does it close an open flag?
            if dt >= CUT: hits.append((dt, name, th, title, link, fl))
            # A flagged item enters the QUEUE on the WIDE window even when it is too old to
            # print in the tiers above -- the question is what is open, not what is fresh.
            if fl: QUEUE.append((dt, name, th, title, link, fl,
                                 brand(title, src), tier_idx))
    print(f'\n{"="*74}\n{tier_name}\n{"="*74}')
    if not hits:
        print('  no keyword hits in this tier.')
        continue
    hits.sort(key=lambda x: x[0], reverse=True)
    clustered = cluster_hits(hits)
    dup_tot = sum(len(d) for _, d in clustered)
    if dup_tot:
        print(f'  [{len(hits)} headlines -> {len(clustered)} DISTINCT EVENTS. '
              f'{dup_tot} are syndication of an event already shown below.]')
    for (dt, name, th, title, link, fl), dupes in clustered[:PER_TIER_CAP]:
        age = (NOW-dt).total_seconds()/60
        agestr = f'{age:.0f}m' if age < 90 else f'{age/60:.1f}h'
        star = ' ***OPEN FLAG '+','.join(w['id'] for w in fl) if fl else ''
        print(f'\n[{agestr:>5}] {name:<12} {"|".join(th)}{star}')
        print(f'        {title[:150]}')
        print(f'        -> {" ; ".join(ROUTE.get(t,"?") for t in th)}')
        if link: print(f'        {link[:110]}')
        if dupes:
            srcs = ', '.join(sorted({d[1] for d in dupes}))[:90]
            print(f'        (+{len(dupes)} same-event reprints: {srcs})')
    grand += len(hits); distinct += len(clustered)
    if len(clustered) > PER_TIER_CAP:
        print(f'\n  ...{len(clustered)-PER_TIER_CAP} more DISTINCT events in this tier (capped at {PER_TIER_CAP}).')

print('\n'+'='*74)
print(f'  TOTAL KEYWORD HITS: {grand}   ->   DISTINCT EVENTS: {distinct}'
      f'   ({grand-distinct} syndicated reprints, {(grand-distinct)/max(grand,1)*100:.0f}%)')
print('  ** READ THE DISTINCT COUNT, NOT THE HIT COUNT. Forty outlets reprinting one statement is')
print('     ONE datum. A big hit-count reads as high signal and is usually the opposite. **')
print('  Every hit carries a "->" line naming the vault note it belongs to. Read it into that')
print('  note, or explicitly decide it is noise. An unrouted hit is a skipped relevance check.')
if problems:
    print('  feed problems (missing coverage, not errors in the hits above):')
    for p in problems: print(f'    - {p}')

# ═══════════════════════════════════════════════════════════════════════════════
# PRIORITY FOLLOW-UP QUEUE — the fetch list.
# Grouped by OPEN FLAG, not by feed, because the unit of work is the QUESTION, not
# the headline. Within a flag: paywalled primary wires first (they are gettable and
# they outrank paraphrase), then by tier, then by recency.
# ═══════════════════════════════════════════════════════════════════════════════
print('\n'+'='*74)
print(f'  PRIORITY FOLLOW-UP QUEUE — fetch these, in this order  (flag window {FLAG_HOURS}h)')
print('='*74)
if not QUEUE:
    print('\n  Nothing in this window touches an open flag. That is a RESULT, not a gap:')
    print('  it means the news moved and the registered questions did not.')
else:
    by_flag = {}
    for row in QUEUE:
        for w in row[5]: by_flag.setdefault(w['id'], (w, []))[1].append(row)
    def rank(r):
        return (0 if any(g in (r[6] or '').lower() for g in GETTABLE) else 1, r[7], -r[0].timestamp())
    for fid in sorted(by_flag, key=lambda i: (by_flag[i][0]['pri'], i)):
        w, rows = by_flag[fid]
        rows.sort(key=rank)
        print(f"\n─── {fid}  [pri {w['pri']}]  {w['note']}   (open since {w['since']})")
        for i, ln in enumerate(textwrap.wrap(w['q'], 84)):
            print(('    Q: ' if i == 0 else '       ') + ln)
        print()
        for dt, name, th, title, link, fl, br, ti in rows[:4]:
            age = (NOW-dt).total_seconds()/60
            agestr = f'{age:.0f}m' if age < 90 else f'{age/60:.1f}h'
            get = '[GET]' if any(g in (br or '').lower() for g in GETTABLE) else '     '
            print(f'    {get} [{agestr:>5}] {br or name}')
            print(f'           {title[:120]}')
            if link: print(f'           {link}')
        if len(rows) > 4: print(f'    ...{len(rows)-4} more touching {fid}')
    open_ids = {w['id'] for w in WATCH} - set(by_flag)
    if open_ids:
        print(f"\n  OPEN FLAGS WITH NO CANDIDATE THIS WINDOW: {', '.join(sorted(open_ids))}")
        print('  Still unresolved. Silence is not closure — these stay on the registry.')
print('='*74)
