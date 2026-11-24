# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-24 05:00 PM EST

- **NFL week:** 11
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-24 week 11 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | — | Joe Burrow | CIN | 31.6 | QB1 | Healthy |  |  |
| 83 | — | Josh Allen | BUF | 27.2 | QB1 | Healthy |  |  |
| 80 | — | Brock Purdy | SF | 27.6 | QB1 | Healthy |  |  |
| 78 | — | Patrick Mahomes | KC | 25.0 | QB1 | Healthy |  |  |
| 76 | — | Trevor Lawrence | JAX | 23.8 | QB1 | Healthy |  |  |
| 74 | — | C.J. Stroud | HOU | 25.3 | QB1 | Healthy |  |  |
| 72 | -1 | Dak Prescott | DAL | 26.7 | QB1 | Healthy |  |  |
| 70 | — | Jared Goff | DET | 23.2 | QB1 | Healthy |  |  |
| 70 | — | Jayden Daniels | WAS | 21.9 | QB1 | Healthy |  |  |
| 69 | +1 | Jordan Love | GB | 24.3 | QB1 | Healthy | BYE |  |
| 66 | — | Caleb Williams | CHI | 21.5 | QB1 | Healthy |  |  |
| 63 | — | Kirk Cousins | MIN | 22.6 | QB1 | Healthy |  |  |
| 54 | — | Cam Ward | TEN | 20.8 | QB1 | Healthy |  |  |
| 54 GUESS (54.47) | — | Drew Lock | SEA | 20.5 | QB1 | Healthy | BYE | SF QB1 floor 45; GUESS inputs |
| 54 | — | Tyler Shough | NO | 21.0 | QB1 | Healthy |  |  |
| 53 | — | Bryce Young | CAR | 19.5 | QB1 | Healthy |  |  |
| 51 | — | Bo Nix | DEN | 17.1 | QB1 | Healthy |  |  |
| 46 | -2 | Matthew Stafford | LAR | 21.1 | QB1 | Healthy | BYE |  |
| 45 | — | Aaron Rodgers | PIT | 17.9 | QB1 | Healthy |  |  |
| 45 | — | Baker Mayfield | TB | 12.0 | QB1 | Healthy |  |  |
| 45 GUESS (45) | — | Carson Wentz | MIN | 2.2 | QB1 | Healthy |  | SF QB1 floor 45; GUESS inputs |
| 45 GUESS (45) | — | Daniel Jones | — | 10.4 | QB1 | Healthy |  | SF QB1 floor 45; buy-low: volume > points; GUESS inputs |
| 45 | — | Deshaun Watson | CLE | 16.7 | QB1 | Healthy | BYE |  |
| 45 | — | Fernando Mendoza | LV | 21.9 | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 17.1 | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 13.4 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 11.7 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 16.9 | QB1 | Healthy | BYE |  |
| 42 | — | Justin Herbert | LAC | 14.6 | QB1 | Questionable |  |  |
| 38 GUESS (38.29) | — | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.75; GUESS inputs |
| 29 | — | Drake Maye | NE | 22.9 | QB1 | Out | BYE |  |
| 28 GUESS (27.84) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |
| 26 | +1 | Sam Darnold | SEA | 17.3 | QB1 | Out | BYE |  |
| 20 GUESS (19.95) | — | Kyler Murray | MIN | 14.4 | QB1 | Out |  | Out x0.65; buy-low: volume > points; GUESS inputs |
| 20 GUESS (19.54) | — | Malik Willis | MIA | 13.3 | QB1 | IR |  | IR x0.75; buy-low: volume > points; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jahmyr Gibbs | DET | 25.9 | RB1 | Healthy |  |  |
| 93 | — | James Cook III | BUF | 18.0 | RB1 | Healthy |  |  |
| 89 | — | Chuba Hubbard | CAR | 19.1 | RB1 | Healthy |  |  |
| 88 | — | Bijan Robinson | ATL | 18.0 | RB1 | Healthy | BYE |  |
| 88 | — | Christian McCaffrey | SF | 20.6 | RB1 | Healthy |  |  |
| 87 | — | Bucky Irving | TB | 16.6 | RB1 | Healthy |  |  |
| 80 | — | Tony Pollard | TEN | 15.2 | RB1 | Healthy |  |  |
| 78 | — | Javonte Williams | DAL | 16.1 | RB1 | Healthy |  |  |
| 76 | — | Derrick Henry | BAL | 15.4 | RB1 | Questionable |  |  |
| 76 | — | Jonathan Taylor | IND | 14.2 | RB1 | Healthy |  |  |
| 75 | — | D'Andre Swift | CHI | 15.3 | RB1 | Healthy |  |  |
| 73 | — | Bhayshul Tuten | JAX | 14.5 | RB1 | Questionable |  |  |
| 72 | — | Jaylen Warren | PIT | 13.9 | RB1 | Healthy |  |  |
| 71 | — | Cam Skattebo | NYG | 10.5 | RB1 | Healthy |  |  |
| 70 | — | Chase Brown | CIN | 11.2 | RB1 | Healthy |  |  |
| 68 | — | Ashton Jeanty | LV | 13.8 | RB1 | Healthy |  |  |
| 63 | — | Kyren Williams | LAR | 14.5 | RB1-split | Questionable | BYE |  |
| 63 | — | Quinshon Judkins | CLE | 10.6 | RB1 | Healthy | BYE |  |
| 62 | — | Ollie Gordon II | MIA | 11.9 | RB1 | Healthy |  |  |
| 58 | — | Kenneth Walker III | KC | 22.9 | RB1 | Out |  |  |
| 57 | +1 | Saquon Barkley | PHI | 8.6 | RB1 | Questionable |  |  |
| 56 | -1 | Omarion Hampton | LAC | 8.9 | RB1 | Healthy |  |  |
| 55 | — | Aaron Jones Sr. | MIN | 9.8 | RB1 | Healthy |  |  |
| 50 | +1 | Rhamondre Stevenson | NE | 10.2 | RB1-split | Healthy | BYE |  |
| 48 | +1 | Braelon Allen | NYJ | 10.6 | RB1 | Healthy |  |  |
| 34 | — | Tyler Allgeier | ARI | 7.5 | RB1-split | Healthy |  |  |
| 30 | — | Alvin Kamara | NO | 9.2 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 10.9 | committee | Healthy | BYE |  |
| 30 | — | Breece Hall | NYJ | 13.0 | committee | Healthy |  |  |
| 30 | — | David Montgomery | HOU | 9.3 | committee | Healthy |  |  |
| 30 | — | Emmett Johnson | KC | 10.8 | committee | Healthy |  |  |
| 30 | — | Jonah Coleman | DEN | 19.0 | committee | Healthy |  |  |
| 30 | — | Jordan Mason | MIN | 6.0 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 12.8 | committee | Out | BYE |  |
| 30 | — | Rachaad White | WAS | 7.7 | committee | Healthy |  |  |
| 30 | — | Travis Etienne Jr. | NO | 7.6 | committee | Healthy |  |  |
| 30 | — | Zach Charbonnet | SEA | 7.6 | committee | Healthy | BYE |  |
| 28 | — | J.K. Dobbins | DEN | 5.8 | RB1-split | Healthy |  |  |
| 28 | — | Jadarian Price | SEA | 6.5 | committee | Healthy | BYE |  |
| 27 | — | Rico Dowdle | PIT | 4.6 | committee | Healthy |  |  |
| 23 | — | Chris Rodriguez Jr. | JAX | 5.8 | committee | Healthy |  |  |
| 23 | — | Woody Marks | HOU | 7.4 | RB1-split | Out |  |  |
| 20 GUESS (20.5) | -1 | RJ Harvey | DEN | 9.2 | committee | IR |  | IR x0.75; committee RB 12% cap 30; GUESS inputs |
| 18 | +1 | Corey Kiner | NE | 2.5 | committee | Healthy | BYE |  |
| 18 | — | Kimani Vidal | LAC | 4.5 | committee | Healthy |  |  |
| 16 | — | Kaleb Johnson | GB | 3.7 | committee | Healthy | BYE |  |
| 16 GUESS (15.72) | — | TreVeyon Henderson | NE | 5.2 | committee | IR | BYE | IR x0.75; committee RB 23% cap 30; GUESS inputs |
| 15 GUESS (14.97) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 16% cap 30; GUESS inputs |
| 12 GUESS (11.78) | — | Brian Robinson Jr. | ATL | 2.2 | committee | IR | BYE | IR x0.75; committee RB 22% cap 30; GUESS inputs |
| 7 | — | Audric Estime | NO | 1.6 | committee | Out |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 97 | — | Jaxon Smith-Njigba | SEA | 22.4 | WR1 | Healthy | BYE |  |
| 95 | — | CeeDee Lamb | DAL | 18.9 | WR1 | Healthy |  |  |
| 94 | — | Amon-Ra St. Brown | DET | 16.3 | WR1 | Healthy |  |  |
| 93 | — | Ja'Marr Chase | CIN | 16.7 | WR1 | Healthy |  |  |
| 81 | — | Chris Olave | NO | 13.3 | WR1 | Healthy |  |  |
| 81 | -1 | Matthew Golden | GB | 14.7 | WR2 | Healthy | BYE |  |
| 81 | — | Parker Washington | JAX | 13.4 | WR1 | Healthy |  |  |
| 80 | — | Christian Watson | GB | 15.8 | WR1 | Healthy | BYE |  |
| 80 | — | Justin Jefferson | MIN | 11.3 | WR1 | Healthy |  |  |
| 80 | — | Malik Nabers | NYG | 12.3 | WR1 | Healthy |  |  |
| 80 | — | Tee Higgins | CIN | 15.6 | WR2 | Healthy |  |  |
| 75 | — | Nico Collins | HOU | 13.8 | WR1 | Healthy |  |  |
| 75 | — | Tetairoa McMillan | CAR | 12.3 | WR1 | Healthy |  |  |
| 74 | — | Zay Flowers | BAL | 12.7 | WR1 | Healthy |  |  |
| 72 | — | Luther Burden III | CHI | 11.4 | WR1 | Healthy |  |  |
| 70 | — | George Pickens | DAL | 14.3 | WR2 | Healthy |  |  |
| 69 | — | Drake London | ATL | 11.3 | WR1 | Questionable | BYE |  |
| 69 | — | Mike Evans | SF | 13.6 | WR1 | Healthy |  |  |
| 65 | — | Garrett Wilson | NYJ | 11.0 | WR1 | Healthy |  |  |
| 64 | +1 | DeVonta Smith | PHI | 12.5 | WR1 | Healthy |  |  |
| 60 | +1 | Jameson Williams | DET | 11.6 | WR2 | Healthy |  |  |
| 60 | — | Stefon Diggs | WAS | 11.0 | WR1 | Healthy |  |  |
| 54 | — | Emeka Egbuka | TB | 8.2 | WR1 | Healthy |  |  |
| 53 | — | DJ Moore | BUF | 10.8 | WR1 | Questionable |  |  |
| 51 | +2 | KC Concepcion Jr. | CLE | 10.7 | WR2 | Healthy | BYE |  |
| 50 | -2 | Rashee Rice | KC | 9.1 | WR1 | Healthy |  |  |
| 47 | — | Khalil Shakir | BUF | 9.7 | WR2 | Healthy |  |  |
| 46 GUESS (45.9) | — | Michael Wilson | ARI | 10.6 | WR | IR |  | IR x0.75; buy-low: volume > points; GUESS inputs |
| 45 | -1 | DK Metcalf | PIT | 7.7 | WR1 | Healthy |  |  |
| 45 | — | Jaylen Waddle | DEN | 7.5 | WR1 | Healthy |  |  |
| 45 | — | Ladd McConkey | LAC | 8.8 | WR1 | Healthy |  |  |
| 45 | -1 | Malik Washington | MIA | 8.8 | WR2 | Healthy |  |  |
| 44 | — | Jalen Coker | CAR | 8.6 | WR2 | Questionable |  |  |
| 44 | — | Rome Odunze | CHI | 7.9 | WR2 | Healthy |  |  |
| 38 | — | Deebo Samuel Sr. | SF | 9.8 | WR2 | Healthy |  |  |
| 37 | -1 | Josh Downs | KC | 8.0 | WR2 | Healthy |  |  |
| 35 | -1 | Denzel Boston | CLE | 6.7 | WR1 | Questionable | BYE |  |
| 33 | — | Ryan Flournoy | DAL | 8.8 | WR | Healthy |  |  |
| 31 | — | Germie Bernard | PIT | 7.6 | WR2 | Healthy |  |  |
| 31 | — | Tre Tucker | LV | 6.7 | WR1 | Healthy |  |  |
| 30 | — | Makai Lemon | PHI | 5.6 | WR2 | Healthy |  |  |
| 29 | — | Courtland Sutton | DEN | 5.1 | WR2 | Healthy |  |  |
| 28 | — | DeMario Douglas | NE | 8.1 | WR1 | Healthy | BYE |  |
| 27 GUESS (26.85) | — | Davante Adams | LAR | 14.5 | WR | IR | BYE | IR x0.50; GUESS inputs |
| 23 | — | Xavier Worthy | KC | 5.8 | WR | Healthy |  |  |
| 22 | -1 | Keon Coleman | BUF | 4.9 | WR | Healthy |  |  |
| 17 | — | Adonai Mitchell | NYJ | 3.8 | WR | Healthy |  |  |
| 16 | — | Brian Thomas Jr. | JAX | 4.1 | WR | Healthy |  |  |
| 15 | — | Jordan Addison | MIN | 6.4 | WR | Out |  |  |
| 14 | — | A.J. Brown | NE | 4.6 | WR | Out | BYE |  |
| 11 | — | Jerry Jeudy | CLE | 3.8 | WR | Healthy | BYE |  |
| 11 | — | Tank Dell | HOU | 4.3 | WR | Healthy |  |  |
| 9 | — | Marvin Harrison Jr. | HOU | 4.6 | WR | Out |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | — | George Kittle | SF | 12.3 | TE1 | Healthy |  |  |
| 87 | — | Trey McBride | ARI | 13.0 | TE1 | Healthy |  |  |
| 84 | — | Isaiah Likely | NYG | 12.1 | TE1 | Healthy |  |  |
| 66 | — | Travis Kelce | KC | 10.9 | TE1 | Healthy |  |  |
| 63 | — | Harold Fannin Jr. | CLE | 8.7 | TE1 | Healthy | BYE |  |
| 59 | — | Sam LaPorta | DET | 8.5 | TE1 | Questionable |  |  |
| 57 | — | Colston Loveland | CHI | 7.5 | TE1 | Healthy |  |  |
| 56 | — | T.J. Hockenson | MIN | 8.1 | TE1 | Healthy |  |  |
| 55 | — | Brock Bowers | LV | 15.6 | TE1 | Out |  |  |
| 53 | — | Tyler Warren | IND | 7.7 | TE1 | Healthy |  |  |
| 48 | — | Chig Okonkwo | WAS | 8.6 | TE1 | Healthy |  |  |
| 42 | — | Tucker Kraft | GB | 7.5 | TE1 | Healthy | BYE |  |
| 31 | — | Dallas Goedert | PHI | 5.9 | TE1 | Questionable |  |  |
| 26 | — | Brenton Strange | JAX | 5.5 | TE1 | Healthy |  |  |
| 22 | — | Kyle Pitts Sr. | ATL | 6.3 | TE1 | Healthy | BYE |  |
| 21 | — | Dalton Kincaid | BUF | 8.5 | TE1 | Out |  |  |
| 19 | — | Juwan Johnson | NO | 6.5 | TE1 | Questionable |  |  |
| 9 | — | Pat Freiermuth | PIT | 4.3 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Jonah Coleman | RB | 30 | 92 | 62 | committee RB 35% cap 30 |
| Davante Adams | WR | 27 | 87 | 60 | IR x0.50; GUESS inputs |
| Carson Wentz | QB | 45 | 0 | 45 | SF QB1 floor 45; GUESS inputs |
| Brock Bowers | TE | 55 | 100 | 45 | Out x0.65 |
| Drake Maye | QB | 29 | 74 | 44 | Out x0.65 |
| Daniel Jones | QB | 45 | 3 | 42 | SF QB1 floor 45; buy-low: volume > points; GUESS inputs |
| Kenneth Walker III | RB | 58 | 98 | 40 | Out x0.65 |
| Jacoby Brissett | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Baker Mayfield | QB | 45 | 9 | 36 | SF QB1 floor 45; buy-low: volume > points |
| Breece Hall | RB | 30 | 65 | 35 | committee RB 38% cap 30 |
| Josh Jacobs | RB | 30 | 63 | 33 | Out x0.65; committee RB 19% cap 30 |
| Dalton Kincaid | TE | 21 | 53 | 32 | Out x0.65 |
| J.J. McCarthy | QB | 45 | 15 | 30 | SF QB1 floor 45; buy-low: volume > points |
| Blake Corum | RB | 30 | 57 | 27 | committee RB 39% cap 30 |
| Emmett Johnson | RB | 30 | 55 | 25 | committee RB 30% cap 30 |
