# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-18 07:01 AM EST

- **NFL week:** 11
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-18 week 11 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | — | Joe Burrow | CIN | 32.5 | QB1 | Healthy |  |  |
| 85 | — | Josh Allen | BUF | 28.4 | QB1 | Healthy |  |  |
| 80 | — | Brock Purdy | SF | 27.6 | QB1 | Healthy |  |  |
| 77 | — | Patrick Mahomes | KC | 24.4 | QB1 | Healthy |  |  |
| 77 | — | Trevor Lawrence | JAX | 24.6 | QB1 | Healthy |  |  |
| 73 | — | C.J. Stroud | HOU | 25.1 | QB1 | Healthy |  |  |
| 71 | — | Jayden Daniels | WAS | 22.6 | QB1 | Healthy |  |  |
| 70 | -2 | Dak Prescott | DAL | 25.0 | QB1 | Healthy |  |  |
| 69 | +1 | Kirk Cousins | MIN | 24.1 | QB1 | Healthy |  |  |
| 68 | — | Jared Goff | DET | 23.1 | QB1 | Healthy |  |  |
| 68 | -1 | Jordan Love | GB | 24.3 | QB1 | Healthy | BYE |  |
| 66 | +5 | Caleb Williams | CHI | 21.9 | QB1 | Healthy |  |  |
| 57 GUESS (56.67) | +12 | Drew Lock | SEA | 20.5 | QB1 | Healthy | BYE | +12 vs last board; SF QB1 floor 45; GUESS inputs |
| 57 | -3 | Tyler Shough | NO | 21.4 | QB1 | Healthy |  |  |
| 55 | +6 | Bo Nix | DEN | 17.4 | QB1 | Healthy |  |  |
| 54 | -2 | Bryce Young | CAR | 19.3 | QB1 | Healthy |  |  |
| 51 | -1 | Matthew Stafford | LAR | 21.1 | QB1 | Healthy | BYE |  |
| 50 | -2 | Cam Ward | TEN | 19.5 | QB1 | Healthy |  |  |
| 47 | -1 | Aaron Rodgers | PIT | 17.9 | QB1 | Healthy |  |  |
| 45 GUESS (45) | — | Carson Wentz | MIN | 2.8 | QB1 | Healthy |  | SF QB1 floor 45; GUESS inputs |
| 45 | — | Daniel Jones | IND | 11.1 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 16.7 | QB1 | Healthy | BYE |  |
| 45 | — | Fernando Mendoza | LV | 13.9 | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 12.5 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 10.6 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 13.3 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 16.9 | QB1 | Healthy | BYE |  |
| 39 GUESS (38.78) | -2 | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.75; GUESS inputs |
| 38 | -2 | Drake Maye | NE | 22.9 | QB1 | Out | BYE |  |
| 33 | +8 | Geno Smith | NYJ | 16.2 | QB1 | Questionable |  | +8 vs last board; Questionable x0.95; buy-low: volume > points |
| 27 GUESS (27.44) | -2 | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |
| 27 | +3 | Sam Darnold | SEA | 17.3 | QB1 | Out | BYE |  |
| 26 | -1 | Baker Mayfield | TB | 10.2 | QB1 | Questionable |  |  |
| 25 GUESS (25) | — | Shedeur Sanders | CLE | 26.7 | QB2 | Healthy | BYE | backup QB cap 25; GUESS inputs |
| 22 GUESS (21.74) | -1 | Kyler Murray | MIN | 14.4 | QB1 | Out |  | Out x0.65; buy-low: volume > points; GUESS inputs |
| 19 GUESS (18.78) | -1 | Malik Willis | MIA | 13.3 | QB1 | IR |  | IR x0.75; buy-low: volume > points; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jahmyr Gibbs | DET | 25.9 | RB1 | Healthy |  |  |
| 94 | — | James Cook III | BUF | 18.2 | RB1 | Healthy |  |  |
| 89 | -1 | Bijan Robinson | ATL | 18.0 | RB1 | Healthy | BYE |  |
| 88 | +2 | Bucky Irving | TB | 16.5 | RB1 | Healthy |  |  |
| 88 | — | Christian McCaffrey | SF | 21.4 | RB1 | Healthy |  |  |
| 88 | — | Chuba Hubbard | CAR | 18.4 | RB1 | Healthy |  |  |
| 88 | +29 | Kenneth Walker III | KC | 22.9 | RB1 | Questionable |  | +29 vs last board; Questionable x0.95 |
| 81 | +1 | Tony Pollard | TEN | 15.8 | RB1 | Healthy |  |  |
| 79 | -1 | Bhayshul Tuten | JAX | 15.4 | RB1 | Healthy |  |  |
| 79 | -2 | Derrick Henry | BAL | 15.3 | RB1 | Healthy |  |  |
| 79 | — | Jonathan Taylor | IND | 15.2 | RB1 | Healthy |  |  |
| 78 | +2 | D'Andre Swift | CHI | 15.8 | RB1 | Healthy |  |  |
| 76 | -3 | Javonte Williams | DAL | 15.5 | RB1 | Healthy |  |  |
| 76 | — | Jaylen Warren | PIT | 15.0 | RB1 | Healthy |  |  |
| 73 | -1 | Cam Skattebo | NYG | 11.3 | RB1 | Healthy |  |  |
| 72 | +1 | Chase Brown | CIN | 11.8 | RB1 | Healthy |  |  |
| 66 | -3 | Kyren Williams | LAR | 14.5 | RB1-split | Healthy | BYE |  |
| 65 | -1 | Ashton Jeanty | LV | 12.7 | RB1 | Healthy |  |  |
| 63 | — | Quinshon Judkins | CLE | 10.6 | RB1 | Healthy | BYE |  |
| 62 | -1 | Ollie Gordon II | MIA | 12.7 | RB1 | Healthy |  |  |
| 57 | +1 | Saquon Barkley | PHI | 7.9 | RB1-split | Healthy |  |  |
| 56 | +3 | Omarion Hampton | LAC | 8.9 | RB1 | Healthy |  |  |
| 55 | — | Aaron Jones Sr. | MIN | 9.7 | RB1 | Healthy |  |  |
| 51 | — | Rhamondre Stevenson | NE | 10.2 | RB1-split | Healthy | BYE |  |
| 48 | +1 | Braelon Allen | NYJ | 10.7 | RB1 | Healthy |  |  |
| 37 | +1 | Tyler Allgeier | ARI | 8.1 | RB1-split | Healthy |  |  |
| 33 | +5 | Woody Marks | HOU | 7.4 | RB1 | Doubtful |  |  |
| 31 | +1 | J.K. Dobbins | DEN | 6.4 | RB1 | Healthy |  |  |
| 30 | — | Alvin Kamara | NO | 9.5 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 10.9 | committee | Healthy | BYE |  |
| 30 | — | Breece Hall | NYJ | 12.1 | committee | Healthy |  |  |
| 30 | — | Emmett Johnson | KC | 9.5 | committee | Healthy |  |  |
| 30 | — | Jonah Coleman | DEN | 14.4 | committee | Healthy |  |  |
| 30 | — | Jordan Mason | MIN | 6.4 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 12.8 | committee | Out | BYE |  |
| 30 | — | Rachaad White | WAS | 9.6 | committee | Healthy |  |  |
| 30 | — | Travis Etienne Jr. | NO | 7.6 | committee | Healthy |  |  |
| 30 | — | Zach Charbonnet | SEA | 7.6 | committee | Healthy | BYE |  |
| 28 | — | Jadarian Price | SEA | 6.5 | committee | Healthy | BYE |  |
| 27 | — | Rico Dowdle | PIT | 4.3 | committee | Healthy |  |  |
| 24 | — | Chris Rodriguez Jr. | JAX | 5.9 | committee | Healthy |  |  |
| 21 GUESS (20.51) | — | RJ Harvey | DEN | 9.2 | committee | IR |  | IR x0.75; committee RB 14% cap 30; GUESS inputs |
| 19 | — | Corey Kiner | NE | 2.5 | committee | Healthy | BYE |  |
| 18 | -1 | Kimani Vidal | LAC | 4.0 | committee | Healthy |  |  |
| 17 | — | Kaleb Johnson | GB | 3.7 | committee | Healthy | BYE |  |
| 16 GUESS (15.73) | — | TreVeyon Henderson | NE | 5.2 | committee | IR | BYE | IR x0.75; committee RB 23% cap 30; GUESS inputs |
| 15 GUESS (15.27) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 17% cap 30; GUESS inputs |
| 14 | — | Audric Estime | NO | 1.6 | committee | Healthy |  |  |
| 11 GUESS (11.07) | — | Brian Robinson Jr. | ATL | 2.2 | committee | IR | BYE | IR x0.75; committee RB 22% cap 30; GUESS inputs |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 22.4 | WR1 | Healthy | BYE |  |
| 95 | — | Amon-Ra St. Brown | DET | 16.8 | WR1 | Healthy |  |  |
| 95 | -1 | CeeDee Lamb | DAL | 18.4 | WR1 | Healthy |  |  |
| 94 | — | Ja'Marr Chase | CIN | 18.0 | WR1 | Healthy |  |  |
| 84 | — | Tee Higgins | CIN | 16.1 | WR2 | Healthy |  |  |
| 83 | +1 | Justin Jefferson | MIN | 11.4 | WR1 | Healthy |  |  |
| 82 | -2 | Matthew Golden | GB | 14.7 | WR2 | Healthy | BYE |  |
| 82 | — | Parker Washington | JAX | 13.3 | WR1 | Healthy |  |  |
| 81 | — | Chris Olave | NO | 13.1 | WR1 | Healthy |  |  |
| 80 | — | Christian Watson | GB | 15.8 | WR1 | Healthy | BYE |  |
| 79 | -1 | Malik Nabers | NYG | 12.0 | WR1 | Healthy |  |  |
| 77 | +8 | Luther Burden III | CHI | 12.4 | WR1 | Healthy |  | +8 vs last board |
| 76 | — | Nico Collins | HOU | 13.9 | WR1 | Healthy |  |  |
| 75 | -1 | Tetairoa McMillan | CAR | 11.8 | WR1 | Healthy |  |  |
| 73 | -2 | Zay Flowers | BAL | 12.7 | WR1 | Healthy |  |  |
| 69 | -1 | Drake London | ATL | 11.3 | WR1 | Questionable | BYE |  |
| 67 | -2 | George Pickens | DAL | 13.6 | WR2 | Healthy |  |  |
| 66 | -2 | Garrett Wilson | NYJ | 11.6 | WR1 | Healthy |  |  |
| 63 | +23 | DeVonta Smith | PHI | 14.0 | WR1 | Questionable |  | +23 vs last board; Questionable x0.95 |
| 61 | +22 | Mike Evans | SF | 12.6 | WR1 | Questionable |  | +22 vs last board; Questionable x0.95 |
| 60 | -1 | Stefon Diggs | WAS | 11.6 | WR1 | Healthy |  |  |
| 57 | +3 | Emeka Egbuka | TB | 8.9 | WR1 | Healthy |  |  |
| 57 | -1 | Jameson Williams | DET | 11.0 | WR2 | Healthy |  |  |
| 54 | -1 | DJ Moore | BUF | 9.6 | WR1 | Healthy |  |  |
| 54 | -2 | Ryan Flournoy | DAL | 16.1 | WR | Healthy |  |  |
| 52 | -3 | DK Metcalf | PIT | 8.4 | WR1 | Healthy |  |  |
| 52 GUESS (51.97) | — | Puka Nacua | LAR | 19.8 | WR | IR | BYE | IR x0.75; GUESS inputs |
| 52 | -1 | Rashee Rice | KC | 9.2 | WR1 | Healthy |  |  |
| 51 | -2 | Malik Washington | MIA | 9.8 | WR2 | Healthy |  |  |
| 50 | -3 | KC Concepcion Jr. | CLE | 10.7 | WR2 | Healthy | BYE |  |
| 49 | +3 | Rome Odunze | CHI | 8.1 | WR2 | Healthy |  |  |
| 48 | — | Jalen Coker | CAR | 8.8 | WR2 | Healthy |  |  |
| 48 GUESS (47.59) | -1 | Michael Wilson | ARI | 10.6 | WR | IR |  | IR x0.75; buy-low: volume > points; GUESS inputs |
| 45 | +16 | Jaylen Waddle | DEN | 7.4 | WR1 | Questionable |  | +16 vs last board; Questionable x0.95; buy-low: volume > points |
| 40 | -1 | Josh Downs | KC | 8.0 | WR2 | Healthy |  |  |
| 39 | -1 | Khalil Shakir | BUF | 6.5 | WR2 | Healthy |  |  |
| 38 | -2 | Denzel Boston | CLE | 6.7 | WR1 | Healthy | BYE |  |
| 38 | +15 | Ladd McConkey | LAC | 7.2 | WR1 | Questionable |  | +15 vs last board; Questionable x0.95 |
| 34 | +1 | Courtland Sutton | DEN | 5.7 | WR2 | Healthy |  |  |
| 34 | +2 | Makai Lemon | PHI | 6.1 | WR | Healthy |  |  |
| 33 | -1 | Germie Bernard | PIT | 7.7 | WR2 | Healthy |  |  |
| 32 | -1 | DeMario Douglas | NE | 8.1 | WR2 | Healthy | BYE |  |
| 32 | — | Tre Tucker | LV | 6.9 | WR1 | Healthy |  |  |
| 30 GUESS (29.92) | +2 | Davante Adams | LAR | 14.5 | WR | IR | BYE | IR x0.50; GUESS inputs |
| 26 | — | Keon Coleman | BUF | 5.4 | WR | Healthy |  |  |
| 26 | +8 | Omar Cooper Jr. | NYJ | 7.5 | WR | Questionable |  | +8 vs last board; Questionable x0.95 |
| 23 | -2 | Xavier Worthy | KC | 5.2 | WR | Healthy |  |  |
| 20 | — | Adonai Mitchell | NYJ | 3.7 | WR2 | Healthy |  |  |
| 19 | -2 | A.J. Brown | NE | 4.6 | WR1 | Out | BYE |  |
| 18 | +1 | Jordan Addison | MIN | 6.4 | WR | Out |  |  |
| 18 | — | Rashod Bateman | BAL | 5.7 | WR | Healthy |  |  |
| 16 | — | Brian Thomas Jr. | JAX | 3.7 | WR | Healthy |  |  |
| 15 | +5 | Marvin Harrison Jr. | HOU | 4.6 | WR | Questionable |  |  |
| 13 | — | Tank Dell | HOU | 4.3 | WR | Healthy |  |  |
| 12 | — | Darius Cooper | PHI | 2.5 | WR | Healthy |  |  |
| 12 | -1 | Jerry Jeudy | CLE | 3.8 | WR | Healthy | BYE |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 86 | +27 | Brock Bowers | LV | 15.6 | TE1 | Questionable |  | +27 vs last board; Questionable x0.95 |
| 85 | +2 | Isaiah Likely | NYG | 13.2 | TE1 | Healthy |  |  |
| 85 | -1 | Trey McBride | ARI | 13.2 | TE1 | Healthy |  |  |
| 77 | -3 | George Kittle | SF | 11.7 | TE1 | Healthy |  |  |
| 57 | -3 | Sam LaPorta | DET | 8.6 | TE1 | Healthy |  |  |
| 56 | +1 | Travis Kelce | KC | 9.6 | TE1 | Healthy |  |  |
| 53 | -10 | Harold Fannin Jr. | CLE | 8.7 | TE1 | Healthy | BYE | -10 vs last board |
| 48 | +8 | Colston Loveland | CHI | 7.2 | TE1 | Healthy |  | +8 vs last board; buy-low: volume > points |
| 48 | +22 | T.J. Hockenson | MIN | 8.0 | TE1 | Questionable |  | +22 vs last board; Questionable x0.95 |
| 47 | -11 | Tyler Warren | IND | 8.3 | TE1 | Healthy |  | -11 vs last board; buy-low: volume > points |
| 45 | -8 | Dalton Kincaid | BUF | 8.5 | TE1 | Healthy |  | -8 vs last board |
| 37 | -6 | Brenton Strange | JAX | 7.9 | TE1 | Healthy |  |  |
| 27 | -9 | Tucker Kraft | GB | 7.5 | TE1 | Healthy | BYE | -9 vs last board |
| 19 | -3 | Dallas Goedert | PHI | 6.1 | TE1 | Healthy |  |  |
| 13 | -5 | Kyle Pitts Sr. | ATL | 6.3 | TE1 | Healthy | BYE |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Shedeur Sanders | QB | 25 | 91 | 66 | backup QB cap 25; GUESS inputs |
| Davante Adams | WR | 30 | 84 | 54 | IR x0.50; GUESS inputs |
| Puka Nacua | WR | 52 | 98 | 46 | IR x0.75; GUESS inputs |
| Carson Wentz | QB | 45 | 0 | 45 | SF QB1 floor 45; GUESS inputs |
| Jacoby Brissett | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Jonah Coleman | RB | 30 | 69 | 39 | committee RB 27% cap 30 |
| Josh Jacobs | RB | 30 | 67 | 37 | Out x0.65; committee RB 19% cap 30 |
| Daniel Jones | QB | 45 | 9 | 36 | SF QB1 floor 45; buy-low: volume > points |
| Ryan Flournoy | WR | 54 | 90 | 36 | proj 45 / prod 90 / role 22 |
| Colston Loveland | TE | 48 | 14 | 34 | +8 vs last board; buy-low: volume > points |
| J.J. McCarthy | QB | 45 | 11 | 34 | SF QB1 floor 45; buy-low: volume > points |
| Drake Maye | QB | 38 | 69 | 31 | Out x0.65 |
| Breece Hall | RB | 30 | 60 | 30 | committee RB 35% cap 30 |
| Justin Herbert | QB | 45 | 17 | 28 | SF QB1 floor 45; buy-low: volume > points |
| Saquon Barkley | RB | 57 | 31 | 26 | proj 65 / prod 31 / role 48 |
