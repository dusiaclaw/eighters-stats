# 2021 scan progress (NLB leagueID 83, VR round 53)
Eighters TeamID 11693.
## Teams
## Player logs pulled
## Candidate game IDs
## Done
- Embrach Mustangs = 276 (pitchers 3770 Kästli David, 3542 Byrnes Christopher)
- 12542, 12543 eighters-check done (confirmed: Eighters away, 0-20 and 1-19)
- 12509 box fetch failed once (retry)
- 12509 eighters-check done (confirmed: Eighters away, 1-32)
- Barracudas II = 321 (pitcher 26400 Del Valle Diaz Elvis)
- Lausanne Indians = 6704 (pitcher 4005 Rihs Yves) [from 12480]
- Sissach Frogs = 348 (pitcher 18275 Müller Marc) [from 12484]
- S = {11693, 6704, 348, 321, 276}
- Next: logs of 4005, 18275, 26400, 3770
- Log 4005 (Lausanne, off) pulled: VR games vs Sissach 12472,12473,12512,12513; vs Barracudas II 12494,12495,12548,12549; vs Embrach 12558,12559; vs Eighters 12480,12481; vs Therwil Flyers II 12560,12561 (Therwil not in S)
- Log 18275 (Sissach, off) pulled: vs Lausanne 12472,12473,12512,12513; vs Barracudas II 12554,12555; vs Embrach 12532,12565; vs Eighters 12484,12485; vs Therwil II 12498,12499,12544,12545
- Candidates in S: 12472,12473,12512,12513,12494,12495,12548,12549,12558,12559,12554,12555,12532,12565
- Log 26400 (Barracudas II, off) pulled: vs Embrach 12468,12469,12527,12528; vs Sissach 12554,12555; vs Lausanne 12494,12495,12548,12549; vs Therwil II 12488,12489,12514,12515; PL games ignored
- Log 3770 (Embrach, off) pulled: vs Barracudas 12468,12469,12527,12528; vs Lausanne 12490,12491,12558; vs Sissach 12532,12533,12564; vs Therwil 12536
- Candidate list by pair:
  Lau-Sis 12472,12473,12512,12513 | Lau-Bar 12494,12495,12548,12549 | Lau-Emb 12490,12491,12558,12559
  Sis-Bar 12554,12555 (only 2 found) | Sis-Emb 12532,12533,12564,12565 | Bar-Emb 12468,12469,12527,12528
- Done: 12468,12469,12472,12473
- Done: 12490,12491,12494,12495
- Done: 12512,12513,12527,12528
- Done: 12532,12533,12548. 12549 box totals inconsistent with pitcher rows -> checking get_game
- Done: 12549 (get_game confirms TOTALS 2-17)
- Done: 12554,12558,12559. 12555 T-side pitcher rows inconsistent -> get_game
- Done: 12555 (get_game; home 8 vs 9 conflict, recorded 8)
- Done: 12564,12565. All 20 candidates done. Checking Sis-Bar (only 2) via log of 12479 Romang
- Log 12479 (Romang, Sissach) pulled: confirms only 12554,12555 vs Barracudas. Probing gap IDs 12476,12482,12502 for possible unlogged Sis-Bar games
- Probes: 12476 = 278 vs 320, 12482 = 11285 vs 11692, 12502 = 349 vs 278 -> other VR group interleaved in same ID range; no extra Sis-Bar game found. Not saved (outside S).
## Status: COMPLETE. 20 non-Eighters games + 3 eighters-check rows.
Pair counts: Lau-Sis 4, Lau-Bar 4, Lau-Emb 4, Sis-Emb 4, Bar-Emb 4, Sis-Bar 2.
Eighters vs: Lau 2, Sis 2, Bar 2, Emb 4. Therwil Flyers II also in this group (played by all 4 opponents) but not by Eighters -> not in S.
## Extension: add Therwil Flyers II to S
Known Therwil candidates from logs: vs Lau 12560,12561; vs Sis 12498,12499,12544,12545; vs Bar 12488,12489,12514,12515; vs Emb 12536
- Therwil Flyers II = 347 (pitchers 28947 Radelfinger Ray, 18254 Margarucci Michael). Done: 12536,12560,12561
- Logs 28947 (Radelfinger) and 18254 (Margarucci) pulled, identical game sets (15 VR games): vs Emb 12478,12479,12536; vs Bar 12488,12489,12514,12515; vs Sis 12498,12499,12544,12545; vs Lau 12504,12505,12560,12561. No Sis-Bar info.
- To fetch: 12478,12479,12488,12489,12498,12499,12504,12505,12514,12515,12544,12545; probe 12537 (possible 2nd Emb-Therwil game on 08-07)
- Done: 12478,12479,12488,12489
- Done: 12498,12499,12504,12505
- Done: 12514,12515,12545. 12544 T pitcher rows sum to 20 RA vs TOTALS 14 -> get_game. 12537 box empty -> get_game
- 12544 get_game confirms 11-14 (TOTALS right). 12537 = Therwil@Embrach 2021-08-07, postponed=1, GameEnded=0, never played (no replay found in logs)
## Status after extension: COMPLETE
CSV: 40 rows = 22 non-Eighters (5 original opponents) + 15 Therwil + 3 eighters-check. (Earlier report said 20 non-Eighters games; correct count is 22.)
Full-group pair counts (incl. 10 known Eighters games): Lau-Sis 4, Lau-Bar 4, Lau-Emb 4, Sis-Emb 4, Bar-Emb 4, Sis-Bar 2, Ther-Lau 4, Ther-Sis 4, Ther-Bar 4, Ther-Emb 3 (4th = 12537 postponed, unplayed), Eig-Lau 2, Eig-Sis 2, Eig-Bar 2, Eig-Emb 4, Eig-Ther 0.
Games per team: Embrach 19, Lausanne 18, Sissach 16, Barracudas II 16, Therwil 15, Eighters 10 (total 47).
