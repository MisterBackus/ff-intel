# FF Intel trade board — Bot or Not Fantasy

Generated 2026-10-22 08:00 AM EDT

- **NFL week:** 7
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-10-22 week 7 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 88 | -12 | Josh Allen | BUF | 30.5 | QB1 | Healthy | BYE | -12 vs last board; SF QB1 floor 45 |
| 82 | +20 | Jared Goff | DET | 27.8 | QB1 | Healthy |  | +20 vs last board; SF QB1 floor 45 |
| 82 | -8 | Joe Burrow | CIN | 25.2 | QB1 | Healthy |  | -8 vs last board; SF QB1 floor 45 |
| 81 | +5 | Brock Purdy | SF | 27.3 | QB1 | Healthy |  |  |
| 78 | +6 | Trevor Lawrence | JAX | 24.4 | QB1 | Healthy | BYE |  |
| 73 | -15 | Drake Maye | NE | 23.3 | QB1 | Healthy |  | -15 vs last board; SF QB1 floor 45 |
| 70 | +28 | Bryce Young | CAR | 24.0 | QB1 | Healthy |  | +28 vs last board; SF QB1 floor 45 |
| 70 | -6 | Patrick Mahomes | KC | 23.0 | QB1 | Healthy |  |  |
| 68 | -18 | Lamar Jackson | BAL | 23.0 | QB1 | Questionable |  | -18 vs last board; Questionable x0.95 |
| 65 | +21 | Kirk Cousins | LV | 24.0 | QB1 | Healthy |  | +21 vs last board; SF QB1 floor 45 |
| 64 | +2 | Jayden Daniels | WAS | 23.9 | QB1 | Healthy | BYE |  |
| 61 | +19 | Tyler Shough | NO | 23.5 | QB1 | Healthy |  | +19 vs last board; SF QB1 floor 45 |
| 60 | -2 | Jordan Love | GB | 22.7 | QB1 | Questionable |  |  |
| 59 | +33 | Aaron Rodgers | PIT | 24.5 | QB1 | Healthy |  | +33 vs last board; SF QB1 floor 45 |
| 58 | -6 | Dak Prescott | DAL | 21.6 | QB1 | Healthy |  |  |
| 55 | -5 | Matthew Stafford | LAR | 22.3 | QB1 | Healthy |  |  |
| 52 | +10 | C.J. Stroud | HOU | 21.9 | QB1 | Healthy |  | +10 vs last board; SF QB1 floor 45 |
| 50 | -6 | Caleb Williams | CHI | 22.8 | QB1 | Healthy |  |  |
| 45 | -1 | Bo Nix | DEN | 14.1 | QB1 | Healthy |  |  |
| 45 | — | Cam Ward | TEN | 11.7 | QB1 | Healthy |  |  |
| 45 | +21 | Daniel Jones | IND | 12.5 | QB1 | Healthy |  | +21 vs last board; SF QB1 floor 45; buy-low: volume > points |
| 45 | — | Deshaun Watson | CLE | 16.0 | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 15.8 | QB1 | Healthy |  |  |
| 45 | +17 | Jacoby Brissett | ARI | 8.7 | QB1 | Healthy |  | +17 vs last board; SF QB1 floor 45; buy-low: volume > points |
| 45 | +25 | Jameis Winston | NYG | 18.6 | QB1 | Healthy |  | +25 vs last board; SF QB1 floor 45; buy-low: volume > points |
| 45 | -3 | Justin Herbert | LAC | 13.4 | QB1 | Healthy | BYE |  |
| 45 | +1 | Kyler Murray | MIN | 11.4 | QB1 | Healthy |  |  |
| 45 | — | Malik Willis | MIA | 13.7 | QB1 | Healthy |  |  |
| 45 | +13 | Michael Penix Jr. | ATL | 20.1 | QB1 | Healthy |  | +13 vs last board; SF QB1 floor 45 |
| 45 | +17 | Sam Darnold | SEA | 16.4 | QB1 | Healthy |  | +17 vs last board; SF QB1 floor 45; buy-low: volume > points |
| 29 GUESS (29.19) | +21 | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | +21 vs last board; IR x0.50; GUESS inputs |
| 22 | -6 | Baker Mayfield | TB | 13.7 | QB1 | Questionable |  |  |
| 20 | -6 | Tanner McKee | PHI | — | QB2 | Healthy |  |  |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 97 | +2 | Jahmyr Gibbs | DET | 28.0 | RB1 | Healthy |  |  |
| 94 | +12 | Kenneth Walker III | KC | 26.2 | RB1 | Healthy |  | +12 vs last board |
| 91 | +17 | Jonathan Taylor | IND | 18.5 | RB1 | Healthy |  | +17 vs last board |
| 90 | +32 | Derrick Henry | BAL | 18.7 | RB1 | Healthy |  | +32 vs last board |
| 90 | +16 | James Cook III | BUF | 18.1 | RB1 | Healthy | BYE | +16 vs last board |
| 88 | -6 | Bijan Robinson | ATL | 19.8 | RB1 | Healthy |  |  |
| 87 | +41 | Chuba Hubbard | CAR | 18.5 | RB1 | Healthy |  | +41 vs last board |
| 86 | +12 | Christian McCaffrey | SF | 18.0 | RB1 | Healthy |  | +12 vs last board |
| 85 | +43 | Javonte Williams | DAL | 16.6 | RB1 | Healthy |  | +43 vs last board |
| 82 | +32 | Kyren Williams | LAR | 17.3 | RB1 | Healthy |  | +32 vs last board |
| 78 | +20 | Ashton Jeanty | LV | 14.6 | RB1 | Healthy |  | +20 vs last board |
| 77 | +35 | Jaylen Warren | PIT | 15.4 | RB1 | Healthy |  | +35 vs last board |
| 73 | +39 | D'Andre Swift | CHI | 15.8 | RB1-split | Healthy |  | +39 vs last board |
| 72 | +28 | Chase Brown | CIN | 10.6 | RB1 | Healthy |  | +28 vs last board; buy-low: volume > points |
| 71 | +31 | Bucky Irving | TB | 12.8 | RB1 | Questionable |  | +31 vs last board; Questionable x0.95; buy-low: volume > points |
| 70 | +32 | Bhayshul Tuten | JAX | 13.7 | RB1 | Healthy | BYE | +32 vs last board |
| 69 | +37 | Ollie Gordon II | MIA | 15.9 | RB1-split | Healthy |  | +37 vs last board |
| 68 | +28 | Aaron Jones Sr. | MIN | 12.8 | RB1 | Healthy |  | +28 vs last board; buy-low: volume > points |
| 60 | +50 | Quinshon Judkins | CLE | 9.5 | RB1 | Questionable |  | +50 vs last board; Questionable x0.95; buy-low: volume > points |
| 57 | +25 | Omarion Hampton | LAC | 8.8 | RB1 | Healthy | BYE | +25 vs last board |
| 55 | — | Tony Pollard | TEN | 7.2 | RB1 | Healthy |  |  |
| 53 | +35 | Rhamondre Stevenson | NE | 9.5 | RB1-split | Healthy |  | +35 vs last board |
| 52 | +28 | J.K. Dobbins | DEN | 7.6 | RB1 | Healthy |  | +28 vs last board; buy-low: volume > points |
| 50 | +34 | Jeremiyah Love | ARI | 9.1 | RB1-split | Questionable |  | +34 vs last board; Questionable x0.95 |
| 49 | +21 | Braelon Allen | NYJ | 9.7 | RB1 | Healthy |  | +21 vs last board |
| 47 | — | Cam Skattebo | NYG | 7.7 | RB1 | Healthy |  |  |
| 46 | +24 | David Montgomery | HOU | 8.4 | RB1-split | Questionable |  | +24 vs last board; Questionable x0.95 |
| 42 | +12 | Woody Marks | HOU | 6.8 | RB1-split | Healthy |  | +12 vs last board; buy-low: volume > points |
| 38 | +8 | Emanuel Wilson | SEA | 8.7 | RB1 | Healthy |  | +8 vs last board; buy-low: volume > points |
| 34 | +18 | MarShawn Lloyd | GB | 6.5 | RB1-split | Healthy |  | +18 vs last board; buy-low: volume > points |
| 30 | +12 | Alvin Kamara | NO | 9.0 | committee | Questionable |  | +12 vs last board; Questionable x0.95; committee RB 27% cap 30 |
| 30 | — | Blake Corum | LAR | 8.0 | committee | Healthy |  |  |
| 30 | +2 | Breece Hall | NYJ | 12.5 | committee | Questionable |  |  |
| 30 | +6 | Dameon Pierce | PHI | 13.0 | committee | Healthy |  |  |
| 30 GUESS (30) | +12 | Jordan Mason | MIN | 11.9 | committee | IR |  | +12 vs last board; IR x0.83; committee RB 12% cap 30; GUESS inputs |
| 30 GUESS (30) | -8 | Josh Jacobs | GB | — | committee | Healthy |  | -8 vs last board; committee RB 35% cap 30; buy-low: volume > points; GUESS inputs |
| 30 | +4 | Kyle Monangai | CHI | 14.2 | committee | Out |  |  |
| 30 | — | Rachaad White | WAS | 13.7 | committee | Healthy | BYE |  |
| 30 | — | Saquon Barkley | PHI | 5.2 | committee | Questionable |  |  |
| 30 GUESS (30) | +14 | Travis Etienne Jr. | NO | 8.5 | committee | IR |  | +14 vs last board; IR x0.83; committee RB 23% cap 30; GUESS inputs |
| 30 | +12 | TreVeyon Henderson | NE | 5.6 | committee | Healthy |  | +12 vs last board; committee RB 32% cap 30 |
| 30 | +10 | Tyler Allgeier | ARI | 5.6 | committee | Healthy |  | +10 vs last board; committee RB 38% cap 30; buy-low: volume > points |
| 24 | — | Chris Rodriguez Jr. | JAX | 5.0 | committee | Healthy | BYE |  |
| 23 GUESS (23.23) | +7 | Zach Charbonnet | SEA | — | committee | PUP |  | PUP x0.83; committee RB 20% cap 30; GUESS inputs |
| 21 | — | Kimani Vidal | LAC | 5.5 | committee | Healthy | BYE |  |
| 19 GUESS (18.66) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 32% cap 30; GUESS inputs |
| 19 | +1 | Kendre Miller | NO | 4.3 | committee | Healthy |  |  |
| 18 | -2 | Brian Robinson Jr. | ATL | 2.2 | committee | Questionable |  |  |
| 16 | — | Emmett Johnson | KC | 3.8 | committee | Healthy |  |  |
| 16 | — | Jaleel McLaughlin | CLE | 7.5 | committee | Healthy |  |  |
| 14 GUESS (14.38) | — | Dylan Sampson | CLE | — | committee | IR |  | IR x0.83; committee RB 20% cap 30; GUESS inputs |
| 14 GUESS (14.05) | — | Jadarian Price | SEA | 4.0 | committee | IR |  | IR x0.83; committee RB 19% cap 30; GUESS inputs |
| 9 GUESS (8.73) | — | Jonah Coleman | DEN | — | committee | IR |  | IR x0.83; committee RB 8% cap 30; GUESS inputs |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | +6 | Jaxon Smith-Njigba | SEA | 23.4 | WR1 | Healthy |  |  |
| 93 | +13 | Amon-Ra St. Brown | DET | 17.1 | WR1 | Healthy |  | +13 vs last board |
| 92 | +22 | CeeDee Lamb | DAL | 17.9 | WR1 | Healthy |  | +22 vs last board |
| 88 | +20 | Puka Nacua | LAR | 18.3 | WR1 | Healthy |  | +20 vs last board |
| 86 | +48 | Zay Flowers | BAL | 15.7 | WR1 | Healthy |  | +48 vs last board |
| 84 | +30 | Chris Olave | NO | 15.2 | WR1 | Healthy |  | +30 vs last board |
| 84 | +28 | Tetairoa McMillan | CAR | 14.6 | WR1 | Healthy |  | +28 vs last board |
| 79 | +17 | Malik Nabers | NYG | 13.7 | WR1 | Healthy |  | +17 vs last board; buy-low: volume > points |
| 77 | +13 | Drake London | ATL | 12.2 | WR1 | Healthy |  | +13 vs last board; buy-low: volume > points |
| 77 | — | Parker Washington | JAX | 13.2 | WR1 | Healthy | BYE |  |
| 76 | +54 | Christian Watson | GB | 17.4 | WR1 | Questionable |  | +54 vs last board; Questionable x0.95 |
| 76 | +2 | Ja'Marr Chase | CIN | 13.3 | WR1 | Healthy |  |  |
| 75 | +35 | Garrett Wilson | NYJ | 12.9 | WR1 | Healthy |  | +35 vs last board; buy-low: volume > points |
| 72 | +36 | Tee Higgins | CIN | 12.4 | WR2 | Healthy |  | +36 vs last board |
| 71 | +15 | Nico Collins | HOU | 15.6 | WR1 | Healthy |  | +15 vs last board |
| 70 | +26 | DeVonta Smith | PHI | 14.0 | WR1 | Healthy |  | +26 vs last board |
| 70 | +46 | Matthew Golden | GB | 14.3 | WR2 | Questionable |  | +46 vs last board; Questionable x0.95 |
| 69 | +3 | Justin Jefferson | MIN | 13.6 | WR1 | Questionable |  |  |
| 68 | +46 | Mike Evans | SF | 12.6 | WR1 | Questionable |  | +46 vs last board; Questionable x0.95 |
| 65 | +49 | Jalen Coker | CAR | 14.0 | WR2 | Healthy |  | +49 vs last board |
| 62 | +20 | George Pickens | DAL | 10.9 | WR2 | Healthy |  | +20 vs last board |
| 62 | +36 | Germie Bernard | PIT | 20.2 | WR2 | Healthy |  | +36 vs last board |
| 62 | +42 | Michael Wilson | ARI | 9.1 | WR1 | Healthy |  | +42 vs last board; buy-low: volume > points |
| 60 | +38 | Luther Burden III | CHI | 9.6 | WR1 | Healthy |  | +38 vs last board; buy-low: volume > points |
| 56 | +32 | Emeka Egbuka | TB | 9.5 | WR1 | Questionable |  | +32 vs last board; Questionable x0.95; buy-low: volume > points |
| 55 | +15 | DK Metcalf | PIT | 9.0 | WR1 | Healthy |  | +15 vs last board; buy-low: volume > points |
| 52 | +24 | Stefon Diggs | WAS | 11.5 | WR2 | Healthy | BYE | +24 vs last board |
| 51 | — | Jameson Williams | DET | 9.7 | WR2 | Healthy |  |  |
| 48 | — | Jaylen Waddle | DEN | 7.3 | WR1 | Questionable |  |  |
| 45 | +21 | Rashee Rice | KC | 7.9 | WR | Questionable |  | +21 vs last board; Questionable x0.95 |
| 42 | — | Jakobi Meyers | JAX | 8.4 | WR2 | Healthy | BYE |  |
| 40 | +20 | Xavier Worthy | KC | 7.0 | WR1 | Healthy |  | +20 vs last board; buy-low: volume > points |
| 37 | — | Keenan Allen | IND | 8.7 | WR2 | Healthy |  |  |
| 37 | +15 | Keon Coleman | BUF | 10.6 | WR2 | Healthy | BYE | +15 vs last board |
| 36 | — | Denzel Boston | CLE | 7.0 | WR1 | Questionable |  |  |
| 35 | — | Rome Odunze | CHI | 6.5 | WR2 | Healthy |  |  |
| 34 | +2 | Jordan Addison | MIN | 6.9 | WR | Healthy |  |  |
| 33 | +1 | A.J. Brown | NE | 4.2 | WR1 | Healthy |  |  |
| 28 | — | Courtland Sutton | DEN | 4.1 | WR2 | Healthy |  |  |
| 28 | +4 | DJ Moore | BUF | 7.6 | WR | Out | BYE |  |
| 26 GUESS (26.07) | +16 | Davante Adams | LAR | 14.5 | WR | IR |  | +16 vs last board; IR x0.50; GUESS inputs |
| 24 | +10 | Deebo Samuel Sr. | SF | 10.5 | WR | Out |  | +10 vs last board; Out x0.65 |
| 24 | — | Rashod Bateman | BAL | 7.5 | WR2 | Questionable |  |  |
| 24 | +18 | Terry McLaurin | WAS | 7.7 | WR1 | Out | BYE | +18 vs last board; Out x0.65 |
| 23 | — | Quentin Johnston | LAC | 4.2 | WR2 | Healthy | BYE |  |
| 23 GUESS (22.52) | +17 | Romeo Doubs | NE | 8.5 | WR | IR |  | +17 vs last board; IR x0.83; GUESS inputs |
| 22 | — | Makai Lemon | PHI | 3.5 | WR | Healthy |  |  |
| 21 | +11 | Ladd McConkey | LAC | 6.5 | WR1 | Out | BYE | +11 vs last board; Out x0.65 |
| 18 | +2 | Omar Cooper Jr. | NYJ | — | WR | Healthy |  |  |
| 17 | — | Brian Thomas Jr. | JAX | 3.5 | WR | Healthy | BYE |  |
| 17 | -9 | Marvin Harrison Jr. | HOU | 4.4 | WR | Healthy |  | -9 vs last board |
| 14 | -6 | Jaylin Noel | HOU | — | WR | Healthy |  |  |
| 13 | — | Jerry Jeudy | CLE | 3.5 | WR | Healthy |  |  |
| 10 | — | Darius Cooper | PHI | 1.4 | WR | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 89 | +33 | Trey McBride | ARI | 13.1 | TE1 | Healthy |  | +33 vs last board |
| 87 | +29 | Brock Bowers | LV | 17.1 | TE1 | Questionable |  | +29 vs last board; Questionable x0.95 |
| 86 | +42 | George Kittle | SF | 12.8 | TE1 | Healthy |  | +42 vs last board |
| 82 | +56 | Isaiah Likely | NYG | 13.2 | TE1 | Healthy |  | +56 vs last board |
| 75 | +43 | Sam LaPorta | DET | 12.6 | TE1 | Healthy |  | +43 vs last board |
| 62 | +28 | Travis Kelce | KC | 10.4 | TE1 | Questionable |  | +28 vs last board; Questionable x0.95 |
| 60 | +30 | Tyler Warren | IND | 11.0 | TE | Questionable |  | +30 vs last board; Questionable x0.95 |
| 51 | +15 | Tucker Kraft | GB | 7.3 | TE1 | Healthy |  | +15 vs last board |
| 50 | — | Harold Fannin Jr. | CLE | 7.3 | TE1 | Healthy |  |  |
| 47 | — | Dalton Kincaid | BUF | 8.2 | TE1 | Questionable | BYE |  |
| 46 | — | Mark Andrews | BAL | — | TE1 | Healthy |  |  |
| 36 | — | Colston Loveland | CHI | 5.5 | TE1 | Healthy |  |  |
| 35 | +5 | T.J. Hockenson | MIN | 1.2 | TE1 | Questionable |  |  |
| 33 | +13 | Dallas Goedert | PHI | 5.6 | TE1 | Healthy |  | +13 vs last board |
| 32 | +8 | Kyle Pitts Sr. | ATL | 7.1 | TE1 | Healthy |  | +8 vs last board |
| 24 | — | Jake Ferguson | DAL | 6.0 | TE1 | Healthy |  |  |
| 14 | -2 | Pat Freiermuth | PIT | 2.1 | TE1 | Healthy |  |  |
| 13 | -9 | Tyler Higbee | LAR | 2.2 | TE1 | Healthy |  | -9 vs last board |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Davante Adams | WR | 26 | 80 | 54 | +16 vs last board; IR x0.50; GUESS inputs |
| Mark Andrews | TE | 46 | 0 | 46 | buy-low: volume > points |
| Jacoby Brissett | QB | 45 | 0 | 45 | +17 vs last board; SF QB1 floor 45; buy-low: volume > points |
| Kyler Murray | QB | 45 | 3 | 42 | SF QB1 floor 45 |
| Kyle Monangai | RB | 30 | 71 | 41 | Out x0.65; committee RB 34% cap 30 |
| Rachaad White | RB | 30 | 69 | 39 | committee RB 30% cap 30 |
| Cam Ward | QB | 45 | 6 | 38 | SF QB1 floor 45; buy-low: volume > points |
| Germie Bernard | WR | 62 | 98 | 36 | +36 vs last board |
| Daniel Jones | QB | 45 | 10 | 35 | +21 vs last board; SF QB1 floor 45; buy-low: volume > points |
| T.J. Hockenson | TE | 35 | 0 | 35 | Questionable x0.95; buy-low: volume > points |
| Dameon Pierce | RB | 30 | 65 | 35 | committee RB 22% cap 30 |
| Justin Herbert | QB | 45 | 13 | 32 | SF QB1 floor 45; buy-low: volume > points |
| Josh Jacobs | RB | 30 | 0 | 30 | -8 vs last board; committee RB 35% cap 30; buy-low: volume > points; GUESS inputs |
| Tony Pollard | RB | 55 | 25 | 30 | buy-low: volume > points |
| Breece Hall | RB | 30 | 58 | 28 | Questionable x0.95; committee RB 38% cap 30 |
