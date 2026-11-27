# 2019 scan (1.Liga, league 84, VR round 57)
## Seed: 13 Eighters games from data/games/2019.json written to 2019.csv (9110 9111 9117 9118 9124 9125 9151 9152 9163 9165 9169 9170 9181)
## Team IDs: 342 Eighters, 1306 SG Mustangs/Lions, 1190 Zürich Challengers 3, 1308 SG Submarines/Bandits/Vikings, 642 Wil Devils II, 343 Zürich Barracudas III
## Logs pulled (cat=off, L84 2019)
3882 Moor (Eig): 10 VR games, all in seed (9110 9111 9124 9125 9151 9152 9163 9165 9169 9170). Seed extra: 9117 9118 9181 (confirmed VR by Stotz/Altherr/Ruosch logs).
19886 Ruosch (Mus 1306), 19671 Stotz (Cha3 1190), 19720 Altherr (Subs 1308), 28740 Sutter Yannic (Wil 642; also PL 410 games 10672-10677 vs Bern2/Sissach - ignore), 29168 Jossi (Barr 343, only 3 games)
## Candidate VR game IDs (from logs; pairs guessed from Opponent)
04-27: 9104 Subs-Barr, 9105 Mus-Barr, 9106 Mus-Subs
05-05: 9110 9111 (seed), 9112 Mus-Cha
05-11: 9113 Wil-Mus, 9114 Wil-Barr, 9115 Mus-Barr
05-12: 9116 Cha-Subs, 9117 9118 (seed)
05-18: 9119 Subs-Wil, 9120 Subs-Barr, 9121 Wil-Barr
05-26: 9124 9125 (seed), 9126 Subs-Wil
06-01: 9133 Wil-Barr, 9135 Wil-Cha
06-15: 9136 Subs-Wil, 9137 Subs-Cha, 9138 Wil-Cha
06-29: 9142 Mus-Cha, 9143 Mus-Wil, 9144 Cha-Wil
07-07: 9151 9152 (seed), 10656 Subs-Barr (odd ID!)
07-14: 9157 Cha-Mus, 9158 Subs-Mus, 9159 Subs-Cha
07-21: 9163 9165 (seed), 9164 Cha-Barr
08-03: 9168 Mus-Barr, 9169 9170 (seed)
08-18: 9180 Mus-Cha, 9181 (seed)
Gaps to probe: 9100-9103 9107-9109 9122-9123 9127-9132 9134 9139-9141 9145-9150 9153-9156 9160-9162 9166-9167 9171-9179 9182+
Extra logs: 16449 Büki (Barr), 21421 Hubschmid (Wil): no new VR IDs.
## Done: all 28 log-found games box-scored and saved (9104-9180 list above + 9134 found by probe, Cha@Barr, 06-01 date inferred). CSV = 41 rows.
Pair counts: all pairs 3 except BAR-CHA 2, MUS-CHA 4, MUS-SUB 2, MUS-WIL 2, EIG-WIL 1. Games/team: CHA15 MUS14 SUB14 BAR14 EIG13 WIL12.
get_standings(57) all-time; names 1306/1308/642 not season-unique (rows exceed my counts) -> weak check only.
NEXT: probe gaps 9122 9123 9127-9132 9139-9141 9145-9150 9153-9156 9160-9162 9166 9167 9171-9179 9182 9100-9103 9107-9109 for missing EIG-WIL x2, MUS-WIL, BAR-CHA, MUS-SUB.
Probes: 9122, 9123 = other group (teams 348 vs 8798), not saved.
9182 get_game: Cha3 @ Eighters 08-18 R57 game#385, GameEnded=0, Forfeit=0, no runs -> UNPLAYED, not saved (would have been 4th Eig-Cha meeting).
9127 box: Bern2(340) @ 8798 = West, not saved. 9128 (1195@340) and 9129 (8798@1195) get_game: West, unplayed 05-26.
Pattern: each tri day uses 3 consecutive IDs per group (ours 9104-06, 9110-12, 9113-15, 9116-18, 9119-21, 9124-26, 9133-35, 9136-38, 9142-44, 9151-52(+?), 9157-59, 9163-65, 9168-70, 9180-82).
9148 box: West (1195 @ 8798), not saved. 9145 get_game: West Thun@LuzernIII 06-30 FORFEIT 0-7 (canceled) -> forfeits exist and have no box/log!
9153 get_game: Barr @ Subs 07-07 #356 GameEnded=0 -> unplayed stub; replaced by 10656 (same pairing/date). Not saved.
9130 (06-01 Eagles III@Sissach 348), 9139 (06-16 Bern2@Thun), 9146 (06-30 Bern2@Thun forfeit) = West, not saved. West IDs: 340 Bern Cardinals 2, 346 Thun, 348 Sissach Frogs, 8798 Luzern Eagles III, 1195 (Luzern Eagles?).
Tri analysis: our group 14 tri-days x3 = 42 scheduled slots = 41 played + 9182 unplayed (9153 stub replaced by 10656). Per team scheduled: CHA16 EIG14 MUS14 SUB14 BAR14 WIL12 -> consistent with schedule as found; no evidence yet of a 15th tri.
Remaining probes: 9171/9174/9177 (gap 08-03..08-18), 9100-9103.
9101 box West (346 @ 1195). 9171 West unplayed 08-03, 9174 West forfeit 08-17.
9177 get_game: Wil Devils II @ Eighters 08-10 #380 Heerenschürli, postponed=1, GameEnded=0 -> NEVER PLAYED (no replacement in any log). 15th tri day 08-10 = IDs 9177-9179? checking 9178/9179.
9178 get_game: Mus @ Wil 08-10 postponed=1 unplayed. 9179: Eighters @ Mus 08-10 postponed=1 unplayed. 9176 West forfeit 08-17.
=> 15th tri (08-10 Heerenschürli, 9177-9179) entirely postponed and never played. Schedule = 15 tris = 45 games; 41 played, 4 unplayed (9177 9178 9179 9182), 9153 stub replaced by 10656.
Remaining gap IDs fit West 3-blocks pattern. Checking 10655/10657 for other replacement games.
10655/10657 box null (not investigated further; no extra games in any of the 8 team logs).
## STATUS: DONE. 41 VR games saved (all group-internal; no cross-group games: group teams never met West teams in VR).
Unplayed, not saved: 9177 Wil@Eig, 9178 Mus@Wil, 9179 Eig@Mus (all 08-10, postponed), 9182 Cha@Eig (08-18), 9153 Barr@Subs stub (replaced by 10656).
