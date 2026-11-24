#!/usr/bin/env python3
"""Builds index.html from src/template.html and data/stats.json.
Run after changing the template or the data, then run make-version.py."""
import pathlib
root = pathlib.Path(__file__).parent
t = (root / 'src' / 'template.html').read_text(encoding='utf-8')
d = (root / 'data' / 'stats.json').read_text(encoding='utf-8').strip()
assert '__DATA__' in t
(root / 'index.html').write_text(t.replace('__DATA__', d, 1), encoding='utf-8')
print('index.html built')
