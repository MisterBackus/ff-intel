# FF Intel trade board — Bot or Not Fantasy

Generated 2026-11-17 07:00 AM EST

- **NFL week:** 10
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-11-17 week 10 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | -1 | Joe Burrow | CIN | 32.5 | QB1 | Healthy |  |  |
| 85 | -1 | Josh Allen | BUF | 28.4 | QB1 | Healthy |  |  |
| 80 | +1 | Brock Purdy | SF | 27.6 | QB1 | Healthy |  |  |
| 77 | +4 | Patrick Mahomes | KC | 24.4 | QB1 | Healthy |  |  |
| 77 | +1 | Trevor Lawrence | JAX | 24.6 | QB1 | Healthy |  |  |
| 73 | +1 | C.J. Stroud | HOU | 25.1 | QB1 | Healthy |  |  |
| 72 | +5 | Dak Prescott | DAL | 25.0 | QB1 | Healthy |  |  |
| 70 | +2 | Jayden Daniels | WAS | 22.6 | QB1 | Healthy |  |  |
| 69 | — | Jared Goff | DET | 23.1 | QB1 | Healthy |  |  |
| 69 | -4 | Jordan Love | GB | 24.3 | QB1 | Healthy |  |  |
| 68 | -3 | Kirk Cousins | MIN | 24.1 | QB1 | Healthy |  |  |
| 61 | — | Caleb Williams | CHI | 21.9 | QB1 | Healthy | BYE |  |
| 60 | -5 | Tyler Shough | NO | 21.4 | QB1 | Healthy |  |  |
| 56 | -4 | Bryce Young | CAR | 19.3 | QB1 | Healthy |  |  |
| 52 | +2 | Cam Ward | TEN | 19.5 | QB1 | Healthy |  |  |
| 52 | +3 | Matthew Stafford | LAR | 21.1 | QB1 | Healthy |  |  |
| 49 | — | Bo Nix | DEN | 17.4 | QB1 | Healthy | BYE |  |
| 48 | +2 | Aaron Rodgers | PIT | 17.9 | QB1 | Healthy |  |  |
| 45 GUESS (45) | — | Carson Wentz | MIN | 2.8 | QB1 | Healthy |  | SF QB1 floor 45; GUESS inputs |
| 45 | — | Daniel Jones | IND | 11.1 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 16.7 | QB1 | Healthy |  |  |
| 45 | — | Drew Lock | SEA | 20.5 | QB1 | Healthy |  |  |
| 45 | — | Fernando Mendoza | LV | 13.9 | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 12.5 | QB1 | Healthy |  |  |
| 45 | — | Jacoby Brissett | BAL | 10.6 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 13.3 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 16.9 | QB1 | Healthy |  |  |
| 41 GUESS (41.02) | -2 | Lamar Jackson | BAL | 18.4 | QB1 | IR |  | IR x0.78; GUESS inputs |
| 40 | -5 | Drake Maye | NE | 22.9 | QB1 | Out |  |  |
| 29 GUESS (28.99) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR | BYE | IR x0.50; GUESS inputs |
| 27 | -1 | Baker Mayfield | TB | 10.2 | QB1 | Questionable | BYE |  |
| 25 | -2 | Geno Smith | NYJ | 16.2 | QB1 | Out |  |  |
| 25 GUESS (25) | — | Shedeur Sanders | CLE | 26.7 | QB2 | Healthy |  | backup QB cap 25; GUESS inputs |
| 24 | +1 | Sam Darnold | SEA | 17.3 | QB1 | Out |  |  |
| 23 GUESS (23.09) | — | Kyler Murray | MIN | 14.4 | QB1 | Out |  | Out x0.65; buy-low: volume > points; GUESS inputs |
| 20 GUESS (20.28) | -2 | Malik Willis | MIA | 13.3 | QB1 | IR |  | IR x0.78; buy-low: volume > points; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jahmyr Gibbs | DET | 25.9 | RB1 | Healthy |  |  |
| 94 | — | James Cook III | BUF | 18.2 | RB1 | Healthy |  |  |
| 90 | — | Bijan Robinson | ATL | 18.0 | RB1 | Healthy |  |  |
| 88 | — | Christian McCaffrey | SF | 21.4 | RB1 | Healthy |  |  |
| 88 | +1 | Chuba Hubbard | CAR | 18.4 | RB1 | Healthy |  |  |
| 86 | -1 | Bucky Irving | TB | 16.5 | RB1 | Healthy | BYE |  |
| 81 | +2 | Derrick Henry | BAL | 15.3 | RB1 | Healthy |  |  |
| 80 | +3 | Bhayshul Tuten | JAX | 15.4 | RB1 | Healthy |  |  |
| 80 | +3 | Tony Pollard | TEN | 15.8 | RB1 | Healthy |  |  |
| 79 | -1 | Jonathan Taylor | IND | 15.2 | RB1 | Healthy |  |  |
| 77 | — | D'Andre Swift | CHI | 15.8 | RB1 | Healthy | BYE |  |
| 77 | -3 | Javonte Williams | DAL | 15.5 | RB1 | Healthy |  |  |
| 76 | -6 | Jaylen Warren | PIT | 15.0 | RB1 | Healthy |  |  |
| 74 | +7 | Cam Skattebo | NYG | 11.3 | RB1 | Healthy |  |  |
| 71 | +4 | Chase Brown | CIN | 11.8 | RB1 | Healthy |  |  |
| 69 | -6 | Kyren Williams | LAR | 14.5 | RB1-split | Healthy |  |  |
| 66 | -1 | Ashton Jeanty | LV | 12.7 | RB1 | Healthy |  |  |
| 63 | — | Ollie Gordon II | MIA | 12.7 | RB1 | Healthy |  |  |
| 63 | +1 | Quinshon Judkins | CLE | 10.6 | RB1 | Healthy |  |  |
| 59 | -2 | Kenneth Walker III | KC | 22.9 | RB1 | Out |  |  |
| 56 | — | Saquon Barkley | PHI | 7.9 | RB1-split | Healthy | BYE |  |
| 55 | — | Aaron Jones Sr. | MIN | 9.7 | RB1 | Healthy |  |  |
| 52 | +6 | Omarion Hampton | LAC | 8.9 | RB1 | Healthy |  |  |
| 51 | -5 | Rhamondre Stevenson | NE | 10.2 | RB1-split | Healthy |  |  |
| 47 | -6 | Braelon Allen | NYJ | 10.7 | RB1 | Healthy |  |  |
| 36 | -4 | Tyler Allgeier | ARI | 8.1 | RB1-split | Healthy |  |  |
| 30 | — | Alvin Kamara | NO | 9.5 | committee | Healthy |  |  |
| 30 | — | Blake Corum | LAR | 10.9 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 12.1 | committee | Healthy |  |  |
| 30 | — | Emmett Johnson | KC | 9.5 | committee | Healthy |  |  |
| 30 | +1 | J.K. Dobbins | DEN | 6.4 | RB1 | Healthy | BYE |  |
| 30 | — | Jonah Coleman | DEN | 14.4 | committee | Healthy | BYE |  |
| 30 | — | Jordan Mason | MIN | 6.4 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 12.8 | committee | Out |  |  |
| 30 | — | Rachaad White | WAS | 9.6 | committee | Healthy |  |  |
| 30 | — | Travis Etienne Jr. | NO | 7.6 | committee | Healthy |  |  |
| 30 | +1 | Zach Charbonnet | SEA | 7.6 | committee | Healthy |  |  |
| 29 | +5 | Jadarian Price | SEA | 6.5 | committee | Healthy |  |  |
| 27 | — | Rico Dowdle | PIT | 4.3 | committee | Healthy |  |  |
| 27 | +1 | Woody Marks | HOU | 7.4 | RB1 | Out |  |  |
| 24 | -6 | Chris Rodriguez Jr. | JAX | 5.9 | committee | Healthy |  |  |
| 21 GUESS (20.68) | — | RJ Harvey | DEN | 9.2 | committee | IR | BYE | IR x0.78; committee RB 14% cap 30; GUESS inputs |
| 19 | +2 | Corey Kiner | NE | 2.5 | committee | Healthy |  |  |
| 19 | -1 | Kimani Vidal | LAC | 4.0 | committee | Healthy |  |  |
| 17 | +3 | Kaleb Johnson | GB | 3.7 | committee | Healthy |  |  |
| 16 GUESS (16.31) | — | TreVeyon Henderson | NE | 5.2 | committee | IR |  | IR x0.78; committee RB 23% cap 30; GUESS inputs |
| 15 GUESS (15.27) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 17% cap 30; GUESS inputs |
| 14 | +1 | Audric Estime | NO | 1.6 | committee | Healthy |  |  |
| 11 GUESS (11.48) | -1 | Brian Robinson Jr. | ATL | 2.2 | committee | IR |  | IR x0.78; committee RB 22% cap 30; GUESS inputs |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 22.4 | WR1 | Healthy |  |  |
| 96 | +1 | CeeDee Lamb | DAL | 18.4 | WR1 | Healthy |  |  |
| 95 | +2 | Amon-Ra St. Brown | DET | 16.8 | WR1 | Healthy |  |  |
| 94 | +1 | Ja'Marr Chase | CIN | 18.0 | WR1 | Healthy |  |  |
| 84 | -4 | Tee Higgins | CIN | 16.1 | WR2 | Healthy |  |  |
| 83 | -1 | Matthew Golden | GB | 14.7 | WR2 | Healthy |  |  |
| 82 | +2 | Justin Jefferson | MIN | 11.4 | WR1 | Healthy |  |  |
| 82 | +5 | Parker Washington | JAX | 13.3 | WR1 | Healthy |  |  |
| 81 | -5 | Chris Olave | NO | 13.1 | WR1 | Healthy |  |  |
| 80 | -3 | Christian Watson | GB | 15.8 | WR1 | Healthy |  |  |
| 80 | -4 | Malik Nabers | NYG | 12.0 | WR1 | Healthy |  |  |
| 76 | +7 | Nico Collins | HOU | 13.9 | WR1 | Healthy |  |  |
| 76 | -3 | Tetairoa McMillan | CAR | 11.8 | WR1 | Healthy |  |  |
| 74 | -4 | Zay Flowers | BAL | 12.7 | WR1 | Healthy |  |  |
| 71 | +1 | Drake London | ATL | 11.3 | WR1 | Questionable |  |  |
| 69 | — | Luther Burden III | CHI | 12.4 | WR1 | Questionable | BYE |  |
| 68 | — | Garrett Wilson | NYJ | 11.6 | WR1 | Healthy |  |  |
| 68 | +12 | George Pickens | DAL | 13.6 | WR2 | Healthy |  | +12 vs last board |
| 62 | +5 | Stefon Diggs | WAS | 11.6 | WR1 | Healthy |  |  |
| 58 | -2 | Jameson Williams | DET | 11.0 | WR2 | Healthy |  |  |
| 56 | +34 | Ryan Flournoy | DAL | 16.1 | WR | Healthy |  | +34 vs last board |
| 55 | +8 | DJ Moore | BUF | 9.6 | WR1 | Healthy |  | +8 vs last board |
| 55 | +2 | DK Metcalf | PIT | 8.4 | WR1 | Healthy |  |  |
| 55 | +2 | Emeka Egbuka | TB | 8.9 | WR1 | Healthy | BYE |  |
| 53 | -4 | KC Concepcion Jr. | CLE | 10.7 | WR2 | Healthy |  |  |
| 53 | +3 | Malik Washington | MIA | 9.8 | WR2 | Healthy |  |  |
| 53 | +1 | Rashee Rice | KC | 9.2 | WR1 | Healthy |  |  |
| 52 GUESS (51.84) | -1 | Puka Nacua | LAR | 19.8 | WR | IR |  | IR x0.78; GUESS inputs |
| 49 GUESS (49.35) | -3 | Michael Wilson | ARI | 10.6 | WR | IR |  | IR x0.78; buy-low: volume > points; GUESS inputs |
| 48 | -8 | Jalen Coker | CAR | 8.8 | WR2 | Healthy |  | -8 vs last board |
| 46 | -1 | Rome Odunze | CHI | 8.1 | WR2 | Healthy | BYE |  |
| 42 | +5 | Josh Downs | KC | 8.0 | WR2 | Healthy |  |  |
| 41 | — | DeVonta Smith | PHI | 14.0 | WR1 | Out | BYE |  |
| 41 | +3 | Khalil Shakir | BUF | 6.5 | WR2 | Healthy |  |  |
| 40 | -6 | Denzel Boston | CLE | 6.7 | WR1 | Healthy |  |  |
| 40 | -1 | Mike Evans | SF | 12.6 | WR1 | Out |  |  |
| 35 | -5 | Germie Bernard | PIT | 7.7 | WR2 | Healthy |  |  |
| 33 | -6 | DeMario Douglas | NE | 8.1 | WR2 | Healthy |  |  |
| 32 | +1 | Courtland Sutton | DEN | 5.7 | WR2 | Healthy | BYE |  |
| 32 | -2 | Makai Lemon | PHI | 6.1 | WR | Healthy | BYE |  |
| 32 | -6 | Tre Tucker | LV | 6.9 | WR1 | Healthy |  |  |
| 29 | — | Jaylen Waddle | DEN | 7.4 | WR1 | Out | BYE |  |
| 28 GUESS (27.62) | -1 | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 26 | -1 | Keon Coleman | BUF | 5.4 | WR | Healthy |  |  |
| 25 | -2 | Xavier Worthy | KC | 5.2 | WR | Healthy |  |  |
| 21 | -1 | A.J. Brown | NE | 4.6 | WR1 | Out |  |  |
| 21 | -3 | Ladd McConkey | LAC | 7.2 | WR | Out |  |  |
| 20 | +1 | Adonai Mitchell | NYJ | 3.7 | WR2 | Healthy |  |  |
| 18 | -4 | Omar Cooper Jr. | NYJ | 7.5 | WR | Out |  |  |
| 18 | +1 | Rashod Bateman | BAL | 5.7 | WR2 | Healthy |  |  |
| 17 | -1 | Jordan Addison | MIN | 6.4 | WR | Out |  |  |
| 16 | -1 | Brian Thomas Jr. | JAX | 3.7 | WR | Healthy |  |  |
| 14 | -1 | Tank Dell | HOU | 4.3 | WR | Healthy |  |  |
| 12 | -1 | Darius Cooper | PHI | 2.5 | WR | Healthy | BYE |  |
| 12 | +1 | Jerry Jeudy | CLE | 3.8 | WR | Healthy |  |  |
| 10 | — | Marvin Harrison Jr. | HOU | 4.6 | WR | Out |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 86 | -3 | Trey McBride | ARI | 13.2 | TE1 | Healthy |  |  |
| 83 | +5 | Isaiah Likely | NYG | 13.2 | TE1 | Healthy |  |  |
| 80 | +1 | George Kittle | SF | 11.7 | TE1 | Healthy |  |  |
| 63 | +15 | Harold Fannin Jr. | CLE | 8.7 | TE1 | Healthy |  | +15 vs last board |
| 60 | -1 | Sam LaPorta | DET | 8.6 | TE1 | Healthy |  |  |
| 59 | -2 | Brock Bowers | LV | 15.6 | TE1 | Out |  |  |
| 58 | -8 | Tyler Warren | IND | 8.3 | TE1 | Healthy |  | -8 vs last board; buy-low: volume > points |
| 55 | -1 | Travis Kelce | KC | 9.6 | TE1 | Questionable |  |  |
| 53 | +1 | Dalton Kincaid | BUF | 8.5 | TE1 | Healthy |  |  |
| 43 | +5 | Brenton Strange | JAX | 7.9 | TE1 | Healthy |  |  |
| 40 | -2 | Colston Loveland | CHI | 7.2 | TE1 | Healthy | BYE |  |
| 36 | -3 | Tucker Kraft | GB | 7.5 | TE1 | Healthy |  |  |
| 26 | -3 | T.J. Hockenson | MIN | 8.0 | TE1 | Out |  |  |
| 22 | — | Dallas Goedert | PHI | 6.1 | TE1 | Healthy | BYE |  |
| 18 | -1 | Kyle Pitts Sr. | ATL | 6.3 | TE1 | Healthy |  |  |
| 9 | — | Tyler Higbee | LAR | 4.6 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Shedeur Sanders | QB | 25 | 91 | 66 | backup QB cap 25; GUESS inputs |
| Davante Adams | WR | 28 | 84 | 56 | IR x0.50; GUESS inputs |
| Puka Nacua | WR | 52 | 98 | 46 | IR x0.78; GUESS inputs |
| Carson Wentz | QB | 45 | 0 | 45 | SF QB1 floor 45; GUESS inputs |
| Brock Bowers | TE | 59 | 100 | 41 | Out x0.65 |
| DeVonta Smith | WR | 41 | 82 | 41 | Out x0.65 |
| Jacoby Brissett | QB | 45 | 6 | 39 | SF QB1 floor 45; buy-low: volume > points |
| Kenneth Walker III | RB | 59 | 98 | 39 | Out x0.65 |
| Jonah Coleman | RB | 30 | 69 | 39 | committee RB 27% cap 30 |
| Josh Jacobs | RB | 30 | 67 | 37 | Out x0.65; committee RB 19% cap 30 |
| Daniel Jones | QB | 45 | 9 | 36 | SF QB1 floor 45; buy-low: volume > points |
| Ryan Flournoy | WR | 56 | 90 | 34 | +34 vs last board |
| J.J. McCarthy | QB | 45 | 11 | 34 | SF QB1 floor 45; buy-low: volume > points |
| Mike Evans | WR | 40 | 71 | 31 | Out x0.65 |
| Breece Hall | RB | 30 | 60 | 30 | committee RB 35% cap 30 |
