# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-26 05:00 PM EST

- **NFL week:** 12
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-26 week 12 values 1.0.0`
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
| 79 | — | Patrick Mahomes | KC | 25.0 | QB1 | Healthy |  |  |
| 77 | — | Brock Purdy | SF | 27.6 | QB1 | Questionable |  |  |
| 75 | — | Trevor Lawrence | JAX | 23.8 | QB1 | Healthy |  |  |
| 74 | +1 | C.J. Stroud | HOU | 25.3 | QB1 | Healthy |  |  |
| 74 | — | Jordan Love | GB | 24.3 | QB1 | Healthy |  |  |
| 72 | — | Dak Prescott | DAL | 26.7 | QB1 | Healthy |  |  |
| 70 | — | Jared Goff | DET | 23.2 | QB1 | Healthy |  |  |
| 69 | — | Jayden Daniels | WAS | 21.9 | QB1 | Healthy |  |  |
| 63 | — | Kirk Cousins | MIN | 22.6 | QB1 | Healthy |  |  |
| 62 | -3 | Caleb Williams | CHI | 21.5 | QB1 | Questionable |  |  |
| 56 | — | Tyler Shough | NO | 21.0 | QB1 | Healthy |  |  |
| 55 | — | Matthew Stafford | LAR | 21.1 | QB1 | Healthy |  |  |
| 53 | — | Cam Ward | TEN | 20.8 | QB1 | Healthy |  |  |
| 53 GUESS (52.52) | — | Drew Lock | SEA | 20.5 | QB1 | Questionable |  | Questionable x0.95; GUESS inputs |
| 52 | — | Bryce Young | CAR | 19.5 | QB1 | Healthy |  |  |
| 49 | — | Bo Nix | DEN | 17.1 | QB1 | Healthy |  |  |
| 45 GUESS (45) | — | Aaron Rodgers | — | 17.9 | QB1 | Healthy |  | SF QB1 floor 45; GUESS inputs |
| 45 | — | Anthony Richardson Sr. | IND | — | QB1 | Healthy |  |  |
| 45 | — | Baker Mayfield | TB | 12.0 | QB1 | Healthy |  |  |
| 45 GUESS (45) | — | Carson Wentz | MIN | 2.2 | QB1 | Healthy |  | SF QB1 floor 45; GUESS inputs |
| 45 | — | Deshaun Watson | CLE | 16.7 | QB1 | Healthy |  |  |
| 45 | — | Fernando Mendoza | LV | 21.9 | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 17.1 | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 13.4 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 11.7 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 16.9 | QB1 | Healthy |  |  |
| 45 | — | Sam Darnold | SEA | 17.3 | QB1 | Healthy |  |  |
| 36 GUESS (35.6) | — | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.71; GUESS inputs |
| 35 | -1 | Justin Herbert | LAC | 14.6 | QB1 | Questionable |  |  |
| 29 | — | Drake Maye | NE | 22.9 | QB1 | Out |  |  |
| 29 GUESS (29.08) | — | Kyler Murray | MIN | 14.4 | QB1 | Questionable |  | Questionable x0.95; buy-low: volume > points; GUESS inputs |
| 28 GUESS (28.32) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |
| 18 GUESS (18.34) | — | Malik Willis | MIA | 13.3 | QB1 | IR |  | IR x0.71; buy-low: volume > points; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jahmyr Gibbs | DET | 25.9 | RB1 | Healthy |  |  |
| 92 | — | James Cook III | BUF | 18.0 | RB1 | Healthy |  |  |
| 90 | -1 | Bijan Robinson | ATL | 18.0 | RB1 | Healthy |  |  |
| 88 | — | Christian McCaffrey | SF | 20.6 | RB1 | Healthy |  |  |
| 88 | — | Chuba Hubbard | CAR | 19.1 | RB1 | Healthy |  |  |
| 86 | -1 | Bucky Irving | TB | 16.6 | RB1 | Healthy |  |  |
| 81 | — | Tony Pollard | TEN | 15.2 | RB1 | Healthy |  |  |
| 77 | — | Javonte Williams | DAL | 16.1 | RB1 | Healthy |  |  |
| 75 | — | Derrick Henry | BAL | 15.4 | RB1 | Questionable |  |  |
| 74 | -1 | Jonathan Taylor | IND | 14.2 | RB1 | Healthy |  |  |
| 73 | -1 | Bhayshul Tuten | JAX | 14.5 | RB1 | Questionable |  |  |
| 73 | -1 | D'Andre Swift | CHI | 15.3 | RB1 | Healthy |  |  |
| 71 | — | Cam Skattebo | NYG | 10.5 | RB1 | Healthy |  |  |
| 71 | -1 | Kyren Williams | LAR | 14.5 | RB1-split | Healthy |  |  |
| 70 | -1 | Jaylen Warren | PIT | 13.9 | RB1 | Healthy |  |  |
| 68 | -1 | Chase Brown | CIN | 11.2 | RB1 | Healthy |  |  |
| 65 | -1 | Ashton Jeanty | LV | 13.8 | RB1 | Healthy |  |  |
| 65 | -1 | Quinshon Judkins | CLE | 10.6 | RB1 | Healthy |  |  |
| 62 | -1 | Ollie Gordon II | MIA | 11.9 | RB1 | Healthy |  |  |
| 60 | -1 | Saquon Barkley | PHI | 8.6 | RB1 | Healthy |  |  |
| 57 | -1 | Kenneth Walker III | KC | 22.9 | RB1 | Out |  |  |
| 53 | -1 | Omarion Hampton | LAC | 8.9 | RB1 | Healthy |  |  |
| 52 | -1 | Aaron Jones Sr. | MIN | 9.8 | RB1 | Healthy |  |  |
| 52 | -1 | Rhamondre Stevenson | NE | 10.2 | RB1-split | Healthy |  |  |
| 46 | — | Braelon Allen | NYJ | 10.6 | RB1 | Healthy |  |  |
| 40 | -1 | Jacory Croskey-Merritt | WAS | 8.5 | RB1-split | Healthy |  |  |
| 32 | — | Tyler Allgeier | ARI | 7.5 | RB1-split | Healthy |  |  |
| 30 | — | Alvin Kamara | NO | 9.2 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 10.9 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 13.0 | committee | Healthy |  |  |
| 30 | — | David Montgomery | HOU | 9.3 | committee | Healthy |  |  |
| 30 | — | Emmett Johnson | KC | 10.8 | committee | Healthy |  |  |
| 30 | — | Jonah Coleman | DEN | 19.0 | committee | Healthy |  |  |
| 30 | — | Jordan Mason | MIN | 6.0 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 12.8 | committee | Out |  |  |
| 30 | — | Travis Etienne Jr. | NO | 7.6 | committee | Healthy |  |  |
| 30 | — | Zach Charbonnet | SEA | 7.6 | committee | Healthy |  |  |
| 29 | — | Jadarian Price | SEA | 6.5 | committee | Healthy |  |  |
| 27 | — | Rachaad White | WAS | 7.7 | committee | Healthy |  |  |
| 25 | +1 | Rico Dowdle | PIT | 4.6 | committee | Healthy |  |  |
| 23 | +1 | Chris Rodriguez Jr. | JAX | 5.8 | committee | Healthy |  |  |
| 21 GUESS (20.98) | -1 | RJ Harvey | DEN | 9.2 | committee | IR |  | IR x0.71; committee RB 12% cap 30; GUESS inputs |
| 19 GUESS (18.72) | +1 | J.K. Dobbins | DEN | 5.8 | RB1-split | Sus |  | Sus x0.71; buy-low: volume > points; GUESS inputs |
| 17 | — | Corey Kiner | NE | 2.5 | committee | Healthy |  |  |
| 17 | — | Kimani Vidal | LAC | 4.5 | committee | Healthy |  |  |
| 15 | +1 | Kaleb Johnson | GB | 3.7 | committee | Healthy |  |  |
| 14 GUESS (14.5) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 16% cap 30; GUESS inputs |
| 14 GUESS (13.87) | — | TreVeyon Henderson | NE | 5.2 | committee | IR |  | IR x0.71; committee RB 23% cap 30; GUESS inputs |
| 10 GUESS (10.07) | — | Brian Robinson Jr. | ATL | 2.2 | committee | IR |  | IR x0.71; committee RB 22% cap 30; GUESS inputs |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 94 | — | Amon-Ra St. Brown | DET | 16.3 | WR1 | Healthy |  |  |
| 93 | — | CeeDee Lamb | DAL | 18.9 | WR1 | Healthy |  |  |
| 92 | — | Ja'Marr Chase | CIN | 16.7 | WR1 | Healthy |  |  |
| 92 | — | Jaxon Smith-Njigba | SEA | 22.4 | WR1 | Questionable |  |  |
| 86 | +1 | Matthew Golden | GB | 14.7 | WR2 | Healthy |  |  |
| 80 | +1 | Chris Olave | NO | 13.3 | WR1 | Healthy |  |  |
| 80 | — | Justin Jefferson | MIN | 11.3 | WR1 | Healthy |  |  |
| 79 | — | Malik Nabers | NYG | 12.3 | WR1 | Healthy |  |  |
| 78 | — | Tee Higgins | CIN | 15.6 | WR2 | Healthy |  |  |
| 76 | — | Drake London | ATL | 11.3 | WR1 | Healthy |  |  |
| 76 | -4 | Parker Washington | JAX | 13.4 | WR1 | Questionable |  |  |
| 75 | +4 | Zay Flowers | BAL | 12.7 | WR1 | Healthy |  |  |
| 74 | +1 | Nico Collins | HOU | 13.8 | WR1 | Healthy |  |  |
| 71 | +1 | George Pickens | DAL | 14.3 | WR2 | Healthy |  |  |
| 71 | +1 | Luther Burden III | CHI | 11.4 | WR1 | Healthy |  |  |
| 70 | — | Tetairoa McMillan | CAR | 12.3 | WR1 | Questionable |  |  |
| 64 | +1 | DeVonta Smith | PHI | 12.5 | WR1 | Healthy |  |  |
| 63 | +1 | Garrett Wilson | NYJ | 11.0 | WR1 | Healthy |  |  |
| 62 | — | Mike Evans | SF | 13.6 | WR1 | Questionable |  |  |
| 60 | +1 | Jameson Williams | DET | 11.6 | WR2 | Healthy |  |  |
| 59 | +4 | Stefon Diggs | WAS | 11.0 | WR1 | Healthy |  |  |
| 55 | +1 | Christian Watson | GB | 15.8 | WR1 | Out |  |  |
| 55 | — | DJ Moore | BUF | 10.8 | WR1 | Healthy |  |  |
| 54 | +1 | KC Concepcion Jr. | CLE | 10.7 | WR2 | Healthy |  |  |
| 53 | +1 | Emeka Egbuka | TB | 8.2 | WR1 | Healthy |  |  |
| 50 | +1 | Rashee Rice | KC | 9.1 | WR1 | Healthy |  |  |
| 46 | — | Jalen Coker | CAR | 8.6 | WR2 | Healthy |  |  |
| 46 | +1 | Khalil Shakir | BUF | 9.7 | WR2 | Healthy |  |  |
| 45 | — | Malik Washington | MIA | 8.8 | WR2 | Healthy |  |  |
| 44 | +1 | Jaylen Waddle | DEN | 7.5 | WR1 | Healthy |  |  |
| 43 | — | DK Metcalf | PIT | 7.7 | WR1 | Healthy |  |  |
| 43 | — | Ladd McConkey | LAC | 8.8 | WR1 | Healthy |  |  |
| 43 GUESS (43.05) | — | Michael Wilson | ARI | 10.6 | WR | IR |  | IR x0.71; buy-low: volume > points; GUESS inputs |
| 43 | — | Rome Odunze | CHI | 7.9 | WR2 | Healthy |  |  |
| 38 | +1 | Denzel Boston | CLE | 6.7 | WR1 | Questionable |  |  |
| 36 | — | Josh Downs | KC | 8.0 | WR2 | Healthy |  |  |
| 34 | — | Deebo Samuel Sr. | SF | 9.8 | WR2 | Healthy |  |  |
| 30 | — | DeMario Douglas | NE | 8.1 | WR1 | Healthy |  |  |
| 30 | — | Makai Lemon | PHI | 5.6 | WR2 | Healthy |  |  |
| 30 | — | Tre Tucker | LV | 6.7 | WR1 | Healthy |  |  |
| 29 | — | Germie Bernard | PIT | 7.6 | WR2 | Healthy |  |  |
| 29 | — | Ryan Flournoy | DAL | 8.8 | WR | Healthy |  |  |
| 28 GUESS (28) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 27 | +11 | Antonio Williams | WAS | — | WR2 | Healthy |  | +11 vs last board; buy-low: volume > points |
| 24 | — | Courtland Sutton | DEN | 5.1 | WR2 | Healthy |  |  |
| 23 | — | Xavier Worthy | KC | 5.8 | WR | Healthy |  |  |
| 21 | — | Jordan Addison | MIN | 6.4 | WR | Doubtful |  |  |
| 20 | — | Keon Coleman | BUF | 4.9 | WR | Healthy |  |  |
| 16 | — | Adonai Mitchell | NYJ | 3.8 | WR2 | Healthy |  |  |
| 16 | — | Brian Thomas Jr. | JAX | 4.1 | WR | Healthy |  |  |
| 14 | +1 | Marvin Harrison Jr. | HOU | 4.6 | WR | Healthy |  |  |
| 11 | — | Jerry Jeudy | CLE | 3.8 | WR | Healthy |  |  |
| 11 | -1 | Tank Dell | HOU | 4.3 | WR | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 88 | — | Trey McBride | ARI | 13.0 | TE1 | Healthy |  |  |
| 85 | — | George Kittle | SF | 12.3 | TE1 | Healthy |  |  |
| 84 | — | Brock Bowers | LV | 15.6 | TE1 | Questionable |  |  |
| 78 | — | Isaiah Likely | NYG | 12.1 | TE1 | Questionable |  |  |
| 67 | — | Harold Fannin Jr. | CLE | 8.7 | TE1 | Questionable |  |  |
| 67 | — | Travis Kelce | KC | 10.9 | TE1 | Healthy |  |  |
| 64 | — | Sam LaPorta | DET | 8.5 | TE1 | Healthy |  |  |
| 53 | — | T.J. Hockenson | MIN | 8.1 | TE1 | Healthy |  |  |
| 52 | — | Tyler Warren | IND | 7.7 | TE1 | Healthy |  |  |
| 50 | — | Tucker Kraft | GB | 7.5 | TE1 | Healthy |  |  |
| 44 | — | Chig Okonkwo | WAS | 8.6 | TE1 | Healthy |  |  |
| 42 | — | Dalton Kincaid | BUF | 8.5 | TE1 | Questionable |  |  |
| 36 | -20 | Colston Loveland | CHI | 7.5 | TE1 | Out |  | -20 vs last board; Out x0.65; buy-low: volume > points |
| 32 | — | Dallas Goedert | PHI | 5.9 | TE1 | Healthy |  |  |
| 28 | — | Brenton Strange | JAX | 5.5 | TE1 | Healthy |  |  |
| 27 | — | Kyle Pitts Sr. | ATL | 6.3 | TE1 | Healthy |  |  |
| 24 | — | Michael Mayer | LV | 8.2 | TE2 | Healthy |  |  |
| 18 | — | Juwan Johnson | NO | 6.5 | TE1 | Questionable |  |  |
| 11 | — | Pat Freiermuth | PIT | 4.3 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Jonah Coleman | RB | 30 | 92 | 62 | committee RB 35% cap 30 |
| Davante Adams | WR | 28 | 86 | 58 | IR x0.50; GUESS inputs |
| Carson Wentz | QB | 45 | 0 | 45 | SF QB1 floor 45; GUESS inputs |
| Anthony Richardson Sr. | QB | 45 | 0 | 45 | SF QB1 floor 45 |
| Drake Maye | QB | 29 | 73 | 44 | Out x0.65 |
| Jacoby Brissett | QB | 45 | 3 | 42 | SF QB1 floor 45; buy-low: volume > points |
| Kenneth Walker III | RB | 57 | 98 | 41 | Out x0.65 |
| Baker Mayfield | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Christian Watson | WR | 55 | 92 | 37 | Out x0.65 |
| Breece Hall | RB | 30 | 65 | 35 | committee RB 38% cap 30 |
| J.J. McCarthy | QB | 45 | 12 | 33 | SF QB1 floor 45; buy-low: volume > points |
| Josh Jacobs | RB | 30 | 62 | 32 | Out x0.65; committee RB 19% cap 30 |
| Antonio Williams | WR | 27 | 0 | 27 | +11 vs last board; buy-low: volume > points |
| Saquon Barkley | RB | 60 | 33 | 27 | buy-low: volume > points |
| Blake Corum | RB | 30 | 56 | 26 | committee RB 39% cap 30 |
