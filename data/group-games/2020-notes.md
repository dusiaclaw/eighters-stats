# 2020 scan progress (league 84, VR round 57)
Eighters TeamID 342. Eighters VR games known: 11149 11150 11158 11160 11174 11175 (not fetched).
## Teams
- 342 Zürich Eighters
- 11295 Embrach Mustangs 2 (pitcher Ruosch Florian 19886, from 11149)
- 11297 SG Pirates III (pitchers Borando Antonio 3498, Isenring Roger 3751, from 11150)
- 11299 Zürich Barracudas Academy (pitchers Brüderli Nils 28937, Lutz Tiago 31889, Eigenheer Seiya Ken 31870, from 11160)
- 1190 Zürich Challengers 3 (pitcher Benz Denyo 19734, from 11175)
## Player logs pulled
## Candidate game IDs
## Done

### Logs pulled (cat=off)
- 19886 Ruosch (Embrach 2): 11149 E8, 11151 PirIII, 11171 Chall3, 11172 BarIII, 11173 Chall3, 11174 E8
- 3751 Isenring (Pirates III): 11150 E8, 11151 Embr2, 11158 E8, 11159 BarAcad, 11167 BarAcad, 11169 PirIV
- 31889 Lutz (Barracudas Academy?): 11159 PirIII, 11160 E8, 11167 PirIII, 11168 PirIV, 11176 PirIV, 11178 BarIII
- 19734 Benz (Challengers 3): 11162 BarIII, 11163 PirIV, 11170 BarIII, 11171 Embr2, 11173 Embr2, 11175 E8
Other teams in league (not in S): SG Pirates IV, Zürich Barracudas III.
### Candidate S-vs-S games (non-Eighters): 11151, 11159, 11167, 11171, 11173
- 3498 Borando (Pirates III): 11150 E8, 11151 Embr2, 11167 BarAcad, 11169 PirIV
- 28937 Brüderli (Barracudas Academy): 11159 PirIII, 11160 E8, 11167 PirIII, 11168 PirIV, 11176 PirIV, 11178 BarIII
Unseen IDs in 11149-11180 to probe: 11152-11157, 11161, 11164-11166, 11177, 11179, 11180
Done: 11151, 11159, 11167
Done: 11171, 11173. Now probing gap IDs.
Probes: 11152 = teams 273 vs 340 (other group); 11153 = 8798 vs 273 (other group, empty box); 11154 = empty box (unknown)
Probes: 11155 = 11294 vs 8798; 11156 = 643 vs 11294; 11157 = 8798 vs 643 (all other group); 11161 = 343 @ 11298 (likely Barracudas III / Pirates IV, not in S)
Probes: 11164 = 643 @ 11294; 11165 = 340 @ 643; 11166 = 11294 @ 340 (all other group)
Probes: 11177 = 343 @ 11298 (not S); 11179, 11180 = Korean teams 11279/11275, 11273/11274 (another league entirely, ID range ends). Checking 11154 via get_game.
11154 (get_game) = Bern Cardinals 2 (340) @ Luzern Eagles III (8798), not played/no box; other group.

## Status: COMPLETE
All IDs 11149-11180 accounted for. Saved 5 non-Eighters S-vs-S games: 11151, 11159, 11167, 11171, 11173.
Excluded (involve teams outside S): 11162, 11163, 11168, 11169, 11170, 11172, 11176, 11178 (vs SG Pirates IV / Zürich Barracudas III), 11161, 11177 (343 @ 11298, presumably those two teams).
Other-group IDs: 11152-11157, 11164-11166 (teams 273, 340, 643, 8798, 11294). 11179-11180: different (Korean) league.

## Extension (coordinator request): S += SG Pirates IV, Zürich Barracudas III
Already have boxes: 11161 = 343 (away) 12 @ 11298 (home) 2, hits 7/1; 11177 = 343 9 @ 11298 6, hits 7/8. Dates TBD from logs.
To fetch: 11162 11163 11168 11169 11170 11172 11176 11178
TeamIDs confirmed: 343 = Zürich Barracudas III (Benz log 11162 opp), 11298 = SG Pirates IV (Benz log 11163 opp). Done: 11162 11163 11168 11169
Done: 11170 11172 11176 11178. Oddity: pitcher Würsten Samuel 15793 listed under 343 in 11170/11178 but under 11299 in 11176. Next: logs of BarIII (Isik 3753, Bekkali 3459) and PirIV (Entner 3611, Sterchi 4116).
Logs: 3459 Bekkali (BarIII): 11161 PirIV, 11162 Chall3, 11170 Chall3, 11172 Embr2 (+11470 PL, ignored). 3611 Entner (PirIV): 11161, 11168, 11169, 11176, 11177. 4116 Sterchi (PirIV): 11163, 11168, 11176. No new VR games. Dates: 11161 = 08-08, 11177 = 09-06.
Done: 11161 11177. Extension COMPLETE (15 non-Eighters games in CSV).
