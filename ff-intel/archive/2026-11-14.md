# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-14 05:00 PM EST

- **NFL week:** 10
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-14 week 10 values 1.0.0`
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
| 75 | -1 | Trevor Lawrence | JAX | 23.4 | QB1 | Healthy |  |  |
| 73 | — | Jordan Love | GB | 25.4 | QB1 | Healthy |  |  |
| 73 | — | Kirk Cousins | MIN | 24.5 | QB1 | Healthy |  |  |
| 72 | — | Patrick Mahomes | KC | 21.8 | QB1 | Healthy |  |  |
| 71 | -1 | C.J. Stroud | HOU | 24.8 | QB1 | Healthy |  |  |
| 69 | -2 | Jared Goff | DET | 22.4 | QB1 | Healthy |  |  |
| 68 | — | Jayden Daniels | WAS | 21.5 | QB1 | Healthy |  |  |
| 65 | — | Dak Prescott | DAL | 22.7 | QB1 | Healthy |  |  |
| 65 | -1 | Tyler Shough | NO | 22.4 | QB1 | Healthy |  |  |
| 63 | -1 | Caleb Williams | CHI | 21.9 | QB1 | Healthy | BYE |  |
| 60 | -1 | Bryce Young | CAR | 20.9 | QB1 | Healthy |  |  |
| 51 | -1 | Cam Ward | TEN | 17.9 | QB1 | Healthy |  |  |
| 50 | -1 | Bo Nix | DEN | 17.4 | QB1 | Healthy | BYE |  |
| 50 | -1 | Matthew Stafford | LAR | 20.4 | QB1 | Healthy |  |  |
| 49 | -1 | Aaron Rodgers | PIT | 17.5 | QB1 | Healthy |  |  |
| 45 | — | Baker Mayfield | TB | 10.2 | QB1 | Healthy | BYE |  |
| 45 GUESS (45) | — | Carson Wentz | MIN | 2.8 | QB1 | Healthy |  | SF QB1 floor 45; GUESS inputs |
| 45 | — | Daniel Jones | IND | 11.4 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 15.7 | QB1 | Healthy |  |  |
| 45 | — | Drew Lock | SEA | 21.0 | QB1 | Healthy |  |  |
| 45 | — | Fernando Mendoza | LV | — | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 17.5 | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 8.7 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 10.1 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 13.0 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 17.5 | QB1 | Healthy |  |  |
| 43 GUESS (42.93) | -1 | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.78; GUESS inputs |
| 29 GUESS (29.44) | -1 | Jalen Hurts | PHI | 19.8 | QB1 | IR | BYE | IR x0.50; GUESS inputs |
| 25 GUESS (25) | — | Shedeur Sanders | CLE | 26.7 | QB2 | Healthy |  | backup QB cap 25; GUESS inputs |
| 24 GUESS (24.3) | -1 | Kyler Murray | MIN | 14.4 | QB1 | Out |  | Out x0.65; buy-low: volume > points; GUESS inputs |
| 24 | — | Sam Darnold | SEA | 17.3 | QB1 | Out |  |  |
| 22 | — | Joe Milton | PHI | 13.2 | QB2 | Healthy | BYE |  |
| 22 GUESS (22.19) | — | Malik Willis | MIA | 13.3 | QB1 | IR |  | IR x0.78; buy-low: volume > points; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jahmyr Gibbs | DET | 24.0 | RB1 | Healthy |  |  |
| 94 | — | James Cook III | BUF | 17.8 | RB1 | Healthy |  |  |
| 90 | — | Bijan Robinson | ATL | 18.3 | RB1 | Healthy |  |  |
| 88 | +1 | Christian McCaffrey | SF | 18.6 | RB1 | Healthy |  |  |
| 87 | — | Bucky Irving | TB | 16.5 | RB1 | Healthy | BYE |  |
| 87 | — | Chuba Hubbard | CAR | 16.7 | RB1 | Healthy |  |  |
| 82 | — | Jaylen Warren | PIT | 16.0 | RB1 | Healthy |  |  |
| 80 | — | Javonte Williams | DAL | 16.4 | RB1 | Healthy |  |  |
| 80 | — | Jonathan Taylor | IND | 15.6 | RB1 | Healthy |  |  |
| 79 | +1 | Derrick Henry | BAL | 15.1 | RB1 | Healthy |  |  |
| 78 | — | Tony Pollard | TEN | 15.2 | RB1 | Healthy |  |  |
| 77 | — | Bhayshul Tuten | JAX | 15.0 | RB1 | Healthy |  |  |
| 77 | — | D'Andre Swift | CHI | 15.8 | RB1 | Healthy | BYE |  |
| 75 | — | Kyren Williams | LAR | 15.7 | RB1 | Healthy |  |  |
| 68 | -1 | Chase Brown | CIN | 10.2 | RB1 | Healthy |  |  |
| 67 | -1 | Ashton Jeanty | LV | 13.1 | RB1 | Healthy |  |  |
| 65 | +2 | Cam Skattebo | NYG | 9.3 | RB1 | Healthy |  |  |
| 65 | -1 | Ollie Gordon II | MIA | 12.5 | RB1 | Healthy |  |  |
| 61 | -29 | Kenneth Walker III | KC | 22.9 | RB1 | Out |  | -29 vs last board; Out x0.65 |
| 61 | -1 | Quinshon Judkins | CLE | 10.1 | RB1 | Healthy |  |  |
| 56 | +2 | Saquon Barkley | PHI | 7.9 | RB1-split | Healthy | BYE |  |
| 54 | -1 | Aaron Jones Sr. | MIN | 9.4 | RB1 | Healthy |  |  |
| 51 | +1 | Braelon Allen | NYJ | 11.4 | RB1 | Healthy |  |  |
| 50 | +5 | Rhamondre Stevenson | NE | 11.2 | RB1-split | Questionable |  |  |
| 46 | — | Omarion Hampton | LAC | 7.8 | RB1 | Healthy |  |  |
| 44 | +1 | Woody Marks | HOU | 7.5 | RB1 | Healthy |  |  |
| 40 | -4 | Tyler Allgeier | ARI | 8.8 | RB1-split | Healthy |  |  |
| 30 | — | Alvin Kamara | NO | 8.7 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 10.0 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 11.9 | committee | Healthy |  |  |
| 30 | — | Chris Rodriguez Jr. | JAX | 6.5 | committee | Healthy |  |  |
| 30 | — | Jonah Coleman | DEN | 14.4 | committee | Healthy | BYE |  |
| 30 | — | Jordan Mason | MIN | 6.5 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 12.8 | committee | Out |  |  |
| 30 | — | Rachaad White | WAS | 10.9 | committee | Healthy |  |  |
| 30 | — | Travis Etienne Jr. | NO | 8.5 | committee | Questionable |  |  |
| 30 | — | Zach Charbonnet | SEA | 6.8 | committee | Healthy |  |  |
| 29 | — | Emmett Johnson | KC | 6.7 | committee | Healthy |  |  |
| 29 | -1 | J.K. Dobbins | DEN | 6.4 | RB1 | Healthy | BYE |  |
| 24 | -1 | Jadarian Price | SEA | 5.5 | committee | Healthy |  |  |
| 22 | +3 | Corey Kiner | NE | — | committee | Healthy |  |  |
| 21 GUESS (21.23) | -1 | RJ Harvey | DEN | 9.2 | committee | IR | BYE | IR x0.78; committee RB 14% cap 30; GUESS inputs |
| 20 | -1 | Kimani Vidal | LAC | 4.5 | committee | Healthy |  |  |
| 20 GUESS (19.62) | +5 | TreVeyon Henderson | NE | 5.2 | committee | IR |  | IR x0.78; committee RB 25% cap 30; GUESS inputs |
| 16 GUESS (15.77) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 19% cap 30; GUESS inputs |
| 15 | — | Kaleb Johnson | GB | 3.2 | committee | Healthy |  |  |
| 14 | — | Audric Estime | NO | — | committee | Healthy |  |  |
| 12 GUESS (12.48) | — | Brian Robinson Jr. | ATL | 2.2 | committee | IR |  | IR x0.78; committee RB 23% cap 30; GUESS inputs |
| 9 | — | Jaleel McLaughlin | CLE | 3.8 | committee | Healthy |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 21.8 | WR1 | Healthy |  |  |
| 95 | — | CeeDee Lamb | DAL | 18.5 | WR1 | Healthy |  |  |
| 92 | — | Ja'Marr Chase | CIN | 16.6 | WR1 | Healthy |  |  |
| 89 | — | Amon-Ra St. Brown | DET | 15.9 | WR1 | Questionable |  |  |
| 87 | — | Tee Higgins | CIN | 17.0 | WR2 | Healthy |  |  |
| 86 | — | Chris Olave | NO | 14.2 | WR1 | Healthy |  |  |
| 84 | — | Malik Nabers | NYG | 12.9 | WR1 | Healthy |  |  |
| 84 | +1 | Matthew Golden | GB | 15.3 | WR2 | Healthy |  |  |
| 83 | — | Christian Watson | GB | 16.9 | WR1 | Healthy |  |  |
| 81 | — | Justin Jefferson | MIN | 11.4 | WR1 | Healthy |  |  |
| 79 | +1 | Tetairoa McMillan | CAR | 12.7 | WR1 | Healthy |  |  |
| 78 | — | Zay Flowers | BAL | 13.2 | WR1 | Healthy |  |  |
| 76 | — | Parker Washington | JAX | 11.9 | WR1 | Healthy |  |  |
| 75 | +1 | Drake London | ATL | 11.1 | WR1 | Healthy |  |  |
| 68 | — | Luther Burden III | CHI | 12.4 | WR1 | Questionable | BYE |  |
| 68 | — | Nico Collins | HOU | 12.9 | WR1 | Healthy |  |  |
| 65 | — | Garrett Wilson | NYJ | 11.5 | WR1 | Questionable |  |  |
| 59 | — | Jameson Williams | DET | 11.5 | WR2 | Healthy |  |  |
| 56 | — | Jalen Coker | CAR | 10.1 | WR2 | Healthy |  |  |
| 56 | +1 | Stefon Diggs | WAS | 10.8 | WR1 | Healthy |  |  |
| 55 | — | George Pickens | DAL | 10.6 | WR2 | Healthy |  |  |
| 54 | +1 | KC Concepcion Jr. | CLE | 11.0 | WR2 | Healthy |  |  |
| 52 | +1 | Emeka Egbuka | TB | 8.9 | WR1 | Healthy | BYE |  |
| 52 | — | Rashee Rice | KC | 8.9 | WR1 | Healthy |  |  |
| 51 | — | DK Metcalf | PIT | 7.7 | WR1 | Healthy |  |  |
| 51 GUESS (51.14) | — | Michael Wilson | ARI | 10.6 | WR | IR |  | IR x0.78; buy-low: volume > points; GUESS inputs |
| 48 | +2 | Malik Washington | MIA | 7.8 | WR2 | Healthy |  |  |
| 47 GUESS (47.14) | — | Puka Nacua | LAR | 19.8 | WR | IR |  | IR x0.78; GUESS inputs |
| 46 | +1 | DJ Moore | BUF | 8.3 | WR1 | Healthy |  |  |
| 46 | — | Rome Odunze | CHI | 8.1 | WR2 | Healthy | BYE |  |
| 43 | +1 | Denzel Boston | CLE | 7.6 | WR1 | Questionable |  |  |
| 41 | — | DeVonta Smith | PHI | 14.0 | WR | Out | BYE |  |
| 41 | +1 | Germie Bernard | PIT | 10.0 | WR2 | Healthy |  |  |
| 40 | +1 | Ladd McConkey | LAC | 7.2 | WR1 | Questionable |  |  |
| 39 | — | Mike Evans | SF | 12.6 | WR | Out |  |  |
| 37 | — | DeMario Douglas | NE | 10.5 | WR2 | Healthy |  |  |
| 37 | +1 | Tre Tucker | LV | 8.8 | WR1 | Healthy |  |  |
| 36 | +1 | Khalil Shakir | BUF | — | WR2 | Healthy |  |  |
| 34 | — | Josh Downs | KC | 7.0 | WR2 | Healthy |  |  |
| 33 | — | Makai Lemon | PHI | 6.1 | WR1 | Healthy | BYE |  |
| 32 | — | Courtland Sutton | DEN | 5.7 | WR2 | Healthy | BYE |  |
| 32 | — | Jordan Addison | MIN | 6.4 | WR2 | Questionable |  |  |
| 31 | +1 | A.J. Brown | NE | 4.9 | WR1 | Questionable |  |  |
| 31 | +1 | Jaylen Waddle | DEN | 7.4 | WR1 | Out | BYE |  |
| 31 | — | Omar Cooper Jr. | NYJ | 9.9 | WR2 | Questionable |  |  |
| 29 GUESS (29.24) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 28 | — | Keon Coleman | BUF | 6.3 | WR | Healthy |  |  |
| 27 | — | Xavier Worthy | KC | 5.9 | WR | Healthy |  |  |
| 18 | — | Adonai Mitchell | NYJ | 0.0 | WR | Questionable |  |  |
| 18 | — | Brian Thomas Jr. | JAX | 3.6 | WR | Healthy |  |  |
| 18 | — | Rashod Bateman | BAL | 5.7 | WR2 | Healthy |  |  |
| 15 | -1 | Tank Dell | HOU | 5.0 | WR2 | Healthy |  |  |
| 13 | — | Darius Cooper | PHI | 2.5 | WR2 | Healthy | BYE |  |
| 11 | — | Jerry Jeudy | CLE | 3.3 | WR | Healthy |  |  |
| 11 | — | Marvin Harrison Jr. | HOU | 4.6 | WR | Out |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 94 | — | Brock Bowers | LV | 17.4 | TE1 | Healthy |  |  |
| 89 | — | Trey McBride | ARI | 14.0 | TE1 | Healthy |  |  |
| 79 | — | George Kittle | SF | 11.9 | TE1 | Healthy |  |  |
| 79 | — | Isaiah Likely | NYG | 11.7 | TE1 | Healthy |  |  |
| 67 | — | Tyler Warren | IND | 9.3 | TE1 | Healthy |  |  |
| 62 | — | Sam LaPorta | DET | 9.4 | TE1 | Healthy |  |  |
| 59 | — | Travis Kelce | KC | 10.3 | TE1 | Healthy |  |  |
| 53 | — | Dalton Kincaid | BUF | 8.7 | TE1 | Healthy |  |  |
| 49 | — | Harold Fannin Jr. | CLE | 8.2 | TE1 | Healthy |  |  |
| 46 | — | Colston Loveland | CHI | 7.2 | TE1 | Healthy | BYE |  |
| 40 | — | Tucker Kraft | GB | 8.0 | TE1 | Healthy |  |  |
| 36 | — | T.J. Hockenson | MIN | 8.0 | TE | Out |  |  |
| 26 | — | Dallas Goedert | PHI | 6.1 | TE1 | Healthy | BYE |  |
| 22 | — | Kyle Pitts Sr. | ATL | 6.5 | TE1 | Healthy |  |  |
| 20 | — | Mark Andrews | BAL | 3.2 | TE1 | Healthy |  |  |
| 11 | — | Tyler Higbee | LAR | 2.3 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Shedeur Sanders | QB | 25 | 94 | 69 | backup QB cap 25; GUESS inputs |
| Davante Adams | WR | 29 | 85 | 56 | IR x0.50; GUESS inputs |
| Puka Nacua | WR | 47 | 98 | 51 | IR x0.78; GUESS inputs |
| Fernando Mendoza | QB | 45 | 0 | 45 | SF QB1 floor 45 |
| Carson Wentz | QB | 45 | 0 | 45 | SF QB1 floor 45; GUESS inputs |
| J.J. McCarthy | QB | 45 | 3 | 42 | SF QB1 floor 45 |
| DeVonta Smith | WR | 41 | 81 | 40 | Out x0.65 |
| Jacoby Brissett | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Jonah Coleman | RB | 30 | 67 | 37 | committee RB 27% cap 30 |
| Kenneth Walker III | RB | 61 | 98 | 37 | -29 vs last board; Out x0.65 |
| Baker Mayfield | QB | 45 | 9 | 36 | SF QB1 floor 45; buy-low: volume > points |
| Khalil Shakir | WR | 36 | 0 | 36 | buy-low: volume > points |
| Daniel Jones | QB | 45 | 11 | 34 | SF QB1 floor 45; buy-low: volume > points |
| Josh Jacobs | RB | 30 | 63 | 33 | Out x0.65; committee RB 21% cap 30 |
| Mike Evans | WR | 39 | 72 | 33 | Out x0.65 |
