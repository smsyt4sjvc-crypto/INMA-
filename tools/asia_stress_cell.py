
# ============================================================================
#  ASIA STRESS — is the Korea crash TRANSMITTING, or is it contained?
#  Equity beta has already been tested 3 sessions and failed. This cell reads
#  the channels that could still transmit: FX/funding, carry, gold, US futures.
#  Run it while Asia is open. Token-free.
# ============================================================================
import subprocess, sys, time
try:
    import yfinance as yf
except Exception:
    subprocess.run([sys.executable,'-m','pip','install','-q','yfinance']); import yfinance as yf
import numpy as np, pandas as pd

GROUPS = {
 'ASIA EQUITY (the event)': [('^KS11','KOSPI'), ('^KQ11','KOSDAQ'), ('^N225','Nikkei'),
                             ('^TWII','Taiwan'), ('^HSI','HangSeng'), ('000001.SS','Shanghai')],
 '★ FX / FUNDING (channel a)': [('KRW=X','USD/KRW'), ('JPY=X','USD/JPY'), ('TWD=X','USD/TWD'),
                                ('CNY=X','USD/CNY'), ('DX-Y.NYB','DXY')],
 '★ US FUTURES (the gauge)': [('NQ=F','Nasdaq fut'), ('ES=F','S&P fut'), ('YM=F','Dow fut'),
                              ('RTY=F','R2K fut')],
 '★ REFEREE (channel d)': [('GC=F','Gold'), ('SI=F','Silver'), ('^TNX','US 10Y'), ('CL=F','WTI')],
 'THE NAMES': [('005930.KS','Samsung Elec'), ('000660.KS','SK hynix'),
               ('2330.TW','TSMC'), ('MU','Micron')],
}
ALL = [t for g in GROUPS.values() for t,_ in g]

def fetch(tickers, period='3mo', tries=3):
    last, best = None, {}
    for i in range(tries):
        try:
            df = yf.download(tickers, period=period, progress=False,
                             auto_adjust=True, threads=True)['Close']
            if isinstance(df, pd.Series): df = df.to_frame(tickers[0])
            out = {c: df[c].dropna() for c in df.columns if df[c].dropna().size > 2}
            if len(out) > len(best): best = out
            if len(out) >= len(tickers) - 2: return out
            last = f'{len(out)}/{len(tickers)} returned'
        except Exception as e:
            last = e
        if i < tries-1:
            print(f'  ...attempt {i+1}: {last}; retry in {2**i}s'); time.sleep(2**i)
    if best:
        print(f'  !! PARTIAL ({len(best)}/{len(tickers)}). Missing lines say NOT AVAILABLE.')
        return best
    print(f'  !! ALL FETCHES FAILED: {last}'); return {}

print('='*68); print('  ASIA STRESS — transmitting, or contained?'); print('='*68)
D = fetch(ALL)
if not D:
    print('\n  NO DATA. Re-run in 60s or use a fresh Colab runtime.'); raise SystemExit

def stats(t):
    s = D.get(t)
    if s is None or len(s) < 2: return None
    px = float(s.iloc[-1]); d1 = (px/float(s.iloc[-2])-1)*100
    n20 = min(21, len(s)); m = (px/float(s.iloc[-n20])-1)*100
    dd = (px/float(s.max())-1)*100
    return px, d1, m, dd, s.index[-1].date()

for g, items in GROUPS.items():
    print(f'\n### {g}')
    print(f'  {"":14}{"last":>12}{"1d%":>9}{"~1mo%":>9}{"vs 3mo hi":>11}   as of')
    for t, lab in items:
        r = stats(t)
        if r is None: print(f'  {lab:14}   -- NOT AVAILABLE'); continue
        px, d1, m, dd, dt = r
        print(f'  {lab:14}{px:>12,.2f}{d1:>+9.2f}{m:>+9.1f}{dd:>+11.1f}   {dt}')

# ---------------- the reads ----------------
print('\n' + '='*68); print('  THE CHANNELS'); print('='*68)

def val(t, i=1):
    r = stats(t); return r[i] if r else None

k1, k20 = val('^KS11'), val('^KS11', 2)
if k20 is not None:
    print(f'\n[event] KOSPI {k1:+.2f}% today, {k20:+.1f}% over ~1 month.')

krw, jpy = val('KRW=X'), val('JPY=X')
print('\n[a] FX / FUNDING — the channel that reaches the S&P without touching Korean beta')
if krw is None: print('    USD/KRW NOT AVAILABLE — channel (a) unreadable.')
else:
    print(f'    USD/KRW {krw:+.2f}% today ({val("KRW=X",2):+.1f}% ~1mo)   USD/JPY {jpy:+.2f}%'
          if jpy is not None else f'    USD/KRW {krw:+.2f}% today')
    print('    ' + ('-> KRW WEAKENING HARD: foreign selling / repatriation pressure. Channel (a) LIVE.'
                    if krw > 0.7 else
                    ('-> KRW soft but orderly. Channel (a) not yet firing.' if krw > 0
                     else '-> KRW FIRM despite the equity crash = domestic, not a capital-flight event.'
                          ' Strongest single argument for containment.')))

print('\n[c] CARRY — the Aug-2024 replay mechanism')
if jpy is None: print('    USD/JPY NOT AVAILABLE.')
else:
    print('    ' + (f'-> YEN STRENGTHENING ({jpy:+.2f}%): carry unwind pressure. This is how Asia stress'
                    '\n       reached US megacaps in Aug-2024.' if jpy < -0.5 else
                    f'-> yen {jpy:+.2f}%: no carry-unwind signal.'))

print('\n[d] REFEREE — does GOLD sell WITH equities?')
g1 = val('GC=F')
if g1 is None: print('    Gold NOT AVAILABLE.')
else:
    print('    ' + (f'-> GOLD DOWN {g1:+.2f}% WITH equities = LIQUIDATION signature'
                    ' (margin calls sell what is liquid).' if g1 < -0.3 else
                    f'-> gold {g1:+.2f}%: bidding or flat while Korea crashes = CONTAINED / rotation, not a'
                    ' forced-selling event.'))

print('\n[GAUGE] US FUTURES — Jake\'s registered contagion gauge')
nq, es = val('NQ=F'), val('ES=F')
if nq is None: print('    NQ NOT AVAILABLE.')
else:
    print(f'    NQ {nq:+.2f}%   ES {es:+.2f}%' if es is not None else f'    NQ {nq:+.2f}%')
    if k1 is not None:
        print('    ' + (f'-> KOSPI {k1:+.1f}% and NQ only {nq:+.2f}% = the equity channel FAILED AGAIN.'
                        '\n       Nth consecutive session of non-transmission; containment case strengthens.'
                        if nq > -1.0 else
                        f'-> KOSPI {k1:+.1f}% and NQ {nq:+.2f}% = THE CHANNEL OPENED. Re-read everything.'))

print('\n' + '='*68)
print('  WHAT WOULD ACTUALLY CHANGE THE READ (none of it is a price)')
print('  1. A NAMED CASUALTY — a Korean securities house, fund gate, or structured product.')
print('     Its ABSENCE is the strongest argument for containment. Watch the wires, not the tape.')
print('  2. KRW breaking out = forced selling of FOREIGN assets to meet domestic margin.')
print('  3. Yen strengthening = carry unwind = the Aug-2024 transmission path.')
print('  4. Gold selling WITH equities = liquidation, not rotation.')
print('  COUNTER: Korea is a retail-margin market that fell 8.8% in a day in Aug-2024 and fully')
print('  recovered in weeks. Circuit breakers break price discovery - you cannot read "orderly"')
print('  or "disorderly" off a market that keeps halting.')
print('='*68)
