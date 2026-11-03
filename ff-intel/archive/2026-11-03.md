# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-03 07:00 AM EST

- **NFL week:** 8
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-03 week 8 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 86 | -1 | Josh Allen | BUF | 30.6 | QB1 | Healthy |  |  |
| 85 | +1 | Joe Burrow | CIN | 30.8 | QB1 | Healthy |  |  |
| 79 | -1 | Trevor Lawrence | JAX | 24.5 | QB1 | Healthy |  |  |
| 78 | +1 | Brock Purdy | SF | 25.7 | QB1 | Healthy | BYE |  |
| 78 | -1 | Drake Maye | NE | 24.9 | QB1 | Healthy |  |  |
| 74 | -4 | Jared Goff | DET | 24.7 | QB1 | Healthy |  |  |
| 70 | +7 | Patrick Mahomes | KC | 21.9 | QB1 | Healthy |  |  |
| 69 | +4 | Dak Prescott | DAL | 22.6 | QB1 | Healthy |  |  |
| 69 | -2 | Jayden Daniels | WAS | 22.5 | QB1 | Healthy |  |  |
| 67 | +8 | Jordan Love | GB | 23.4 | QB1 | Healthy |  | +8 vs last board; SF QB1 floor 45 |
| 67 | +7 | Kirk Cousins | LV | 25.3 | QB1 | Healthy |  |  |
| 62 | -4 | Caleb Williams | CHI | 22.1 | QB1 | Healthy |  |  |
| 61 | +2 | Bryce Young | CAR | 19.8 | QB1 | Healthy |  |  |
| 61 | +5 | Tyler Shough | NO | 22.6 | QB1 | Healthy | BYE |  |
| 54 | +2 | C.J. Stroud | HOU | 21.7 | QB1 | Healthy | BYE |  |
| 52 | -4 | Matthew Stafford | LAR | 21.2 | QB1 | Questionable |  |  |
| 47 | +2 | Bo Nix | DEN | 17.0 | QB1 | Healthy |  |  |
| 45 | -1 | Aaron Rodgers | PIT | 17.5 | QB1 | Healthy |  |  |
| 45 | — | Baker Mayfield | TB | 10.2 | QB1 | Healthy |  |  |
| 45 | — | Cam Ward | TEN | 17.9 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 15.7 | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 18.9 | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 10.2 | QB1 | Healthy | BYE |  |
| 45 | — | Jacoby Brissett | ARI | 10.1 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 12.9 | QB1 | Healthy |  |  |
| 45 | — | Malik Willis | MIA | 14.7 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 17.8 | QB1 | Healthy |  |  |
| 45 | — | Sam Darnold | SEA | 17.3 | QB1 | Healthy |  |  |
| 45 | — | Tanner McKee | PHI | 10.8 | QB1 | Healthy |  |  |
| 41 | +6 | Kyler Murray | MIN | 14.4 | QB1 | Questionable |  |  |
| 29 GUESS (29.45) | +2 | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |
| 25 | -22 | Lamar Jackson | BAL | 18.4 | QB1 | Out |  | -22 vs last board; Out x0.65 |
| 16 | -19 | Tyler Huntley | BAL | 14.9 | QB1 | Out |  | -19 vs last board; Out x0.65; buy-low: volume > points |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 96 | -2 | Jahmyr Gibbs | DET | 25.5 | RB1 | Healthy |  |  |
| 93 | -1 | Kenneth Walker III | KC | 21.3 | RB1 | Healthy |  |  |
| 89 | — | Bijan Robinson | ATL | 17.6 | RB1 | Healthy |  |  |
| 88 | — | James Cook III | BUF | 18.0 | RB1 | Questionable |  |  |
| 86 | -3 | Jonathan Taylor | IND | 16.7 | RB1 | Healthy |  |  |
| 85 | +4 | Chuba Hubbard | CAR | 17.4 | RB1 | Healthy |  |  |
| 84 | — | Derrick Henry | BAL | 16.3 | RB1 | Healthy |  |  |
| 83 | -4 | Javonte Williams | DAL | 15.9 | RB1 | Healthy |  |  |
| 81 | +1 | Christian McCaffrey | SF | 18.1 | RB1 | Questionable | BYE |  |
| 80 | +1 | Kyren Williams | LAR | 16.7 | RB1 | Healthy |  |  |
| 77 | +2 | Bucky Irving | TB | 15.2 | RB1 | Healthy |  |  |
| 75 | +5 | D'Andre Swift | CHI | 17.3 | RB1 | Healthy |  |  |
| 73 | -5 | Ashton Jeanty | LV | 14.2 | RB1 | Healthy |  |  |
| 73 | +6 | Tony Pollard | TEN | 15.2 | RB1 | Healthy |  |  |
| 72 | +3 | Bhayshul Tuten | JAX | 15.8 | RB1 | Questionable |  |  |
| 72 | — | Jaylen Warren | PIT | 16.0 | RB1 | Healthy |  |  |
| 69 | +2 | Chase Brown | CIN | 10.4 | RB1 | Healthy |  |  |
| 62 | +13 | Braelon Allen | NYJ | 12.4 | RB1 | Healthy |  | +13 vs last board |
| 62 | -7 | Ollie Gordon II | MIA | 13.9 | RB1 | Healthy |  |  |
| 62 | -1 | Quinshon Judkins | CLE | 10.9 | RB1 | Healthy |  |  |
| 58 | +6 | Rhamondre Stevenson | NE | 10.9 | RB1-split | Healthy |  |  |
| 57 | -7 | Aaron Jones Sr. | MIN | 10.3 | RB1 | Healthy |  |  |
| 56 | +3 | Cam Skattebo | NYG | 9.3 | RB1 | Questionable | BYE |  |
| 53 | -5 | Omarion Hampton | LAC | 8.1 | RB1 | Healthy |  |  |
| 41 | -1 | Emanuel Wilson | SEA | 11.8 | RB1 | Healthy |  |  |
| 40 | +11 | Tyler Allgeier | ARI | 9.2 | RB1-split | Healthy |  | +11 vs last board |
| 40 | +4 | Woody Marks | HOU | 7.4 | RB1 | Questionable | BYE |  |
| 38 | -3 | J.K. Dobbins | DEN | 6.9 | RB1 | Healthy |  |  |
| 30 | +2 | Alvin Kamara | NO | 9.1 | committee | Healthy | BYE |  |
| 30 | — | Blake Corum | LAR | 9.7 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 12.5 | committee | Out |  |  |
| 30 | — | Jonah Coleman | DEN | 13.2 | committee | Healthy |  |  |
| 30 | — | Jordan Mason | MIN | 6.9 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 18.9 | committee | Healthy |  |  |
| 30 | — | Kyle Monangai | CHI | 14.2 | committee | Out |  |  |
| 30 | — | Rachaad White | WAS | 13.3 | committee | Healthy |  |  |
| 30 | — | Saquon Barkley | PHI | 7.8 | committee | Healthy |  |  |
| 30 GUESS (30) | — | Travis Etienne Jr. | NO | 8.5 | committee | IR | BYE | IR x0.82; committee RB 21% cap 30; GUESS inputs |
| 28 | +1 | David Montgomery | HOU | 8.4 | committee | Out | BYE |  |
| 26 | +4 | Chris Rodriguez Jr. | JAX | 6.0 | committee | Questionable |  |  |
| 26 | -3 | Jeremiyah Love | ARI | 8.0 | RB1-split | Out |  |  |
| 24 | +8 | Emmett Johnson | KC | 6.3 | committee | Healthy |  | +8 vs last board; committee RB 12% cap 30 |
| 23 | — | Kimani Vidal | LAC | 4.8 | committee | Healthy |  |  |
| 23 | -13 | Zach Charbonnet | SEA | 4.4 | committee | Healthy |  | -13 vs last board; committee RB 3% cap 30 |
| 22 GUESS (21.81) | -1 | RJ Harvey | DEN | 9.2 | committee | IR |  | IR x0.82; committee RB 16% cap 30; GUESS inputs |
| 18 GUESS (17.62) | +2 | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 21% cap 30; GUESS inputs |
| 17 | -1 | TreVeyon Henderson | NE | 5.2 | committee | Out |  |  |
| 12 | — | Brian Robinson Jr. | ATL | 2.2 | committee | Out |  |  |
| 11 | -3 | Jaleel McLaughlin | CLE | 3.8 | committee | Healthy |  |  |
| 9 | -3 | Jaydon Blue | PHI | 1.4 | committee | Healthy |  |  |
| 8 | -3 | Zonovan Knight | ARI | 4.0 | committee | Out |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 23.5 | WR1 | Healthy |  |  |
| 94 | — | CeeDee Lamb | DAL | 17.3 | WR1 | Healthy |  |  |
| 92 | +4 | Puka Nacua | LAR | 18.4 | WR1 | Healthy |  |  |
| 89 | — | Amon-Ra St. Brown | DET | 16.4 | WR1 | Questionable |  |  |
| 88 | +8 | Ja'Marr Chase | CIN | 15.2 | WR1 | Healthy |  | +8 vs last board |
| 87 | +8 | Tee Higgins | CIN | 16.9 | WR2 | Healthy |  | +8 vs last board |
| 82 | — | Chris Olave | NO | 14.3 | WR1 | Healthy | BYE |  |
| 82 | -4 | Zay Flowers | BAL | 14.6 | WR1 | Healthy |  |  |
| 81 | +1 | Malik Nabers | NYG | 13.8 | WR1 | Healthy | BYE |  |
| 78 | +6 | Justin Jefferson | MIN | 12.1 | WR1 | Healthy |  |  |
| 78 | +2 | Tetairoa McMillan | CAR | 12.6 | WR1 | Healthy |  |  |
| 75 | +2 | Matthew Golden | GB | 13.8 | WR2 | Healthy |  |  |
| 74 | +1 | Christian Watson | GB | 15.7 | WR1 | Questionable |  |  |
| 74 | -7 | Parker Washington | JAX | 11.7 | WR1 | Healthy |  |  |
| 71 | +2 | Garrett Wilson | NYJ | 11.5 | WR1 | Healthy |  |  |
| 70 | -3 | Drake London | ATL | 11.3 | WR1 | Questionable |  |  |
| 66 | +7 | Luther Burden III | CHI | 11.8 | WR1 | Healthy |  |  |
| 65 | +2 | Nico Collins | HOU | 12.8 | WR1 | Healthy | BYE |  |
| 62 | +19 | Malik Washington | MIA | 12.5 | WR1 | Healthy |  | +19 vs last board |
| 61 | +7 | Michael Wilson | ARI | 10.8 | WR1 | Questionable |  |  |
| 60 | — | Jalen Coker | CAR | 11.0 | WR2 | Healthy |  |  |
| 60 | +5 | Jameson Williams | DET | 12.5 | WR2 | Healthy |  |  |
| 58 | +2 | Stefon Diggs | WAS | 11.4 | WR1 | Healthy |  |  |
| 57 | -2 | George Pickens | DAL | 10.6 | WR2 | Healthy |  |  |
| 52 | -1 | Jaylen Waddle | DEN | 8.0 | WR1 | Healthy |  |  |
| 50 | +3 | Rashee Rice | KC | 9.3 | WR1 | Healthy |  |  |
| 49 | -4 | DK Metcalf | PIT | 7.7 | WR1 | Healthy |  |  |
| 47 | +2 | Mike Evans | SF | 12.6 | WR1 | Out | BYE |  |
| 46 | +3 | DJ Moore | BUF | 9.0 | WR1 | Questionable |  |  |
| 42 | +3 | Ladd McConkey | LAC | 7.2 | WR1 | Healthy |  |  |
| 42 | +4 | Rome Odunze | CHI | 7.3 | WR2 | Healthy |  |  |
| 42 | -23 | Tre Tucker | LV | 9.4 | WR1 | Healthy |  | -23 vs last board |
| 40 | +5 | Denzel Boston | CLE | 6.2 | WR1 | Healthy |  |  |
| 38 | -1 | DeVonta Smith | PHI | 14.0 | WR1 | Out |  |  |
| 38 | — | Xavier Worthy | KC | 5.6 | WR2 | Healthy |  |  |
| 37 | -6 | Germie Bernard | PIT | 10.0 | WR2 | Healthy |  |  |
| 36 | +5 | Jordan Addison | MIN | 6.8 | WR2 | Healthy |  |  |
| 35 | — | Emeka Egbuka | TB | 9.5 | WR1 | Out |  |  |
| 33 | -2 | KC Concepcion Jr. | CLE | 5.2 | WR2 | Healthy |  |  |
| 33 | -22 | Omar Cooper Jr. | NYJ | 10.0 | WR2 | Healthy |  | -22 vs last board |
| 32 | +10 | DeMario Douglas | NE | 9.4 | WR2 | Healthy |  | +10 vs last board |
| 31 | +4 | Makai Lemon | PHI | 5.8 | WR2 | Healthy |  |  |
| 30 | -6 | Keon Coleman | BUF | 7.3 | WR | Healthy |  |  |
| 29 | -1 | Chris Godwin Jr. | TB | 4.5 | WR2 | Healthy |  |  |
| 28 GUESS (27.7) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 27 | -1 | Courtland Sutton | DEN | 4.8 | WR2 | Healthy |  |  |
| 22 | -2 | Rashod Bateman | BAL | 6.3 | WR2 | Healthy |  |  |
| 22 GUESS (21.67) | -1 | Romeo Doubs | NE | 8.5 | WR | IR |  | IR x0.82; GUESS inputs |
| 21 | — | A.J. Brown | NE | 4.9 | WR1 | Out |  |  |
| 20 | +1 | Brian Thomas Jr. | JAX | 4.1 | WR | Healthy |  |  |
| 20 | — | Marvin Harrison Jr. | HOU | 4.8 | WR2 | Healthy | BYE |  |
| 13 | +2 | Darius Cooper | PHI | 2.2 | WR | Healthy |  |  |
| 13 | -1 | Jerry Jeudy | CLE | 3.1 | WR | Healthy |  |  |
| 12 | — | Tez Johnson | TB | 0.0 | WR | Healthy |  |  |
| 10 | -1 | Konata Mumpfield | LAR | 1.0 | WR2 | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 93 | +4 | Brock Bowers | LV | 17.2 | TE1 | Healthy |  |  |
| 93 | +1 | Trey McBride | ARI | 14.7 | TE1 | Healthy |  |  |
| 83 | — | George Kittle | SF | 12.5 | TE1 | Healthy | BYE |  |
| 74 | +1 | Isaiah Likely | NYG | 11.4 | TE1 | Healthy | BYE |  |
| 64 | -1 | Travis Kelce | KC | 9.6 | TE1 | Healthy |  |  |
| 61 | +1 | Sam LaPorta | DET | 10.1 | TE1 | Healthy |  |  |
| 54 | -1 | Tyler Warren | IND | 9.8 | TE1 | Healthy |  |  |
| 52 | +4 | Dalton Kincaid | BUF | 9.4 | TE1 | Healthy |  |  |
| 52 | +7 | T.J. Hockenson | MIN | 8.8 | TE1 | Healthy |  |  |
| 47 | +5 | Colston Loveland | CHI | 7.2 | TE1 | Healthy |  |  |
| 40 | -3 | Tucker Kraft | GB | 8.9 | TE1 | Healthy |  |  |
| 25 | +2 | Kyle Pitts Sr. | ATL | 6.8 | TE1 | Healthy |  |  |
| 21 | -1 | Dallas Goedert | PHI | 5.9 | TE1 | Healthy |  |  |
| 20 | -1 | Mark Andrews | BAL | 3.4 | TE1 | Healthy |  |  |
| 10 | -1 | Hunter Henry | NE | 4.5 | TE1 | Out |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Josh Jacobs | RB | 30 | 96 | 66 | committee RB 22% cap 30 |
| Davante Adams | WR | 28 | 85 | 57 | IR x0.50; GUESS inputs |
| Jacoby Brissett | QB | 45 | 0 | 45 | SF QB1 floor 45; buy-low: volume > points |
| DeVonta Smith | WR | 38 | 81 | 44 | Out x0.65 |
| J.J. McCarthy | QB | 45 | 3 | 42 | SF QB1 floor 45 |
| Baker Mayfield | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Kyle Monangai | RB | 30 | 66 | 36 | Out x0.65; committee RB 26% cap 30 |
| Tanner McKee | QB | 45 | 9 | 36 | SF QB1 floor 45 |
| Justin Herbert | QB | 45 | 12 | 32 | SF QB1 floor 45; buy-low: volume > points |
| Rachaad White | RB | 30 | 62 | 32 | committee RB 33% cap 30 |
| Jonah Coleman | RB | 30 | 60 | 30 | committee RB 20% cap 30 |
| Breece Hall | RB | 30 | 58 | 28 | Out x0.65; committee RB 28% cap 30 |
| Mike Evans | WR | 47 | 74 | 27 | Out x0.65 |
| Malik Willis | QB | 45 | 19 | 26 | SF QB1 floor 45; buy-low: volume > points |
| Kyler Murray | QB | 41 | 16 | 25 | Questionable x0.95; buy-low: volume > points |
