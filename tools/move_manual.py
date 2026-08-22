#!/usr/bin/env python3
"""
move_manual.py -- append a hand-fetched MOVE reading into the dashboard.

WHY THIS EXISTS. Every automated route to the MOVE index is blocked from a
datacentre IP: Yahoo 429s from this container AND from GitHub runners, CNBC 403s,
WSJ 401s, Nasdaq does not carry it, Stooq is JS-gated, and FRED's VXTYN was
discontinued in May 2020. MOVE is ICE BofA proprietary and has no free feed.

What is NOT blocked is a residential IP -- i.e. Jake's phone or laptop. So the
fallback is a human reading one number a day. This tool is what makes that one
number PERSIST: without it a pasted value is a comment in a chat log, and the
dashboard stays blind.

USAGE
    python3 tools/move_manual.py 2026-08-21 73.40
    python3 tools/move_manual.py --from-paste "MOVE 73.40"       # date = today
    python3 tools/move_manual.py --status                        # what's missing

⚠️ A HAND-ENTERED ROW IS STILL DATA AND IS TREATED AS SUCH: it lands in the same
CSV as every fetched series and is scored identically. The provenance column is
what keeps that honest -- never silently mix it with a machine pull.
"""
import csv, os, sys
from datetime import date, datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SER  = os.path.join(ROOT, "data", "fragility", "series")
CSV  = os.path.join(SER, "move.csv")
PROV = os.path.join(ROOT, "data", "fragility", "move_provenance.csv")


def load():
    if not os.path.exists(CSV):
        return {}
    out = {}
    with open(CSV) as fh:
        for r in csv.DictReader(fh):
            try:
                out[r["date"]] = float(r["value"])
            except (ValueError, KeyError, TypeError):
                pass
    return out


def save(rows):
    os.makedirs(SER, exist_ok=True)
    with open(CSV, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "value"])
        w.writerows(sorted((d, round(v, 6)) for d, v in rows.items()))


def note_provenance(d, v):
    new = not os.path.exists(PROV)
    with open(PROV, "a", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["date", "value", "entered_utc", "source"])
        w.writerow([d, v, datetime.utcnow().isoformat(timespec="seconds"), "manual"])


def status():
    rows = load()
    if not rows:
        print("move.csv is empty.")
        return
    last = max(rows)
    ld = datetime.strptime(last, "%Y-%m-%d").date()
    gap = (date.today() - ld).days
    print(f"MOVE last value : {rows[last]:.2f} on {last}  ({gap} days old)")
    missing = []
    d = ld + timedelta(days=1)
    while d < date.today():
        if d.weekday() < 5:
            missing.append(d.isoformat())
        d += timedelta(days=1)
    if missing:
        print(f"MISSING weekdays ({len(missing)}): {', '.join(missing[-10:])}")
        print("\nEach one is a row that cannot be recovered later -- MOVE has no "
              "history endpoint at any price.")
    else:
        print("No missing weekdays.")


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return
    if a[0] == "--status":
        status()
        return

    if a[0] == "--from-paste":
        txt = " ".join(a[1:])
        nums = [t for t in txt.replace(",", " ").split()
                if t.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if not nums:
            sys.exit(f"no number found in: {txt!r}")
        d, v = date.today().isoformat(), float(nums[-1])
    else:
        if len(a) < 2:
            sys.exit("usage: move_manual.py YYYY-MM-DD VALUE")
        d, v = a[0], float(a[1])
        datetime.strptime(d, "%Y-%m-%d")           # validate or raise

    if not (20 <= v <= 300):
        sys.exit(f"⛔ {v} is outside any plausible MOVE range (20-300). "
                 "Refusing -- check you did not paste a price or a percent.")

    rows = load()
    prev = rows.get(d)
    rows[d] = v
    save(rows)
    note_provenance(d, v)
    if prev is not None and abs(prev - v) > 1e-9:
        print(f"⚠️ OVERWROTE {d}: {prev:.2f} -> {v:.2f}")
    print(f"✅ MOVE {v:.2f} recorded for {d}  ({len(rows)} rows total)")
    print("\nNow run:  python3 tools/fragility.py")


if __name__ == "__main__":
    main()
