"""Eighters-only season record (no group table) from a scan CSV, for seasons without a clear group.
Usage (from the repo folder): python3 -I tools/build_records.py . data/group-games <year>... [--write]
Reads <year>.csv and <year>_meta.json (eighters_id, optional eighters_alt_ids); keeps VR rows only."""
import csv, json, sys
repo, scan, *rest = sys.argv[1:]
write = '--write' in rest
years = [y for y in rest if y != '--write']
path = f'{repo}/data/stats.json'
S = json.load(open(path, encoding='utf-8'))
S.setdefault('records', {})
for y in years:
    m = json.load(open(f'{scan}/{y}_meta.json', encoding='utf-8'))
    ids = {str(m['eighters_id'])} | {str(i) for i in m.get('eighters_alt_ids', [])}
    r = dict(W=0, L=0, T=0, RS=0, RA=0, hw=0, hl=0, aw=0, al=0, n=0)
    seen = set()
    for g in csv.DictReader(open(f'{scan}/{y}.csv', encoding='utf-8')):
        if g['round'] != 'VR' or g['id'] in seen:
            continue
        home = g['home_id'] in ids
        if not home and g['away_id'] not in ids:
            continue
        seen.add(g['id'])
        us, them = (int(g['home_r']), int(g['away_r'])) if home else (int(g['away_r']), int(g['home_r']))
        r['n'] += 1; r['RS'] += us; r['RA'] += them
        if us == them:
            r['T'] += 1; continue
        k = 'W' if us > them else 'L'
        r[k] += 1
        r[('h' if home else 'a') + k.lower()] += 1
    if not r['T']:
        del r['T']
    print(y, r)
    S['records'][y] = r
if write:
    open(path, 'w', encoding='utf-8').write(json.dumps(S, separators=(',', ':'), ensure_ascii=False, sort_keys=True))
    print('written')
