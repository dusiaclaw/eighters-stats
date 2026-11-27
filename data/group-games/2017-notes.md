# 2017 progress
## Logs pulled
- Moor Martin 3882 (Eighters) L84 2017 off+pit: games 4641,4642,4657,4665,4667,4674,4676,4695 (all VR round 57)
  Opponents: SG Submarines/Bandits (345), Zürich Barracudas III, Wil Devils II, SG MUS/VIK, Zürich Lions II
## Done (box)
4641
## Doubts
## Team IDs
342 Zürich Eighters; 345 SG Submarines/Bandits (16581 Qizmolli Arlind, 19847 Rüegg Timo, 3873 Meyer Michael) [4641]
343 Zürich Barracudas III (15793 Würsten Samuel) [4642]; 642 Wil Devils II (3497 Borando Alessio, 28740 Sutter Yannic) [4657]
Done: 4642 4657
309 SG MUS/VIK (3732 Hubler Isabell) [4665]; 393 Zürich Lions II (4181 Voelcker Julius, 3955 Pfister Jemain, 3795 Köstinger Urs) [4667]
Done: 4665 4667
Done: 4674 4676 4695. More pitchers: 642: 3498 Borando Antonio, 3751 Isenring Roger; 343: 3753 Isik Yusuf, 3459 Bekkali Farid; 393: 4116 Sterchi Rene, 19654 Chenonier
Eighters pitchers: 3474 Bienz Alain, 9133 Betschart Christian, 4122 Stoll Martin, 4019 Rosenberger Thomas, 19627 Rohrer Daniel
Eighters so far 8 games; missing likely home vs SubBandits, away vs MUS/VIK -> check other Eighters logs
- Log Meyer Michael 3873 (345 SubBandits): VR 4641(E) 4643(Barr) 4680(Wil) 4684(MUS) 4685(Wil) 4653(Lions 07-16) 4699(MUS 07-23) 4713(Lions 08-05) 4707(Barr 09-02) 4708(MUS 09-02); PL 4838,4840
  -> 3x MUS/VIK, only 1x Eighters: check
- list_teams(84): 345 SubBandits not listed (no season-unique group IDs; 1230 SG EAG/BAR & 1231 Bucaneros created 2017 = other group)
- Log Hubler 3732 (309 MUS/VIK): 4644(Lions 04-29) 4656(Wil 05-13) 4665(E) 4683(Wil 06-24) 4684(SB) 4699(SB) 4710(Barr 08-05) 4712(E 08-05) 4708(SB)
- Log Isik 3753 (343 Barr): 4642(E) 4643(SB) 4645(Lions 04-29) 4676(E) 4682(Wil 06-17) 4711(E 08-05!) 4720(Lions 08-12) 4707(SB) 4709(MUS 09-02); PL 4858,4859 vs Bern Mammoths
  (4710 MUS-Barr from Hubler log also)
- Log Köstinger 3795 (393 Lions): 4644(MUS) 4645(Barr) 4667(E) 4695(E) 4697(Wil 07-08) 4653(SB) 4713(SB) 4714(Wil 08-05)  (+4720 Barr)
- Log Borando Antonio 3498 (642 Wil): 4656(MUS) 4657(E) 4674(E) 4675(Barr 06-11) 4680(SB) 4682(Barr) 4683(MUS) 4685(SB) 4697(Lions) 4714(Lions) 4721(Lions 08-12); PL 4856/4857 Sissach, 4860/4861 SB
## Candidate VR list (31 games): 4641 4642 4643 4644 4645 4653 4656 4657 4665 4667 4674 4675 4676 4680 4682 4683 4684 4685 4695 4697 4699 4707 4708 4709 4710 4711 4712 4713 4714 4720 4721
 Pair counts odd: E-SB 1, E-Barr 3, SB-MUS 3, Lions-Wil 3, MUS-Lions 1 -> confirm with box scores
Done: 4711 4712 (Eighters 10 games complete per logs)
Done: 4643 4644 4645
Done: 4653 4656 4675
Done: 4680 4682 4683
Done: 4684 4685 4697
Done: 4699 4707 4708
Done: 4709 4710 4713
Done: 4714 4720 4721 -> all 31 candidate games saved. Next: check ID gaps (West group?)
## Check vs league pitching stats (get_stats Individual cat=pit round 57; per-team sums)
 Official pitching sums: E GS11 W4 L7 RA125 (CSV: 10g 4-6 RA112) -> 1 missing E loss, opp scored 13
 MUS GS12 W4 L8 RA128 (CSV 10g 2-8 RA96) -> 2 missing MUS wins, RA +32
 Lions GS11 4-7 RA121 (CSV 10g 4-6 RA112) -> 1 missing L, RA+9
 Barr (343, Würsten row labelled SG EAG/BAR) GS12 8-4 RA92 (CSV 11g 8-3 RA82) -> 1 missing L, RA+10
 Wil, SB match CSV exactly.
 Hypothesis: missing E-MUS (MUS 13), Lions-MUS (MUS 9), Barr-? (opp 10). Pull Augsburger Aron 3445 log.
- Logs Jost 19876 -> 4791 (MUS vs Lions 05-27, VR, high ID!); Acosta 16578 (E) + Florentino 19724 (MUS) -> 4658 (E vs MUS 05-13). Augsburger Aron 3445 pit log: nothing new.
Done: 4658 4791
- After adding 4658/4791: E, Lions, Wil, SB match pitching sums exactly. MUS W-L/GS match (4-8, 12) but RA 109 vs pitcher-sum 128 (+19).
- Würsten 15793 log -> 4691 Barr vs Bucaneros Solothurn (1231, West) 07-01 VR = cross-group game (Barr L, RA 10). Fetch box.
- Thommen 4148 (MUS) shows G4 RA19 in pitcher stats but only 1 appearance (RA 0) in our boxes -> check his log.
- 4691 box: Würsten & Zürrer pitch with TeamID 1230 SG EAG/BAR (West SG team), not 343 -> NOT a Barr III game; not saved. Würsten pitched for both 343 and 1230 (stats row mixes them).
- Thommen 4148 log: 4651, 4669, 4694 vs Bucaneros/SG EAG/BAR (West games, another team) = RA 19 -> explains MUS +19. MUS reconciled.
## RESULT: all 6 teams reconcile with league pitching stats (W, L, GS, RA). 33 games saved. No unplayed/forfeit games found.
