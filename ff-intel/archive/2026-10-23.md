# FF Intel trade board — Bot or Not Fantasy

Generated 2026-10-23 08:01 AM EDT

- **NFL week:** 7
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-10-23 week 7 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 88 | — | Josh Allen | BUF | 30.5 | QB1 | Healthy | BYE |  |
| 82 | — | Brock Purdy | SF | 27.3 | QB1 | Healthy |  |  |
| 82 | — | Jared Goff | DET | 27.8 | QB1 | Healthy |  |  |
| 82 | — | Joe Burrow | CIN | 25.2 | QB1 | Healthy |  |  |
| 79 | — | Trevor Lawrence | JAX | 24.4 | QB1 | Healthy | BYE |  |
| 73 | — | Drake Maye | NE | 23.3 | QB1 | Healthy |  |  |
| 70 | — | Bryce Young | CAR | 24.0 | QB1 | Healthy |  |  |
| 70 | — | Patrick Mahomes | KC | 23.0 | QB1 | Healthy |  |  |
| 68 | — | Lamar Jackson | BAL | 23.0 | QB1 | Questionable |  |  |
| 64 | — | Jayden Daniels | WAS | 23.9 | QB1 | Healthy | BYE |  |
| 64 | — | Jordan Love | GB | 22.7 | QB1 | Healthy |  |  |
| 62 | -2 | Kirk Cousins | LV | 24.0 | QB1 | Healthy |  |  |
| 61 | — | Tyler Shough | NO | 23.5 | QB1 | Healthy |  |  |
| 59 | — | Aaron Rodgers | PIT | 24.5 | QB1 | Healthy |  |  |
| 58 | — | Dak Prescott | DAL | 21.6 | QB1 | Healthy |  |  |
| 55 | — | Matthew Stafford | LAR | 22.3 | QB1 | Healthy |  |  |
| 54 | +4 | Caleb Williams | CHI | 22.8 | QB1 | Healthy |  |  |
| 50 | -2 | C.J. Stroud | HOU | 21.9 | QB1 | Healthy |  |  |
| 46 GUESS (46.01) | +1 | Jameis Winston | NYG | 18.6 | QB1 | Healthy |  | SF QB1 floor 45; buy-low: volume > points; GUESS inputs |
| 45 | — | Bo Nix | DEN | 14.1 | QB1 | Healthy |  |  |
| 45 | — | Cam Ward | TEN | 11.7 | QB1 | Healthy |  |  |
| 45 | — | Daniel Jones | IND | 12.5 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 16.0 | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 15.8 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | ARI | 8.7 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 13.4 | QB1 | Healthy | BYE |  |
| 45 | — | Kyler Murray | MIN | 11.4 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 20.1 | QB1 | Healthy |  |  |
| 45 | — | Sam Darnold | SEA | 16.4 | QB1 | Healthy |  |  |
| 29 GUESS (28.52) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; buy-low: volume > points; GUESS inputs |
| 23 | -1 | Baker Mayfield | TB | 13.7 | QB1 | Questionable |  |  |
| 19 | +10 | J.J. McCarthy | NYG | — | QB2 | Healthy |  | +10 vs last board; backup QB cap 25 |
| 18 | -4 | Tanner McKee | PHI | — | QB2 | Healthy |  |  |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 97 | — | Jahmyr Gibbs | DET | 28.0 | RB1 | Healthy |  |  |
| 94 | — | Kenneth Walker III | KC | 26.2 | RB1 | Healthy |  |  |
| 91 | — | Jonathan Taylor | IND | 18.5 | RB1 | Healthy |  |  |
| 90 | +1 | James Cook III | BUF | 18.1 | RB1 | Healthy | BYE |  |
| 89 | -1 | Derrick Henry | BAL | 18.7 | RB1 | Healthy |  |  |
| 88 | — | Bijan Robinson | ATL | 19.8 | RB1 | Healthy |  |  |
| 86 | — | Chuba Hubbard | CAR | 18.5 | RB1 | Healthy |  |  |
| 85 | -1 | Christian McCaffrey | SF | 18.0 | RB1 | Healthy |  |  |
| 84 | — | Javonte Williams | DAL | 16.6 | RB1 | Healthy |  |  |
| 81 | — | Kyren Williams | LAR | 17.3 | RB1 | Healthy |  |  |
| 78 | +1 | Ashton Jeanty | LV | 14.6 | RB1 | Healthy |  |  |
| 76 | — | Jaylen Warren | PIT | 15.4 | RB1 | Healthy |  |  |
| 71 | — | Chase Brown | CIN | 10.6 | RB1 | Healthy |  |  |
| 70 | -1 | Bucky Irving | TB | 12.8 | RB1 | Questionable |  |  |
| 70 | -2 | D'Andre Swift | CHI | 15.8 | RB1-split | Healthy |  |  |
| 69 | — | Bhayshul Tuten | JAX | 13.7 | RB1 | Healthy | BYE |  |
| 69 | — | Ollie Gordon II | MIA | 15.9 | RB1-split | Healthy |  |  |
| 67 | -1 | Aaron Jones Sr. | MIN | 12.8 | RB1 | Healthy |  |  |
| 58 | -1 | Quinshon Judkins | CLE | 9.5 | RB1 | Questionable |  |  |
| 56 | -1 | Omarion Hampton | LAC | 8.8 | RB1 | Healthy | BYE |  |
| 55 | — | Tony Pollard | TEN | 7.2 | RB1 | Healthy |  |  |
| 53 | — | Rhamondre Stevenson | NE | 9.5 | RB1-split | Healthy |  |  |
| 52 | -1 | J.K. Dobbins | DEN | 7.6 | RB1 | Healthy |  |  |
| 51 | +4 | Cam Skattebo | NYG | 7.7 | RB1 | Healthy |  |  |
| 48 | -1 | Braelon Allen | NYJ | 9.7 | RB1 | Healthy |  |  |
| 41 | -1 | Woody Marks | HOU | 6.8 | RB1-split | Healthy |  |  |
| 38 | — | Emanuel Wilson | SEA | 8.7 | RB1 | Healthy |  |  |
| 36 | -3 | David Montgomery | HOU | 8.4 | RB1-split | Doubtful |  |  |
| 30 | — | Blake Corum | LAR | 8.0 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 12.5 | committee | Questionable |  |  |
| 30 | — | Dameon Pierce | PHI | 13.0 | committee | Healthy |  |  |
| 30 GUESS (30) | — | Jordan Mason | MIN | 11.9 | committee | IR |  | IR x0.83; committee RB 12% cap 30; GUESS inputs |
| 30 GUESS (30) | — | Josh Jacobs | GB | — | committee | Healthy |  | committee RB 35% cap 30; buy-low: volume > points; GUESS inputs |
| 30 | — | Kyle Monangai | CHI | 14.2 | committee | Out |  |  |
| 30 | — | Rachaad White | WAS | 13.7 | committee | Healthy | BYE |  |
| 30 | — | Saquon Barkley | PHI | 5.2 | committee | Questionable |  |  |
| 30 GUESS (30) | — | Travis Etienne Jr. | NO | 8.5 | committee | IR |  | IR x0.83; committee RB 23% cap 30; GUESS inputs |
| 30 | — | TreVeyon Henderson | NE | 5.6 | committee | Healthy |  |  |
| 30 | — | Tyler Allgeier | ARI | 5.6 | committee | Healthy |  |  |
| 28 | -2 | Alvin Kamara | NO | 9.0 | committee | Questionable |  |  |
| 26 GUESS (26.15) | — | Zach Charbonnet | SEA | — | committee | Questionable |  | Questionable x0.95; committee RB 20% cap 30; GUESS inputs |
| 24 | — | Chris Rodriguez Jr. | JAX | 5.0 | committee | Healthy | BYE |  |
| 22 | +2 | Kendre Miller | NO | 4.3 | committee | Healthy |  |  |
| 22 | — | Kimani Vidal | LAC | 5.5 | committee | Healthy | BYE |  |
| 19 | — | Brian Robinson Jr. | ATL | 2.2 | committee | Questionable |  |  |
| 18 GUESS (18.5) | -1 | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 32% cap 30; GUESS inputs |
| 17 | — | Emmett Johnson | KC | 3.8 | committee | Healthy |  |  |
| 17 | — | Jaleel McLaughlin | CLE | 7.5 | committee | Healthy |  |  |
| 15 GUESS (14.6) | +1 | Dylan Sampson | CLE | — | committee | IR |  | IR x0.83; committee RB 20% cap 30; GUESS inputs |
| 10 | — | Roschon Johnson | CHI | 0.0 | committee | Healthy |  |  |
| 9 GUESS (9.33) | — | Jonah Coleman | DEN | — | committee | IR |  | IR x0.83; committee RB 8% cap 30; GUESS inputs |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 23.4 | WR1 | Healthy |  |  |
| 93 | — | Amon-Ra St. Brown | DET | 17.1 | WR1 | Healthy |  |  |
| 92 | — | CeeDee Lamb | DAL | 17.9 | WR1 | Healthy |  |  |
| 86 | — | Zay Flowers | BAL | 15.7 | WR1 | Healthy |  |  |
| 84 | — | Chris Olave | NO | 15.2 | WR1 | Healthy |  |  |
| 83 | -5 | Puka Nacua | LAR | 18.3 | WR1 | Questionable |  |  |
| 82 | -3 | Tetairoa McMillan | CAR | 14.6 | WR1 | Healthy |  |  |
| 80 | +1 | Malik Nabers | NYG | 13.7 | WR1 | Healthy |  |  |
| 77 | — | Christian Watson | GB | 17.4 | WR1 | Questionable |  |  |
| 77 | — | Ja'Marr Chase | CIN | 13.3 | WR1 | Healthy |  |  |
| 77 | — | Parker Washington | JAX | 13.2 | WR1 | Healthy | BYE |  |
| 75 | -2 | Drake London | ATL | 12.2 | WR1 | Healthy |  |  |
| 75 | — | Garrett Wilson | NYJ | 12.9 | WR1 | Healthy |  |  |
| 74 | +4 | Justin Jefferson | MIN | 13.6 | WR1 | Healthy |  |  |
| 73 | +1 | Tee Higgins | CIN | 12.4 | WR2 | Healthy |  |  |
| 71 | — | Nico Collins | HOU | 15.6 | WR1 | Healthy |  |  |
| 70 | -1 | Matthew Golden | GB | 14.3 | WR2 | Questionable |  |  |
| 69 | +4 | Jalen Coker | CAR | 14.0 | WR2 | Healthy |  |  |
| 69 | — | Mike Evans | SF | 12.6 | WR1 | Questionable |  |  |
| 67 | -4 | DeVonta Smith | PHI | 14.0 | WR1 | Questionable |  |  |
| 62 | — | Germie Bernard | PIT | 20.2 | WR2 | Healthy |  |  |
| 60 | — | George Pickens | DAL | 10.9 | WR2 | Questionable |  |  |
| 60 | -1 | Luther Burden III | CHI | 9.6 | WR1 | Healthy |  |  |
| 60 | -2 | Michael Wilson | ARI | 9.1 | WR1 | Healthy |  |  |
| 58 | +1 | Emeka Egbuka | TB | 9.5 | WR1 | Questionable |  |  |
| 56 | +3 | Stefon Diggs | WAS | 11.5 | WR2 | Healthy | BYE |  |
| 54 | -2 | DK Metcalf | PIT | 9.0 | WR1 | Healthy |  |  |
| 52 | — | Jameson Williams | DET | 9.7 | WR2 | Healthy |  |  |
| 50 | — | Jaylen Waddle | DEN | 7.3 | WR1 | Questionable |  |  |
| 45 | — | Rashee Rice | KC | 7.9 | WR | Questionable |  |  |
| 42 | — | Jakobi Meyers | JAX | 8.4 | WR2 | Healthy | BYE |  |
| 41 | — | Xavier Worthy | KC | 7.0 | WR1 | Healthy |  |  |
| 38 | +1 | Denzel Boston | CLE | 7.0 | WR1 | Questionable |  |  |
| 38 | +1 | Keenan Allen | IND | 8.7 | WR2 | Healthy |  |  |
| 37 | — | Rome Odunze | CHI | 6.5 | WR2 | Healthy |  |  |
| 36 | -1 | Keon Coleman | BUF | 10.6 | WR2 | Healthy | BYE |  |
| 35 | — | Jordan Addison | MIN | 6.9 | WR | Healthy |  |  |
| 33 | -1 | A.J. Brown | NE | 4.2 | WR1 | Healthy |  |  |
| 29 | +1 | Courtland Sutton | DEN | 4.1 | WR2 | Healthy |  |  |
| 28 | — | DJ Moore | BUF | 7.6 | WR | Out | BYE |  |
| 27 GUESS (26.73) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 27 | — | Tre Tucker | LV | — | WR1 | Healthy |  |  |
| 25 | — | Deebo Samuel Sr. | SF | 10.5 | WR | Out |  |  |
| 25 | — | Rashod Bateman | BAL | 7.5 | WR2 | Healthy |  |  |
| 23 GUESS (23.15) | -1 | Terry McLaurin | WAS | 7.7 | WR1 | Out | BYE | Out x0.65; GUESS inputs |
| 22 | -1 | DeMario Douglas | NE | — | WR2 | Healthy |  |  |
| 22 | — | Ladd McConkey | LAC | 6.5 | WR1 | Out | BYE |  |
| 22 | — | Makai Lemon | PHI | 3.5 | WR | Healthy |  |  |
| 22 | — | Quentin Johnston | LAC | 4.2 | WR2 | Healthy | BYE |  |
| 22 GUESS (22.27) | — | Romeo Doubs | NE | 8.5 | WR | IR |  | IR x0.83; GUESS inputs |
| 18 | -1 | Omar Cooper Jr. | NYJ | — | WR | Healthy |  |  |
| 17 | — | Brian Thomas Jr. | JAX | 3.5 | WR | Healthy | BYE |  |
| 17 | — | Marvin Harrison Jr. | HOU | 4.4 | WR | Healthy |  |  |
| 14 | — | Jaylin Noel | HOU | — | WR | Healthy |  |  |
| 13 | — | Jerry Jeudy | CLE | 3.5 | WR | Healthy |  |  |
| 10 | — | Darius Cooper | PHI | 1.4 | WR | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 91 | +4 | Brock Bowers | LV | 17.1 | TE1 | Healthy |  |  |
| 91 | +2 | Trey McBride | ARI | 13.1 | TE1 | Healthy |  |  |
| 83 | -2 | George Kittle | SF | 12.8 | TE1 | Healthy |  |  |
| 81 | — | Isaiah Likely | NYG | 13.2 | TE1 | Healthy |  |  |
| 73 | — | Sam LaPorta | DET | 12.6 | TE1 | Healthy |  |  |
| 60 | — | Travis Kelce | KC | 10.4 | TE1 | Questionable |  |  |
| 58 | — | Tyler Warren | IND | 11.0 | TE | Questionable |  |  |
| 50 | +3 | Harold Fannin Jr. | CLE | 7.3 | TE1 | Healthy |  |  |
| 48 | — | Tucker Kraft | GB | 7.3 | TE1 | Healthy |  |  |
| 47 | +2 | Dalton Kincaid | BUF | 8.2 | TE1 | Questionable | BYE |  |
| 37 | -7 | Mark Andrews | BAL | — | TE1 | Healthy |  |  |
| 32 | — | Colston Loveland | CHI | 5.5 | TE1 | Healthy |  |  |
| 32 | +4 | Kyle Pitts Sr. | ATL | 7.1 | TE1 | Healthy |  |  |
| 31 | -2 | T.J. Hockenson | MIN | 1.2 | TE1 | Questionable |  |  |
| 30 | +1 | Dallas Goedert | PHI | 5.6 | TE1 | Questionable |  |  |
| 19 | -2 | Jake Ferguson | DAL | 6.0 | TE1 | Healthy |  |  |
| 12 | — | Tyler Higbee | LAR | 2.2 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Davante Adams | WR | 27 | 80 | 53 | IR x0.50; GUESS inputs |
| Jacoby Brissett | QB | 45 | 0 | 45 | SF QB1 floor 45; buy-low: volume > points |
| Kyler Murray | QB | 45 | 3 | 42 | SF QB1 floor 45 |
| Kyle Monangai | RB | 30 | 70 | 40 | Out x0.65; committee RB 34% cap 30 |
| Cam Ward | QB | 45 | 7 | 38 | SF QB1 floor 45; buy-low: volume > points |
| Rachaad White | RB | 30 | 67 | 37 | committee RB 30% cap 30 |
| Mark Andrews | TE | 37 | 0 | 37 | buy-low: volume > points |
| Germie Bernard | WR | 62 | 98 | 36 | proj 62 / prod 98 / role 25 |
| Daniel Jones | QB | 45 | 10 | 35 | SF QB1 floor 45; buy-low: volume > points |
| Dameon Pierce | RB | 30 | 63 | 33 | committee RB 22% cap 30 |
| Justin Herbert | QB | 45 | 13 | 32 | SF QB1 floor 45; buy-low: volume > points |
| Tony Pollard | RB | 55 | 24 | 31 | buy-low: volume > points |
| T.J. Hockenson | TE | 31 | 0 | 31 | Questionable x0.95; buy-low: volume > points |
| Josh Jacobs | RB | 30 | 0 | 30 | committee RB 35% cap 30; buy-low: volume > points; GUESS inputs |
| Aaron Rodgers | QB | 59 | 87 | 28 | SF QB1 floor 45 |
