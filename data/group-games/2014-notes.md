# 2014 scan (1.Liga, league 84, VR round 57)
## Logs pulled
3882 Martin Moor (off): Eighters VR games 3086(04-12, opp null) 3087(04-12 Dulliken Truck Star) 3092,3093(04-26 null) 3114(05-24 Luzern Eagles 2) 3115(05-24 Yverdon Golgoths) 3135(07-05 Barracudas III) 3136(07-05 Yverdon) 3141(08-10 Barracudas III) 3142(08-10 null)
## Done
3086 (342@351 7-20; 351 name unknown, not in list_teams(84)), 3087 (643 Dulliken@342 17-4)
3092 (351@342 7-13), 3093 (342@904 4-7, short 3 inn; 904 name unknown; 904 pitcher 16642)
3114 (342@349 Luzern2 3-4; Luzern P 8236 Maldonado), 3115 (641 Yverdon@342 6-7; Yverdon P 15786 Reganely)
3136 (641@342 4-5); 3135 box fetch failed once, retry
3135 (342@343 9-10; Barr P 15793 Würsten, 3466 Berchtold), 3141 (342@343 9-8; Barr P 17462 Greber), 3142 (904@342 11-7)
Eighters games so far: 10. vs 351 x2, 904 x2, 641 x2, 343 x2, 643 x1, 349 x1. Next: Sutton 4142 log to find missed games.
Sutton 4142 log pulled: new 3117 (05-31 342@643 13-4; Dulliken P 15282 Matter), 3130 (06-22, box teams 482@905 0-21 ?? -> get_game)
3130 get_game: 482 @ 905 0-21 at Romanshorn, 06-22, VR 57. Team 482 lineup = Eighters licences (01 23 ...: Sutton, Schoch, Mahler, R. Bienz 3475) -> SECOND EIGHTERS TEAM 482 (name null). 905 = likely Romanshorn (field), P 3522 Colin Bruce. NOT saved (not team 342).
get_standings(57): null-name teams (351, 904, 482, 905) absent. Dulliken 10-20, Yverdon 6-13 (both created 2013, so 2013+2014 combined?) -> not season-unique.
Log 3466 Berchtold (Barr III): VR 3096(05-03 vs Yverdon) 3107(05-17 vs Luzern2) 3135 3137(07-05 vs Yverdon) 3141 3190(08-05 opp null); PR 3193
Log 15793 Würsten (Barr III): VR 3095(05-03 Dulliken) 3096 3107 3108(05-17 null) 3106(05-31 null) 3135 3137 3150(07-27 Luzern2) 3141 3143(08-10 null) 3190; PR 3191 3193 3194 3195
Log 8236 Maldonado (Luzern2): VR 3107 3109(05-17 null) 3114 3116(05-24 Yverdon) 3128(06-21 null) 3150 3151(07-27 null); PL 3200 3201
Candidate group: 342, 343 Barr III, 349 Luzern2, 351 ?, 641 Yverdon, 643 Dulliken, 904 ? (7 teams)
TODO boxes: 3095 3096 3106 3107 3108 3109 3116 3128 3137 3143 3150 3151 3190
Log 4048 R.Schaller (351): 3086 3088(04-12 Dulliken) 3092 3094(04-26 null) 3104(05-11 Dulliken) 3106(05-31 Barr) 3123(06-15 null) 3124(06-15 Yverdon) 3151(07-27 Luzern) 3152(07-27 Barr)
Log 16642 (904): 3093 3108(05-17 Barr) 3123(06-15 null) 3125(06-15 Yverdon) 3153(07-27 Yverdon) 3155(07-27 Dulliken) 3142 3143(08-10 Barr)
TODO add: 3088 3094 3104 3123 3124 3125 3152 3153 3154? 3155
Log 16649 Almstetter (Yverdon): 3096 3115 3116 3124 3125 3136 3137 3153 3154(07-27 Dulliken) 3144(08-03 null) 3145(08-03 Luzern); PR 3193
Log 15282 Matter (Dulliken): 3087 3088 3095 3105(05-11 Barr) 3117
TODO boxes: 3088 3094 3095 3096 3104 3105 3106 3107 3108 3109 3116 3123 3124 3125 3128 3137 3143 3144 3145 3150 3151 3152 3153 3154 3155 3190
Log 4109 Staub (Dulliken): 3087 3088 3095 3104 3154 3155 (+3105 from Matter, 3117); PR 3191
done 3088 3094 3095
done 3096 3104 3105 (note: 3095 and 3105 both 343 @ 643)
done 3106 3107 3108
done 3109 3116 3123
done 3124 (9-9 tie? doubtful) 3125 3128
## TASK NARROWED (coordinator): only Eighters' own VR games needed; treat 342 AND 482 (and similar dup IDs) as Eighters. 3130 (482@905 0-21) IS an Eighters game -> save.
Log 16516 Weidmann (482 player): VR 3098(05-04 null) 3100(05-04 SG MUS/VIK) 3112 3113(05-18 null) 3130 3148(07-20 MUS/VIK) 3190(08-05 null; also Barr III game!) 3142(342 game); PR 3195
Logs 16509 Rohner, 16581 Qizmolli (482): VR 3098 3100 3112 3113 3130 3148 3190 (+3117 Qizmolli w/ 342). 482 TODO boxes: 3098 3100 3112 3113 3148 3190
done 3098 (906@482 28-2) 3100 (482@309 9-18) 3112 (482@344 5-6)
done 3113 (344@482 18-7) 3148 (309@482 20-2) 3130 saved. 3190 box: 905@482 24-1 but Barr III players (Berchtold, Würsten) also list 3190 -> get_game
3190 get_game: 905@482 24-1 linescore, GameEnded=0, BoxScoreGenerated=0; 905 roster club-2 licences (Barracudas players Berchtold, Bekkali + Larson, Berger). Saved with note. 482 so far 7 games: missing 2nd vs 906? Next: log 3526 (906 P), pitching logs 3474 Bienz etc.
Log 3526 (906): 3098 3099(05-04 vs SG MUS/VIK) 3110 3111(05-18 vs SG Submarines/Bandits) -> 482 group incl. 309 MUS/VIK, 344, 905, 906, SG Sub/Bandits(named, id?)
Pitch log 3474 A.Bienz: 3093 L, 3112 L (482), 3113 ND (482), 3114 L, 3117 W, 3135 ND, 3136 W => 2-3 consistent w/ box
Open: 342 2nd game vs Luzern2 missing; 482 2nd game vs 906 (and any vs Sub/Bandits) missing. Try TeamStats.
TeamStats pit 2014 (named teams only; 482/351/904/905/906/344 absent): 342 G11 W5 L6 IP57.1 RA110 HA113. My 11 saved 342 games: W5 L6, IP 57.1 (match), RA 98, HA 102 (mismatch +12 RA, +11 HA - unexplained). Luzern2 G9 (I know 8: 3107 3109 3114 3116 3128 3145 3150 3151). SG Submarines/Bandits = 345 (G8).
Log 3821 Lindegger (Luzern2): 3114 3116 3145 3146(08-03) 3150 3151; 3146 box = 351@349 5-6 (saved). Luzern's 9 games all accounted -> NO 2nd Eighters(342)-Luzern game in DB.
Probes: 3129 = 905@345 (not Eighters), 3149 = 345@309 (not Eighters), 3097 & 3147 box null -> get_game
UNPLAYED: 3147 (2014-07-20, 482 @ 345 SG Submarines/Bandits, Romanshorn) GameEnded=0, no score -> listed, not saved. 3097 = 643@641 unplayed (not Eighters). Next: probe remaining unknown IDs for unplayed Eighters games.
Probes not Eighters: 3089 (344@905), 3090 (905@345), 3091 (345@344), 3101 (906@905)
Probes not Eighters: 3102 (905@344), 3103 (344@906). 3118, 3119 box null -> get_game
3118 get_game: FORFEIT 349 @ 342 0-7 (Eighters win), saved source=game. 3119 = forfeit 643@349 7-0 (not Eighters). Continue probing 3120-3122 3126 3127 3131-3134 3138-3140
3120 = 344@906 (not Eighters). 3121 3122 3126 box null -> get_game
3121 (906@309), 3122 (309@344), 3126 (643@904): unplayed, not Eighters.
3127 = 349@643 unplayed (not Eighters).
UNPLAYED Eighters(482) games (listed, NOT saved): 3131 (06-22, 345 SG Submarines/Bandits @ 482, GameEnded 0), 3132 (07-26, 482 @ 906, postponed=1, never played), 3133 (08-05, 905 @ 482, postponed=1 -> replayed/recorded as 3190 same date), 3147 (07-20, 482 @ 345, GameEnded 0)
Schedule check: 342 = 6 opponents x2 = 12 games, all 12 saved (11 played + 3118 forfeit win). 482 = 5 opponents x2 = 10 scheduled: 7 played saved, 3 never played (3131 3132 3147); 3133 postponed dup of 3190.
FINAL: 342 12 games W6 L6 (incl. 3118 forfeit W 7-0), RS 88 RA 98, home 6 away 6. 482 7 games W0 L7, RS 26 RA 135, home 4 away 3. Combined 19 games 6-13, RS 114 RA 233.
Pitcher check: Sutton 3-1, Moor 0-2, A.Bienz 2-3 (incl. 3112 L for 482), Acosta L 3142 -> 342 played decisions 5-6 = TeamStats W5 L6, IP 57.1 matches. TeamStats RA 110/HA 113 vs box TOTALS 98/102 unexplained.
