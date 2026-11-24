# Eighters-stats

Season and player stats for the **Zürich Eighters** baseball club, 2016–2026: team scoreboard, line scores and standings, a page per player with their jersey, and the full roster with the positions each player covered.

No account, no ads, no tracking. It is one web page that also installs as an app.

**Open it:** https://dusiaclaw.github.io/eighters-stats/

## What's inside
- **Team:** record, runs, standings, runs by inning, team totals and every season compared. Pick one season, a from–to range, or combine any seasons you like.
- **Players:** the player's Eighters jersey with name and number, key stats with team ranks, innings by position, season-by-season history and a link to the EasyScore player page. Leaderboards and a sortable full stats table.
- **Roster:** every player as a compact tile with a 9-position strip (brighter = more innings in the selected seasons).
- **2026 games:** click a game to open its EasyScore box score with the win-probability chart.
- **Settings** (gear button): light or dark theme, include or hide Lions & Ravens players, version and updates, what's new, install instructions, license.

## Install (Android / Chrome)
Open the app's web address in Chrome → menu → **Install app**.

**iPhone / iPad:** open it in Safari → Share → **Add to Home Screen**.
**Computer (Chrome or Edge):** click the install icon at the end of the address bar.

## Hosting on GitHub Pages
Repo **Settings › Pages** → Source **Deploy from a branch** → branch `main`, folder `/ (root)`. The app is then served at `https://<owner>.github.io/eighters-stats/`.

## Updating the data
The stats come from [EasyScore](https://www.easyscore.com) season totals and are stored in `data/stats.json` (players, seasons, 2026 games and standings, innings by position). After changing the data or `src/template.html`:

```
python3 build.py        # writes index.html from src/template.html + data/stats.json
```

## Releasing a new version
1. Edit `APP_VERSION` and add an entry to `CHANGELOG` in `src/template.html`.
2. Run `python3 build.py`, then `python3 make-version.py` (writes `version.json`, bumps the cache name in `sw.js`, writes `CHANGELOG.md`).
3. Commit and push. Installed apps pick up the new version at the next start (Settings › Check for updates).

## Data sources
Stats: [EasyScore](https://www.easyscore.com) (publicly available). Names and jersey numbers: the club team list and [eighters.ch](https://eighters.ch). "Z-License" is a placeholder name for players scored without a profile. Records for 2016–2023 come from pitcher win/loss decisions; 2024–2026 from the group standings.

## License
GPL-3.0 – see `LICENSE`. Fonts: Archivo, Anton and Big Shoulders Display via Google Fonts (SIL Open Font License). Jersey artwork drawn after the KNoah Eighters team jersey. Lions and Ravens logos belong to their clubs.
