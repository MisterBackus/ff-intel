# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-09 05:00 PM EST

- **NFL week:** 9
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-09 week 9 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | — | Joe Burrow | CIN | 30.8 | QB1 | Healthy |  |  |
| 87 | — | Josh Allen | BUF | 30.6 | QB1 | Healthy |  |  |
| 80 | — | Brock Purdy | SF | 25.7 | QB1 | Healthy |  |  |
| 79 | — | Drake Maye | NE | 24.9 | QB1 | Healthy |  |  |
| 77 | — | Trevor Lawrence | JAX | 24.5 | QB1 | Healthy |  |  |
| 75 | — | Jared Goff | DET | 24.7 | QB1 | Healthy |  |  |
| 71 | — | Jayden Daniels | WAS | 22.5 | QB1 | Healthy |  |  |
| 69 | — | Jordan Love | GB | 23.4 | QB1 | Healthy |  |  |
| 68 | — | Kirk Cousins | LV | 25.3 | QB1 | Healthy |  |  |
| 68 | — | Tyler Shough | NO | 22.6 | QB1 | Healthy |  |  |
| 67 | — | Patrick Mahomes | KC | 21.9 | QB1 | Questionable |  |  |
| 66 | — | Dak Prescott | DAL | 22.6 | QB1 | Healthy |  |  |
| 65 | — | Caleb Williams | CHI | 22.1 | QB1 | Healthy |  |  |
| 62 | — | C.J. Stroud | HOU | 21.7 | QB1 | Healthy |  |  |
| 61 | — | Bryce Young | CAR | 19.8 | QB1 | Healthy |  |  |
| 57 | — | Matthew Stafford | LAR | 21.2 | QB1 | Healthy |  |  |
| 51 | — | Bo Nix | DEN | 17.0 | QB1 | Healthy |  |  |
| 50 | — | Geno Smith | NYJ | 18.9 | QB1 | Healthy |  |  |
| 45 | — | Aaron Rodgers | PIT | 17.5 | QB1 | Healthy | BYE |  |
| 45 | — | Baker Mayfield | TB | 10.2 | QB1 | Healthy |  |  |
| 45 | — | Cam Ward | TEN | 17.9 | QB1 | Healthy | BYE |  |
| 45 | — | Carson Wentz | MIN | 6.3 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 10.1 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 17.8 | QB1 | Healthy |  |  |
| 43 | -3 | Malik Willis | MIA | 14.7 | QB1 | Questionable |  |  |
| 38 | — | Justin Herbert | LAC | 12.9 | QB1 | Questionable |  |  |
| 33 | — | Drew Lock | SEA | 27.4 | QB1 | Questionable |  |  |
| 32 GUESS (31.81) | — | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.80; GUESS inputs |
| 29 GUESS (29.03) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |
| 27 GUESS (27.31) | — | Tyler Huntley | BAL | 14.9 | QB1 | IR |  | IR x0.80; buy-low: volume > points; GUESS inputs |
| 25 | — | Sam Darnold | SEA | 17.3 | QB1 | Out |  |  |
| 23 | -22 | Gardner Minshew II | ARI | — | QB1 | Questionable |  | -22 vs last board; Questionable x0.95 |
| 22 | — | J.J. McCarthy | NYG | 10.2 | QB1 | Questionable |  |  |
| 22 | — | Kyler Murray | MIN | 14.4 | QB1 | Out |  |  |
| 19 | — | Joe Milton | PHI | — | QB2 | Healthy |  |  |
| 18 | — | Shedeur Sanders | CLE | — | QB2 | Healthy |  |  |
| 17 | — | Deshaun Watson | CLE | 15.7 | QB1 | Out |  |  |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 96 | — | Jahmyr Gibbs | DET | 25.5 | RB1 | Healthy |  |  |
| 93 | — | James Cook III | BUF | 18.0 | RB1 | Healthy |  |  |
| 93 | — | Kenneth Walker III | KC | 21.3 | RB1 | Healthy |  |  |
| 88 | — | Bijan Robinson | ATL | 17.6 | RB1 | Healthy |  |  |
| 86 | — | Christian McCaffrey | SF | 18.1 | RB1 | Healthy |  |  |
| 85 | — | Jonathan Taylor | IND | 16.7 | RB1 | Healthy |  |  |
| 84 | — | Chuba Hubbard | CAR | 17.4 | RB1 | Healthy |  |  |
| 80 | — | Derrick Henry | BAL | 16.3 | RB1 | Healthy |  |  |
| 80 | — | Javonte Williams | DAL | 15.9 | RB1 | Healthy |  |  |
| 79 | — | D'Andre Swift | CHI | 17.3 | RB1 | Healthy |  |  |
| 78 | — | Bhayshul Tuten | JAX | 15.8 | RB1 | Healthy |  |  |
| 77 | — | Kyren Williams | LAR | 16.7 | RB1 | Healthy |  |  |
| 76 | — | Bucky Irving | TB | 15.2 | RB1 | Healthy |  |  |
| 72 | — | Tony Pollard | TEN | 15.2 | RB1 | Healthy | BYE |  |
| 71 | — | Ashton Jeanty | LV | 14.2 | RB1 | Healthy |  |  |
| 71 | — | Jaylen Warren | PIT | 16.0 | RB1 | Healthy | BYE |  |
| 67 | — | Chase Brown | CIN | 10.4 | RB1 | Healthy |  |  |
| 65 | — | Quinshon Judkins | CLE | 10.9 | RB1 | Healthy |  |  |
| 63 | — | Ollie Gordon II | MIA | 13.9 | RB1 | Healthy |  |  |
| 59 | — | Braelon Allen | NYJ | 12.4 | RB1 | Healthy |  |  |
| 56 | — | Aaron Jones Sr. | MIN | 10.3 | RB1 | Healthy |  |  |
| 53 | — | Saquon Barkley | PHI | 7.8 | RB1-split | Healthy |  |  |
| 50 | — | Omarion Hampton | LAC | 8.1 | RB1 | Healthy |  |  |
| 47 | — | Tyler Allgeier | ARI | 9.2 | RB1-split | Healthy |  |  |
| 41 | — | Woody Marks | HOU | 7.4 | RB1 | Healthy |  |  |
| 40 | — | Alvin Kamara | NO | 9.1 | RB1-split | Healthy |  |  |
| 37 | — | Rhamondre Stevenson | NE | 10.9 | RB1-split | Out |  |  |
| 36 | — | J.K. Dobbins | DEN | 6.9 | RB1 | Healthy |  |  |
| 35 | — | Cam Skattebo | NYG | 9.3 | RB1 | Out |  |  |
| 30 | — | Blake Corum | LAR | 9.7 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 12.5 | committee | Healthy |  |  |
| 30 | — | Jonah Coleman | DEN | 13.2 | committee | Healthy |  |  |
| 30 | — | Jordan Mason | MIN | 6.9 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 18.9 | committee | Out |  |  |
| 30 | — | Rachaad White | WAS | 13.3 | committee | Healthy |  |  |
| 30 GUESS (30) | — | Travis Etienne Jr. | NO | 8.5 | committee | IR |  | IR x0.80; committee RB 31% cap 30; GUESS inputs |
| 26 | — | David Montgomery | HOU | 8.4 | committee | Out |  |  |
| 24 | — | Chris Rodriguez Jr. | JAX | 6.0 | committee | Healthy |  |  |
| 24 | — | Jadarian Price | SEA | 4.0 | committee | Healthy |  |  |
| 23 | — | Emmett Johnson | KC | 6.3 | committee | Healthy |  |  |
| 22 | — | Kimani Vidal | LAC | 4.8 | committee | Healthy |  |  |
| 22 GUESS (21.88) | — | RJ Harvey | DEN | 9.2 | committee | IR |  | IR x0.80; committee RB 16% cap 30; GUESS inputs |
| 20 | — | Devin Singletary | NYG | — | committee | Healthy |  |  |
| 20 | — | Zach Charbonnet | SEA | 4.4 | committee | Healthy |  |  |
| 16 GUESS (15.87) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 21% cap 30; GUESS inputs |
| 16 | — | TreVeyon Henderson | NE | 5.2 | committee | Out |  |  |
| 14 GUESS (14.18) | — | Brian Robinson Jr. | ATL | 2.2 | committee | IR |  | IR x0.80; committee RB 25% cap 30; buy-low: volume > points; GUESS inputs |
| 10 | — | Jaleel McLaughlin | CLE | 3.8 | committee | Healthy |  |  |
| 10 | — | Jaydon Blue | PHI | 1.4 | committee | Healthy |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 23.5 | WR1 | Healthy |  |  |
| 94 | — | Amon-Ra St. Brown | DET | 16.4 | WR1 | Healthy |  |  |
| 94 | — | CeeDee Lamb | DAL | 17.3 | WR1 | Healthy |  |  |
| 87 | — | Ja'Marr Chase | CIN | 15.2 | WR1 | Healthy |  |  |
| 87 | — | Puka Nacua | LAR | 18.4 | WR1 | Questionable |  |  |
| 87 | — | Tee Higgins | CIN | 16.9 | WR2 | Healthy |  |  |
| 85 | — | Chris Olave | NO | 14.3 | WR1 | Healthy |  |  |
| 84 | — | Malik Nabers | NYG | 13.8 | WR1 | Healthy |  |  |
| 80 | — | Zay Flowers | BAL | 14.6 | WR1 | Healthy |  |  |
| 76 | — | Christian Watson | GB | 15.7 | WR1 | Healthy |  |  |
| 76 | — | Justin Jefferson | MIN | 12.1 | WR1 | Healthy |  |  |
| 76 | — | Tetairoa McMillan | CAR | 12.6 | WR1 | Healthy |  |  |
| 74 | — | Matthew Golden | GB | 13.8 | WR2 | Healthy |  |  |
| 73 | — | Drake London | ATL | 11.3 | WR1 | Healthy |  |  |
| 72 | — | Parker Washington | JAX | 11.7 | WR1 | Healthy |  |  |
| 68 | — | Nico Collins | HOU | 12.8 | WR1 | Healthy |  |  |
| 62 | — | Luther Burden III | CHI | 11.8 | WR1 | Questionable |  |  |
| 61 | — | Jameson Williams | DET | 12.5 | WR2 | Healthy |  |  |
| 61 | — | Malik Washington | MIA | 12.5 | WR1 | Healthy |  |  |
| 57 | — | Jalen Coker | CAR | 11.0 | WR2 | Healthy |  |  |
| 57 | +1 | Stefon Diggs | WAS | 11.4 | WR1 | Healthy |  |  |
| 56 | — | Emeka Egbuka | TB | 9.5 | WR1 | Healthy |  |  |
| 49 | — | Rashee Rice | KC | 9.3 | WR1 | Healthy |  |  |
| 48 | — | DJ Moore | BUF | 9.0 | WR1 | Healthy |  |  |
| 46 | — | DK Metcalf | PIT | 7.7 | WR1 | Healthy | BYE |  |
| 45 | — | Mike Evans | SF | 12.6 | WR | Out |  |  |
| 43 | — | Garrett Wilson | NYJ | 11.5 | WR | Out |  |  |
| 42 | — | Denzel Boston | CLE | 6.2 | WR1 | Healthy |  |  |
| 42 | -23 | Michael Wilson | ARI | 10.8 | WR1 | Out |  | -23 vs last board; Out x0.65; buy-low: volume > points |
| 41 | — | Rome Odunze | CHI | 7.3 | WR2 | Healthy |  |  |
| 41 | — | Tre Tucker | LV | 9.4 | WR1 | Healthy |  |  |
| 39 | — | DeVonta Smith | PHI | 14.0 | WR | Out |  |  |
| 39 | — | Ladd McConkey | LAC | 7.2 | WR1 | Questionable |  |  |
| 36 | — | Omar Cooper Jr. | NYJ | 10.0 | WR2 | Healthy |  |  |
| 35 | — | Germie Bernard | PIT | 10.0 | WR2 | Healthy | BYE |  |
| 34 | — | George Pickens | DAL | 10.6 | WR | Out |  |  |
| 34 | — | Jaylen Waddle | DEN | 8.0 | WR1 | Out |  |  |
| 34 | — | Jordan Addison | MIN | 6.8 | WR2 | Healthy |  |  |
| 31 | — | DeMario Douglas | NE | 9.4 | WR1 | Healthy |  |  |
| 31 | — | KC Concepcion Jr. | CLE | 5.2 | WR2 | Questionable |  |  |
| 29 | — | Makai Lemon | PHI | 5.8 | WR1 | Healthy |  |  |
| 28 GUESS (27.8) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 28 | — | Keon Coleman | BUF | 7.3 | WR | Healthy |  |  |
| 25 | — | Courtland Sutton | DEN | 4.8 | WR2 | Healthy |  |  |
| 24 | — | Chris Godwin Jr. | TB | 4.5 | WR2 | Healthy |  |  |
| 23 | — | Xavier Worthy | KC | 5.6 | WR2 | Out |  |  |
| 19 | — | Adonai Mitchell | NYJ | — | WR1 | Healthy |  |  |
| 19 | — | Rashod Bateman | BAL | 6.3 | WR2 | Healthy |  |  |
| 19 GUESS (19.1) | — | Romeo Doubs | NE | 8.5 | WR | IR |  | IR x0.80; GUESS inputs |
| 18 | — | Marvin Harrison Jr. | HOU | 4.8 | WR2 | Healthy |  |  |
| 17 | — | A.J. Brown | NE | 4.9 | WR | Out |  |  |
| 17 | — | Brian Thomas Jr. | JAX | 4.1 | WR | Healthy |  |  |
| 11 | — | Darius Cooper | PHI | 2.2 | WR2 | Healthy |  |  |
| 10 | — | Jerry Jeudy | CLE | 3.1 | WR | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 93 | — | Brock Bowers | LV | 17.2 | TE1 | Healthy |  |  |
| 93 | — | Trey McBride | ARI | 14.7 | TE1 | Healthy |  |  |
| 83 | — | George Kittle | SF | 12.5 | TE1 | Healthy |  |  |
| 74 | — | Isaiah Likely | NYG | 11.4 | TE1 | Healthy |  |  |
| 63 | — | Travis Kelce | KC | 9.6 | TE1 | Healthy |  |  |
| 60 | — | Sam LaPorta | DET | 10.1 | TE1 | Healthy |  |  |
| 51 | — | Dalton Kincaid | BUF | 9.4 | TE1 | Healthy |  |  |
| 51 | — | T.J. Hockenson | MIN | 8.8 | TE1 | Healthy |  |  |
| 50 | — | Tyler Warren | IND | 9.8 | TE1 | Healthy |  |  |
| 47 | — | Harold Fannin Jr. | CLE | 7.7 | TE1 | Healthy |  |  |
| 40 | — | Colston Loveland | CHI | 7.2 | TE1 | Healthy |  |  |
| 39 | — | Tucker Kraft | GB | 8.9 | TE1 | Healthy |  |  |
| 19 | — | Mark Andrews | BAL | 3.4 | TE1 | Healthy |  |  |
| 18 | — | Dallas Goedert | PHI | 5.9 | TE1 | Healthy |  |  |
| 17 | — | Kyle Pitts Sr. | ATL | 6.8 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Josh Jacobs | RB | 30 | 96 | 66 | Out x0.65; committee RB 22% cap 30 |
| Drew Lock | QB | 33 | 94 | 61 | Questionable x0.95 |
| Davante Adams | WR | 28 | 85 | 57 | IR x0.50; GUESS inputs |
| Carson Wentz | QB | 45 | 0 | 45 | SF QB1 floor 45 |
| Jacoby Brissett | QB | 45 | 3 | 42 | SF QB1 floor 45; buy-low: volume > points |
| DeVonta Smith | WR | 39 | 81 | 42 | Out x0.65 |
| Baker Mayfield | QB | 45 | 9 | 36 | SF QB1 floor 45; buy-low: volume > points |
| Rachaad White | RB | 30 | 62 | 32 | committee RB 33% cap 30 |
| Jonah Coleman | RB | 30 | 60 | 30 | committee RB 20% cap 30 |
| Mike Evans | WR | 45 | 73 | 28 | Out x0.65 |
| Breece Hall | RB | 30 | 57 | 28 | committee RB 28% cap 30 |
| Justin Herbert | QB | 38 | 12 | 26 | Questionable x0.95; buy-low: volume > points |
| Saquon Barkley | RB | 53 | 28 | 25 | proj 58 / prod 28 / role 46 |
| Malik Willis | QB | 43 | 18 | 25 | Questionable x0.95; buy-low: volume > points |
| Bo Nix | QB | 51 | 27 | 24 | SF QB1 floor 45; buy-low: volume > points |
