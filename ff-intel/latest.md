# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-06 07:00 AM EST

- **NFL week:** 9
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-06 week 9 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | +2 | Joe Burrow | CIN | 30.8 | QB1 | Healthy |  |  |
| 87 | — | Josh Allen | BUF | 30.6 | QB1 | Healthy |  |  |
| 79 | -1 | Brock Purdy | SF | 25.7 | QB1 | Healthy |  |  |
| 79 | — | Drake Maye | NE | 24.9 | QB1 | Healthy |  |  |
| 77 | -1 | Trevor Lawrence | JAX | 24.5 | QB1 | Healthy |  |  |
| 75 | — | Jared Goff | DET | 24.7 | QB1 | Healthy |  |  |
| 71 | +2 | Jayden Daniels | WAS | 22.5 | QB1 | Healthy |  |  |
| 71 | — | Patrick Mahomes | KC | 21.9 | QB1 | Healthy |  |  |
| 68 | — | Jordan Love | GB | 23.4 | QB1 | Healthy |  |  |
| 68 | +1 | Kirk Cousins | LV | 25.3 | QB1 | Healthy |  |  |
| 68 | -1 | Tyler Shough | NO | 22.6 | QB1 | Healthy |  |  |
| 65 | +1 | Dak Prescott | DAL | 22.6 | QB1 | Healthy |  |  |
| 64 | +1 | Caleb Williams | CHI | 22.1 | QB1 | Healthy |  |  |
| 61 | -1 | Bryce Young | CAR | 19.8 | QB1 | Healthy |  |  |
| 61 | -1 | C.J. Stroud | HOU | 21.7 | QB1 | Healthy |  |  |
| 56 | — | Matthew Stafford | LAR | 21.2 | QB1 | Healthy |  |  |
| 50 | — | Bo Nix | DEN | 17.0 | QB1 | Healthy |  |  |
| 49 | +1 | Geno Smith | NYJ | 18.9 | QB1 | Healthy |  |  |
| 45 | — | Aaron Rodgers | PIT | 17.5 | QB1 | Healthy | BYE |  |
| 45 | — | Baker Mayfield | TB | 10.2 | QB1 | Healthy |  |  |
| 45 | -3 | Cam Ward | TEN | 17.9 | QB1 | Healthy | BYE |  |
| 45 | — | J.J. McCarthy | NYG | 10.2 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | ARI | 10.1 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 12.9 | QB1 | Healthy |  |  |
| 45 | — | Malik Willis | MIA | 14.7 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 17.8 | QB1 | Healthy |  |  |
| 36 | — | Kyler Murray | MIN | 14.4 | QB1 | Questionable |  |  |
| 34 | — | Drew Lock | SEA | 27.4 | QB1 | Questionable |  |  |
| 32 GUESS (31.7) | -1 | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.80; GUESS inputs |
| 29 GUESS (28.69) | -1 | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |
| 26 GUESS (25.69) | +4 | Tyler Huntley | BAL | 14.9 | QB1 | IR |  | IR x0.80; buy-low: volume > points; GUESS inputs |
| 25 | -1 | Deshaun Watson | CLE | 15.7 | QB1 | Questionable |  |  |
| 24 | -1 | Sam Darnold | SEA | 17.3 | QB1 | Out |  |  |
| 22 | +6 | Gardner Minshew II | ARI | — | QB2 | Healthy |  |  |
| 19 | +6 | Joe Milton | PHI | — | QB2 | Healthy |  |  |
| 14 GUESS (14.3) | -31 | Tanner McKee | PHI | 10.8 | QB1 | Questionable |  | -31 vs last board; Questionable x0.95; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 96 | — | Jahmyr Gibbs | DET | 25.5 | RB1 | Healthy |  |  |
| 93 | — | James Cook III | BUF | 18.0 | RB1 | Healthy |  |  |
| 93 | — | Kenneth Walker III | KC | 21.3 | RB1 | Healthy |  |  |
| 88 | — | Bijan Robinson | ATL | 17.6 | RB1 | Healthy |  |  |
| 85 | — | Jonathan Taylor | IND | 16.7 | RB1 | Healthy |  |  |
| 84 | — | Chuba Hubbard | CAR | 17.4 | RB1 | Healthy |  |  |
| 82 | — | Christian McCaffrey | SF | 18.1 | RB1 | Questionable |  |  |
| 81 | -2 | Derrick Henry | BAL | 16.3 | RB1 | Healthy |  |  |
| 80 | -2 | Javonte Williams | DAL | 15.9 | RB1 | Healthy |  |  |
| 78 | +7 | Bhayshul Tuten | JAX | 15.8 | RB1 | Healthy |  |  |
| 78 | +2 | D'Andre Swift | CHI | 17.3 | RB1 | Healthy |  |  |
| 77 | -2 | Kyren Williams | LAR | 16.7 | RB1 | Healthy |  |  |
| 76 | +2 | Bucky Irving | TB | 15.2 | RB1 | Healthy |  |  |
| 73 | +3 | Jaylen Warren | PIT | 16.0 | RB1 | Healthy | BYE |  |
| 72 | +1 | Tony Pollard | TEN | 15.2 | RB1 | Healthy | BYE |  |
| 70 | -1 | Ashton Jeanty | LV | 14.2 | RB1 | Healthy |  |  |
| 67 | -1 | Chase Brown | CIN | 10.4 | RB1 | Healthy |  |  |
| 65 | +4 | Quinshon Judkins | CLE | 10.9 | RB1 | Healthy |  |  |
| 61 | -1 | Ollie Gordon II | MIA | 13.9 | RB1 | Healthy |  |  |
| 60 | +1 | Braelon Allen | NYJ | 12.4 | RB1 | Healthy |  |  |
| 56 | +1 | Cam Skattebo | NYG | 9.3 | RB1 | Questionable |  |  |
| 55 | -2 | Aaron Jones Sr. | MIN | 10.3 | RB1 | Healthy |  |  |
| 55 | -2 | Rhamondre Stevenson | NE | 10.9 | RB1-split | Healthy |  |  |
| 49 | -2 | Omarion Hampton | LAC | 8.1 | RB1 | Healthy |  |  |
| 43 | +3 | Tyler Allgeier | ARI | 9.2 | RB1-split | Healthy |  |  |
| 41 | — | Woody Marks | HOU | 7.4 | RB1 | Healthy |  |  |
| 36 | -2 | J.K. Dobbins | DEN | 6.9 | RB1 | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 9.7 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 12.5 | committee | Healthy |  |  |
| 30 | — | Jonah Coleman | DEN | 13.2 | committee | Healthy |  |  |
| 30 | — | Jordan Mason | MIN | 6.9 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 18.9 | committee | Healthy |  |  |
| 30 | — | Rachaad White | WAS | 13.3 | committee | Healthy |  |  |
| 30 | — | Saquon Barkley | PHI | 7.8 | committee | Questionable |  |  |
| 29 GUESS (29.31) | — | Travis Etienne Jr. | NO | 8.5 | committee | IR |  | IR x0.80; committee RB 20% cap 30; GUESS inputs |
| 28 | — | Alvin Kamara | NO | 9.1 | committee | Questionable |  |  |
| 26 | -1 | Chris Rodriguez Jr. | JAX | 6.0 | committee | Healthy |  |  |
| 26 | — | David Montgomery | HOU | 8.4 | committee | Out |  |  |
| 25 | +4 | Jadarian Price | SEA | 4.0 | committee | Healthy |  |  |
| 25 | -2 | TreVeyon Henderson | NE | 5.2 | committee | Questionable |  |  |
| 24 | — | Emmett Johnson | KC | 6.3 | committee | Healthy |  |  |
| 23 | — | Kimani Vidal | LAC | 4.8 | committee | Healthy |  |  |
| 21 GUESS (21) | — | RJ Harvey | DEN | 9.2 | committee | IR |  | IR x0.80; committee RB 16% cap 30; GUESS inputs |
| 21 | -1 | Zach Charbonnet | SEA | 4.4 | committee | Healthy |  |  |
| 17 | — | Brian Robinson Jr. | ATL | 2.2 | committee | Questionable |  |  |
| 16 GUESS (16.39) | -1 | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 21% cap 30; GUESS inputs |
| 10 | -1 | Jaleel McLaughlin | CLE | 3.8 | committee | Healthy |  |  |
| 10 | +1 | Jaydon Blue | PHI | 1.4 | committee | Healthy |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 23.5 | WR1 | Healthy |  |  |
| 94 | — | CeeDee Lamb | DAL | 17.3 | WR1 | Healthy |  |  |
| 91 | — | Puka Nacua | LAR | 18.4 | WR1 | Healthy |  |  |
| 89 | — | Amon-Ra St. Brown | DET | 16.4 | WR1 | Questionable |  |  |
| 87 | — | Ja'Marr Chase | CIN | 15.2 | WR1 | Healthy |  |  |
| 87 | +2 | Tee Higgins | CIN | 16.9 | WR2 | Healthy |  |  |
| 84 | -1 | Chris Olave | NO | 14.3 | WR1 | Healthy |  |  |
| 80 | +1 | Malik Nabers | NYG | 13.8 | WR1 | Questionable |  |  |
| 80 | — | Zay Flowers | BAL | 14.6 | WR1 | Healthy |  |  |
| 76 | — | Justin Jefferson | MIN | 12.1 | WR1 | Healthy |  |  |
| 76 | — | Tetairoa McMillan | CAR | 12.6 | WR1 | Healthy |  |  |
| 74 | — | Matthew Golden | GB | 13.8 | WR2 | Healthy |  |  |
| 73 | +1 | Drake London | ATL | 11.3 | WR1 | Healthy |  |  |
| 72 | — | Christian Watson | GB | 15.7 | WR1 | Questionable |  |  |
| 72 | -1 | Parker Washington | JAX | 11.7 | WR1 | Healthy |  |  |
| 68 | — | Nico Collins | HOU | 12.8 | WR1 | Healthy |  |  |
| 66 | — | Garrett Wilson | NYJ | 11.5 | WR1 | Questionable |  |  |
| 66 | — | Mike Evans | SF | 12.6 | WR1 | Questionable |  |  |
| 64 | — | Luther Burden III | CHI | 11.8 | WR1 | Healthy |  |  |
| 61 | — | Malik Washington | MIA | 12.5 | WR1 | Healthy |  |  |
| 60 | +1 | Jameson Williams | DET | 12.5 | WR2 | Healthy |  |  |
| 60 | — | Michael Wilson | ARI | 10.8 | WR1 | Questionable |  |  |
| 58 | — | Jalen Coker | CAR | 11.0 | WR2 | Healthy |  |  |
| 56 | -1 | Emeka Egbuka | TB | 9.5 | WR1 | Healthy |  |  |
| 56 | -2 | Stefon Diggs | WAS | 11.4 | WR1 | Healthy |  |  |
| 54 | -2 | DeVonta Smith | PHI | 14.0 | WR | Questionable |  |  |
| 53 | — | George Pickens | DAL | 10.6 | WR2 | Questionable |  |  |
| 52 | +1 | Jaylen Waddle | DEN | 8.0 | WR1 | Healthy |  |  |
| 49 | — | Rashee Rice | KC | 9.3 | WR1 | Healthy |  |  |
| 46 | — | DJ Moore | BUF | 9.0 | WR1 | Questionable |  |  |
| 46 | -1 | DK Metcalf | PIT | 7.7 | WR1 | Healthy | BYE |  |
| 42 | +3 | Ladd McConkey | LAC | 7.2 | WR1 | Healthy |  |  |
| 41 | +1 | Rome Odunze | CHI | 7.3 | WR2 | Healthy |  |  |
| 41 | -1 | Tre Tucker | LV | 9.4 | WR1 | Healthy |  |  |
| 39 | — | Denzel Boston | CLE | 6.2 | WR1 | Questionable |  |  |
| 37 | +1 | Xavier Worthy | KC | 5.6 | WR2 | Healthy |  |  |
| 35 | — | Germie Bernard | PIT | 10.0 | WR2 | Healthy | BYE |  |
| 35 | +3 | Omar Cooper Jr. | NYJ | 10.0 | WR | Healthy |  |  |
| 34 | — | Jordan Addison | MIN | 6.8 | WR2 | Healthy |  |  |
| 32 | +1 | DeMario Douglas | NE | 9.4 | WR1 | Healthy |  |  |
| 32 | — | KC Concepcion Jr. | CLE | 5.2 | WR2 | Healthy |  |  |
| 28 GUESS (27.65) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 28 | +1 | Makai Lemon | PHI | 5.8 | WR2 | Healthy |  |  |
| 27 | -1 | Keon Coleman | BUF | 7.3 | WR | Questionable |  |  |
| 26 | — | Courtland Sutton | DEN | 4.8 | WR2 | Healthy |  |  |
| 25 | -5 | A.J. Brown | NE | 4.9 | WR | Questionable |  |  |
| 25 | -1 | Chris Godwin Jr. | TB | 4.5 | WR2 | Healthy |  |  |
| 20 GUESS (19.64) | — | Romeo Doubs | NE | 8.5 | WR | IR |  | IR x0.80; GUESS inputs |
| 19 | — | Rashod Bateman | BAL | 6.3 | WR2 | Healthy |  |  |
| 18 | -1 | Marvin Harrison Jr. | HOU | 4.8 | WR2 | Healthy |  |  |
| 17 | — | Adonai Mitchell | NYJ | — | WR2 | Healthy |  |  |
| 17 | — | Brian Thomas Jr. | JAX | 4.1 | WR | Healthy |  |  |
| 11 | — | Jerry Jeudy | CLE | 3.1 | WR | Healthy |  |  |
| 10 | — | Darius Cooper | PHI | 2.2 | WR1 | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 93 | -1 | Brock Bowers | LV | 17.2 | TE1 | Healthy |  |  |
| 93 | +3 | Trey McBride | ARI | 14.7 | TE1 | Healthy |  |  |
| 84 | -1 | George Kittle | SF | 12.5 | TE1 | Healthy |  |  |
| 75 | -5 | Isaiah Likely | NYG | 11.4 | TE1 | Healthy |  |  |
| 65 | +3 | Travis Kelce | KC | 9.6 | TE1 | Healthy |  |  |
| 62 | +3 | Sam LaPorta | DET | 10.1 | TE1 | Healthy |  |  |
| 54 | +3 | T.J. Hockenson | MIN | 8.8 | TE1 | Healthy |  |  |
| 53 | -2 | Tyler Warren | IND | 9.8 | TE1 | Healthy |  |  |
| 51 | -3 | Dalton Kincaid | BUF | 9.4 | TE1 | Questionable |  |  |
| 48 | — | Harold Fannin Jr. | CLE | 7.7 | TE1 | Questionable |  |  |
| 45 | — | Colston Loveland | CHI | 7.2 | TE1 | Healthy |  |  |
| 42 | — | Tucker Kraft | GB | 8.9 | TE1 | Healthy |  |  |
| 24 | — | Kyle Pitts Sr. | ATL | 6.8 | TE1 | Healthy |  |  |
| 20 | — | Dallas Goedert | PHI | 5.9 | TE1 | Healthy |  |  |
| 19 | — | Mark Andrews | BAL | 3.4 | TE1 | Healthy |  |  |
| 14 | — | Hunter Henry | NE | 4.5 | TE2 | Questionable |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Josh Jacobs | RB | 30 | 96 | 66 | committee RB 22% cap 30 |
| Drew Lock | QB | 34 | 94 | 60 | Questionable x0.95 |
| Davante Adams | WR | 28 | 85 | 57 | IR x0.50; GUESS inputs |
| Jacoby Brissett | QB | 45 | 0 | 45 | SF QB1 floor 45; buy-low: volume > points |
| J.J. McCarthy | QB | 45 | 3 | 42 | SF QB1 floor 45 |
| Baker Mayfield | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Justin Herbert | QB | 45 | 12 | 33 | SF QB1 floor 45; buy-low: volume > points |
| Rachaad White | RB | 30 | 62 | 32 | committee RB 33% cap 30 |
| Jonah Coleman | RB | 30 | 60 | 30 | committee RB 20% cap 30 |
| Breece Hall | RB | 30 | 57 | 28 | committee RB 28% cap 30 |
| Malik Willis | QB | 45 | 18 | 27 | SF QB1 floor 45; buy-low: volume > points |
| DeVonta Smith | WR | 54 | 81 | 27 | Questionable x0.95 |
| Bo Nix | QB | 50 | 27 | 23 | SF QB1 floor 45; buy-low: volume > points |
| Jalen Hurts | QB | 29 | 52 | 22 | IR x0.50; GUESS inputs |
| Gardner Minshew II | QB | 22 | 0 | 22 | backup QB cap 25 |
