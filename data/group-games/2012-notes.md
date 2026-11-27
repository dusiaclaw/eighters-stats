# 2012 scan progress (1.Liga leagueID 84, VR round 57)
Eighters TeamID 342 (Zürich Eighters, abbrev EIGW).
## Teams seen in Individual stats 2012 (lg 84)
309 SG MUS/VIK (3435 Albrecht, 3770 Kästli); 343 Zürich Barracudas III (9080, 8239); 345 SG Submarines/Bandits (3847, 4082); 349 Luzern Eagles 2 (3609, 3821); 342 Eighters (4142 Sutton, 3665, 4122, 3882 Moor)
(118 of 209 player rows have no team -> other teams exist)
## Logs pulled
- 4142 Sutton (EIG) off: VR 2040,2041 (04-22), 2045,2046 (04-28), 2050 (04-29 vs SUB), 2061 (05-13), 2069 (06-03 vs MUS/VIK), 2079 (06-16 vs BAR III), 2085,2086 (06-30), 2095 (07-14). PR games 2144-2167 ignored.
## Done
- 2040 done (box+game: EIG away 14, 351 home 8 @ Thun; 351 name null, not in list_teams 84)
- 2041 done (box: 336 away 20, EIG home 2; pitcher 4232 for 336)
- list_teams 84/83: 336 and 351 not in any list (deleted team records?). 345 SG Submarines/Bandits is listed under lg 83 but played lg 84 in 2012.
- get_standings(57) (cumulative): no rows for 336/351. Candidate season-limited IDs: 309 SG MUS/VIK 28-18 RS565 RA391; 349 Luzern Eagles 2 23-19; 345 SUB 28-11; 340 Bern Cardinals 2 23-19; 273 Sissach Frogs II 8-9 (all 2011+2012 combined probably)
- 2045 done (EIG away 20, 336 home 8; 336 pitchers 3635, 4075, 4203 Wenger Kai)
- 2046 done (350 away 10, EIG home 11; 350 pitcher 8168)
- 2050 done (box+game: SUB 345 away 21, team 482 home 1). !! 482 lineup = Eighters players (licence club 23: Rosenberger, Bienz, Björnstad 8299, Christen 8311, Coker, Müller 8344, Tankura 9160, Sutton). => SECOND EIGHTERS TEAM 482 (name null, deleted record) in 1.Liga 2012. Sutton's log mixes 342 and 482 games.
- Team IDs with null names so far: 336, 350, 351 (opponents of 342), 482 (Eighters 2).
- 2061 done (341 away 15, EIG 342 home 12; 341 pitchers 3810, 6388 Kessler Benjamin)
- 2069 done (MUS/VIK 309 away 25, 482 home 3; 309 pitchers 3732, 4498). Same core players (Stoll, Gfeller, Moor, Sutton) pitch for both 342 and 482 -> maybe one club with two team IDs, or data quirk.
- 2079 done (BAR III 343 away 12, 482 home 13; 343 pitcher 3606)
- 2085 done (481 away 29, 482 home 5; 481 pitcher 6363; 482 pitchers Betschart 9133, Stoll)
- 2086 done (482 away 4, 481 home 25; 481 pitcher 3955)
- 2095 done (342 away 5, 350 home 20; 350 pitcher 4111)
- SPLIT of Sutton VR log by TeamID: team 342 = 2040(@351),2041(336),2045(@336),2046(350),2061(341),2095(@350) = 6 games (matches Individual TeamsGames=6 for 342).
  team 482 = 2050(345),2069(309),2079(343),2085(481),2086(@481) = 5 games.
- Opponents of 342: 336, 341, 350, 351 (all null-name, deleted IDs; 351 plays at Thun, licences club 3). Opponents of 482: 345 SUB, 309 MUS/VIK, 343 BAR III, 481.
- 2144 (PR, not saved): Eighters use TeamID 342 (away) vs 309 MUS/VIK in placement round -> PR games use 342; 482 maybe alias/duplicate record.
- Log 3882 Moor (off) pulled: VR only 2040,2041,2045,2046,2061,2095 = exactly the six 342 games. PR 2144,2145,2147,2150,2151,2166,2167.
- DECISION: follow 342 (Moor's team, used in PR, = brief's Eighters ID). 482 = second Eighters team (shared players Sutton, Stoll, Gfeller, A. Bienz) in another 1.Liga group (with 345, 309, 343, 481). Report it.
- 342 group candidates: 336, 341, 350, 351. Next logs: 4203 (336), 3810 (341), 8168 (350), 3913 (351)
- Log 4203 Wenger (336) pulled: VR 2039 (04-22, opp null), 2041 (EIG), 2045 (EIG), 2047 (04-28, null), 2058+2059 (05-12 vs Luzern Eagles 2 349), 2081 (06-23, null). PR 2158,2159,2164 ignored. => 349 Luzern Eagles 2 is in the group.
- Log 3810 (341?) pulled: VR 2036 (04-21 null), 2038 (04-21 LUZ2 349), 2043 (04-22 BAR III 343), 2044 (04-22 null), 2061 (EIG), 2065 (05-20 LUZ2), 2066 (05-20 null), 2072,2073 (06-09 null), 2074 (06-10 null), 2075 (06-10 SUB 345), 2081,2082 (06-23 null), 2090 (07-07 BAR III), 2092 (07-07 MUS/VIK). 15 VR games!
  => 341 plays both "342-side" and "482-side" opponents: NOT two clean groups. Hypothesis: one 1.Liga group of ~11 IDs, and 342/482 are the SAME Eighters team under two IDs (never same opponent with both; combined 11 games).
- TeamStats VR 2012 (lg84, round 57): 12 team rows; named: 349 LUZ2 G6, 342 EIG G6, 343 BAR III G9, 345 SUB G8, 309 MUS/VIK G8; 7 rows with null team (336,341,350,351,481,482 + one more unknown).
- list_rounds 84: only VR 57 / PR 69 / PL 410 / Finalrunde 296; no group rounds.
- Working hypothesis: 2 groups ~6 teams. A (342 side): 342, 336, 341, 350, 351, 349?  B (482 side): 482, 345, 309, 343, 481, ?. 341 has cross-group games vs 343, 345, 309.
- Next logs: 8168 (350), 3913 (351), 3609 (349)
- Log 8168 (350) pulled: VR 2036,2037(LUZ2),2046(EIG),2047,2054,2055,2073,2095(EIG).
## SCOPE NARROWED (coordinator): only Eighters' own VR games; 342 AND 482 both = Eighters.
- Check: TeamStats 342 G6 R64 H44 = my 6 games RS 64 (14+2+20+11+12+5) OK.
- 482 known RS 26 (H 26) in 5 games; TeamStats null rows: candidate R57/H43 row (shares GameScore fields with 342) -> 482 likely has more games. Pull logs of 482-only players (8299 Björnstad, 9160 Tankura, 8311 Christen).
- Log 8299 Björnstad (482) pulled: VR 2049 (04-29 null), 2050, 2062 (05-20 MUS/VIK), 2063 (05-20 BAR III), 2068 (06-03 SUB), 2069, 2085, 2086. NEW for 482: 2049, 2062, 2063, 2068.
- 2049 done (482 away 13, 344 home 16)
- 2062 done (482 away 1, 309 home 25)
- 2063 done (343 away 17, 482 home 5)
- 2068 done (get_game: 482 away 12, SUB home 13; box TOTALS correct, pitcher rows wrong)
- CHECK 482: 9 games RS 57 H 43 = TeamStats null row (R57 H43) EXACT. 342: 6 games RS 64 H 44 = TeamStats EXACT. Eighters VR complete: 15 games.
## FINAL (narrowed scope)
Eighters VR 2012: 15 games. 342: 6 G, 3-3, RS 64 RA 81 (3 home/3 away). 482: 9 G, 1-8, RS 57 RA 183 (5 home/4 away). Total 4-11, RS 121, RA 264, 8 home/7 away.
No forfeits / postponed found. 2050 and 2068 played at Romanshorn (2050 lists 482 as home).
