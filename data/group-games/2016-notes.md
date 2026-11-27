# 2016 scan (1.Liga, league 84, VR round 57)
## Logs pulled
3882 Moor (off): 4224, 4240 VR; 4412 PR (Sissach) 
15777 Mahler (off): 4203,4204,4206,4207,4357 (all TeamID 482!), 4214, 4240, 4271 (TeamID 342)
## KEY DOUBT: two "Eighters-like" teams in league 84 2016
342 Zürich Eighters: 4214 @Bern Mammoths 1196, 4224 @Lions II 393, 4240 vs Martigny 1192, 4271 @Bern Mammoths
482 (no name in EasyScore; players have Eighters licences 01 23 ..., same players as 342: Mahler, Bienz, Betschart, Rosenberger, Locher):
  4203 @344 (Wil field, licences 01 5/0005), 4204 vs 1197, 4206 @1194 (Austrian-looking names), 4207 vs 1197, 4357 @1112
  -> saved separately in 2016_other482.csv for now
## Box format note: games with unnamed teams return inline huge box (GameInfo null) -> use pitchersOnly=1
4019 Rosenberger, 16506 Locher, 3474 Bienz (off) logs: Eighters VR = 4203,4204,4206,4207,4214,4224,4240,4263,4271,4357 (10). Same player continuity across 342/482 -> 342 and 482 are the SAME Eighters squad (Locher plays all 10).
4263: 906 @ 482 7-8 (07-10)
Team names unresolvable: 482,344,1194,1197,1112,906 not in list_teams(84/83/80/88/106/117/474), not in get_standings(57). Team join seems to fail -> unnamed.
Team IDs 1190-1197 created 2016-04-01 (Challengers 3=1190, Martigny=1192, Bern Mammoths=1196).
Opponent pitchers: 344 Gardoni 3654/Borando A 3498; 1197 Würsten 15793/Egli Tim 19543; 1194 Widemschek 19617/Mähr 8336; 906 Sutter Yannic 28740; 1112 Fernandes 47288, Bloch Kurt 3488; 1196 Lüscher 9152/Heise 8325/Alleyn 15761; 393 Dreiding 3594/Kessler 6388; 1192 Evans 19650
3654 Gardoni (344) log: 4203,4205,4219,4220,4231,4255 VR; PR 4389 vs Martigny. Boxes saved.
=> Group cluster (unnamed IDs): 482 (Eighters), 344, 1197, 1194, 1112, 906. Eighters' 342-ID games (Bern Mammoths x2, Lions II, Martigny) look cross-group.
19543 Egli Tim log (plays for BOTH 343 Barracudas III and 1197): VR 4197,4198,4204,4205,4207,4220,4238,4260,4261,4264,4237,4269,4270; PR 4411 (Lions II), 4412 (Sissach)
8264 Nenning (1194): 4206, 4231 only
Boxes: 4197 343@1190 12-6 (04-02); 4198 1191@343 11-9 (04-02); 4237 343@1107 12-13 (07-16)
=> PATTERN: each club seems to have a named ID and an unnamed duplicate ID (342/482 Eighters, 343/1197 Barracudas III). Group must be defined by CLUB, not TeamID.
[usage-limit pause here; resumed]
## Resumed
TeamStats pit r57 (named teams only): 342 Eighters 4G 2-2 RA57 = my 4 342-games EXACT. 343 Barr III 10G 3-7 RA101; 1190 Chall3 8G 1-7 RA87; 1196 Bern Mammoths 7G 6-1 RA44; 393 Lions II 4G 1-3 RA58; 1192 Martigny 4G 1-3 RA33; 348 Sissach 1G 0-1 RA7.
Individual pit r57 summed by pitcher team: Eighters pitchers (Bienz, Moor, Stoll, Betschart) W4 L5 RA110 = EXACT match to my 10 Eighters box games (342+482, 4357 counted as 1 RA box-only). Unnamed-ID teams have no pitchers listed at all.
4357 get_game: 482 @ 1112 (Romanshorn), AwayRuns 13 HomeRuns 6, GameEnded 0, box 1 inning only (box score 0-1; my earlier 1-0 entry had sides swapped). Saved as 13-6 source=game with note.
Merged 2016_other482.csv into 2016.csv (deleted). Wrote 2016_meta.json.
STATUS: Eighters complete (10 VR games). Group table NOT complete: opponent teams mostly unnamed duplicate IDs; full league probing (IDs ~4197-4271, 4357) not done.
CSV rewrite glitch: rows 4263/4271/4357 re-added manually; 18 rows total. Eighters (342+482) 10 games: box-based 4-5 RS83 RA110 (matches pitching totals); with 4357 as 13-6 per get_game: 5-5 RS96 RA115.
