# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-19 05:00 PM EST

- **NFL week:** 11
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-19 week 11 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 88 | — | Joe Burrow | CIN | 32.5 | QB1 | Healthy |  |  |
| 84 | — | Josh Allen | BUF | 28.4 | QB1 | Healthy |  |  |
| 80 | — | Brock Purdy | SF | 27.6 | QB1 | Healthy |  |  |
| 78 | — | Patrick Mahomes | KC | 24.4 | QB1 | Healthy |  |  |
| 78 | — | Trevor Lawrence | JAX | 24.6 | QB1 | Healthy |  |  |
| 74 | — | C.J. Stroud | HOU | 25.1 | QB1 | Healthy |  |  |
| 72 | — | Jayden Daniels | WAS | 22.6 | QB1 | Healthy |  |  |
| 71 | — | Dak Prescott | DAL | 25.0 | QB1 | Healthy |  |  |
| 70 | — | Kirk Cousins | MIN | 24.1 | QB1 | Healthy |  |  |
| 69 | — | Jared Goff | DET | 23.1 | QB1 | Healthy |  |  |
| 69 | — | Jordan Love | GB | 24.3 | QB1 | Healthy | BYE |  |
| 67 | — | Caleb Williams | CHI | 21.9 | QB1 | Healthy |  |  |
| 58 GUESS (57.5) | — | Drew Lock | SEA | 20.5 | QB1 | Healthy | BYE | SF QB1 floor 45; GUESS inputs |
| 58 | — | Tyler Shough | NO | 21.4 | QB1 | Healthy |  |  |
| 55 | — | Bo Nix | DEN | 17.4 | QB1 | Healthy |  |  |
| 55 | — | Bryce Young | CAR | 19.3 | QB1 | Healthy |  |  |
| 52 | — | Cam Ward | TEN | 19.5 | QB1 | Healthy |  |  |
| 52 | — | Matthew Stafford | LAR | 21.1 | QB1 | Healthy | BYE |  |
| 47 | -1 | Aaron Rodgers | PIT | 17.9 | QB1 | Healthy |  |  |
| 45 GUESS (45) | — | Carson Wentz | MIN | 2.8 | QB1 | Healthy |  | SF QB1 floor 45; GUESS inputs |
| 45 | — | Daniel Jones | IND | 11.1 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 16.7 | QB1 | Healthy | BYE |  |
| 45 | — | Fernando Mendoza | LV | 13.9 | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 12.5 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 10.6 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 13.3 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 16.9 | QB1 | Healthy | BYE |  |
| 39 GUESS (39.17) | — | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.75; GUESS inputs |
| 34 | — | Geno Smith | NYJ | 16.2 | QB1 | Questionable |  |  |
| 33 | -1 | Drake Maye | NE | 22.9 | QB1 | Out | BYE |  |
| 30 | +4 | Baker Mayfield | TB | 10.2 | QB1 | Questionable |  |  |
| 28 GUESS (27.77) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |
| 28 | — | Sam Darnold | SEA | 17.3 | QB1 | Out | BYE |  |
| 21 GUESS (21.1) | -1 | Kyler Murray | MIN | 14.4 | QB1 | Out |  | Out x0.65; buy-low: volume > points; GUESS inputs |
| 19 GUESS (18.68) | — | Malik Willis | MIA | 13.3 | QB1 | IR |  | IR x0.75; buy-low: volume > points; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jahmyr Gibbs | DET | 25.9 | RB1 | Healthy |  |  |
| 94 | — | James Cook III | BUF | 18.2 | RB1 | Healthy |  |  |
| 90 | +1 | Bijan Robinson | ATL | 18.0 | RB1 | Healthy | BYE |  |
| 88 | — | Bucky Irving | TB | 16.5 | RB1 | Healthy |  |  |
| 88 | — | Christian McCaffrey | SF | 21.4 | RB1 | Healthy |  |  |
| 88 | — | Chuba Hubbard | CAR | 18.4 | RB1 | Healthy |  |  |
| 88 | — | Kenneth Walker III | KC | 22.9 | RB1 | Questionable |  |  |
| 81 | — | Tony Pollard | TEN | 15.8 | RB1 | Healthy |  |  |
| 79 | — | Derrick Henry | BAL | 15.3 | RB1 | Healthy |  |  |
| 79 | — | Jonathan Taylor | IND | 15.2 | RB1 | Healthy |  |  |
| 78 | — | D'Andre Swift | CHI | 15.8 | RB1 | Healthy |  |  |
| 78 | +1 | Javonte Williams | DAL | 15.5 | RB1 | Healthy |  |  |
| 75 | — | Bhayshul Tuten | JAX | 15.4 | RB1 | Questionable |  |  |
| 75 | — | Jaylen Warren | PIT | 15.0 | RB1 | Healthy |  |  |
| 73 | — | Cam Skattebo | NYG | 11.3 | RB1 | Healthy |  |  |
| 73 | +1 | Chase Brown | CIN | 11.8 | RB1 | Healthy |  |  |
| 66 | +1 | Ashton Jeanty | LV | 12.7 | RB1 | Healthy |  |  |
| 66 | — | Kyren Williams | LAR | 14.5 | RB1-split | Healthy | BYE |  |
| 63 | +1 | Ollie Gordon II | MIA | 12.7 | RB1 | Healthy |  |  |
| 63 | — | Quinshon Judkins | CLE | 10.6 | RB1 | Healthy | BYE |  |
| 57 | — | Saquon Barkley | PHI | 7.9 | RB1-split | Healthy |  |  |
| 56 | — | Omarion Hampton | LAC | 8.9 | RB1 | Healthy |  |  |
| 55 | — | Aaron Jones Sr. | MIN | 9.7 | RB1 | Healthy |  |  |
| 52 | +1 | Rhamondre Stevenson | NE | 10.2 | RB1-split | Healthy | BYE |  |
| 48 | — | Braelon Allen | NYJ | 10.7 | RB1 | Healthy |  |  |
| 36 | -1 | Tyler Allgeier | ARI | 8.1 | RB1-split | Healthy |  |  |
| 31 | — | J.K. Dobbins | DEN | 6.4 | RB1 | Healthy |  |  |
| 30 | — | Alvin Kamara | NO | 9.5 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 10.9 | committee | Healthy | BYE |  |
| 30 | — | Breece Hall | NYJ | 12.1 | committee | Healthy |  |  |
| 30 | — | David Montgomery | HOU | 8.4 | committee | Healthy |  |  |
| 30 | — | Emmett Johnson | KC | 9.5 | committee | Healthy |  |  |
| 30 | — | Jonah Coleman | DEN | 14.4 | committee | Healthy |  |  |
| 30 | — | Jordan Mason | MIN | 6.4 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 12.8 | committee | Out | BYE |  |
| 30 | — | Rachaad White | WAS | 9.6 | committee | Healthy |  |  |
| 30 | — | Travis Etienne Jr. | NO | 7.6 | committee | Healthy |  |  |
| 30 | — | Zach Charbonnet | SEA | 7.6 | committee | Healthy | BYE |  |
| 28 | — | Jadarian Price | SEA | 6.5 | committee | Healthy | BYE |  |
| 27 | — | Rico Dowdle | PIT | 4.3 | committee | Healthy |  |  |
| 27 | — | Woody Marks | HOU | 7.4 | RB1 | Out |  |  |
| 23 | +1 | Chris Rodriguez Jr. | JAX | 5.9 | committee | Questionable |  |  |
| 21 GUESS (20.67) | — | RJ Harvey | DEN | 9.2 | committee | IR |  | IR x0.75; committee RB 14% cap 30; GUESS inputs |
| 18 | -1 | Corey Kiner | NE | 2.5 | committee | Healthy | BYE |  |
| 18 | — | Kimani Vidal | LAC | 4.0 | committee | Healthy |  |  |
| 17 | — | Kaleb Johnson | GB | 3.7 | committee | Healthy | BYE |  |
| 16 GUESS (15.61) | — | TreVeyon Henderson | NE | 5.2 | committee | IR | BYE | IR x0.75; committee RB 23% cap 30; GUESS inputs |
| 15 GUESS (15.1) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 17% cap 30; GUESS inputs |
| 14 | — | Audric Estime | NO | 1.6 | committee | Healthy |  |  |
| 11 GUESS (11) | — | Brian Robinson Jr. | ATL | 2.2 | committee | IR | BYE | IR x0.75; committee RB 22% cap 30; GUESS inputs |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 22.4 | WR1 | Healthy | BYE |  |
| 94 | -1 | Amon-Ra St. Brown | DET | 16.8 | WR1 | Healthy |  |  |
| 94 | — | CeeDee Lamb | DAL | 18.4 | WR1 | Healthy |  |  |
| 94 | — | Ja'Marr Chase | CIN | 18.0 | WR1 | Healthy |  |  |
| 84 | — | Tee Higgins | CIN | 16.1 | WR2 | Healthy |  |  |
| 83 | — | Justin Jefferson | MIN | 11.4 | WR1 | Healthy |  |  |
| 82 | — | Parker Washington | JAX | 13.3 | WR1 | Healthy |  |  |
| 81 | -1 | Matthew Golden | GB | 14.7 | WR2 | Healthy | BYE |  |
| 80 | -1 | Chris Olave | NO | 13.1 | WR1 | Healthy |  |  |
| 79 | -1 | Christian Watson | GB | 15.8 | WR1 | Healthy | BYE |  |
| 79 | — | Malik Nabers | NYG | 12.0 | WR1 | Healthy |  |  |
| 76 | -1 | Luther Burden III | CHI | 12.4 | WR1 | Healthy |  |  |
| 75 | -1 | Nico Collins | HOU | 13.9 | WR1 | Healthy |  |  |
| 74 | -1 | Tetairoa McMillan | CAR | 11.8 | WR1 | Healthy |  |  |
| 73 | — | Zay Flowers | BAL | 12.7 | WR1 | Healthy |  |  |
| 69 | — | Drake London | ATL | 11.3 | WR1 | Questionable | BYE |  |
| 66 | — | Garrett Wilson | NYJ | 11.6 | WR1 | Healthy |  |  |
| 66 | -1 | George Pickens | DAL | 13.6 | WR2 | Healthy |  |  |
| 63 | — | DeVonta Smith | PHI | 14.0 | WR1 | Questionable |  |  |
| 61 | +1 | Stefon Diggs | WAS | 11.6 | WR1 | Healthy |  |  |
| 60 | -1 | Mike Evans | SF | 12.6 | WR2 | Questionable |  |  |
| 56 | -1 | Emeka Egbuka | TB | 8.9 | WR1 | Healthy |  |  |
| 56 | -1 | Jameson Williams | DET | 11.0 | WR2 | Healthy |  |  |
| 53 | -1 | Ryan Flournoy | DAL | 16.1 | WR | Healthy |  |  |
| 52 | -2 | DJ Moore | BUF | 9.6 | WR1 | Healthy |  |  |
| 52 GUESS (51.56) | — | Puka Nacua | LAR | 19.8 | WR | IR | BYE | IR x0.75; GUESS inputs |
| 51 | -1 | DK Metcalf | PIT | 8.4 | WR1 | Healthy |  |  |
| 51 | -1 | Rashee Rice | KC | 9.2 | WR1 | Healthy |  |  |
| 50 | — | KC Concepcion Jr. | CLE | 10.7 | WR2 | Healthy | BYE |  |
| 50 | -1 | Malik Washington | MIA | 9.8 | WR2 | Healthy |  |  |
| 48 | — | Jalen Coker | CAR | 8.8 | WR2 | Healthy |  |  |
| 48 | -1 | Rome Odunze | CHI | 8.1 | WR2 | Healthy |  |  |
| 47 GUESS (47.14) | -1 | Michael Wilson | ARI | 10.6 | WR | IR |  | IR x0.75; buy-low: volume > points; GUESS inputs |
| 45 | -1 | Jaylen Waddle | DEN | 7.4 | WR1 | Questionable |  |  |
| 40 | — | Josh Downs | KC | 8.0 | WR2 | Healthy |  |  |
| 38 | -1 | Khalil Shakir | BUF | 6.5 | WR2 | Healthy |  |  |
| 37 | -1 | Denzel Boston | CLE | 6.7 | WR1 | Healthy | BYE |  |
| 37 | — | Ladd McConkey | LAC | 7.2 | WR1 | Questionable |  |  |
| 33 | -1 | Courtland Sutton | DEN | 5.7 | WR2 | Healthy |  |  |
| 33 | -1 | Makai Lemon | PHI | 6.1 | WR | Healthy |  |  |
| 32 | -1 | Germie Bernard | PIT | 7.7 | WR2 | Healthy |  |  |
| 31 | -1 | DeMario Douglas | NE | 8.1 | WR2 | Healthy | BYE |  |
| 31 | -1 | Tre Tucker | LV | 6.9 | WR1 | Healthy |  |  |
| 30 GUESS (29.61) | — | Davante Adams | LAR | 14.5 | WR | IR | BYE | IR x0.50; GUESS inputs |
| 26 | — | Omar Cooper Jr. | NYJ | 7.5 | WR | Questionable |  |  |
| 24 | -2 | Keon Coleman | BUF | 5.4 | WR | Healthy |  |  |
| 22 | -1 | Xavier Worthy | KC | 5.2 | WR | Healthy |  |  |
| 19 | — | A.J. Brown | NE | 4.6 | WR1 | Out | BYE |  |
| 19 | -1 | Adonai Mitchell | NYJ | 3.7 | WR2 | Healthy |  |  |
| 17 | -1 | Jordan Addison | MIN | 6.4 | WR | Out |  |  |
| 17 | -1 | Rashod Bateman | BAL | 5.7 | WR | Healthy |  |  |
| 15 | -1 | Brian Thomas Jr. | JAX | 3.7 | WR | Healthy |  |  |
| 12 | -1 | Tank Dell | HOU | 4.3 | WR | Healthy |  |  |
| 11 | -1 | Jerry Jeudy | CLE | 3.8 | WR | Healthy | BYE |  |
| 9 | -1 | Marvin Harrison Jr. | HOU | 4.6 | WR | Out |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | — | Brock Bowers | LV | 15.6 | TE1 | Questionable |  |  |
| 86 | — | Isaiah Likely | NYG | 13.2 | TE1 | Healthy |  |  |
| 86 | — | Trey McBride | ARI | 13.2 | TE1 | Healthy |  |  |
| 78 | — | George Kittle | SF | 11.7 | TE1 | Healthy |  |  |
| 60 | — | Sam LaPorta | DET | 8.6 | TE1 | Healthy |  |  |
| 58 | — | Travis Kelce | KC | 9.6 | TE1 | Healthy |  |  |
| 56 | — | Harold Fannin Jr. | CLE | 8.7 | TE1 | Healthy | BYE |  |
| 52 | — | Colston Loveland | CHI | 7.2 | TE1 | Healthy |  |  |
| 51 | — | Tyler Warren | IND | 8.3 | TE1 | Healthy |  |  |
| 50 | — | T.J. Hockenson | MIN | 8.0 | TE1 | Questionable |  |  |
| 46 | — | Dalton Kincaid | BUF | 8.5 | TE1 | Questionable |  |  |
| 41 | — | Brenton Strange | JAX | 7.9 | TE1 | Healthy |  |  |
| 31 | — | Tucker Kraft | GB | 7.5 | TE1 | Healthy | BYE |  |
| 24 | — | Dallas Goedert | PHI | 6.1 | TE1 | Healthy |  |  |
| 18 | — | Kyle Pitts Sr. | ATL | 6.3 | TE1 | Healthy | BYE |  |
| 8 | — | Pat Freiermuth | PIT | 2.1 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Davante Adams | WR | 30 | 83 | 53 | IR x0.50; GUESS inputs |
| Puka Nacua | WR | 52 | 98 | 46 | IR x0.75; GUESS inputs |
| Carson Wentz | QB | 45 | 0 | 45 | SF QB1 floor 45; GUESS inputs |
| Jonah Coleman | RB | 30 | 69 | 39 | committee RB 27% cap 30 |
| Jacoby Brissett | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Drake Maye | QB | 33 | 71 | 38 | Out x0.65 |
| Josh Jacobs | RB | 30 | 67 | 37 | Out x0.65; committee RB 19% cap 30 |
| Ryan Flournoy | WR | 53 | 90 | 37 | proj 44 / prod 90 / role 20 |
| Daniel Jones | QB | 45 | 9 | 36 | SF QB1 floor 45; buy-low: volume > points |
| J.J. McCarthy | QB | 45 | 12 | 33 | SF QB1 floor 45; buy-low: volume > points |
| Colston Loveland | TE | 52 | 20 | 32 | buy-low: volume > points |
| Breece Hall | RB | 30 | 61 | 31 | committee RB 35% cap 30 |
| Justin Herbert | QB | 45 | 18 | 27 | SF QB1 floor 45; buy-low: volume > points |
| Baker Mayfield | QB | 30 | 3 | 27 | Questionable x0.95; buy-low: volume > points |
| Saquon Barkley | RB | 57 | 31 | 26 | proj 65 / prod 31 / role 49 |
