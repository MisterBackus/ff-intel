# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-10 05:00 PM EST

- **NFL week:** 9
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-10 week 9 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 88 | — | Joe Burrow | CIN | 31.4 | QB1 | Healthy |  |  |
| 88 | — | Josh Allen | BUF | 28.8 | QB1 | Healthy |  |  |
| 81 | — | Brock Purdy | SF | 26.3 | QB1 | Healthy |  |  |
| 80 | — | Drake Maye | NE | 25.1 | QB1 | Healthy |  |  |
| 77 | — | Trevor Lawrence | JAX | 23.4 | QB1 | Healthy |  |  |
| 74 | — | C.J. Stroud | HOU | 24.8 | QB1 | Healthy |  |  |
| 74 | — | Jordan Love | GB | 25.4 | QB1 | Healthy |  |  |
| 72 | — | Jared Goff | DET | 22.4 | QB1 | Healthy |  |  |
| 71 | — | Patrick Mahomes | KC | 21.8 | QB1 | Questionable |  |  |
| 70 | — | Jayden Daniels | WAS | 21.5 | QB1 | Healthy |  |  |
| 68 | — | Dak Prescott | DAL | 22.7 | QB1 | Healthy |  |  |
| 67 | — | Tyler Shough | NO | 22.4 | QB1 | Healthy |  |  |
| 66 | — | Kirk Cousins | MIN | 24.5 | QB1 | Healthy |  |  |
| 65 | — | Caleb Williams | CHI | 21.9 | QB1 | Healthy |  |  |
| 64 | — | Bryce Young | CAR | 20.9 | QB1 | Healthy |  |  |
| 55 | — | Matthew Stafford | LAR | 20.4 | QB1 | Healthy |  |  |
| 54 | — | Bo Nix | DEN | 17.4 | QB1 | Healthy |  |  |
| 53 | +1 | Shedeur Sanders | CLE | 26.7 | QB2 | Healthy |  |  |
| 49 | +1 | Cam Ward | TEN | 17.9 | QB1 | Healthy | BYE |  |
| 48 | +1 | Geno Smith | NYJ | 17.5 | QB1 | Healthy |  |  |
| 47 | +1 | Aaron Rodgers | PIT | 17.5 | QB1 | Healthy | BYE |  |
| 47 | +1 | Michael Penix Jr. | ATL | 17.5 | QB1 | Healthy |  |  |
| 45 | — | Baker Mayfield | TB | 10.2 | QB1 | Healthy |  |  |
| 45 | — | Carson Wentz | MIN | 2.8 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 10.1 | QB1 | Healthy |  |  |
| 39 | +1 | Justin Herbert | LAC | 13.0 | QB1 | Questionable |  |  |
| 33 GUESS (33.12) | — | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.80; GUESS inputs |
| 31 GUESS (30.81) | -12 | Malik Willis | MIA | 13.3 | QB1 | IR |  | -12 vs last board; IR x0.80; buy-low: volume > points; GUESS inputs |
| 29 GUESS (29.12) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |
| 29 GUESS (29.18) | — | Tyler Huntley | BAL | 14.9 | QB1 | IR |  | IR x0.80; buy-low: volume > points; GUESS inputs |
| 26 | — | Drew Lock | SEA | 21.0 | QB1 | Questionable |  |  |
| 25 | — | Kyler Murray | MIN | 14.4 | QB1 | Out |  |  |
| 24 | — | Joe Milton | PHI | 13.2 | QB2 | Healthy |  |  |
| 23 | — | Sam Darnold | SEA | 17.3 | QB1 | Out |  |  |
| 20 | — | J.J. McCarthy | NYG | 8.7 | QB1 | Questionable |  |  |
| 18 | — | Deshaun Watson | CLE | 15.7 | QB1 | Out |  |  |
| 15 | — | Gardner Minshew II | ARI | 7.0 | QB1 | Questionable |  |  |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jahmyr Gibbs | DET | 24.0 | RB1 | Healthy |  |  |
| 95 | — | Kenneth Walker III | KC | 22.9 | RB1 | Healthy |  |  |
| 94 | — | James Cook III | BUF | 17.8 | RB1 | Healthy |  |  |
| 91 | — | Bijan Robinson | ATL | 18.3 | RB1 | Healthy |  |  |
| 87 | — | Christian McCaffrey | SF | 18.6 | RB1 | Healthy |  |  |
| 87 | — | Chuba Hubbard | CAR | 16.7 | RB1 | Healthy |  |  |
| 86 | — | Bucky Irving | TB | 16.5 | RB1 | Healthy |  |  |
| 84 | — | Javonte Williams | DAL | 16.4 | RB1 | Healthy |  |  |
| 83 | — | Jonathan Taylor | IND | 15.6 | RB1 | Healthy |  |  |
| 80 | — | Derrick Henry | BAL | 15.1 | RB1 | Healthy |  |  |
| 78 | — | Jaylen Warren | PIT | 16.0 | RB1 | Healthy | BYE |  |
| 77 | — | Bhayshul Tuten | JAX | 15.0 | RB1 | Healthy |  |  |
| 77 | — | D'Andre Swift | CHI | 15.8 | RB1 | Healthy |  |  |
| 77 | — | Tony Pollard | TEN | 15.2 | RB1 | Healthy | BYE |  |
| 76 | — | Kyren Williams | LAR | 15.7 | RB1 | Healthy |  |  |
| 69 | — | Ashton Jeanty | LV | 13.1 | RB1 | Healthy |  |  |
| 69 | — | Chase Brown | CIN | 10.2 | RB1 | Healthy |  |  |
| 66 | — | Ollie Gordon II | MIA | 12.5 | RB1 | Healthy |  |  |
| 64 | — | Quinshon Judkins | CLE | 10.1 | RB1 | Healthy |  |  |
| 60 | +1 | Braelon Allen | NYJ | 11.4 | RB1 | Healthy |  |  |
| 57 | +1 | Aaron Jones Sr. | MIN | 9.4 | RB1 | Healthy |  |  |
| 55 | — | Saquon Barkley | PHI | 7.9 | RB1-split | Healthy |  |  |
| 49 | — | Omarion Hampton | LAC | 7.8 | RB1 | Healthy |  |  |
| 49 | +1 | Tyler Allgeier | ARI | 8.8 | RB1-split | Healthy |  |  |
| 43 | — | Woody Marks | HOU | 7.5 | RB1 | Healthy |  |  |
| 35 | — | Cam Skattebo | NYG | 9.3 | RB1 | Out |  |  |
| 33 | -3 | Rhamondre Stevenson | NE | 11.2 | RB1-split | Out |  |  |
| 30 | — | Alvin Kamara | NO | 8.7 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 10.0 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 11.9 | committee | Healthy |  |  |
| 30 | — | J.K. Dobbins | DEN | 6.4 | RB1 | Healthy |  |  |
| 30 | — | Jonah Coleman | DEN | 14.4 | committee | Healthy |  |  |
| 30 | — | Jordan Mason | MIN | 6.5 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 12.8 | committee | Out |  |  |
| 30 | — | Rachaad White | WAS | 10.9 | committee | Healthy |  |  |
| 30 GUESS (30) | +2 | Travis Etienne Jr. | NO | 8.5 | committee | IR |  | IR x0.80; committee RB 25% cap 30; GUESS inputs |
| 27 | — | Chris Rodriguez Jr. | JAX | 6.5 | committee | Healthy |  |  |
| 27 | — | David Montgomery | HOU | 8.4 | committee | Out |  |  |
| 27 | +1 | Emmett Johnson | KC | 6.7 | committee | Healthy |  |  |
| 27 | — | Zach Charbonnet | SEA | 6.8 | committee | Healthy |  |  |
| 25 | -1 | Jadarian Price | SEA | 5.5 | committee | Healthy |  |  |
| 23 | — | Devin Singletary | NYG | 4.9 | committee | Healthy |  |  |
| 22 GUESS (22.11) | — | RJ Harvey | DEN | 9.2 | committee | IR |  | IR x0.80; committee RB 14% cap 30; GUESS inputs |
| 21 | +1 | Kimani Vidal | LAC | 4.5 | committee | Healthy |  |  |
| 15 GUESS (15.37) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 19% cap 30; GUESS inputs |
| 15 | — | TreVeyon Henderson | NE | 5.2 | committee | Out |  |  |
| 13 GUESS (13.27) | — | Brian Robinson Jr. | ATL | 2.2 | committee | IR |  | IR x0.80; committee RB 23% cap 30; GUESS inputs |
| 10 | — | Jaleel McLaughlin | CLE | 3.8 | committee | Healthy |  |  |
| 10 | — | Jaydon Blue | PHI | 1.4 | committee | Healthy |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 21.8 | WR1 | Healthy |  |  |
| 96 | — | CeeDee Lamb | DAL | 18.5 | WR1 | Healthy |  |  |
| 94 | — | Amon-Ra St. Brown | DET | 15.9 | WR1 | Healthy |  |  |
| 92 | — | Ja'Marr Chase | CIN | 16.6 | WR1 | Healthy |  |  |
| 88 | — | Tee Higgins | CIN | 17.0 | WR2 | Healthy |  |  |
| 85 | -1 | Chris Olave | NO | 14.2 | WR1 | Healthy |  |  |
| 84 | — | Malik Nabers | NYG | 12.9 | WR1 | Healthy |  |  |
| 83 | — | Christian Watson | GB | 16.9 | WR1 | Healthy |  |  |
| 83 | — | Matthew Golden | GB | 15.3 | WR2 | Healthy |  |  |
| 79 | +1 | Justin Jefferson | MIN | 11.4 | WR1 | Healthy |  |  |
| 79 | — | Tetairoa McMillan | CAR | 12.7 | WR1 | Healthy |  |  |
| 77 | — | Zay Flowers | BAL | 13.2 | WR1 | Healthy |  |  |
| 76 | — | Parker Washington | JAX | 11.9 | WR1 | Healthy |  |  |
| 74 | — | Drake London | ATL | 11.1 | WR1 | Healthy |  |  |
| 70 | — | Nico Collins | HOU | 12.9 | WR1 | Healthy |  |  |
| 67 | — | Luther Burden III | CHI | 12.4 | WR1 | Questionable |  |  |
| 59 | +1 | Jameson Williams | DET | 11.5 | WR2 | Healthy |  |  |
| 58 | — | Stefon Diggs | WAS | 10.8 | WR1 | Healthy |  |  |
| 57 | +1 | Jalen Coker | CAR | 10.1 | WR2 | Healthy |  |  |
| 57 | — | Puka Nacua | LAR | 19.8 | WR | Questionable |  |  |
| 54 | — | Emeka Egbuka | TB | 8.9 | WR1 | Healthy |  |  |
| 52 | -1 | Rashee Rice | KC | 8.9 | WR1 | Healthy |  |  |
| 51 | — | KC Concepcion Jr. | CLE | 11.0 | WR2 | Questionable |  |  |
| 49 | — | DJ Moore | BUF | 8.3 | WR1 | Healthy |  |  |
| 48 | — | Malik Washington | MIA | 7.8 | WR1 | Healthy |  |  |
| 47 | — | DK Metcalf | PIT | 7.7 | WR1 | Healthy | BYE |  |
| 47 | +1 | Rome Odunze | CHI | 8.1 | WR2 | Healthy |  |  |
| 45 | +1 | Denzel Boston | CLE | 7.6 | WR1 | Healthy |  |  |
| 43 | — | Garrett Wilson | NYJ | 11.5 | WR | Out |  |  |
| 43 GUESS (42.58) | — | Michael Wilson | ARI | 10.6 | WR | Out |  | Out x0.65; buy-low: volume > points; GUESS inputs |
| 43 | +1 | Tre Tucker | LV | 8.8 | WR1 | Healthy |  |  |
| 41 | +1 | Ladd McConkey | LAC | 7.2 | WR1 | Questionable |  |  |
| 40 | -4 | Mike Evans | SF | 12.6 | WR | Out |  |  |
| 38 | +1 | DeMario Douglas | NE | 10.5 | WR1 | Healthy |  |  |
| 38 | — | DeVonta Smith | PHI | 14.0 | WR | Out |  |  |
| 38 | — | Germie Bernard | PIT | 10.0 | WR2 | Healthy | BYE |  |
| 36 | — | George Pickens | DAL | 10.6 | WR | Out |  |  |
| 36 | -1 | Omar Cooper Jr. | NYJ | 9.9 | WR2 | Healthy |  |  |
| 33 | +1 | Jordan Addison | MIN | 6.4 | WR2 | Healthy |  |  |
| 32 | — | Courtland Sutton | DEN | 5.7 | WR2 | Healthy |  |  |
| 32 | — | Makai Lemon | PHI | 6.1 | WR1 | Healthy |  |  |
| 31 | — | Jaylen Waddle | DEN | 7.4 | WR1 | Out |  |  |
| 28 GUESS (28.31) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 28 | +1 | Keon Coleman | BUF | 6.3 | WR | Healthy |  |  |
| 24 | — | Chris Godwin Jr. | TB | 4.3 | WR2 | Healthy |  |  |
| 22 | -3 | Xavier Worthy | KC | 5.9 | WR2 | Out |  |  |
| 20 | — | Adonai Mitchell | NYJ | 0.0 | WR1 | Healthy |  |  |
| 20 GUESS (19.54) | — | Romeo Doubs | NE | 8.5 | WR | IR |  | IR x0.80; GUESS inputs |
| 18 | — | Marvin Harrison Jr. | HOU | 4.6 | WR2 | Healthy |  |  |
| 17 | — | Brian Thomas Jr. | JAX | 3.6 | WR | Healthy |  |  |
| 17 | — | Rashod Bateman | BAL | 5.7 | WR2 | Healthy |  |  |
| 16 | — | A.J. Brown | NE | 4.9 | WR | Out |  |  |
| 14 | — | Darius Cooper | PHI | 2.5 | WR2 | Healthy |  |  |
| 12 | — | Jerry Jeudy | CLE | 3.3 | WR | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 94 | — | Brock Bowers | LV | 17.4 | TE1 | Healthy |  |  |
| 89 | -1 | Trey McBride | ARI | 14.0 | TE1 | Healthy |  |  |
| 78 | -8 | George Kittle | SF | 11.9 | TE1 | Healthy |  | -8 vs last board |
| 75 | -1 | Isaiah Likely | NYG | 11.7 | TE1 | Healthy |  |  |
| 62 | +13 | Tyler Warren | IND | 9.3 | TE1 | Healthy |  | +13 vs last board; buy-low: volume > points |
| 61 | -9 | Travis Kelce | KC | 10.3 | TE1 | Healthy |  | -9 vs last board |
| 60 | +2 | Sam LaPorta | DET | 9.4 | TE1 | Healthy |  |  |
| 53 | — | T.J. Hockenson | MIN | 8.0 | TE1 | Healthy |  |  |
| 51 | +1 | Harold Fannin Jr. | CLE | 8.2 | TE1 | Healthy |  |  |
| 50 | +2 | Dalton Kincaid | BUF | 8.7 | TE1 | Healthy |  |  |
| 42 | — | Colston Loveland | CHI | 7.2 | TE1 | Healthy |  |  |
| 35 | +1 | Tucker Kraft | GB | 8.0 | TE1 | Healthy |  |  |
| 18 | — | Dallas Goedert | PHI | 6.1 | TE1 | Healthy |  |  |
| 17 | — | Kyle Pitts Sr. | ATL | 6.5 | TE1 | Healthy |  |  |
| 17 | +1 | Mark Andrews | BAL | 3.2 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Davante Adams | WR | 28 | 85 | 57 | IR x0.50; GUESS inputs |
| Carson Wentz | QB | 45 | 0 | 45 | SF QB1 floor 45 |
| DeVonta Smith | WR | 38 | 81 | 43 | Out x0.65 |
| Shedeur Sanders | QB | 53 | 94 | 41 | proj 42 / prod 94 / role 1 |
| Puka Nacua | WR | 57 | 98 | 41 | Questionable x0.95 |
| Jonah Coleman | RB | 30 | 69 | 39 | committee RB 27% cap 30 |
| Jacoby Brissett | QB | 45 | 8 | 37 | SF QB1 floor 45; buy-low: volume > points |
| Josh Jacobs | RB | 30 | 65 | 35 | Out x0.65; committee RB 21% cap 30 |
| Baker Mayfield | QB | 45 | 11 | 34 | SF QB1 floor 45; buy-low: volume > points |
| Drew Lock | QB | 26 | 58 | 32 | Questionable x0.95 |
| Mike Evans | WR | 40 | 72 | 32 | Out x0.65 |
| Breece Hall | RB | 30 | 60 | 30 | committee RB 33% cap 30 |
| Justin Herbert | QB | 39 | 14 | 25 | Questionable x0.95; buy-low: volume > points |
| T.J. Hockenson | TE | 53 | 29 | 24 | buy-low: volume > points |
| Rachaad White | RB | 30 | 54 | 24 | committee RB 34% cap 30 |
