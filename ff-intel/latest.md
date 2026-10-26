# FF Intel trade board — Bot or Not Fantasy

Generated 2026-10-26 08:00 AM EDT

- **NFL week:** 7
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-10-26 week 7 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 89 | — | Josh Allen | BUF | 30.5 | QB1 | Healthy | BYE |  |
| 83 | — | Jared Goff | DET | 27.8 | QB1 | Healthy |  |  |
| 82 | — | Brock Purdy | SF | 27.3 | QB1 | Healthy |  |  |
| 82 | +1 | Joe Burrow | CIN | 25.2 | QB1 | Healthy |  |  |
| 78 | -1 | Trevor Lawrence | JAX | 24.4 | QB1 | Healthy | BYE |  |
| 74 | — | Drake Maye | NE | 23.3 | QB1 | Healthy |  |  |
| 71 | — | Bryce Young | CAR | 24.0 | QB1 | Healthy |  |  |
| 70 | — | Patrick Mahomes | KC | 23.0 | QB1 | Healthy |  |  |
| 64 | — | Jayden Daniels | WAS | 23.9 | QB1 | Healthy | BYE |  |
| 63 | — | Jordan Love | GB | 22.7 | QB1 | Healthy |  |  |
| 63 | — | Kirk Cousins | LV | 24.0 | QB1 | Healthy |  |  |
| 60 | — | Aaron Rodgers | PIT | 24.5 | QB1 | Healthy |  |  |
| 60 | — | Tyler Shough | NO | 23.5 | QB1 | Healthy |  |  |
| 55 | — | Dak Prescott | DAL | 21.6 | QB1 | Healthy |  |  |
| 54 | — | Matthew Stafford | LAR | 22.3 | QB1 | Healthy |  |  |
| 53 | — | Caleb Williams | CHI | 22.8 | QB1 | Healthy |  |  |
| 50 | — | C.J. Stroud | HOU | 21.9 | QB1 | Healthy |  |  |
| 45 | — | Baker Mayfield | TB | 13.7 | QB1 | Healthy |  |  |
| 45 | — | Bo Nix | DEN | 14.1 | QB1 | Healthy |  |  |
| 45 | — | Daniel Jones | IND | 12.5 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 16.0 | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 15.8 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | ARI | 8.7 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 13.4 | QB1 | Healthy | BYE |  |
| 45 | — | Kyler Murray | MIN | 11.4 | QB1 | Healthy |  |  |
| 45 | — | Lamar Jackson | BAL | 23.0 | QB1 | Out |  |  |
| 45 | — | Michael Penix Jr. | ATL | 20.1 | QB1 | Healthy |  |  |
| 45 | — | Sam Darnold | SEA | 16.4 | QB1 | Healthy |  |  |
| 45 | — | Tyler Huntley | BAL | 21.7 | QB1 | Healthy |  |  |
| 28 GUESS (27.78) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; buy-low: volume > points; GUESS inputs |
| 18 | — | J.J. McCarthy | NYG | — | QB2 | Healthy |  |  |
| 18 | — | Tanner McKee | PHI | — | QB2 | Healthy |  |  |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 97 | — | Jahmyr Gibbs | DET | 28.0 | RB1 | Healthy |  |  |
| 94 | — | Kenneth Walker III | KC | 26.2 | RB1 | Healthy |  |  |
| 91 | — | Jonathan Taylor | IND | 18.5 | RB1 | Healthy |  |  |
| 90 | — | James Cook III | BUF | 18.1 | RB1 | Healthy | BYE |  |
| 89 | — | Derrick Henry | BAL | 18.7 | RB1 | Healthy |  |  |
| 88 | — | Bijan Robinson | ATL | 19.8 | RB1 | Healthy |  |  |
| 86 | — | Chuba Hubbard | CAR | 18.5 | RB1 | Healthy |  |  |
| 84 | — | Javonte Williams | DAL | 16.6 | RB1 | Healthy |  |  |
| 81 | — | Christian McCaffrey | SF | 18.0 | RB1 | Questionable |  |  |
| 81 | — | Kyren Williams | LAR | 17.3 | RB1 | Healthy |  |  |
| 79 | — | Ashton Jeanty | LV | 14.6 | RB1 | Healthy |  |  |
| 76 | — | Jaylen Warren | PIT | 15.4 | RB1 | Healthy |  |  |
| 75 | — | Bucky Irving | TB | 12.8 | RB1 | Healthy |  |  |
| 72 | — | Chase Brown | CIN | 10.6 | RB1 | Healthy |  |  |
| 70 | — | Bhayshul Tuten | JAX | 13.7 | RB1 | Healthy | BYE |  |
| 70 | — | D'Andre Swift | CHI | 15.8 | RB1-split | Healthy |  |  |
| 67 | — | Ollie Gordon II | MIA | 15.9 | RB1-split | Healthy |  |  |
| 65 | — | Aaron Jones Sr. | MIN | 12.8 | RB1 | Questionable |  |  |
| 63 | — | Quinshon Judkins | CLE | 9.5 | RB1 | Healthy |  |  |
| 59 | — | Omarion Hampton | LAC | 8.8 | RB1 | Healthy | BYE |  |
| 57 | — | Tony Pollard | TEN | 7.2 | RB1 | Healthy |  |  |
| 54 | — | Rhamondre Stevenson | NE | 9.5 | RB1-split | Healthy |  |  |
| 53 | — | J.K. Dobbins | DEN | 7.6 | RB1 | Healthy |  |  |
| 51 | — | Braelon Allen | NYJ | 9.7 | RB1 | Healthy |  |  |
| 50 GUESS (49.53) | — | Josh Jacobs | GB | — | RB1 | Healthy |  | buy-low: volume > points; GUESS inputs |
| 49 | — | Cam Skattebo | NYG | 7.7 | RB1 | Questionable |  |  |
| 40 | — | Emanuel Wilson | SEA | 8.7 | RB1 | Healthy |  |  |
| 39 | — | Woody Marks | HOU | 6.8 | RB1-split | Questionable |  |  |
| 30 | — | Alvin Kamara | NO | 9.0 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 8.0 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 12.5 | committee | Out |  |  |
| 30 | — | Dameon Pierce | PHI | 13.0 | committee | Healthy |  |  |
| 30 | — | David Montgomery | HOU | 8.4 | RB1-split | Out |  |  |
| 30 | — | Jordan Mason | MIN | 11.9 | committee | Healthy |  |  |
| 30 | — | Kyle Monangai | CHI | 14.2 | committee | Out |  |  |
| 30 | — | RJ Harvey | DEN | 8.4 | committee | Healthy |  |  |
| 30 | — | Saquon Barkley | PHI | 5.2 | committee | Questionable |  |  |
| 30 GUESS (30) | — | Travis Etienne Jr. | NO | 8.5 | committee | IR |  | IR x0.83; committee RB 23% cap 30; GUESS inputs |
| 30 | — | TreVeyon Henderson | NE | 5.6 | committee | Healthy |  |  |
| 30 | — | Tyler Allgeier | ARI | 5.6 | committee | Healthy |  |  |
| 25 | — | Chris Rodriguez Jr. | JAX | 5.0 | committee | Healthy | BYE |  |
| 25 | — | Kimani Vidal | LAC | 5.5 | committee | Healthy | BYE |  |
| 22 | — | Kendre Miller | NO | 4.3 | committee | Healthy |  |  |
| 19 GUESS (18.53) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 32% cap 30; GUESS inputs |
| 19 GUESS (19.43) | — | Dylan Sampson | CLE | — | committee | Healthy |  | committee RB 20% cap 30; GUESS inputs |
| 18 | — | Emmett Johnson | KC | 3.8 | committee | Healthy |  |  |
| 18 GUESS (17.56) | — | Zach Charbonnet | SEA | — | committee | Out |  | Out x0.65; committee RB 20% cap 30; GUESS inputs |
| 17 | — | Jaleel McLaughlin | CLE | 7.5 | committee | Healthy |  |  |
| 13 | — | Brian Robinson Jr. | ATL | 2.2 | committee | Out |  |  |
| 13 | — | Jonah Coleman | DEN | — | committee | Healthy |  |  |
| 11 | — | Zonovan Knight | ARI | — | committee | Healthy |  |  |
| 9 | — | Roschon Johnson | CHI | 0.0 | committee | Healthy |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 23.4 | WR1 | Healthy |  |  |
| 93 | — | Amon-Ra St. Brown | DET | 17.1 | WR1 | Healthy |  |  |
| 92 | — | CeeDee Lamb | DAL | 17.9 | WR1 | Healthy |  |  |
| 87 | — | Puka Nacua | LAR | 18.3 | WR1 | Healthy |  |  |
| 85 | — | Zay Flowers | BAL | 15.7 | WR1 | Healthy |  |  |
| 83 | — | Chris Olave | NO | 15.2 | WR1 | Healthy |  |  |
| 81 | — | Tetairoa McMillan | CAR | 14.6 | WR1 | Healthy |  |  |
| 80 | — | Christian Watson | GB | 17.4 | WR1 | Healthy |  |  |
| 79 | — | Malik Nabers | NYG | 13.7 | WR1 | Healthy |  |  |
| 76 | — | Ja'Marr Chase | CIN | 13.3 | WR1 | Healthy |  |  |
| 76 | — | Parker Washington | JAX | 13.2 | WR1 | Healthy | BYE |  |
| 74 | — | Garrett Wilson | NYJ | 12.9 | WR1 | Healthy |  |  |
| 73 | — | Justin Jefferson | MIN | 13.6 | WR1 | Healthy |  |  |
| 73 | — | Matthew Golden | GB | 14.3 | WR2 | Healthy |  |  |
| 72 | — | Tee Higgins | CIN | 12.4 | WR2 | Healthy |  |  |
| 71 | — | Nico Collins | HOU | 15.6 | WR1 | Healthy |  |  |
| 70 | — | Drake London | ATL | 12.2 | WR1 | Questionable |  |  |
| 68 | — | Jalen Coker | CAR | 14.0 | WR2 | Healthy |  |  |
| 63 | — | George Pickens | DAL | 10.9 | WR2 | Healthy |  |  |
| 63 | — | Germie Bernard | PIT | 20.2 | WR2 | Healthy |  |  |
| 60 | — | Michael Wilson | ARI | 9.1 | WR1 | Healthy |  |  |
| 59 | — | Luther Burden III | CHI | 9.6 | WR1 | Healthy |  |  |
| 56 | — | DK Metcalf | PIT | 9.0 | WR1 | Healthy |  |  |
| 54 | — | Stefon Diggs | WAS | 11.5 | WR2 | Healthy | BYE |  |
| 52 | — | Jameson Williams | DET | 9.7 | WR2 | Healthy |  |  |
| 49 | -3 | Jaylen Waddle | DEN | 7.3 | WR1 | Questionable |  |  |
| 46 | — | Mike Evans | SF | 12.6 | WR | Out |  |  |
| 42 | — | DeVonta Smith | PHI | 14.0 | WR | Out |  |  |
| 42 | — | Xavier Worthy | KC | 7.0 | WR1 | Healthy |  |  |
| 41 | — | Denzel Boston | CLE | 7.0 | WR1 | Healthy |  |  |
| 38 | — | Rome Odunze | CHI | 6.5 | WR2 | Healthy |  |  |
| 37 | — | Emeka Egbuka | TB | 9.5 | WR | Out |  |  |
| 36 | -1 | Keon Coleman | BUF | 10.6 | WR2 | Healthy | BYE |  |
| 35 | -1 | Jordan Addison | MIN | 6.9 | WR2 | Healthy |  |  |
| 34 | — | A.J. Brown | NE | 4.2 | WR1 | Healthy |  |  |
| 31 | +1 | Chris Godwin Jr. | TB | 5.9 | WR1 | Healthy |  |  |
| 31 | — | Rashee Rice | KC | 7.9 | WR | Out |  |  |
| 30 | — | Courtland Sutton | DEN | 4.1 | WR2 | Healthy |  |  |
| 29 | — | DJ Moore | BUF | 7.6 | WR | Out | BYE |  |
| 28 | — | Tre Tucker | LV | — | WR1 | Healthy |  |  |
| 27 GUESS (26.88) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 27 | — | Rashod Bateman | BAL | 7.5 | WR2 | Healthy |  |  |
| 24 | — | Makai Lemon | PHI | 3.5 | WR1 | Healthy |  |  |
| 23 | — | DeMario Douglas | NE | — | WR2 | Healthy |  |  |
| 23 GUESS (23.18) | — | Romeo Doubs | NE | 8.5 | WR | IR |  | IR x0.83; GUESS inputs |
| 22 | — | Ladd McConkey | LAC | 6.5 | WR1 | Out | BYE |  |
| 20 | — | Omar Cooper Jr. | NYJ | — | WR2 | Healthy |  |  |
| 19 | — | Brian Thomas Jr. | JAX | 3.5 | WR | Healthy | BYE |  |
| 18 | — | Marvin Harrison Jr. | HOU | 4.4 | WR | Healthy |  |  |
| 16 | — | Jaylin Noel | HOU | — | WR2 | Questionable |  |  |
| 14 | — | Jerry Jeudy | CLE | 3.5 | WR | Healthy |  |  |
| 14 | — | Konata Mumpfield | LAR | — | WR2 | Healthy |  |  |
| 13 | — | Darius Cooper | PHI | 1.4 | WR2 | Healthy |  |  |
| 8 | — | Tank Dell | HOU | — | WR | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 91 | — | Brock Bowers | LV | 17.1 | TE1 | Healthy |  |  |
| 91 | — | Trey McBride | ARI | 13.1 | TE1 | Healthy |  |  |
| 83 | — | George Kittle | SF | 12.8 | TE1 | Healthy |  |  |
| 81 | — | Isaiah Likely | NYG | 13.2 | TE1 | Healthy |  |  |
| 73 | — | Sam LaPorta | DET | 12.6 | TE1 | Healthy |  |  |
| 63 | — | Travis Kelce | KC | 10.4 | TE1 | Healthy |  |  |
| 50 | — | Harold Fannin Jr. | CLE | 7.3 | TE1 | Healthy |  |  |
| 48 | — | Tucker Kraft | GB | 7.3 | TE1 | Healthy |  |  |
| 47 | — | Dalton Kincaid | BUF | 8.2 | TE1 | Questionable | BYE |  |
| 40 | — | Tyler Warren | IND | 11.0 | TE | Out |  |  |
| 37 | — | Mark Andrews | BAL | — | TE1 | Healthy |  |  |
| 33 | — | T.J. Hockenson | MIN | 1.2 | TE1 | Healthy |  |  |
| 32 | — | Colston Loveland | CHI | 5.5 | TE1 | Healthy |  |  |
| 32 | — | Kyle Pitts Sr. | ATL | 7.1 | TE1 | Healthy |  |  |
| 31 | — | Dallas Goedert | PHI | 5.6 | TE1 | Healthy |  |  |
| 19 | — | Jake Ferguson | DAL | 6.0 | TE1 | Healthy |  |  |
| 12 | — | Tyler Higbee | LAR | 2.2 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Davante Adams | WR | 27 | 79 | 52 | IR x0.50; GUESS inputs |
| Josh Jacobs | RB | 50 | 0 | 50 | buy-low: volume > points; GUESS inputs |
| Jacoby Brissett | QB | 45 | 0 | 45 | SF QB1 floor 45; buy-low: volume > points |
| Kyler Murray | QB | 45 | 3 | 42 | SF QB1 floor 45 |
| Kyle Monangai | RB | 30 | 70 | 40 | Out x0.65; committee RB 34% cap 30 |
| Daniel Jones | QB | 45 | 7 | 38 | SF QB1 floor 45; buy-low: volume > points |
| Mark Andrews | TE | 37 | 0 | 37 | buy-low: volume > points |
| Dameon Pierce | RB | 30 | 65 | 35 | committee RB 22% cap 30 |
| Germie Bernard | WR | 63 | 98 | 35 | proj 64 / prod 98 / role 26 |
| Justin Herbert | QB | 45 | 10 | 35 | SF QB1 floor 45; buy-low: volume > points |
| Tony Pollard | RB | 57 | 24 | 33 | buy-low: volume > points |
| T.J. Hockenson | TE | 33 | 0 | 33 | buy-low: volume > points |
| DeVonta Smith | WR | 42 | 74 | 32 | Out x0.65 |
| Baker Mayfield | QB | 45 | 14 | 31 | SF QB1 floor 45 |
| Breece Hall | RB | 30 | 59 | 29 | Out x0.65; committee RB 38% cap 30 |
