# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-16 07:00 AM EST

- **NFL week:** 10
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-16 week 10 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | — | Joe Burrow | CIN | 31.4 | QB1 | Healthy |  |  |
| 87 | — | Josh Allen | BUF | 28.8 | QB1 | Healthy |  |  |
| 80 | — | Brock Purdy | SF | 26.3 | QB1 | Healthy |  |  |
| 75 | — | Trevor Lawrence | JAX | 23.4 | QB1 | Healthy |  |  |
| 72 | — | Jordan Love | GB | 25.4 | QB1 | Healthy |  |  |
| 72 | — | Kirk Cousins | MIN | 24.5 | QB1 | Healthy |  |  |
| 72 | — | Patrick Mahomes | KC | 21.8 | QB1 | Healthy |  |  |
| 71 | +1 | C.J. Stroud | HOU | 24.8 | QB1 | Healthy |  |  |
| 69 | — | Jared Goff | DET | 22.4 | QB1 | Healthy |  |  |
| 67 | — | Jayden Daniels | WAS | 21.5 | QB1 | Healthy |  |  |
| 65 | — | Dak Prescott | DAL | 22.7 | QB1 | Healthy |  |  |
| 64 | — | Tyler Shough | NO | 22.4 | QB1 | Healthy |  |  |
| 61 | — | Caleb Williams | CHI | 21.9 | QB1 | Healthy | BYE |  |
| 59 | — | Bryce Young | CAR | 20.9 | QB1 | Healthy |  |  |
| 50 | — | Cam Ward | TEN | 17.9 | QB1 | Healthy |  |  |
| 50 | — | Drake Maye | NE | 25.1 | QB1 | Out |  |  |
| 49 | — | Bo Nix | DEN | 17.4 | QB1 | Healthy | BYE |  |
| 49 | — | Matthew Stafford | LAR | 20.4 | QB1 | Healthy |  |  |
| 47 | — | Aaron Rodgers | PIT | 17.5 | QB1 | Healthy |  |  |
| 45 GUESS (45) | — | Carson Wentz | MIN | 2.8 | QB1 | Healthy |  | SF QB1 floor 45; GUESS inputs |
| 45 | — | Daniel Jones | IND | 11.4 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 15.7 | QB1 | Healthy |  |  |
| 45 | — | Drew Lock | SEA | 21.0 | QB1 | Healthy |  |  |
| 45 | — | Fernando Mendoza | LV | — | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 8.7 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 10.1 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 13.0 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 17.5 | QB1 | Healthy |  |  |
| 42 GUESS (42.01) | — | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.78; GUESS inputs |
| 29 GUESS (28.91) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR | BYE | IR x0.50; GUESS inputs |
| 28 | — | Baker Mayfield | TB | 10.2 | QB1 | Questionable | BYE |  |
| 27 | — | Geno Smith | NYJ | 17.5 | QB1 | Out |  |  |
| 25 GUESS (25) | — | Shedeur Sanders | CLE | 26.7 | QB2 | Healthy |  | backup QB cap 25; GUESS inputs |
| 23 GUESS (23.24) | — | Kyler Murray | MIN | 14.4 | QB1 | Out |  | Out x0.65; buy-low: volume > points; GUESS inputs |
| 23 | — | Sam Darnold | SEA | 17.3 | QB1 | Out |  |  |
| 22 GUESS (21.56) | — | Malik Willis | MIA | 13.3 | QB1 | IR |  | IR x0.78; buy-low: volume > points; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jahmyr Gibbs | DET | 24.0 | RB1 | Healthy |  |  |
| 94 | — | James Cook III | BUF | 17.8 | RB1 | Healthy |  |  |
| 90 | — | Bijan Robinson | ATL | 18.3 | RB1 | Healthy |  |  |
| 88 | — | Christian McCaffrey | SF | 18.6 | RB1 | Healthy |  |  |
| 87 | — | Chuba Hubbard | CAR | 16.7 | RB1 | Healthy |  |  |
| 86 | — | Bucky Irving | TB | 16.5 | RB1 | Healthy | BYE |  |
| 82 | — | Jaylen Warren | PIT | 16.0 | RB1 | Healthy |  |  |
| 80 | — | Javonte Williams | DAL | 16.4 | RB1 | Healthy |  |  |
| 80 | — | Jonathan Taylor | IND | 15.6 | RB1 | Healthy |  |  |
| 79 | — | Derrick Henry | BAL | 15.1 | RB1 | Healthy |  |  |
| 78 | — | Bhayshul Tuten | JAX | 15.0 | RB1 | Healthy |  |  |
| 77 | — | D'Andre Swift | CHI | 15.8 | RB1 | Healthy | BYE |  |
| 77 | — | Tony Pollard | TEN | 15.2 | RB1 | Healthy |  |  |
| 75 | — | Kyren Williams | LAR | 15.7 | RB1 | Healthy |  |  |
| 67 | — | Ashton Jeanty | LV | 13.1 | RB1 | Healthy |  |  |
| 67 | — | Chase Brown | CIN | 10.2 | RB1 | Healthy |  |  |
| 65 | — | Ollie Gordon II | MIA | 12.5 | RB1 | Healthy |  |  |
| 64 | — | Cam Skattebo | NYG | 9.3 | RB1 | Healthy |  |  |
| 61 | — | Kenneth Walker III | KC | 22.9 | RB1 | Out |  |  |
| 61 | — | Quinshon Judkins | CLE | 10.1 | RB1 | Healthy |  |  |
| 56 | — | Rhamondre Stevenson | NE | 11.2 | RB1-split | Healthy |  |  |
| 56 | — | Saquon Barkley | PHI | 7.9 | RB1-split | Healthy | BYE |  |
| 54 | — | Aaron Jones Sr. | MIN | 9.4 | RB1 | Healthy |  |  |
| 52 | +1 | Braelon Allen | NYJ | 11.4 | RB1 | Healthy |  |  |
| 47 | +1 | Omarion Hampton | LAC | 7.8 | RB1 | Healthy |  |  |
| 40 | — | Tyler Allgeier | ARI | 8.8 | RB1-split | Healthy |  |  |
| 30 | — | Alvin Kamara | NO | 8.7 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 10.0 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 11.9 | committee | Healthy |  |  |
| 30 | — | Chris Rodriguez Jr. | JAX | 6.5 | committee | Healthy |  |  |
| 30 | +1 | Emmett Johnson | KC | 6.7 | committee | Healthy |  |  |
| 30 | — | Jonah Coleman | DEN | 14.4 | committee | Healthy | BYE |  |
| 30 | — | Jordan Mason | MIN | 6.5 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 12.8 | committee | Out |  |  |
| 30 | — | Rachaad White | WAS | 10.9 | committee | Healthy |  |  |
| 30 | — | Travis Etienne Jr. | NO | 8.5 | committee | Healthy |  |  |
| 30 | — | Zach Charbonnet | SEA | 6.8 | committee | Healthy |  |  |
| 29 | — | J.K. Dobbins | DEN | 6.4 | RB1 | Healthy | BYE |  |
| 27 | — | Rico Dowdle | PIT | 4.2 | committee | Healthy |  |  |
| 26 | -2 | Woody Marks | HOU | 7.5 | RB1 | Out |  |  |
| 24 | — | Jadarian Price | SEA | 5.5 | committee | Healthy |  |  |
| 21 GUESS (21.48) | — | RJ Harvey | DEN | 9.2 | committee | IR | BYE | IR x0.78; committee RB 14% cap 30; GUESS inputs |
| 20 | — | Kimani Vidal | LAC | 4.5 | committee | Healthy |  |  |
| 18 | — | Corey Kiner | NE | — | committee | Healthy |  |  |
| 16 GUESS (16.33) | — | TreVeyon Henderson | NE | 5.2 | committee | IR |  | IR x0.78; committee RB 25% cap 30; GUESS inputs |
| 15 GUESS (15.18) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 19% cap 30; GUESS inputs |
| 14 | — | Kaleb Johnson | GB | 3.2 | committee | Healthy |  |  |
| 13 | -1 | Audric Estime | NO | — | committee | Healthy |  |  |
| 12 GUESS (12.15) | — | Brian Robinson Jr. | ATL | 2.2 | committee | IR |  | IR x0.78; committee RB 23% cap 30; GUESS inputs |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 21.8 | WR1 | Healthy |  |  |
| 95 | — | CeeDee Lamb | DAL | 18.5 | WR1 | Healthy |  |  |
| 94 | — | Amon-Ra St. Brown | DET | 15.9 | WR1 | Healthy |  |  |
| 92 | — | Ja'Marr Chase | CIN | 16.6 | WR1 | Healthy |  |  |
| 87 | — | Tee Higgins | CIN | 17.0 | WR2 | Healthy |  |  |
| 86 | -1 | Chris Olave | NO | 14.2 | WR1 | Healthy |  |  |
| 84 | — | Malik Nabers | NYG | 12.9 | WR1 | Healthy |  |  |
| 84 | — | Matthew Golden | GB | 15.3 | WR2 | Healthy |  |  |
| 83 | +1 | Christian Watson | GB | 16.9 | WR1 | Healthy |  |  |
| 81 | -1 | Justin Jefferson | MIN | 11.4 | WR1 | Healthy |  |  |
| 79 | — | Tetairoa McMillan | CAR | 12.7 | WR1 | Healthy |  |  |
| 79 | — | Zay Flowers | BAL | 13.2 | WR1 | Healthy |  |  |
| 77 | — | Parker Washington | JAX | 11.9 | WR1 | Healthy |  |  |
| 71 | — | Drake London | ATL | 11.1 | WR1 | Questionable |  |  |
| 69 | — | Garrett Wilson | NYJ | 11.5 | WR1 | Healthy |  |  |
| 69 | — | Luther Burden III | CHI | 12.4 | WR1 | Questionable | BYE |  |
| 69 | — | Nico Collins | HOU | 12.9 | WR1 | Healthy |  |  |
| 60 | — | Jameson Williams | DET | 11.5 | WR2 | Healthy |  |  |
| 57 | — | Stefon Diggs | WAS | 10.8 | WR1 | Healthy |  |  |
| 56 | — | George Pickens | DAL | 10.6 | WR2 | Healthy |  |  |
| 56 | — | Jalen Coker | CAR | 10.1 | WR2 | Healthy |  |  |
| 56 | — | KC Concepcion Jr. | CLE | 11.0 | WR2 | Healthy |  |  |
| 55 | — | DK Metcalf | PIT | 7.7 | WR1 | Healthy |  |  |
| 53 | — | Emeka Egbuka | TB | 8.9 | WR1 | Healthy | BYE |  |
| 53 GUESS (53.35) | — | Puka Nacua | LAR | 19.8 | WR | IR |  | IR x0.78; GUESS inputs |
| 52 | — | Rashee Rice | KC | 8.9 | WR1 | Healthy |  |  |
| 51 GUESS (51.39) | — | Michael Wilson | ARI | 10.6 | WR | IR |  | IR x0.78; buy-low: volume > points; GUESS inputs |
| 49 | +2 | Malik Washington | MIA | 7.8 | WR2 | Healthy |  |  |
| 48 | — | Denzel Boston | CLE | 7.6 | WR1 | Healthy |  |  |
| 47 | — | DJ Moore | BUF | 8.3 | WR1 | Healthy |  |  |
| 46 | — | Rome Odunze | CHI | 8.1 | WR2 | Healthy | BYE |  |
| 43 | — | Germie Bernard | PIT | 10.0 | WR2 | Healthy |  |  |
| 41 | — | DeVonta Smith | PHI | 14.0 | WR | Out | BYE |  |
| 40 | — | Mike Evans | SF | 12.6 | WR | Out |  |  |
| 38 | — | DeMario Douglas | NE | 10.5 | WR2 | Healthy |  |  |
| 38 | — | Khalil Shakir | BUF | — | WR2 | Healthy |  |  |
| 38 | — | Tre Tucker | LV | 8.8 | WR1 | Healthy |  |  |
| 35 | — | Josh Downs | KC | 7.0 | WR | Healthy |  |  |
| 34 | — | Makai Lemon | PHI | 6.1 | WR1 | Healthy | BYE |  |
| 31 | — | Courtland Sutton | DEN | 5.7 | WR2 | Healthy | BYE |  |
| 29 GUESS (28.87) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 28 | -1 | Jaylen Waddle | DEN | 7.4 | WR1 | Out | BYE |  |
| 27 | — | Keon Coleman | BUF | 6.3 | WR | Healthy |  |  |
| 26 | — | Xavier Worthy | KC | 5.9 | WR2 | Healthy |  |  |
| 23 | — | Ladd McConkey | LAC | 7.2 | WR | Out |  |  |
| 22 | — | A.J. Brown | NE | 4.9 | WR1 | Out |  |  |
| 22 | — | Jordan Addison | MIN | 6.4 | WR | Out |  |  |
| 22 | — | Omar Cooper Jr. | NYJ | 9.9 | WR2 | Out |  |  |
| 20 | — | Ryan Flournoy | DAL | — | WR | Healthy |  |  |
| 18 | — | Adonai Mitchell | NYJ | 0.0 | WR | Healthy |  |  |
| 17 | — | Brian Thomas Jr. | JAX | 3.6 | WR | Healthy |  |  |
| 17 | — | Rashod Bateman | BAL | 5.7 | WR2 | Healthy |  |  |
| 15 | — | Tank Dell | HOU | 5.0 | WR2 | Healthy |  |  |
| 13 | — | Darius Cooper | PHI | 2.5 | WR2 | Healthy | BYE |  |
| 11 | — | Jerry Jeudy | CLE | 3.3 | WR | Healthy |  |  |
| 10 | — | Marvin Harrison Jr. | HOU | 4.6 | WR | Out |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 89 | — | Trey McBride | ARI | 14.0 | TE1 | Healthy |  |  |
| 79 | — | George Kittle | SF | 11.9 | TE1 | Healthy |  |  |
| 78 | — | Isaiah Likely | NYG | 11.7 | TE1 | Healthy |  |  |
| 68 | — | Tyler Warren | IND | 9.3 | TE1 | Healthy |  |  |
| 61 | -29 | Brock Bowers | LV | 17.4 | TE1 | Out |  | -29 vs last board; Out x0.65 |
| 61 | — | Sam LaPorta | DET | 9.4 | TE1 | Healthy |  |  |
| 56 | — | Travis Kelce | KC | 10.3 | TE1 | Questionable |  |  |
| 52 | — | Dalton Kincaid | BUF | 8.7 | TE1 | Healthy |  |  |
| 48 | — | Harold Fannin Jr. | CLE | 8.2 | TE1 | Healthy |  |  |
| 42 | — | Colston Loveland | CHI | 7.2 | TE1 | Healthy | BYE |  |
| 41 | — | Tucker Kraft | GB | 8.0 | TE1 | Healthy |  |  |
| 33 | — | Brenton Strange | JAX | — | TE1 | Healthy |  |  |
| 29 | — | T.J. Hockenson | MIN | 8.0 | TE | Out |  |  |
| 22 | — | Dallas Goedert | PHI | 6.1 | TE1 | Healthy | BYE |  |
| 18 | -1 | Kyle Pitts Sr. | ATL | 6.5 | TE1 | Healthy |  |  |
| 9 | — | Tyler Higbee | LAR | 2.3 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Shedeur Sanders | QB | 25 | 94 | 69 | backup QB cap 25; GUESS inputs |
| Davante Adams | WR | 29 | 85 | 56 | IR x0.50; GUESS inputs |
| Puka Nacua | WR | 53 | 98 | 45 | IR x0.78; GUESS inputs |
| Fernando Mendoza | QB | 45 | 0 | 45 | SF QB1 floor 45 |
| Carson Wentz | QB | 45 | 0 | 45 | SF QB1 floor 45; GUESS inputs |
| J.J. McCarthy | QB | 45 | 3 | 42 | SF QB1 floor 45 |
| DeVonta Smith | WR | 41 | 81 | 40 | Out x0.65 |
| Jacoby Brissett | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Brock Bowers | TE | 61 | 100 | 39 | -29 vs last board; Out x0.65 |
| Khalil Shakir | WR | 38 | 0 | 38 | buy-low: volume > points |
| Jonah Coleman | RB | 30 | 67 | 37 | committee RB 27% cap 30 |
| Kenneth Walker III | RB | 61 | 98 | 37 | Out x0.65 |
| Drake Maye | QB | 50 | 85 | 35 | Out x0.65 |
| Daniel Jones | QB | 45 | 12 | 33 | SF QB1 floor 45; buy-low: volume > points |
| Josh Jacobs | RB | 30 | 63 | 33 | Out x0.65; committee RB 21% cap 30 |
