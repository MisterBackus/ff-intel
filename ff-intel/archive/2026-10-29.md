# FF Intel trade board — Bot or Not Fantasy

Generated 2026-10-29 08:00 AM EDT

- **NFL week:** 8
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-10-29 week 8 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | — | Josh Allen | BUF | 30.5 | QB1 | Healthy |  |  |
| 82 | — | Joe Burrow | CIN | 27.2 | QB1 | Healthy |  |  |
| 80 | — | Trevor Lawrence | JAX | 24.4 | QB1 | Healthy |  |  |
| 78 | — | Brock Purdy | SF | 25.7 | QB1 | Healthy | BYE |  |
| 78 | — | Jared Goff | DET | 26.8 | QB1 | Healthy |  |  |
| 77 | — | Drake Maye | NE | 24.6 | QB1 | Healthy |  |  |
| 71 | — | Jayden Daniels | WAS | 23.9 | QB1 | Healthy |  |  |
| 70 | — | Lamar Jackson | BAL | 23.0 | QB1 | Questionable |  |  |
| 65 | — | Caleb Williams | CHI | 23.6 | QB1 | Healthy |  |  |
| 64 | -1 | Dak Prescott | DAL | 22.7 | QB1 | Healthy |  |  |
| 62 | — | Patrick Mahomes | KC | 20.3 | QB1 | Healthy |  |  |
| 59 | — | Bryce Young | CAR | 21.1 | QB1 | Healthy |  |  |
| 59 | — | Jordan Love | GB | 22.6 | QB1 | Healthy |  |  |
| 59 | — | Kirk Cousins | LV | 24.1 | QB1 | Healthy |  |  |
| 55 | — | Matthew Stafford | LAR | 22.6 | QB1 | Healthy |  |  |
| 55 | — | Tyler Shough | NO | 22.6 | QB1 | Healthy | BYE |  |
| 54 GUESS (53.85) | — | Tyler Huntley | BAL | 20.5 | QB1 | Healthy |  | SF QB1 floor 45; GUESS inputs |
| 50 | — | C.J. Stroud | HOU | 21.7 | QB1 | Healthy | BYE |  |
| 45 | — | Aaron Rodgers | PIT | 21.4 | QB1 | Healthy |  |  |
| 45 | — | Baker Mayfield | TB | 12.4 | QB1 | Healthy |  |  |
| 45 | — | Bo Nix | DEN | 16.1 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 16.6 | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 18.3 | QB1 | Healthy |  |  |
| 45 | — | J.J. McCarthy | NYG | 10.2 | QB1 | Healthy | BYE |  |
| 45 | — | Jacoby Brissett | ARI | 12.0 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 13.4 | QB1 | Healthy |  |  |
| 45 | — | Kyler Murray | MIN | 12.3 | QB1 | Healthy |  |  |
| 45 | — | Malik Willis | MIA | 13.7 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 21.7 | QB1 | Healthy |  |  |
| 45 | — | Sam Darnold | SEA | 16.5 | QB1 | Healthy |  |  |
| 45 | — | Tanner McKee | PHI | 13.5 | QB1 | Healthy |  |  |
| 26 GUESS (25.84) | — | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 94 | — | Kenneth Walker III | KC | 23.1 | RB1 | Healthy |  |  |
| 93 | — | Jahmyr Gibbs | DET | 25.8 | RB1 | Questionable |  |  |
| 92 | — | James Cook III | BUF | 18.1 | RB1 | Healthy |  |  |
| 92 | — | Jonathan Taylor | IND | 18.4 | RB1 | Healthy |  |  |
| 89 | — | Bijan Robinson | ATL | 19.0 | RB1 | Healthy |  |  |
| 86 | — | Javonte Williams | DAL | 17.3 | RB1 | Healthy |  |  |
| 84 | — | Derrick Henry | BAL | 16.8 | RB1 | Healthy |  |  |
| 80 | — | Christian McCaffrey | SF | 18.1 | RB1 | Questionable | BYE |  |
| 80 | — | Chuba Hubbard | CAR | 16.8 | RB1 | Healthy |  |  |
| 80 | — | Kyren Williams | LAR | 17.3 | RB1 | Healthy |  |  |
| 78 | — | Ashton Jeanty | LV | 15.0 | RB1 | Healthy |  |  |
| 74 | — | Bucky Irving | TB | 14.4 | RB1 | Healthy |  |  |
| 72 | — | Jaylen Warren | PIT | 15.4 | RB1 | Healthy |  |  |
| 71 | — | D'Andre Swift | CHI | 16.0 | RB1 | Healthy |  |  |
| 69 | — | Bhayshul Tuten | JAX | 13.7 | RB1 | Healthy |  |  |
| 69 | — | Ollie Gordon II | MIA | 16.2 | RB1-split | Healthy |  |  |
| 68 | — | Chase Brown | CIN | 10.1 | RB1 | Healthy |  |  |
| 68 | — | Tony Pollard | TEN | 12.7 | RB1 | Healthy |  |  |
| 66 | — | Quinshon Judkins | CLE | 11.7 | RB1 | Healthy |  |  |
| 61 | — | Aaron Jones Sr. | MIN | 11.2 | RB1 | Questionable |  |  |
| 58 | — | Omarion Hampton | LAC | 8.8 | RB1 | Healthy |  |  |
| 53 | — | Rhamondre Stevenson | NE | 11.0 | RB1-split | Healthy |  |  |
| 50 | — | Cam Skattebo | NYG | 9.3 | RB1 | Questionable | BYE |  |
| 48 | — | J.K. Dobbins | DEN | 7.7 | RB1 | Healthy |  |  |
| 46 | — | Braelon Allen | NYJ | 10.8 | RB1 | Questionable |  |  |
| 44 | — | Emanuel Wilson | SEA | 11.8 | RB1 | Healthy |  |  |
| 39 | — | Woody Marks | HOU | 7.4 | RB1 | Questionable | BYE |  |
| 35 GUESS (34.7) | — | Zach Charbonnet | SEA | — | RB1 | Questionable |  | Questionable x0.95; buy-low: volume > points; GUESS inputs |
| 30 | — | Alvin Kamara | NO | 9.1 | committee | Healthy | BYE |  |
| 30 | — | Blake Corum | LAR | 9.2 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 12.5 | committee | Questionable |  |  |
| 30 | — | Jordan Mason | MIN | 9.3 | committee | Healthy |  |  |
| 30 | — | Josh Jacobs | GB | 17.6 | committee | Healthy |  |  |
| 30 | — | Kyle Monangai | CHI | 14.2 | committee | Questionable |  |  |
| 30 | — | RJ Harvey | DEN | 9.2 | committee | Healthy |  |  |
| 30 | — | Saquon Barkley | PHI | 7.0 | committee | Questionable |  |  |
| 30 GUESS (30) | — | Travis Etienne Jr. | NO | 8.5 | committee | IR | BYE | IR x0.82; committee RB 21% cap 30; GUESS inputs |
| 30 | — | TreVeyon Henderson | NE | 5.2 | committee | Healthy |  |  |
| 29 | -1 | Tyler Allgeier | ARI | 5.7 | committee | Questionable |  |  |
| 28 | — | David Montgomery | HOU | 8.4 | committee | Out | BYE |  |
| 27 | — | Jonah Coleman | DEN | 7.9 | committee | Healthy |  |  |
| 25 | — | Kimani Vidal | LAC | 5.5 | committee | Healthy |  |  |
| 24 | -1 | Chris Rodriguez Jr. | JAX | 5.0 | committee | Healthy |  |  |
| 24 GUESS (24.47) | -1 | Dameon Pierce | PHI | 12.2 | committee | IR |  | IR x0.82; committee RB 28% cap 30; GUESS inputs |
| 22 | — | Kendre Miller | NO | 4.3 | committee | Healthy | BYE |  |
| 19 | — | Brian Robinson Jr. | ATL | 2.2 | committee | Questionable |  |  |
| 19 | — | Zonovan Knight | ARI | 7.8 | committee | Healthy |  |  |
| 18 | — | Emmett Johnson | KC | 3.6 | committee | Healthy |  |  |
| 17 GUESS (17.38) | — | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 25% cap 30; GUESS inputs |
| 15 | — | Jaleel McLaughlin | CLE | 7.5 | committee | Healthy |  |  |
| 9 | — | Roschon Johnson | CHI | 0.7 | committee | Healthy |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 23.9 | WR1 | Healthy |  |  |
| 94 | — | CeeDee Lamb | DAL | 18.4 | WR1 | Healthy |  |  |
| 89 | — | Amon-Ra St. Brown | DET | 17.6 | WR1 | Questionable |  |  |
| 89 | — | Zay Flowers | BAL | 17.0 | WR1 | Healthy |  |  |
| 88 | — | Puka Nacua | LAR | 18.2 | WR1 | Healthy |  |  |
| 82 | — | Chris Olave | NO | 14.3 | WR1 | Healthy | BYE |  |
| 81 | — | Parker Washington | JAX | 13.2 | WR1 | Healthy |  |  |
| 80 | — | Malik Nabers | NYG | 13.8 | WR1 | Healthy | BYE |  |
| 78 | — | Tee Higgins | CIN | 14.3 | WR2 | Healthy |  |  |
| 77 | — | Christian Watson | GB | 16.1 | WR1 | Healthy |  |  |
| 77 | — | Drake London | ATL | 12.7 | WR1 | Healthy |  |  |
| 76 | — | Ja'Marr Chase | CIN | 13.5 | WR1 | Questionable |  |  |
| 76 | — | Tetairoa McMillan | CAR | 13.2 | WR1 | Healthy |  |  |
| 71 | — | Justin Jefferson | MIN | 12.1 | WR1 | Healthy |  |  |
| 69 | — | Garrett Wilson | NYJ | 11.6 | WR1 | Healthy |  |  |
| 69 | — | Matthew Golden | GB | 13.2 | WR2 | Questionable |  |  |
| 64 | — | Nico Collins | HOU | 12.8 | WR1 | Healthy | BYE |  |
| 63 | — | Tre Tucker | LV | 18.8 | WR1 | Healthy |  |  |
| 61 | — | DeVonta Smith | PHI | 14.0 | WR1 | Questionable |  |  |
| 61 | — | Jalen Coker | CAR | 11.5 | WR2 | Healthy |  |  |
| 58 | — | Luther Burden III | CHI | 11.4 | WR1 | Healthy |  |  |
| 57 | — | Omar Cooper Jr. | NYJ | 20.0 | WR2 | Healthy |  |  |
| 56 | -3 | George Pickens | DAL | 11.3 | WR2 | Questionable |  |  |
| 55 | — | Emeka Egbuka | TB | 9.5 | WR1 | Questionable |  |  |
| 55 | — | Jameson Williams | DET | 12.0 | WR2 | Healthy |  |  |
| 55 | -3 | Stefon Diggs | WAS | 11.5 | WR1 | Questionable |  |  |
| 54 | -3 | Michael Wilson | ARI | 9.1 | WR1 | Questionable |  |  |
| 51 | — | DK Metcalf | PIT | 8.6 | WR1 | Healthy |  |  |
| 51 | — | Jaylen Waddle | DEN | 7.3 | WR1 | Questionable |  |  |
| 45 | — | DJ Moore | BUF | 7.6 | WR1 | Questionable |  |  |
| 45 | — | Mike Evans | SF | 12.6 | WR | Out | BYE |  |
| 45 | — | Rashee Rice | KC | 7.9 | WR1 | Questionable |  |  |
| 44 | — | Germie Bernard | PIT | 12.2 | WR2 | Healthy |  |  |
| 39 | — | Xavier Worthy | KC | 6.1 | WR2 | Healthy |  |  |
| 38 | — | Rome Odunze | CHI | 6.9 | WR2 | Healthy |  |  |
| 37 | — | Denzel Boston | CLE | 6.1 | WR1 | Healthy |  |  |
| 37 | — | Keon Coleman | BUF | 10.6 | WR | Healthy |  |  |
| 37 | — | Ladd McConkey | LAC | 6.5 | WR1 | Questionable |  |  |
| 36 | — | KC Concepcion Jr. | CLE | — | WR2 | Healthy |  |  |
| 33 | — | A.J. Brown | NE | 4.9 | WR1 | Questionable |  |  |
| 32 | — | Jordan Addison | MIN | 6.2 | WR2 | Healthy |  |  |
| 31 | — | Chris Godwin Jr. | TB | 5.6 | WR2 | Healthy |  |  |
| 28 | — | Courtland Sutton | DEN | 4.4 | WR2 | Healthy |  |  |
| 28 GUESS (27.72) | — | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 28 | — | Makai Lemon | PHI | 5.3 | WR | Healthy |  |  |
| 26 | — | Rashod Bateman | BAL | 6.9 | WR2 | Healthy |  |  |
| 23 GUESS (22.94) | — | Romeo Doubs | NE | 8.5 | WR | IR |  | IR x0.82; GUESS inputs |
| 21 | — | DeMario Douglas | NE | 3.8 | WR2 | Healthy |  |  |
| 20 | — | Brian Thomas Jr. | JAX | 3.5 | WR | Healthy |  |  |
| 19 | — | Caleb Douglas | MIA | — | WR2 | Healthy |  |  |
| 17 | — | Marvin Harrison Jr. | HOU | 4.8 | WR | Healthy | BYE |  |
| 15 | — | Jerry Jeudy | CLE | 3.6 | WR | Healthy |  |  |
| 15 | — | Tank Dell | HOU | 5.0 | WR | Healthy | BYE |  |
| 12 | — | Konata Mumpfield | LAR | 2.0 | WR2 | Healthy |  |  |
| 11 | — | Darius Cooper | PHI | 1.8 | WR | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 93 | — | Trey McBride | ARI | 14.4 | TE1 | Healthy |  |  |
| 85 | — | Brock Bowers | LV | 15.7 | TE1 | Questionable |  |  |
| 84 | — | George Kittle | SF | 12.5 | TE1 | Healthy | BYE |  |
| 75 | — | Isaiah Likely | NYG | 11.4 | TE1 | Healthy | BYE |  |
| 65 | — | Sam LaPorta | DET | 10.9 | TE1 | Healthy |  |  |
| 65 | — | Travis Kelce | KC | 9.7 | TE1 | Healthy |  |  |
| 56 | — | Tyler Warren | IND | 11.0 | TE1 | Questionable |  |  |
| 50 | — | T.J. Hockenson | MIN | 6.3 | TE1 | Healthy |  |  |
| 49 | — | Dalton Kincaid | BUF | 8.2 | TE1 | Questionable |  |  |
| 47 | — | Tucker Kraft | GB | 8.1 | TE1 | Healthy |  |  |
| 45 | — | Colston Loveland | CHI | 7.1 | TE1 | Healthy |  |  |
| 33 | — | Kyle Pitts Sr. | ATL | 7.6 | TE1 | Healthy |  |  |
| 31 | — | Dallas Goedert | PHI | 6.0 | TE1 | Healthy |  |  |
| 28 | — | Mark Andrews | BAL | 3.8 | TE1 | Healthy |  |  |
| 15 | — | Jake Ferguson | DAL | 5.1 | TE1 | Healthy |  |  |
| 9 | — | Tyler Higbee | LAR | 2.3 | TE2 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Josh Jacobs | RB | 30 | 88 | 58 | committee RB 9% cap 30 |
| Davante Adams | WR | 28 | 85 | 57 | IR x0.50; GUESS inputs |
| J.J. McCarthy | QB | 45 | 0 | 45 | SF QB1 floor 45 |
| Jacoby Brissett | QB | 45 | 3 | 42 | SF QB1 floor 45; buy-low: volume > points |
| Omar Cooper Jr. | WR | 57 | 98 | 41 | proj 59 / prod 98 / role 2 |
| Kyler Murray | QB | 45 | 6 | 38 | SF QB1 floor 45; buy-low: volume > points |
| Kyle Monangai | RB | 30 | 67 | 37 | Questionable x0.95; committee RB 30% cap 30 |
| KC Concepcion Jr. | WR | 36 | 0 | 36 | buy-low: volume > points |
| Baker Mayfield | QB | 45 | 10 | 35 | SF QB1 floor 45; buy-low: volume > points |
| Dameon Pierce | RB | 24 | 59 | 35 | IR x0.82; committee RB 28% cap 30; GUESS inputs |
| Zach Charbonnet | RB | 35 | 0 | 35 | Questionable x0.95; buy-low: volume > points; GUESS inputs |
| Tre Tucker | WR | 63 | 96 | 33 | proj 56 / prod 96 / role 46 |
| Justin Herbert | QB | 45 | 13 | 32 | SF QB1 floor 45; buy-low: volume > points |
| Breece Hall | RB | 30 | 61 | 31 | Questionable x0.95; committee RB 33% cap 30 |
| Tanner McKee | QB | 45 | 16 | 29 | SF QB1 floor 45 |
