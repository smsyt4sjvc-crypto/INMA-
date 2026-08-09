#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════════════
#  THE LIBRARIAN — the single ingest gate.        Built 2026-08-08 (Jake's spec:
#  "a librarian that fetches things — there's errors every time we upload")
#
#  ONE COMMAND, run on EVERY inbound before any analysis:
#
#      python3 tools/librarian.py <<'EOF'
#      <the pasted text, or the extracted text of an upload>
#      EOF
#
#  It replaces the old multi-step STEP ZERO with five checks in one call:
#    1. CLOCK      — verified PDT + UTC printed first (the timestamp rule, baked in)
#    2. ROUTER     — the thread-map brief (⟲ trail, ⛔ corrections, ★★★, 🚩 flags)
#    3. SWEEP      — full-text scan of wiki/ for the inbound's DISTINCTIVE TOKENS,
#                    independent of the keyword map. Files the sweep finds that the
#                    router did NOT are flagged as VOCABULARY-GAP candidates.
#                    ⭐ This is the check that does not depend on anyone having
#                    predicted the vocabulary. It is why the librarian exists.
#    4. DUPE CHECK — the inbound's tokens vs raw/ + handoffs/ filenames (60 days).
#                    (Would have caught the 8/8 duplicate: the 8/4 Bernstein PDF
#                    was sitting in raw/ under 'bernstein…magnet-chokepoint'.)
#    5. OPEN ITEMS — today's + recent 🔴 open list, so what is OWED is in view.
#
#  THE BRIEF IS AN INDEX, NOT A SUBSTITUTE: if a line touches the inbound, OPEN
#  THE ENTRY. For document uploads / multi-thread dumps, the sanctioned escalation
#  is a librarian SUBAGENT that reads every surfaced entry in full and reports
#  back — spawned per-inbound inside the session (no standing daemon; see CLAUDE.md §0).
# ═══════════════════════════════════════════════════════════════════════════
import os, re, sys, subprocess, time
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI, RAW, HAND = (os.path.join(ROOT, d) for d in ('wiki', 'raw', 'handoffs'))

STOP = set('''the and for that with this from have been will was were are is not you your can could
would should about into over under more most than then them they their there here when where what
which while these those been being other after before between during against each such only also
just like some very much many said says new all but has had its per our out one two three per cent
percent billion million trillion year years month months week weeks day days today yesterday
tomorrow report reports reported according breaking news update market markets stock stocks price
prices company companies group total pace record levels level high low higher lower first second
third last next now still even both same source sources chart data'''.split())

def clock():
    pdt = subprocess.run(['date', '+%Y-%m-%d %I:%M%p %Z'], env={**os.environ, 'TZ': 'America/Los_Angeles'},
                         capture_output=True, text=True).stdout.strip()
    utc = subprocess.run(['date', '-u', '+%Y-%m-%d %H:%M UTC'], capture_output=True, text=True).stdout.strip()
    return pdt, utc

def distinctive_tokens(text, cap=45):
    """Tokens likely to be ENTITIES or MEASURES: originally-capitalised words, all-caps
    ticker-like strings, hyphenated terms, and 2-grams of capitalised words."""
    toks = Counter()
    words = re.findall(r"[A-Za-z][A-Za-z0-9&./-]{1,}", text)
    for i, w in enumerate(words):
        lw = w.lower().strip('.-/')
        if len(lw) < 3 or lw in STOP:
            continue
        cap_like = w[0].isupper() or w.isupper() or '-' in w
        if not cap_like:
            continue
        toks[lw] += 1
        if i + 1 < len(words) and words[i+1][:1].isupper():
            nx = words[i+1].lower().strip('.-/')
            if nx not in STOP and len(nx) >= 3:
                toks[f"{lw} {nx}"] += 1
    # prefer bigrams and repeated tokens; drop bare fragments of kept bigrams
    ranked = sorted(toks.items(), key=lambda kv: (-(' ' in kv[0]), -kv[1], kv[0]))
    return [t for t, _ in ranked[:cap]]

def sweep(tokens):
    """Grep each token across wiki/*.md, then keep only DISCRIMINATING tokens:
    a token found in more than ~35% of notes (china, america, market…) identifies
    nothing and is dropped before scoring. Per-file DISTINCT-token counts follow."""
    n_notes = sum(1 for _, _, fs in os.walk(WIKI) for x in fs if x.endswith('.md')) or 1
    ubiq_bar = max(4, int(n_notes * 0.35))
    tok_files, dropped = {}, []
    for tok in tokens:
        pat = re.escape(tok).replace(r'\ ', r'[\s-]+')
        try:
            out = subprocess.run(['grep', '-ril', '-E', pat, WIKI], capture_output=True, text=True, timeout=20).stdout
        except subprocess.TimeoutExpired:
            continue
        fs = [f for f in out.strip().split('\n') if f]
        if len(fs) > ubiq_bar:
            dropped.append(tok); continue
        tok_files[tok] = fs
    hits = {}
    for tok, fs in tok_files.items():
        for f in fs:
            hits.setdefault(os.path.relpath(f, ROOT), set()).add(tok)
    return {f: s for f, s in hits.items() if len(s) >= 2}, dropped

def dupes(tokens, days=60):
    now, out = time.time(), []
    for d in (RAW, HAND):
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            p = os.path.join(d, fn)
            if now - os.path.getmtime(p) > days * 86400:
                continue
            base = fn.lower()
            m = [t for t in tokens if ' ' not in t and (t in base or t.rstrip('s') in base)]
            if len(m) >= 2:
                out.append((os.path.relpath(p, ROOT), m))
    return sorted(out, key=lambda x: -len(x[1]))[:8]

def main():
    text = sys.stdin.read()
    if not text.strip():
        print('usage: python3 tools/librarian.py <<EOF ... EOF'); return
    pdt, utc = clock()
    W = 92
    print('═' * W)
    print('  📚 LIBRARIAN — the ingest gate. Run BEFORE analysis, on every inbound.'.ljust(W))
    print(f'  🕐 VERIFIED CLOCK: {pdt}   ({utc}) — stamp entries from THIS, not from vibes.')
    print('═' * W)

    # 2. router brief (thread map)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'vault_router.py')],
                       input=text, capture_output=True, text=True, timeout=120)
    print(r.stdout.rstrip())
    routed = set(re.findall(r'wiki/[\w/-]+\.md', r.stdout))
    router_strong = bool(re.search(r'matched threads:.*?\((?:[2-9]|\d\d+)\)', r.stdout))

    # 3. map-independent full-text sweep
    toks = distinctive_tokens(text)
    S, ubiq = sweep(toks)
    print('\n' + '─' * W)
    print('  🔎 FULL-TEXT SWEEP (map-independent) — DISCRIMINATING entity/measure tokens per note')
    if ubiq:
        print(f'     (dropped as ubiquitous, matching >35% of notes: {", ".join(ubiq[:10])})')
    if not S:
        print('     no multi-token hits. If the router ALSO matched nothing, this may be genuinely')
        print('     new territory — open a note, and add the vocabulary to the thread map.')
    for f, sset in sorted(S.items(), key=lambda kv: -len(kv[1]))[:10]:
        # cross-links are NORMAL — the gap warning is reserved for a sweep that finds a
        # note the map could not reach at all (router silent/weak) or an overwhelming hit.
        gap = (f not in routed) and not router_strong
        flag = '   ⚠️ MAP COULD NOT REACH THIS — vocabulary gap, add tokens to the thread map' if gap else ''
        print(f'     {len(sset):>2}  {f}{flag}')
        print(f'         tokens: {", ".join(sorted(sset)[:8])}')

    # 4. raw/ + handoffs/ dupe check
    D = dupes([t for t in toks if ' ' not in t])
    print('\n' + '─' * W)
    print('  🗃️  ARTIFACT DUPE CHECK (raw/ + handoffs/, 60 days) — has this been archived before?')
    if not D:
        print('     nothing similar on file.')
    for p, m in D:
        print(f'     ≈ {p}   (matched: {", ".join(m)})')
        print('       → if this inbound is ABOUT the same object, the vault already has an entry. FIND IT.')

    # 5. open items
    print('\n' + '─' * W)
    print('  🔴 OPEN ITEMS this inbound might close (chat_log --open, tail):')
    try:
        o = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'chat_log.py'), '--open'],
                           capture_output=True, text=True, timeout=30).stdout
        tail = [l for l in o.split('\n') if l.strip()][-14:]
        print('\n'.join('     ' + l for l in tail))
    except Exception as e:
        print(f'     (chat_log unavailable: {e})')

    print('═' * W)
    print('  THE BRIEF IS AN INDEX, NOT A SUBSTITUTE. If a line touches the inbound, OPEN THE ENTRY.')
    print('  Uploads / multi-thread dumps → spawn the librarian SUBAGENT to read entries in full.')
    print('═' * W)

if __name__ == '__main__':
    main()
