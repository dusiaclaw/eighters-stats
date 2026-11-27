"""Build group tables for given years from scan CSVs + Eighters games in stats.json.
Usage (from the repo folder): python3 -I tools/build_standings.py . data/group-games <year> [<year>...]  (prints JSON; --write to store)"""
import csv, json, sys
repo, scan, *rest = sys.argv[1:]
write = '--write' in rest
years = [y for y in rest if y != '--write']
EIG = 'Zürich Eighters'
EAST23 = {EIG, 'SG Pirates/Lions', 'Embrach Mustangs 2', 'SG Wittenbach-Romanshorn 2/Wil Devils 4', 'Zürich Barracudas 4', 'Zürich Challengers 3'}
GROUP = {'2020': ('1. Liga', None), '2021': ('NLB', None), '2022': ('1. Liga', None), '2023': ('1. Liga Ost', EAST23)}
path = f'{repo}/data/stats.json'
S = json.load(open(path))
out = {}
for y in years:
    games = []  # (date, id, away, home, away_r, home_r)
    for r in csv.DictReader(open(f'{scan}/{y}.csv', encoding='utf-8')):
        if r['round'] != 'VR' or 'eighters-check' in (r.get('note') or ''):
            continue
        games.append((r['date'], int(r['id']), r['away'], r['home'], int(r['away_r']), int(r['home_r'])))
    for g in S['games'][y]:
        if g.get('rd', 'VR') != 'VR':
            continue
        a, h = (g['opp'], EIG) if g['home'] else (EIG, g['opp'])
        ar, hr = (g['ra'], g['r']) if g['home'] else (g['r'], g['ra'])
        games.append((g['d'], g['id'], a, h, ar, hr))
    ids = [g[1] for g in games]
    assert len(ids) == len(set(ids)), f'{y}: duplicate game ids'
    games.sort()
    T = {}
    def t(n):
        return T.setdefault(n, dict(W=0, L=0, hw=0, hl=0, aw=0, al=0, RS=0, RA=0, res=[]))
    ties = []
    for d, gid, a, h, ar, hr in games:
        A, H = t(a), t(h)
        A['RS'] += ar; A['RA'] += hr; H['RS'] += hr; H['RA'] += ar
        if ar == hr:
            ties.append(gid); continue
        aw = ar > hr
        A['W' if aw else 'L'] += 1; H['L' if aw else 'W'] += 1
        A['aw' if aw else 'al'] += 1; H['hl' if aw else 'hw'] += 1
        A['res'].append('W' if aw else 'L'); H['res'].append('L' if aw else 'W')
    keep = GROUP[y][1]
    rows = []
    for n, x in T.items():
        if keep and n not in keep:
            continue
        s = x['res']; k = 0
        while k < len(s) and s[-1 - k] == s[-1]:
            k += 1
        rows.append([n, x['W'], x['L'], f'{s[-1]}{k}' if s else '', f"{x['hw']}-{x['hl']}", f"{x['aw']}-{x['al']}", x['RS'], x['RA']])
    rows.sort(key=lambda r: (-(r[1] / max(r[1] + r[2], 1)), -r[1], -(r[6] - r[7]), r[0]))
    names = {r[0] for r in rows}
    n = sum(1 for g in games if g[2] in names or g[3] in names)
    out[y] = {'rows': rows, 'n_games': n, 'ties': ties}
    print(y, f"{out[y]['n_games']} games", 'ties:', ties)
    for r in rows:
        print('  ', r)
if write:
    for y, v in out.items():
        S['standings'][y] = {'group': GROUP[y][0], 'rows': v['rows'], 'built': 1, 'n': v['n_games']}
    open(path, 'w', encoding='utf-8').write(json.dumps(S, separators=(',', ':'), ensure_ascii=False, sort_keys=True))
    print('written')
