# 2023 scan (1.Liga, league 84, VR round 57)
## Team IDs (from pitcher rows of Eighters games)
342 Zürich Eighters
12090 SG Pirates/Lions (pitchers: 21164 Sutter Noah, 3499 Borando Fabio, 3497 Borando Alessio) [box 15926]
11295 Embrach Mustangs 2 (3732 Hubler Isabell, 19886 Ruosch Florian) [box 15930]
12091 SG Wittenbach-Romanshorn 2/Wil Devils 4 (17587 Garcia Jover Jose Carlos) [box 15931]
12089 Zürich Barracudas 4 (3753 Isik Yusuf, 21198 Suzuki Taiga, 3459 Bekkali Farid, 15793 Würsten Samuel) [box 15934]
1190 Zürich Challengers 3 (19670 Stotz Joseph) [box 15939]
346 Thun Hunters (3635 Flückiger Moritz, 37198 Birrer Yanis Samuel) [box 15955]
340 Bern Cardinals 2 (4006 Rissi Christof, 31414 Scherr Oliver) [box 16374]
## Player logs pulled (cat=off)
3499 Borando Fabio (Pirates), 21164 Sutter Noah (Pirates), 3732 Hubler (Embrach), 17587 Garcia Jover (Wittenbach),
3753 Isik (Barracudas), 19670 Stotz (Challengers), 3635 Flückiger (Thun), 4006 Rissi (Bern)
## NOTE round confusion
Rissi (Bern 2) log lists 16374 (08-26) and 16375 (09-02) vs Eighters as Round 410 PL, not VR!
## Group structure (likely)
East VR IDs ~15922-15956: Eighters, Pirates/Lions 12090, Embrach 2 11295, Wittenbach/Wil 12091, Barracudas 4 12089, Challengers 3 1190 (6-team double RR = 30 games)
 + cross games in East range: 15929 Embrach-Bern2, 15945/15946 Wittenbach-Hünenberg, 15955/15956 Eighters-Thun
West VR IDs ~15957-15986+: Thun 346, Bern 2 340, Lausanne Indians 2, Luzern Eagles 2, Hünenberg Unicorns
 cross: 15976 Barracudas-Lausanne2, 15980 Thun-Embrach2, 15986 Barracudas-Hünenberg, 15972 Bern-Hünenberg
## Candidate VR games (from logs) among S
15923 Barr-Chall3 04-30; 15929 Embrach-Bern 05-07; 15932 Witt-Embrach 05-13; 15936 Witt-Pirates 05-21; 15938 Witt-Chall3 05-21;
15941 Witt-Chall3 06-04; 15942 Pirates-Embrach 06-18; 15943 Barr-Embrach 06-18; 15944 Pirates-Barr 06-18; 15947 Witt-Pirates 07-16;
15948 Witt-Embrach 07-16; 15949 Pirates-Embrach 07-16; 15950 Barr-Chall3 06-25; 16022 Barr-Pirates 04-30;
15964 Thun-Bern 05-20; 15968 Bern-Thun 06-04; 15980 Thun-Embrach 07-08
Unknown IDs in East range to probe: 15922,15924,15925,15928,15933,15937,15953,15954
## Done (in 2023.csv)
15923 15929 15932 15936 15938 15941
15942 15943 15944 15947 15948 15949
15950 16022 15964 15968 15980; 15922 box empty
15924 get_game: Chall3 @ Pirates 15-10 04-30 VR confirmed (Chall3 and Barr4 share players, e.g. Bekkali, Scholz, Lopatka)
15925 box: 12090 @ 12089 but TOTALS null -> get_game (forfeit/unplayed?)
15928 Embrach@Bern 15-20 saved; 15933 Embrach@Barr 10-6 saved; 15937 Chall@Pirates 15-13 saved
15953 Chall3 @ team 349 (17-19), 15954 349 @ Chall3 (14-16): team 349 unknown name -> get_game
Team 349 = Luzern Eagles 2 (West). 15953/15954 = Chall3 vs Luzern2 07-16, cross-group, NOT in S (not saved).
Extra logs: 34579 Dickow (Chall3), 38134 Lopatka (Barr4; also played for Chall3 in 15924). Barr4 also 15977 vs Lausanne2 (cross).
Missing so far: Embrach-Chall3 (0 of 2), Witt-Barr4 (0 of 2). Checking 15922, 15925.
15925 get_game: Pirates@Barr4 04-30, AwayRuns 8 HomeRuns 11 but GameEnded=0, no box -> DUPLICATE of 16022 (same date/score); not saved
15922: get_game returns [] (does not exist). East ID range 15923-15956 fully accounted.
get_standings(57) is ALL-TIME (all years) but 2023-only team names usable:
 SG Pirates/Lions 6-6 RS129 RA135 (my 10 games: 6-4, RS117 RA106 -> 2 more games, both L, 12 RS 29 RA)
 SG Witt/Wil 9-3 RS156 RA79 (my 8 non-Hünenberg: 6-2 RS103 RA51 -> 4 more incl 2 vs Hünenberg 15945/46)
 Barracudas 4 6-6 RS113 RA105 (my 8: 4-4 RS59 RA64 -> 4 more incl Lausanne 15976/77, Hünenberg 15986)
Logs 9121 Werder (Pirates): +15978,15979 Pirates vs Hünenberg 07-02 (cross, not S). 3547 Cartsunis (Witt): +15988 Witt vs Hünenberg 07-22.
15987 probe: Barr4 @ Witt 5-17 (saved). Each East team seems to have 12 VR games; Embrach (11 found) and Chall3 (10 found) short -> probing 15981+ for Embrach-Chall3.
Ruosch 19886 (Embrach) log: no Chall3 games. Probes 15981, 15982 empty; 15983 (team 12092 @ Bern2), 15984 (Bern2 @ Hünenberg), 15985 (Hünenberg @ 12092) = West games, not S. Stopped probing.
## STATUS: DONE. Embrach-Chall3 pair: 0 games found (Embrach 11 and Chall3 10 VR games found vs 12 for others).
## Follow-up task: adding East cross-group games; 15953/15954 appended
16374 get_game: Round 410 (PL), Bern2 @ Eighters 7-3, 08-26, field Bern Allmend
16375 get_game: Round 410 (PL), Eighters @ Bern2 2-10, 09-02, field Thun
added 15978 15979 15945 15946
added 15988 15976 15977 15986; 12092 = Lausanne Indians 2
CHECK vs get_standings(57): CSV gives Pirates 12-game 6-6 (H3-3 A3-3) RS129 RA135; Witt 9-3 (H4-2 A5-1) 156/79; Barr4 6-6 (H3-3 A3-3) 113/105 -> ALL EXACT MATCH with official rows (incl home/away splits). Confirms 15986 TOTALS and that 15925 is not counted.
Embrach-Chall3 search: logs 18477 Blickenstorfer Ilai (Chall3, not shared w/ Barr) and 34565 Hug Markus (Embrach) -> no Embrach-Chall3 game. Not found anywhere. (Hug's log also lists 15956 = Eighters-Thun 07-23, so Hug apparently played for Thun that day.)
## FOLLOW-UP DONE. CSV now 32 rows.
