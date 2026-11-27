# 2013 progress
## Logs pulled
- Martin Moor 3882, L84 2013 off: 9 VR games (round 57): 2424,2425 (04-20), 2203 vs Luzern Eagles 2 (05-04), 2434 vs Yverdon Golgoths (05-04), 2610,2611 (06-23), 2613 vs Luzern Eagles 2 (06-30), 2615 vs Yverdon (06-30), 2442 (07-13)
## Done (box scores)
- 2424 done (get_game too: team 351 name null)
- 2425 done
- 2203, 2434 done
- 2449, 2604 done (get_game 2604)
- 2605, 2610 done
- 2611, 2613 done
- 2615, 2442 done. ALL 12 Eighters VR games saved.
## Candidate IDs
## Doubts
- get_standings(57) pulled: no row for team 351 (deleted team?). Teams created 2013 in L84: Yverdon Golgoths 641, Wil Devils II 642, Dulliken Truck Star 643 (all by another user decf90e1 -> maybe the 2013 schedule creator)
- TeamStats L84 2013 round 57 (off) pulled: 13 team rows. Named: Luzern Eagles 2 349 G12, Eighters 342 G12, Dulliken Truck Star 643 G9, Barracudas III 343 G10, SG MUS/VIK 309 G9, Wil Devils II 642 G9, Yverdon Golgoths 641 G8, SG Submarines/Bandits 345 G8. Plus 5 unnamed rows (Team null; deleted teams, incl. 351 and 336). Unnamed rows R: 126, 86, 67, 217, 131.
- Eighters have 12 VR games; Moor log has only 9 -> need another Eighters log (Stratmann 4127).
- Stratmann 4127 log: VR adds 2449 (05-26 vs SG MUS/VIK), 2604 (06-16 opp null), 2605 (06-16 vs Barracudas III). PR games 2682, 2683 (10-19) ignored.
- Eighters VR list (12): 2424,2425,2203,2434,2449,2604,2605,2610,2611,2613,2615,2442
- IMPORTANT: Eighters appear under TWO TeamIDs in 2013 VR: 342 (games created by user 0b7d..., e.g. 2424) and 482 (unnamed/deleted; games 2449, 2604, created by user decf90e1). Opponent 481 unnamed (lic club 11). Unnamed IDs so far: 336, 351, 481, 482.
- Eighters sum of runs from TOTALS = 100, but TeamStats R=110 (mismatch, to check).
- Opponent IDs: 351 x2 (2424,2611), 336 x2 (2425,2610), 349 x2, 641 x2, 341 x1 + 481 x1 (same club?), 309 x1, 343 x1.
- Opponent pitchers for logs: 351 Schönthal 4069 / Reber 6399; 336 pitcher 4203, 3815; 349 Holenstein 3724; 641 Glauser 15773; 341/481 Cordero Cruz 6363; 309 3732; 343 3521
- Cordero Cruz 6363 log (club lic 11): 17 VR games: 2430(04-28 null),2431(04-28 Yverdon),2432,2433(05-04 MUS/VIK x2),2574(06-09 Luzern),2575(06-09 null),2604(06-16 null=Eighters482),2606(06-16 Barracudas III),2617(07-06 null),2618(07-06 Yverdon),2442(07-13 Eighters),2443(07-13 Dulliken),2582(07-14 vs Eighters!),2583(07-20 null),2584(07-20 SG Sub/Bandits),2445(07-27 Luzern),2446(07-27 null). Finalrunde 2684,2685 ignored.
  -> 2582 (07-14) is an Eighters game NOT in Moor/Stratmann logs: Eighters may have >12 VR games. Need more Eighters logs (Stoll 4122).
- Stoll 4122 (Eighters lic 01 23) log VR: 2427,2428 (04-27 vs Wil Devils II x2), 2448 (05-26 vs Barracudas III), 2449, 2604, 2605, 2611, 2613, 2615, 2442, 2444 (07-13 vs Dulliken), 2580 (07-14 vs Dulliken), 2582 (07-14 null), 2583 (07-20 null), 2585 (07-20 vs SG Sub/Bandits). PR 2682,2683 ignored.
  -> NEW Eighters VR candidates: 2427, 2428, 2448, 2444, 2580, 2582, 2583, 2585. Eighters now >=20 VR games (TeamStats G12 counted only TeamID 342 games).
  -> 2582, 2583: Eighters vs Cordero Cruz's team (341/481?).
- Bienz 3474 log: no new VR games (PR 2664,2665,2669,2682,2683 ignored).
- Eighters VR list now 20 (doubleheader each matchday): 2424,2425 | 2427,2428 | 2203,2434 | 2448,2449 | 2604,2605 | 2610,2611 | 2613,2615 | 2442,2444 | 2580,2582 | 2583,2585
- 2427, 2428 done
- 2448, 2444 done
- 2580, 2582 done
- 2583, 2585 done. All 20 Eighters VR games saved.
- TASK NARROWED by coordinator: only Eighters' own VR games needed (no group table).
- Check: TeamStats 342 G12 R110 = sum of my 12 games under 342 (110). Unnamed TeamStats row with R=67 = sum of my 8 games under 482 (67) -> both ID sets look complete.
- get_game 2611: 351 @ 342, 7-8 confirmed (TOTALS correct).
- Pitcher W/L check: Moor L in 2424,2203,2442,2615 + W 2613 = (1-4) as box shows; Sutton W 2444, 2580 = (2-0) as box shows; Bienz W 2611; Sutton W 2585. Consistent.
- No forfeits, no postponed games found. 2013_meta.json written. DONE.
