
# ============================================================================
#  VIX TERM STRUCTURE — "CALM or COILED?"
#  Settles the 7/28 disagreement: is the low VIX genuine calm (Claude's read)
#  or pre-event paralysis with thin hedges (Jake's read, backed by Mag-7 RVOL)?
#  Run it BEFORE the 11:00am PT FOMC. Token-free.
# ============================================================================
import subprocess, sys
try:
    import yfinance as yf
except Exception:
    subprocess.run([sys.executable,'-m','pip','install','-q','yfinance']); import yfinance as yf
import numpy as np, pandas as pd

VOLS = [('^VIX9D','VIX9D  9-day'), ('^VIX','VIX   30-day'),
        ('^VIX3M','VIX3M  3-month'), ('^VIX6M','VIX6M  6-month')]
EXTRA = [('^VVIX','VVIX  vol-of-vol'), ('^SKEW','SKEW  tail bid')]
MAG7  = ['NVDA','MSFT','AAPL','GOOGL','AMZN','META','TSLA']

def hist(t, period='1y'):
    try:
        h = yf.download(t, period=period, progress=False, auto_adjust=True)['Close'].dropna()
        if hasattr(h,'columns'): h = h.iloc[:,0]
        return h
    except Exception:
        return None

print('='*64)
print('  VIX TERM STRUCTURE — calm or coiled?')
print('='*64)

# ---------- 1. the curve ----------
lv, series = {}, {}
print('\n### THE CURVE (spot levels)')
for t, lab in VOLS:
    h = hist(t)
    if h is None or not len(h):
        print(f'  {lab:16} n/a'); continue
    series[t] = h; lv[t] = float(h.iloc[-1])
    ch = (float(h.iloc[-1])/float(h.iloc[-2])-1)*100 if len(h) > 1 else float('nan')
    print(f'  {lab:16}{lv[t]:>8.2f}   {ch:>+7.2f}%')
for t, lab in EXTRA:
    h = hist(t)
    if h is None or not len(h): continue
    series[t] = h; lv[t] = float(h.iloc[-1])
    ch = (float(h.iloc[-1])/float(h.iloc[-2])-1)*100 if len(h) > 1 else float('nan')
    print(f'  {lab:16}{lv[t]:>8.2f}   {ch:>+7.2f}%')

# ---------- 2. THE DISCRIMINATOR ----------
print('\n### THE DISCRIMINATOR  (VIX9D / VIX)')
if '^VIX9D' in lv and '^VIX' in lv:
    r = lv['^VIX9D']/lv['^VIX']
    s = (series['^VIX9D']/series['^VIX'].reindex(series['^VIX9D'].index).ffill()).dropna()
    pct = (s < r).mean()*100
    print(f'  ratio {r:.3f}   ({pct:.0f}th percentile of the last 12 months)')
    if   r >= 1.05: v = 'COILED — near-dated event premium. JAKE IS RIGHT: hedges thin, reaction unabsorbed.'
    elif r >= 1.00: v = 'MILDLY COILED — front end bid. Leans Jake.'
    elif r >= 0.92: v = 'NORMAL — no event premium priced. Leans Claude (genuine calm).'
    else:           v = 'COMPLACENT — front end unusually cheap vs 30d. Strongest form of the calm read.'
    print(f'  VERDICT: {v}')

print('\n### SLOPE  (VIX / VIX3M)')
if '^VIX' in lv and '^VIX3M' in lv:
    r2 = lv['^VIX']/lv['^VIX3M']
    print(f'  ratio {r2:.3f}   ->  ' + ('BACKWARDATION = real stress, not just event risk'
          if r2 > 1.0 else ('FLAT/kinked — transition' if r2 > 0.95 else 'CONTANGO = normal, no systemic bid')))

# ---------- 3. is the low VIX just DISPERSION arithmetic? ----------
print('\n### CORRELATION CHECK — is the low VIX just dispersion math?')
print('    (realised 10d vol: index vs average Mag-7 component)')
def rvol(h, n=10):
    lr = np.log(h/h.shift(1)).dropna()
    return float(lr.tail(n).std()*np.sqrt(252)*100)
spx = hist('^GSPC','6mo')
idx_v = rvol(spx) if spx is not None and len(spx) > 12 else None
comp = []
for t in MAG7:
    h = hist(t,'6mo')
    if h is not None and len(h) > 12:
        v = rvol(h); comp.append(v); print(f'    {t:6}{v:>7.1f}%')
if idx_v and comp:
    avg = sum(comp)/len(comp)
    ratio = idx_v/avg
    print(f'    {"SPX":6}{idx_v:>7.1f}%   |  Mag-7 avg {avg:.1f}%   |  index/component = {ratio:.2f}')
    print('    ' + ('-> LOW ratio = correlation collapse. The low VIX is substantially DISPERSION ARITHMETIC,'
                    '\n       not a judgment that risk is contained. (Claude conceded this 7/28.)'
                    if ratio < 0.55 else
                    '-> ratio normal/high = components moving TOGETHER. A low VIX here would be a real'
                    '\n       judgment about risk, not an artifact.'))

# ---------- 4. variance risk premium ----------
print('\n### VARIANCE RISK PREMIUM  (VIX vs realised SPX vol)')
if idx_v and '^VIX' in lv:
    vrp = lv['^VIX'] - idx_v
    print(f'  VIX {lv["^VIX"]:.2f}  −  realised10d {idx_v:.1f}  =  {vrp:+.1f} pts')
    print('  ' + ('-> NEGATIVE: implied is BELOW realised. Options are cheap vs what the tape is actually doing.'
                  '\n     This is the strongest quantitative form of Jake\'s "hedge is underpriced" case.'
                  if vrp < 0 else
                  '-> positive: normal insurance premium. Hedges are not obviously cheap.'))

print('\n' + '='*64)
print('  HOW TO READ IT')
print('  VIX9D/VIX >= 1.00      -> COILED  (event premium, thin hedges)  = Jake')
print('  VIX9D/VIX <  0.92      -> CALM    (no event premium priced)     = Claude')
print('  VIX/VIX3M  >  1.00     -> BACKWARDATION = real stress on top of event risk')
print('  index/component < 0.55 -> the low VIX is dispersion math, not a risk judgment')
print('  VRP negative           -> implied below realised = the hedge is genuinely cheap')
print('  COUNTER (do not skip): the base rate is VIX CRUSHING after the event, not popping.')
print('  A coiled VIX pays on MAGNITUDE in either direction, not on direction. In-line = it expires worthless.')
print('='*64)
