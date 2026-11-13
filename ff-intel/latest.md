# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-13 07:00 AM EST

- **NFL week:** 10
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-13 week 10 values 1.0.0`
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
| 80 | — | Brock Purdy | SF | 26.3 | QB1 | Healthy |  |  |
| 78 | — | Drake Maye | NE | 25.1 | QB1 | Healthy |  |  |
| 76 | — | Trevor Lawrence | JAX | 23.4 | QB1 | Healthy |  |  |
| 73 | — | Jordan Love | GB | 25.4 | QB1 | Healthy |  |  |
| 73 | +1 | Kirk Cousins | MIN | 24.5 | QB1 | Healthy |  |  |
| 72 | — | C.J. Stroud | HOU | 24.8 | QB1 | Healthy |  |  |
| 72 | -2 | Patrick Mahomes | KC | 21.8 | QB1 | Healthy |  |  |
| 71 | +1 | Jared Goff | DET | 22.4 | QB1 | Healthy |  |  |
| 68 | -1 | Jayden Daniels | WAS | 21.5 | QB1 | Healthy |  |  |
| 66 | — | Dak Prescott | DAL | 22.7 | QB1 | Healthy |  |  |
| 66 | — | Tyler Shough | NO | 22.4 | QB1 | Healthy |  |  |
| 63 | — | Caleb Williams | CHI | 21.9 | QB1 | Healthy | BYE |  |
| 61 | -2 | Bryce Young | CAR | 20.9 | QB1 | Healthy |  |  |
| 52 | — | Cam Ward | TEN | 17.9 | QB1 | Healthy |  |  |
| 51 | — | Bo Nix | DEN | 17.4 | QB1 | Healthy | BYE |  |
| 51 | — | Matthew Stafford | LAR | 20.4 | QB1 | Healthy |  |  |
| 50 | — | Aaron Rodgers | PIT | 17.5 | QB1 | Healthy |  |  |
| 45 | — | Baker Mayfield | TB | 10.2 | QB1 | Healthy | BYE |  |
| 45 | — | Daniel Jones | IND | 11.4 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 15.7 | QB1 | Healthy |  |  |
| 45 | — | Fernando Mendoza | LV | — | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 17.5 | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 8.7 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 10.1 | QB1 | Healthy |  |  |
| 45 | +6 | Justin Herbert | LAC | 13.0 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 17.5 | QB1 | Healthy |  |  |
| 44 GUESS (43.58) | — | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.78; GUESS inputs |
| 31 GUESS (30.66) | — | Kyler Murray | MIN | 14.4 | QB1 | Doubtful |  | Doubtful x0.80; buy-low: volume > points; GUESS inputs |
| 30 GUESS (29.79) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR | BYE | IR x0.50; GUESS inputs |
| 28 GUESS (28.1) | — | Tyler Huntley | BAL | 14.9 | QB1 | IR |  | IR x0.78; buy-low: volume > points; GUESS inputs |
| 25 GUESS (25) | — | Shedeur Sanders | CLE | 26.7 | QB2 | Healthy |  | backup QB cap 25; GUESS inputs |
| 24 | — | Drew Lock | SEA | 21.0 | QB1 | Questionable |  |  |
| 24 | — | Sam Darnold | SEA | 17.3 | QB1 | Out |  |  |
| 22 | — | Joe Milton | PHI | 13.2 | QB2 | Healthy | BYE |  |
| 22 GUESS (22) | — | Malik Willis | MIA | 13.3 | QB1 | IR |  | IR x0.78; buy-low: volume > points; GUESS inputs |
| 10 GUESS (10.33) | — | Carson Wentz | MIN | 2.8 | QB1 | Questionable |  | Questionable x0.95; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jahmyr Gibbs | DET | 24.0 | RB1 | Healthy |  |  |
| 95 | — | Kenneth Walker III | KC | 22.9 | RB1 | Healthy |  |  |
| 94 | — | James Cook III | BUF | 17.8 | RB1 | Healthy |  |  |
| 90 | -1 | Bijan Robinson | ATL | 18.3 | RB1 | Healthy |  |  |
| 87 | +1 | Bucky Irving | TB | 16.5 | RB1 | Healthy | BYE |  |
| 87 | — | Christian McCaffrey | SF | 18.6 | RB1 | Healthy |  |  |
| 87 | — | Chuba Hubbard | CAR | 16.7 | RB1 | Healthy |  |  |
| 82 | +1 | Jaylen Warren | PIT | 16.0 | RB1 | Healthy |  |  |
| 80 | +1 | Javonte Williams | DAL | 16.4 | RB1 | Healthy |  |  |
| 80 | -3 | Jonathan Taylor | IND | 15.6 | RB1 | Healthy |  |  |
| 79 | — | Derrick Henry | BAL | 15.1 | RB1 | Healthy |  |  |
| 77 | — | D'Andre Swift | CHI | 15.8 | RB1 | Healthy | BYE |  |
| 75 | — | Kyren Williams | LAR | 15.7 | RB1 | Healthy |  |  |
| 74 | — | Tony Pollard | TEN | 15.2 | RB1 | Questionable |  |  |
| 73 | -1 | Bhayshul Tuten | JAX | 15.0 | RB1 | Questionable |  |  |
| 69 | +1 | Ashton Jeanty | LV | 13.1 | RB1 | Healthy |  |  |
| 69 | — | Chase Brown | CIN | 10.2 | RB1 | Healthy |  |  |
| 66 | -1 | Ollie Gordon II | MIA | 12.5 | RB1 | Healthy |  |  |
| 63 | -1 | Cam Skattebo | NYG | 9.3 | RB1 | Healthy |  |  |
| 62 | — | Quinshon Judkins | CLE | 10.1 | RB1 | Healthy |  |  |
| 55 | -1 | Aaron Jones Sr. | MIN | 9.4 | RB1 | Healthy |  |  |
| 55 | — | Saquon Barkley | PHI | 7.9 | RB1-split | Healthy | BYE |  |
| 51 | — | Braelon Allen | NYJ | 11.4 | RB1 | Healthy |  |  |
| 47 | -3 | Omarion Hampton | LAC | 7.8 | RB1 | Healthy |  |  |
| 46 | +1 | Rhamondre Stevenson | NE | 11.2 | RB1-split | Questionable |  |  |
| 45 | +1 | Tyler Allgeier | ARI | 8.8 | RB1-split | Healthy |  |  |
| 40 | — | Woody Marks | HOU | 7.5 | RB1 | Questionable |  |  |
| 31 | — | J.K. Dobbins | DEN | 6.4 | RB1 | Healthy | BYE |  |
| 30 | — | Alvin Kamara | NO | 8.7 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 10.0 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 11.9 | committee | Healthy |  |  |
| 30 | +1 | Chris Rodriguez Jr. | JAX | 6.5 | committee | Questionable |  |  |
| 30 | — | Jonah Coleman | DEN | 14.4 | committee | Healthy | BYE |  |
| 30 | — | Jordan Mason | MIN | 6.5 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 12.8 | committee | Out |  |  |
| 30 | — | Rachaad White | WAS | 10.9 | committee | Healthy |  |  |
| 30 GUESS (30) | — | Travis Etienne Jr. | NO | 8.5 | committee | IR |  | IR x0.78; committee RB 25% cap 30; GUESS inputs |
| 30 | — | Zach Charbonnet | SEA | 6.8 | committee | Healthy |  |  |
| 29 | — | Emmett Johnson | KC | 6.7 | committee | Healthy |  |  |
| 25 | — | Jadarian Price | SEA | 5.5 | committee | Healthy |  |  |
| 23 GUESS (22.68) | — | RJ Harvey | DEN | 9.2 | committee | IR | BYE | IR x0.78; committee RB 14% cap 30; GUESS inputs |
| 22 | -1 | Kimani Vidal | LAC | 4.5 | committee | Healthy |  |  |
| 19 | — | Corey Kiner | NE | — | committee | Healthy |  |  |
| 16 GUESS (15.98) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 19% cap 30; GUESS inputs |
| 16 | — | Kaleb Johnson | GB | 3.2 | committee | Healthy |  |  |
| 16 | — | TreVeyon Henderson | NE | 5.2 | committee | Out |  |  |
| 14 GUESS (13.51) | — | Brian Robinson Jr. | ATL | 2.2 | committee | IR |  | IR x0.78; committee RB 23% cap 30; GUESS inputs |
| 12 GUESS (11.93) | — | Jaydon Blue | — | 1.4 | committee | Healthy |  | committee RB 20% cap 30; GUESS inputs |
| 10 | -1 | Jaleel McLaughlin | CLE | 3.8 | committee | Healthy |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 21.8 | WR1 | Healthy |  |  |
| 95 | — | CeeDee Lamb | DAL | 18.5 | WR1 | Healthy |  |  |
| 92 | +1 | Ja'Marr Chase | CIN | 16.6 | WR1 | Healthy |  |  |
| 89 | — | Amon-Ra St. Brown | DET | 15.9 | WR1 | Questionable |  |  |
| 87 | +1 | Tee Higgins | CIN | 17.0 | WR2 | Healthy |  |  |
| 86 | — | Chris Olave | NO | 14.2 | WR1 | Healthy |  |  |
| 84 | +1 | Malik Nabers | NYG | 12.9 | WR1 | Healthy |  |  |
| 83 | +1 | Christian Watson | GB | 16.9 | WR1 | Healthy |  |  |
| 83 | — | Matthew Golden | GB | 15.3 | WR2 | Healthy |  |  |
| 80 | — | Justin Jefferson | MIN | 11.4 | WR1 | Healthy |  |  |
| 78 | — | Tetairoa McMillan | CAR | 12.7 | WR1 | Healthy |  |  |
| 78 | — | Zay Flowers | BAL | 13.2 | WR1 | Healthy |  |  |
| 76 | +1 | Parker Washington | JAX | 11.9 | WR1 | Healthy |  |  |
| 74 | — | Drake London | ATL | 11.1 | WR1 | Healthy |  |  |
| 68 | +1 | Luther Burden III | CHI | 12.4 | WR1 | Questionable | BYE |  |
| 68 | — | Nico Collins | HOU | 12.9 | WR1 | Healthy |  |  |
| 65 | +1 | Garrett Wilson | NYJ | 11.5 | WR1 | Questionable |  |  |
| 59 | +1 | Jameson Williams | DET | 11.5 | WR2 | Healthy |  |  |
| 58 | +1 | Mike Evans | SF | 12.6 | WR | Questionable |  |  |
| 56 | +1 | Jalen Coker | CAR | 10.1 | WR2 | Healthy |  |  |
| 55 | +1 | Stefon Diggs | WAS | 10.8 | WR1 | Healthy |  |  |
| 53 | — | KC Concepcion Jr. | CLE | 11.0 | WR2 | Healthy |  |  |
| 52 | +1 | George Pickens | DAL | 10.6 | WR2 | Questionable |  |  |
| 52 | +1 | Rashee Rice | KC | 8.9 | WR1 | Healthy |  |  |
| 51 | +1 | DK Metcalf | PIT | 7.7 | WR1 | Healthy |  |  |
| 51 | — | Emeka Egbuka | TB | 8.9 | WR1 | Healthy | BYE |  |
| 51 GUESS (50.69) | +1 | Michael Wilson | ARI | 10.6 | WR | IR |  | IR x0.78; buy-low: volume > points; GUESS inputs |
| 47 GUESS (47.12) | -15 | Puka Nacua | LAR | 19.8 | WR | IR |  | -15 vs last board; IR x0.78; GUESS inputs |
| 46 | — | Malik Washington | MIA | 7.8 | WR2 | Healthy |  |  |
| 46 | +1 | Rome Odunze | CHI | 8.1 | WR2 | Healthy | BYE |  |
| 45 | — | DJ Moore | BUF | 8.3 | WR1 | Healthy |  |  |
| 42 | +1 | Denzel Boston | CLE | 7.6 | WR1 | Questionable |  |  |
| 40 | — | DeVonta Smith | PHI | 14.0 | WR | Out | BYE |  |
| 40 | — | Germie Bernard | PIT | 10.0 | WR2 | Healthy |  |  |
| 39 | +1 | Ladd McConkey | LAC | 7.2 | WR1 | Questionable |  |  |
| 37 | — | DeMario Douglas | NE | 10.5 | WR2 | Healthy |  |  |
| 36 | +1 | Tre Tucker | LV | 8.8 | WR1 | Healthy |  |  |
| 35 | +1 | Khalil Shakir | BUF | — | WR2 | Healthy |  |  |
| 34 | +1 | Jordan Addison | MIN | 6.4 | WR2 | Healthy |  |  |
| 33 | +1 | Makai Lemon | PHI | 6.1 | WR1 | Healthy | BYE |  |
| 32 | — | Courtland Sutton | DEN | 5.7 | WR2 | Healthy | BYE |  |
| 31 | +1 | Jaylen Waddle | DEN | 7.4 | WR1 | Out | BYE |  |
| 31 | +1 | Omar Cooper Jr. | NYJ | 9.9 | WR2 | Questionable |  |  |
| 30 | — | A.J. Brown | NE | 4.9 | WR1 | Questionable |  |  |
| 29 GUESS (29.11) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 28 | — | Keon Coleman | BUF | 6.3 | WR | Healthy |  |  |
| 27 | — | Xavier Worthy | KC | 5.9 | WR | Healthy |  |  |
| 19 | +1 | Adonai Mitchell | NYJ | 0.0 | WR | Healthy |  |  |
| 17 | — | Brian Thomas Jr. | JAX | 3.6 | WR | Healthy |  |  |
| 17 | — | Rashod Bateman | BAL | 5.7 | WR2 | Questionable |  |  |
| 16 | — | Marvin Harrison Jr. | HOU | 4.6 | WR | Questionable |  |  |
| 16 | +2 | Tank Dell | HOU | 5.0 | WR2 | Healthy |  |  |
| 13 | — | Darius Cooper | PHI | 2.5 | WR2 | Healthy | BYE |  |
| 11 | — | Jerry Jeudy | CLE | 3.3 | WR | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 94 | — | Brock Bowers | LV | 17.4 | TE1 | Healthy |  |  |
| 89 | — | Trey McBride | ARI | 14.0 | TE1 | Healthy |  |  |
| 78 | — | George Kittle | SF | 11.9 | TE1 | Healthy |  |  |
| 78 | — | Isaiah Likely | NYG | 11.7 | TE1 | Healthy |  |  |
| 65 | +6 | Tyler Warren | IND | 9.3 | TE1 | Healthy |  |  |
| 60 | — | Sam LaPorta | DET | 9.4 | TE1 | Healthy |  |  |
| 58 | -1 | Travis Kelce | KC | 10.3 | TE1 | Healthy |  |  |
| 53 | — | T.J. Hockenson | MIN | 8.0 | TE1 | Questionable |  |  |
| 45 | +3 | Dalton Kincaid | BUF | 8.7 | TE1 | Questionable |  |  |
| 43 | -8 | Harold Fannin Jr. | CLE | 8.2 | TE1 | Questionable |  | -8 vs last board; Questionable x0.95 |
| 42 | -1 | Colston Loveland | CHI | 7.2 | TE1 | Healthy | BYE |  |
| 37 | — | Tucker Kraft | GB | 8.0 | TE1 | Healthy |  |  |
| 18 | — | Dallas Goedert | PHI | 6.1 | TE1 | Healthy | BYE |  |
| 17 | — | Kyle Pitts Sr. | ATL | 6.5 | TE1 | Healthy |  |  |
| 17 | — | Mark Andrews | BAL | 3.2 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Shedeur Sanders | QB | 25 | 94 | 69 | backup QB cap 25; GUESS inputs |
| Davante Adams | WR | 29 | 85 | 56 | IR x0.50; GUESS inputs |
| Puka Nacua | WR | 47 | 98 | 51 | -15 vs last board; IR x0.78; GUESS inputs |
| Fernando Mendoza | QB | 45 | 0 | 45 | SF QB1 floor 45 |
| J.J. McCarthy | QB | 45 | 3 | 42 | SF QB1 floor 45 |
| DeVonta Smith | WR | 40 | 81 | 41 | Out x0.65 |
| Jacoby Brissett | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Jonah Coleman | RB | 30 | 68 | 38 | committee RB 27% cap 30 |
| Baker Mayfield | QB | 45 | 8 | 37 | SF QB1 floor 45; buy-low: volume > points |
| Khalil Shakir | WR | 35 | 0 | 35 | buy-low: volume > points |
| Drew Lock | QB | 24 | 58 | 34 | Questionable x0.95 |
| Daniel Jones | QB | 45 | 11 | 34 | SF QB1 floor 45; buy-low: volume > points |
| Josh Jacobs | RB | 30 | 64 | 34 | Out x0.65; committee RB 21% cap 30 |
| Justin Herbert | QB | 45 | 14 | 31 | SF QB1 floor 45; buy-low: volume > points |
| Breece Hall | RB | 30 | 60 | 30 | committee RB 33% cap 30 |
