# 2018 scan progress (league 84 1.Liga Baseball, VR round 57)
## Logs pulled
- 3882 Moor (off): 5370 (04-21 SG Mustangs/Lions), 5371 (04-21 Mustangs/Lions), 5379 (05-06 ?), 5385 (05-12 Bern Mammoths), 5404 (06-03 Bern Mammoths), 5394 (06-16 ?), 5395 (06-16 Sissach Frogs), 5414 (07-07 Mustangs/Lions), 5415 (07-07 ?), 5426 (07-21 Sissach Frogs), 5428 (07-21 ?)
## Done
- 5370, 5371 done. 1306 = SG Mustangs/Lions (pitchers Hubler Isabell 3732, Augsburger Aron 3445)
- 5379 (342@1195, pitchers Thommen Nolan 4148, 17500), 5385 (342@1196 Bern Mammoths, pitchers Réganély 15786, Mottay 47419) done
- list_teams(84): 1306 SG Mustangs/Lions, 1305 SG Devils/Submarines, 1308 SG Submarines/Bandits/Vikings created 2018-04-08 (season-unique candidates). 1195 NOT in league-84 list (name TBD).
- 5404 (1196@342), 5394 (342@1195; 1195 pitcher 4146) done
- 5395 (348 Sissach Frogs @342; 348 pitchers Meier Sebastian 7016, Rushiti 21174), 5414 (342@1306; 1306 pitchers Ortiz 19794, Sterchi 4116) done. 348 not in league-84 team list either.
- 5415 (1195@342; 1195 pitchers Thommen 4148, Senti Beat 18282), 5426 (348@342; 348 pitchers Löliger 3829, Gongas 47217) done
- 5428 (342@1195; 1195 pitchers Thommen Colin 4147, 21175) done
- get_game 5379: HomeTeamName NULL for 1195 (no name in EasyScore); field Bern Allmend; 1195 batters Correa 9077, Despaigne Perez 19652, Vieira 19907. Matches box 6-16.
## Eighters by Moor log: 11 games. vs 1306 x3, 1195 x4, 1196 x2, 348 x2. Next: Stoll 4122 log to check for missed games.
- Log 4122 Stoll: adds 5420 (07-14 Bern Mammoths). Others already known.
- 5420 (1196@342, E8 won 11-9; 1196 pitcher Alleyn 15761) done. Log 15789 Suzuki: no new games.
- Eighters total so far 12: vs1306 x3 (5370,5371,5414), vs1195 x4 (5379,5394,5415,5428), vs1196 x3 (5385,5404,5420), vs348 x2 (5395,5426)
## Next: logs 4148 (1195), 3445 (1306), 15786 (1196), 7016 (348)
- Log 4148 Thommen Nolan (1195) VR: 5361 MusL 04-14, 5363 Siss 04-14, 5372 Mam 04-28, 5374 MusL 04-28, 5378 Mam 05-06, 5379 E8, 5393 Siss 06-16, 5394 E8, 5415 E8, 5416 MusL 07-07, 5427 Siss 07-21, 5428 E8, 5433 Siss 07-28, 5434 MusL 07-28, 5438 Mam 08-05, 5439 Mam 08-05 => 16 games, 4 vs each => group of 5, 4 games per pair. (PL games 5688,5692,5700,5708,5709 ignored.) In this log the opponent name 'Zürich Eighters' shows, so 1195 simply lacks a name.
- Eighters only 12 found -> missing 1 vs 1306, 1 vs 1196, 2 vs 348?
- To fetch (non-E8, 1195): 5361 5363 5372 5374 5378 5393 5416 5427 5433 5434 5438 5439
- Log 7016 Meier (348) VR: 5362 MusL 04-14, 5363 1195, 5384 Mam 05-12, 5393 1195, 5395 E8, 5396 MusL 06-09, 5397 Mam 06-09, 5411 Mam 06-30, 5421 Mam 07-14, 5426 E8, 5427 1195, 5432 MusL 07-28, 5433 1195 (13). PL ignored (5689-5691 vs Wil Devils II, 5700,5708,5709 vs 1195).
- Log 3445 Augsburger (1306): 5362, 5370, 5371, 5398 (MusL vs Mam 06-09 NEW). Sparse; try 3732 Hubler.
- Log 3732 Hubler (1306): adds 5373 (MusL-Mam 04-28), 5412 (MusL-Mam 06-30); also 5361,5370,5374,5396,5416.
- Pair tally (34 known): E8-MusL 3, E8-1195 4, E8-Mam 3, E8-348 2, 1195-MusL 4, 1195-348 4, 1195-Mam 4, 348-MusL 3, 348-Mam 4, MusL-Mam 3. Missing 6 if 4/pair.
- Log 15786 Réganély (1196): no new games (5372,5373,5378,5384,5385,5397,5398,5404,5411,5412,5421,5438,5439).
- get_standings(57) cumulative: SG Mustangs/Lions 13-14 RS288 RA342 (27 G > 16 => not season-unique, probably 2018+2019). 1195 not listed (no name). Sissach Frogs 25-20 (multi-season). Not usable as direct check except comparing later.
- Hypothesis: missing E8 games are forfeits/unplayed with no box -> invisible in logs. Probing gap IDs near E8 single-game days: 5377 5380 5383 5386 5403 5405 5419 5422
- 5380 (get_game): 1196 @ 342, 2018-05-06, GameNumber 323, GameEnded 0, Forfeit 0, postponed 0, no score -> NOT PLAYED (not saved). 5379 is GameNumber 322 (OrderInSchedule 21). 5386 empty box -> get_game.
- 5386 (get_game): 348 Sissach Frogs (registered as NLB team) @ 342, 2018-05-12, GameNumber 329, field Sissach, GameEnded 0 -> NOT PLAYED. GameNumber = ID-5057 for 5379/5380/5386 -> group schedule probably IDs ~5358-5397 (#301-340) plus later re-created games. Probing gaps by box score.
- Probes 5358 (1305@642), 5359 (343@1305), 5360 (642@343), 5364 (1305@1307): OTHER group (teams 1305, 642, 343, 1307) -> IDs interleaved, not consecutive. Targeted probes next: 5403 5405 (06-03), 5410 5413 (06-30), 5419 5422 (07-14).
- Probes: 5405 (642@1308) other group; 5419 (642@1190) other group; 5413, 5422 empty box -> get_game.
- 5413 (get_game): 348 @ 1306, 2018-06-30, #356, GameEnded 0 -> NOT PLAYED (348-MusL missing pair found).
- 5422 (get_game): 342 @ 348, 2018-07-14, #365, GameEnded 0 -> NOT PLAYED. Remaining missing: E8-MusL 1, MusL-Mam 1. Probing 5403, 5406 (06-03).
- 5406 (343@642) other group. 5403 empty box -> get_game.
- 5403 (get_game): 342 @ 1306, 2018-06-03, #337, GameEnded 0 -> NOT PLAYED. Remaining missing: MusL-Mam 1. Probe 5402.
- 5402 (get_game): 1306 @ 1196, 2018-06-03, #336, GameEnded 0 -> NOT PLAYED.
## Schedule accounted: 40 slots (5 teams x 4 per pair) = 34 played + 6 unplayed (5380, 5386, 5403, 5402, 5413, 5422). No cross-group VR games seen in any group-team log.
## Unplayed (not saved): 5380 1196@342 05-06; 5386 348@342 05-12; 5402 1306@1196 06-03; 5403 342@1306 06-03; 5413 348@1306 06-30; 5422 342@348 07-14
## TODO box scores (non-E8): 5361 5362 5363 5372 5373 5374 5378 5384 5393 5396 5397 5398 5411 5412 5416 5421 5427 5432 5433 5434 5438 5439
Done: 5361 5362 5363
Done: 5372 5373 5374 (5374 odd: B pitchers sum 10.2 IP)
Done: 5378 5384 5393
Done: 5396 5397 5398
Done: 5411 5412 5416
Done: 5421 5427 5432
Done: 5433 5434 5438 5439. ALL 34 played games saved. Renamed TBD_1195.
## Status: COMPLETE
34 played VR games saved (all box TOTALS). 6 scheduled games never played (GameEnded 0, no forfeit flag): 5380, 5386, 5402, 5403, 5413, 5422.
Computed 2018 VR: 1195 12-4 (222-111); 348 7-6 (138-134); 1196 7-7 (165-171); 1306 6-7 (150-169); 342 Eighters 2-10 (102-192).
Pairs: all 4 except 1196-1306 3, 1196-342 3, 1306-342 3, 1306-348 3, 342-348 2 (each gap = one of the unplayed games).
Standings check: no season-unique team ID usable (1306 row 13-14 is cumulative >16 G; 1195 has no name and no row; 348/1196/342 multi-season).
Oddities: 5374, 5438 home pitcher IP sums >9 (10.2, 10.0); 5439 pitcher 19794 (1306 player) listed under 1195. TOTALS used.
