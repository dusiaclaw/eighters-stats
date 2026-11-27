# 2022 scan (1.Liga, league 84, VR round 57)
## Teams in S
- 342 Zürich Eighters
- 11294 Hünenberg Unicorns
- 1190 Zürich Challengers 3 (pitchers 16611 Kämpfer Florin, 19672 Siemers Nicholas; from box 14338)
- 340 Bern Cardinals 2 (pitcher 4006 Rissi Christof; from box 14370)
## Logs pulled
- 3972 Benny Räber (Hünenberg) off — done (by caller)
## Candidate non-Eighters VR games
Hünenberg: 14337 (vs Ch3), 14361 (vs Ch3, DONE given), 14367, 14368, 14376, 14377, 14390, 14399 (vs Bern2), 14398 (vs Ch3)
## Done
14361
- 16611 Kämpfer Florin (Ch3) off — done: non-E VR 14337 (vs Hün), 14361 (vs Hün), 14433 (vs Bern2, 08-13), 14511 (vs Bern2, 06-18)
- 4006 Rissi Christof (Bern2) off — done: non-E VR 14433 (vs Ch3), 14511 (vs Ch3), 14390, 14399 (vs Hün)
## Candidates added: 14433, 14511 (Ch3 vs Bern2)
- done: 14367, 14337. Extra pitchers: 12457 Bernhardt (Hün), 16333 Alleyn Yves (Bern2), 19670 Stotz Joseph (Ch3)
- done: 14368, 14376
- done: 14377, 14390
- done: 14399. 14398 box TOTALS say Ch3(away) 11 @ Hün 12 but pitcher lines inconsistent (IP 2.1 vs 4.1) -> verifying with get_game
- done: 14398 (get_game confirmed 11-12, 3 inn, field Bern Allmend)
- done: 14433, 14511. Next: logs 19670 Stotz Joseph (Ch3), 31564 Lobsiger Samuel (Bern2) for completeness
- 19670 Stotz Joseph (Ch3) off — done: non-E VR 14337, 14361, 14398 (Hün), 14397 (Bern2, 07-10, NEW), 14511, 14433 (Bern2)
- 31564 Lobsiger Samuel (Bern2) off — done: Hün 14367/14368 (06-12), 14390 (07-02), 14399 (07-10), 14376/14377 (08-07); Ch3 14397, 14433; also plays Thun Hunters (14412,14413,14354,14422,14383) and Sissach Frogs II (14343,14345,14420) — outside S, ignored
## Candidate added: 14397
- done: 14397. Checking 14437 via get_game for round/replay info on Eighters-Ch3 extra games
- 14437 get_game: Round 57, origRound null, GameNumber 903, dtCreated 2022-04-22 (same batch as the original schedule) -> scheduled VR game, not a replay
## Status: COMPLETE (12 non-Eighters games)
Pair counts: E-Ch3 9, E-Hün 4, E-Bern2 3, Hün-Ch3 3, Hün-Bern2 6, Ch3-Bern2 3
## Follow-up: group size check (coordinator request)
- list_teams(84): 340 Bern Cardinals 2, 6707 Bern Cardinals III, 346 Thun Hunters, 273 Sissach Frogs II
- CORRECTION: box 14412 = Bern Cardinals III (6707) @ Thun (346); box 14343 = Sissach II (273) @ Bern III (6707). Lobsiger 31564's Thun/Sissach games were for Bern III, not Bern 2. Player logs are per player, not per team.
- Next: logs 4251 Zimmermann Cédric (Thun), 7016 Meier Sebastian (Sissach II)
- 4251 Zimmermann Cédric (Thun) off: VR opponents only Bern Cardinals III (14412, 14413, 14349, 14351), Therwil Flyers III (14352), Sissach II (14372, 14373)
- 7016 Meier Sebastian (Sissach II) off: VR opponents only Bern Cardinals III (14343, 14345, 14420), Thun (14372, 14382)
- CONCLUSION: no Thun/Sissach games vs Hünenberg, Challengers 3, Bern 2 or Eighters. Separate group (Bern III, Thun, Sissach II, Therwil III). 2022 group = {Eighters, Hünenberg, Challengers 3, Bern Cardinals 2}. No scores fetched for them; CSV unchanged (12 rows).
