# 2011 scan progress (league 84 1.Liga Baseball)
- TeamStats 2011 L84: Eighters 342 (10 G), Therwil Flyers II 347 (10), SG MUS/VIK 309 (10), Barracudas III 343 (8), Sissach 348 (5), SG Submarines/Bandits 345 (5), Thun Hunters 346 (3), Luzern Eagles 2 349 (2), plus 3 rows with null team.
- Next: find Eighters player id (Individual pit stats).
- Log 3882 Martin Moor (off, L84 2011) pulled: he WAS an Eighters player 2011. VR (round 57): 1411 vs SG Sub/Bandits 05-22; 1413 vs SG MUS/VIK 05-22; 1416 vs MUS/VIK 06-05; 1417 vs Barracudas III 06-05; 1422 (opp null) 06-19; 1423 vs Barr III 06-19; 1426, 1427 (opp null) 06-26. PR (69) 1552,1553,1572-1575 ignored.
- lgleaders 2011 empty.
- Done: 1411 (Eighters @ Sub/Bandits 3-18). Sub/Bandits pitcher 3547 Cartsunis Peter
- Done: 1416 (Eighters @ MUS/VIK 10-13). MUS/VIK pitcher 3732 Hubler Isabell. 1413 box fetch failed twice
- Done: 1417 (Barr III @ Eighters 26-4). Barr III pitcher 3606 Eichmann Roman
- Done: 1422 (Eighters @ team 344 11-10). 344 pitchers 3751, 3458 Beier Thomas. 344 name unknown (log opp null)
- list_teams(84): 2011-era IDs present: 340 Bern Cardinals 2, 349 Luzern Eagles 2, 309 SG MUS/VIK, 273 Sissach Frogs II, 346 Thun Hunters, 343 Barr III, 342 Eighters, 393 Lions II (created 2011-09-24). 344,345,347,348 not listed (team moved?)
- get_standings(57) pulled (cumulative, names only). Possibly season-unique: Therwil Flyers II 9-1 RS164 RA56 (H4-1, A5-0). Others multi-season. Team 344 not in standings names list by ID; names without IDs.
- Done: 1423 (Barr III @ Eighters 10-11). Barr III pitcher 4144 Tarantino
- Done: 1426 (Eighters @ team 341 1-14). 341 pitcher 4119
- Done: 1427 via get_game (341 @ Eighters 29-4, 5 inn, field Hünenberg). AwayTeamName null => team 341 record has no name. 341 players: 4001 Riedi Claudio, 3478 Bisig Marco, 4164 Tschudi Sven, 4119 Stevens Nelson, 3594 Dreiding Mario (P), 3916 Novas Gil
- Done: 1413 (MUS/VIK @ Eighters 15-6; retry worked). MUS/VIK pitcher 3573 Cruz Guzman Luis. Eighters pitchers 3474 Bienz, 4122 Stoll, 4142 Sutton, 3665 Gfeller. Next: log 4122 Stoll to check Eighters games Moor missed
- Log 4122 Stoll (off) pulled: adds VR 1451 vs Sub/Bandits 07-17, 1452 (opp null) 07-17. Eighters VR = 10 games: 1411,1413,1416,1417,1422,1423,1426,1427,1451,1452. Group likely 6 teams: 342,309,343,345,344,341 (double RR = 30 games)
- Done: 1451 (Sub/Bandits @ Eighters 16-4). Sub/Bandits pitcher 3649 Fussenegger Marc
- Done: 1452 (Eighters @ 344 10-11). Eighters VR complete (10). Next logs: 309 Cruz Guzman 3573, 343 Eichmann 3606, 345 Fussenegger 3649, 344 pitcher 3751, 341 Tschudi 4164
- Log 4164 Tschudi (341, off): VR 1401 (opp null, prob 344) 05-08; 1402 Barr III 05-08; 1426,1427 Eighters; 1436 MUS/VIK 07-02; 1437 Sub/Band 07-02; 1445 MUS/VIK 07-16; 1447 Barr III 07-16. Missing for 341: 2nd vs 344, 2nd vs 345 (Tschudi absent?)
- Log 3751 (344, off): VR 1400 Barr III 05-08; 1401 (341) 05-08; 1421 Barr III 06-19; 1422 Eighters; 1424,1425 MUS/VIK 06-26; 1452 Eighters 07-17. YTD AB consistent (no gaps for this player). 344 no games vs 345 in his log; only 1 vs 341.
- Log 3649 Fussenegger (345, off): VR 1437 (341) 07-02, 1438 MUS/VIK 07-02, 1451 Eighters. Only 3 games.
- Log 3547 Cartsunis (345, off): VR 1411 Eighters, 1412 MUS/VIK 05-22, 1438 MUS/VIK 07-02, 1451 Eighters. With 1437 => 345 has 5 VR games (= TeamStats G 5). TeamStats G appears to = VR games: Eighters 10, MUS/VIK 10, Barr III 8, 345 5.
- Log 3606 Eichmann (343, off): VR 1400 (344), 1402 (341), 1417 Eighters, 1421 (344), 1423 Eighters, 1418 MUS/VIK (dated 07-09). +1447 vs 341 from Tschudi = 7; TeamStats says 8 -> look for 2nd MUS/VIK game
- Log 3573 Cruz Guzman (309, off): VR 1412 (345), 1413, 1416 Eighters, 1418 Barr III 07-09, 1445 (341), 1446 Barr III 07-16.
- FULL candidate list (24 games, no cross-group opponents seen):
  Eighters: 1411,1413,1416,1417,1422,1423,1426,1427,1451,1452 (done)
  Others: 1400(343-344),1401(344-341),1402(341-343),1412(345-309),1418(343-309),1421(344-343),1424,1425(344-309),1436(341-309),1437(341-345),1438(345-309),1445(341-309),1446(309-343),1447(341-343)
  Per team: 342 10, 309 10, 343 8, 341 8, 344 7, 345 5 (sum 48 = 24 games). Matches TeamStats G for 342,309,343,345.
  Missing pairs vs double RR: 344-341 (1 of 2), 345-343 (0/2), 345-344 (0/2), 345-341 (1/2) -> 6 games not in EasyScore (forfeits/unplayed?)
- Done: 1400 (343 @ 344 5-7)
- Done: 1401 (344 @ 341 0-10). TASK NARROWED by coordinator: only Eighters VR games needed; also check alt Eighters IDs (e.g. 482) via TeamStats round 57.
- TeamStats L84 2011 round 57: Eighters 342 G10 R64 H81 -> matches the 10 saved games exactly (R 64, H 81). No alt Eighters ID seen in any log/box (all Eighters players under 342). Four unnamed (null) rows exist (R/H 10/9, 26/23, 57/47, 120/89) - IDs not shown; 341/344 presumably among them.
- Eighters 2-8, home 1-4, away 1-4, RS 64, RA 162. Two games each vs 309,343,345,341,344; no unplayed/forfeit Eighters games.
- DONE (narrowed task).
