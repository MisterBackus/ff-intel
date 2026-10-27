# FF Intel trade board — Bot or Not Fantasy

Generated 2026-10-27 08:00 AM EDT

- **NFL week:** 7
- **League:** 10-team Superflex Half-PPR (Sleeper `1395904889149739008`)
- **Formula:** 1.0.0 — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news
- **Commit:** `intel: 2026-10-27 week 7 values 1.0.0`
- **Sources:** Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring; Sleeper league matchup players_points for production (played weeks only); Sleeper weekly player stats for snap / carry / target share; Sleeper player directory for injury status, depth chart, search_rank; Sleeper trending adds (48h) for the news/trend component
- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.

## How to read a value

Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.
Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.

## QB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 87 | -2 | Josh Allen | BUF | 30.5 | QB1 | Healthy | BYE |  |
| 83 | +1 | Joe Burrow | CIN | 27.2 | QB1 | Healthy |  |  |
| 79 | -3 | Brock Purdy | SF | 25.7 | QB1 | Healthy |  |  |
| 79 | +5 | Drake Maye | NE | 24.6 | QB1 | Healthy |  |  |
| 79 | -4 | Jared Goff | DET | 26.8 | QB1 | Healthy |  |  |
| 76 | -2 | Trevor Lawrence | JAX | 24.4 | QB1 | Healthy | BYE |  |
| 69 | +16 | Caleb Williams | CHI | 23.6 | QB1 | Healthy |  | +16 vs last board; SF QB1 floor 45 |
| 65 | +1 | Jayden Daniels | WAS | 23.9 | QB1 | Healthy | BYE |  |
| 64 | +9 | Dak Prescott | DAL | 22.7 | QB1 | Healthy |  | +9 vs last board; SF QB1 floor 45 |
| 62 | -1 | Jordan Love | GB | 22.6 | QB1 | Healthy |  |  |
| 62 | -8 | Patrick Mahomes | KC | 20.3 | QB1 | Healthy |  | -8 vs last board; SF QB1 floor 45 |
| 61 | -2 | Kirk Cousins | LV | 24.1 | QB1 | Healthy |  |  |
| 60 | -11 | Bryce Young | CAR | 21.1 | QB1 | Healthy |  | -11 vs last board; SF QB1 floor 45 |
| 56 | +2 | Matthew Stafford | LAR | 22.6 | QB1 | Healthy |  |  |
| 56 | -4 | Tyler Shough | NO | 22.6 | QB1 | Healthy |  |  |
| 52 | +2 | C.J. Stroud | HOU | 21.7 | QB1 | Healthy |  |  |
| 46 | -13 | Aaron Rodgers | PIT | 21.4 | QB1 | Healthy |  | -13 vs last board; SF QB1 floor 45 |
| 46 | +1 | Lamar Jackson | BAL | 23.0 | QB1 | Out |  |  |
| 45 | — | Baker Mayfield | TB | 12.4 | QB1 | Healthy |  |  |
| 45 | — | Bo Nix | DEN | 16.1 | QB1 | Healthy |  |  |
| 45 | — | Daniel Jones | IND | 11.4 | QB1 | Healthy |  |  |
| 45 | — | Deshaun Watson | CLE | 16.6 | QB1 | Healthy |  |  |
| 45 | — | Geno Smith | NYJ | 18.3 | QB1 | Healthy |  |  |
| 45 | +27 | J.J. McCarthy | NYG | 10.2 | QB1 | Healthy |  | +27 vs last board; SF QB1 floor 45 |
| 45 | — | Jacoby Brissett | ARI | 12.0 | QB1 | Healthy |  |  |
| 45 | — | Justin Herbert | LAC | 13.4 | QB1 | Healthy | BYE |  |
| 45 | — | Kyler Murray | MIN | 12.3 | QB1 | Healthy |  |  |
| 45 | — | Michael Penix Jr. | ATL | 21.7 | QB1 | Healthy |  |  |
| 45 | — | Sam Darnold | SEA | 16.5 | QB1 | Healthy |  |  |
| 45 | +27 | Tanner McKee | PHI | 13.5 | QB1 | Healthy |  | +27 vs last board; SF QB1 floor 45 |
| 45 | — | Tyler Huntley | BAL | 20.5 | QB1 | Healthy |  |  |
| 27 GUESS (27) | -1 | Jalen Hurts | PHI | 19.8 | QB1 | IR |  | IR x0.50; GUESS inputs |

## RB

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | +1 | Jahmyr Gibbs | DET | 25.8 | RB1 | Healthy |  |  |
| 94 | — | Kenneth Walker III | KC | 23.1 | RB1 | Healthy |  |  |
| 92 | +1 | Jonathan Taylor | IND | 18.4 | RB1 | Healthy |  |  |
| 90 | — | James Cook III | BUF | 18.1 | RB1 | Healthy | BYE |  |
| 89 | +1 | Bijan Robinson | ATL | 19.0 | RB1 | Healthy |  |  |
| 87 | +3 | Javonte Williams | DAL | 17.3 | RB1 | Healthy |  |  |
| 85 | -4 | Derrick Henry | BAL | 16.8 | RB1 | Healthy |  |  |
| 81 | — | Christian McCaffrey | SF | 18.1 | RB1 | Questionable |  |  |
| 81 | -5 | Chuba Hubbard | CAR | 16.8 | RB1 | Healthy |  |  |
| 81 | — | Kyren Williams | LAR | 17.3 | RB1 | Healthy |  |  |
| 79 | — | Ashton Jeanty | LV | 15.0 | RB1 | Healthy |  |  |
| 75 | — | Bucky Irving | TB | 14.4 | RB1 | Healthy |  |  |
| 74 | -2 | Jaylen Warren | PIT | 15.4 | RB1 | Healthy |  |  |
| 72 | +2 | D'Andre Swift | CHI | 16.0 | RB1 | Healthy |  |  |
| 70 | +13 | Tony Pollard | TEN | 12.7 | RB1 | Healthy |  | +13 vs last board; buy-low: volume > points |
| 69 | -1 | Bhayshul Tuten | JAX | 13.7 | RB1 | Healthy | BYE |  |
| 69 | +2 | Ollie Gordon II | MIA | 16.2 | RB1-split | Healthy |  |  |
| 68 | -4 | Chase Brown | CIN | 10.1 | RB1 | Healthy |  |  |
| 65 | +2 | Quinshon Judkins | CLE | 11.7 | RB1 | Healthy |  |  |
| 61 | -4 | Aaron Jones Sr. | MIN | 11.2 | RB1 | Questionable |  |  |
| 58 | -1 | Omarion Hampton | LAC | 8.8 | RB1 | Healthy | BYE |  |
| 54 | — | Rhamondre Stevenson | NE | 11.0 | RB1-split | Healthy |  |  |
| 51 | — | Braelon Allen | NYJ | 10.8 | RB1 | Healthy |  |  |
| 51 | +2 | Cam Skattebo | NYG | 9.3 | RB1 | Questionable |  |  |
| 50 | -3 | J.K. Dobbins | DEN | 7.7 | RB1 | Healthy |  |  |
| 45 | +5 | Emanuel Wilson | SEA | 11.8 | RB1 | Healthy |  |  |
| 41 | +2 | Woody Marks | HOU | 7.4 | RB1 | Questionable |  |  |
| 30 | — | Blake Corum | LAR | 9.2 | committee | Healthy |  |  |
| 30 | — | Breece Hall | NYJ | 12.5 | committee | Out |  |  |
| 30 | — | Dameon Pierce | PHI | 12.2 | committee | Healthy |  |  |
| 30 | +11 | Dylan Sampson | CLE | 9.2 | committee | Healthy |  | +11 vs last board; committee RB 5% cap 30 |
| 30 | — | Jordan Mason | MIN | 9.3 | committee | Healthy |  |  |
| 30 | -20 | Josh Jacobs | GB | 17.6 | committee | Healthy |  | -20 vs last board; committee RB 9% cap 30 |
| 30 | — | Kyle Monangai | CHI | 14.2 | committee | Out |  |  |
| 30 | — | RJ Harvey | DEN | 9.2 | committee | Healthy |  |  |
| 30 | — | Saquon Barkley | PHI | 7.0 | committee | Questionable |  |  |
| 30 GUESS (30) | — | Travis Etienne Jr. | NO | 8.5 | committee | IR |  | IR x0.83; committee RB 21% cap 30; GUESS inputs |
| 30 | — | TreVeyon Henderson | NE | 5.2 | committee | Healthy |  |  |
| 30 | — | Tyler Allgeier | ARI | 5.7 | committee | Healthy |  |  |
| 29 | -1 | Alvin Kamara | NO | 9.1 | committee | Healthy |  |  |
| 28 | -2 | David Montgomery | HOU | 8.4 | committee | Out |  |  |
| 27 | +13 | Jonah Coleman | DEN | 7.9 | committee | Healthy |  | +13 vs last board; committee RB 14% cap 30 |
| 24 | -1 | Kimani Vidal | LAC | 5.5 | committee | Healthy | BYE |  |
| 22 | -3 | Chris Rodriguez Jr. | JAX | 5.0 | committee | Healthy | BYE |  |
| 22 | — | Kendre Miller | NO | 4.3 | committee | Healthy |  |  |
| 22 GUESS (22.45) | +4 | Zach Charbonnet | SEA | — | RB1 | Out |  | Out x0.65; buy-low: volume > points; GUESS inputs |
| 20 | +9 | Zonovan Knight | ARI | 7.8 | committee | Healthy |  | +9 vs last board; committee RB 16% cap 30 |
| 17 GUESS (17.37) | -2 | De'Von Achane | MIA | 7.0 | committee | IR |  | IR x0.50; committee RB 25% cap 30; GUESS inputs |
| 16 | -2 | Emmett Johnson | KC | 3.6 | committee | Healthy |  |  |
| 15 | -2 | Jaleel McLaughlin | CLE | 7.5 | committee | Healthy |  |  |
| 12 | -1 | Brian Robinson Jr. | ATL | 2.2 | committee | Out |  |  |
| 9 | — | Roschon Johnson | CHI | 0.7 | committee | Healthy |  |  |

## WR

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 98 | — | Jaxon Smith-Njigba | SEA | 23.9 | WR1 | Healthy |  |  |
| 94 | +2 | CeeDee Lamb | DAL | 18.4 | WR1 | Healthy |  |  |
| 89 | +1 | Amon-Ra St. Brown | DET | 17.6 | WR1 | Questionable |  |  |
| 89 | +2 | Puka Nacua | LAR | 18.2 | WR1 | Healthy |  |  |
| 89 | +4 | Zay Flowers | BAL | 17.0 | WR1 | Healthy |  |  |
| 84 | +1 | Chris Olave | NO | 14.3 | WR1 | Healthy |  |  |
| 80 | +4 | Ja'Marr Chase | CIN | 13.5 | WR1 | Healthy |  |  |
| 80 | +1 | Malik Nabers | NYG | 13.8 | WR1 | Healthy |  |  |
| 80 | +8 | Tee Higgins | CIN | 14.3 | WR2 | Healthy |  | +8 vs last board |
| 78 | -2 | Christian Watson | GB | 16.1 | WR1 | Healthy |  |  |
| 78 | +2 | Parker Washington | JAX | 13.2 | WR1 | Healthy | BYE |  |
| 76 | -5 | Tetairoa McMillan | CAR | 13.2 | WR1 | Healthy |  |  |
| 73 | +3 | Drake London | ATL | 12.7 | WR1 | Questionable |  |  |
| 72 | -1 | Justin Jefferson | MIN | 12.1 | WR1 | Healthy |  |  |
| 69 | -5 | Garrett Wilson | NYJ | 11.6 | WR1 | Healthy |  |  |
| 69 | — | Matthew Golden | GB | 13.2 | WR2 | Questionable |  |  |
| 66 | -5 | Nico Collins | HOU | 12.8 | WR1 | Healthy |  |  |
| 65 | +37 | Tre Tucker | LV | 18.8 | WR1 | Healthy |  | +37 vs last board |
| 60 | -3 | George Pickens | DAL | 11.3 | WR2 | Healthy |  |  |
| 60 | +1 | Luther Burden III | CHI | 11.4 | WR1 | Healthy |  |  |
| 59 | +7 | Jameson Williams | DET | 12.0 | WR2 | Healthy |  |  |
| 59 | +39 | Omar Cooper Jr. | NYJ | 20.0 | WR2 | Healthy |  | +39 vs last board |
| 58 | -6 | Jalen Coker | CAR | 11.5 | WR2 | Questionable |  |  |
| 57 | -3 | Michael Wilson | ARI | 9.1 | WR1 | Healthy |  |  |
| 54 | — | Stefon Diggs | WAS | 11.5 | WR1 | Healthy | BYE |  |
| 52 | -4 | DK Metcalf | PIT | 8.6 | WR1 | Healthy |  |  |
| 52 | +3 | Jaylen Waddle | DEN | 7.3 | WR1 | Questionable |  |  |
| 45 | -18 | Germie Bernard | PIT | 12.2 | WR2 | Healthy |  | -18 vs last board |
| 43 | -3 | Mike Evans | SF | 12.6 | WR | Out |  |  |
| 41 | -1 | Xavier Worthy | KC | 6.1 | WR2 | Healthy |  |  |
| 39 | +1 | Rome Odunze | CHI | 6.9 | WR2 | Healthy |  |  |
| 38 | -4 | DeVonta Smith | PHI | 14.0 | WR | Out |  |  |
| 37 | -4 | Denzel Boston | CLE | 6.1 | WR1 | Healthy |  |  |
| 36 | +2 | A.J. Brown | NE | 4.9 | WR1 | Healthy |  |  |
| 36 | -1 | Emeka Egbuka | TB | 9.5 | WR1 | Out |  |  |
| 36 | — | Keon Coleman | BUF | 10.6 | WR | Healthy | BYE |  |
| 33 | -2 | Jordan Addison | MIN | 6.2 | WR2 | Healthy |  |  |
| 32 | +2 | Chris Godwin Jr. | TB | 5.6 | WR2 | Healthy |  |  |
| 30 | — | Courtland Sutton | DEN | 4.4 | WR2 | Healthy |  |  |
| 29 | — | DJ Moore | BUF | 7.6 | WR1 | Out | BYE |  |
| 29 | +5 | Makai Lemon | PHI | 5.3 | WR1 | Healthy |  |  |
| 29 | -2 | Rashee Rice | KC | 7.9 | WR1 | Out |  |  |
| 28 | +1 | Rashod Bateman | BAL | 6.9 | WR2 | Healthy |  |  |
| 26 GUESS (26.27) | -1 | Davante Adams | LAR | 14.5 | WR | IR |  | IR x0.50; GUESS inputs |
| 24 | +2 | Ladd McConkey | LAC | 6.5 | WR1 | Out | BYE |  |
| 24 GUESS (23.76) | +1 | Romeo Doubs | NE | 8.5 | WR | IR |  | IR x0.83; GUESS inputs |
| 23 | — | DeMario Douglas | NE | 3.8 | WR2 | Healthy |  |  |
| 20 | +1 | Brian Thomas Jr. | JAX | 3.5 | WR | Healthy | BYE |  |
| 17 | -1 | Marvin Harrison Jr. | HOU | 4.8 | WR | Healthy |  |  |
| 16 | +2 | Jerry Jeudy | CLE | 3.6 | WR | Healthy |  |  |
| 16 | +8 | Tank Dell | HOU | 5.0 | WR | Healthy |  | +8 vs last board |
| 15 | -1 | Jaylin Noel | HOU | 0.7 | WR2 | Questionable |  |  |
| 13 | -1 | Konata Mumpfield | LAR | 2.0 | WR2 | Healthy |  |  |
| 12 | -1 | Darius Cooper | PHI | 1.8 | WR2 | Healthy |  |  |

## TE

| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |
|---:|---:|---|---|---:|---|---|---|---|
| 93 | +2 | Trey McBride | ARI | 14.4 | TE1 | Healthy |  |  |
| 90 | -1 | Brock Bowers | LV | 15.7 | TE1 | Healthy |  |  |
| 85 | +2 | George Kittle | SF | 12.5 | TE1 | Healthy |  |  |
| 76 | -5 | Isaiah Likely | NYG | 11.4 | TE1 | Healthy |  |  |
| 67 | +4 | Travis Kelce | KC | 9.7 | TE1 | Healthy |  |  |
| 66 | -7 | Sam LaPorta | DET | 10.9 | TE1 | Healthy |  |  |
| 54 | +4 | Harold Fannin Jr. | CLE | 7.7 | TE1 | Healthy |  |  |
| 51 | +18 | T.J. Hockenson | MIN | 6.3 | TE1 | Healthy |  | +18 vs last board; buy-low: volume > points |
| 51 | +3 | Tucker Kraft | GB | 8.1 | TE1 | Healthy |  |  |
| 44 | -3 | Dalton Kincaid | BUF | 8.2 | TE1 | Questionable | BYE |  |
| 43 | +11 | Colston Loveland | CHI | 7.1 | TE1 | Healthy |  | +11 vs last board; buy-low: volume > points |
| 38 | -2 | Tyler Warren | IND | 11.0 | TE1 | Out |  |  |
| 32 | — | Kyle Pitts Sr. | ATL | 7.6 | TE1 | Healthy |  |  |
| 30 | -1 | Dallas Goedert | PHI | 6.0 | TE1 | Healthy |  |  |
| 25 | -12 | Mark Andrews | BAL | 3.8 | TE1 | Healthy |  | -12 vs last board; buy-low: volume > points |
| 17 | -2 | Jake Ferguson | DAL | 6.0 | TE1 | Healthy |  |  |
| 10 | -2 | Tyler Higbee | LAR | 2.3 | TE1 | Healthy |  |  |

## Sanity: 15 biggest value vs production-percentile gaps

| Player | Pos | Value | Prod % | Gap | Why |
|---|---|---:|---:|---:|---|
| Davante Adams | WR | 26 | 85 | 59 | IR x0.50; GUESS inputs |
| Josh Jacobs | RB | 30 | 88 | 58 | -20 vs last board; committee RB 9% cap 30 |
| J.J. McCarthy | QB | 45 | 0 | 45 | +27 vs last board; SF QB1 floor 45 |
| Daniel Jones | QB | 45 | 3 | 42 | SF QB1 floor 45; buy-low: volume > points |
| DeVonta Smith | WR | 38 | 79 | 41 | Out x0.65 |
| Omar Cooper Jr. | WR | 59 | 98 | 39 | +39 vs last board |
| Jacoby Brissett | QB | 45 | 6 | 38 | SF QB1 floor 45; buy-low: volume > points |
| Kyle Monangai | RB | 30 | 68 | 38 | Out x0.65; committee RB 30% cap 30 |
| Tyler Warren | TE | 38 | 75 | 37 | Out x0.65 |
| Kyler Murray | QB | 45 | 10 | 35 | SF QB1 floor 45; buy-low: volume > points |
| Baker Mayfield | QB | 45 | 13 | 32 | SF QB1 floor 45; buy-low: volume > points |
| Breece Hall | RB | 30 | 62 | 32 | Out x0.65; committee RB 33% cap 30 |
| Tre Tucker | WR | 65 | 96 | 31 | +37 vs last board |
| Dameon Pierce | RB | 30 | 60 | 30 | committee RB 28% cap 30 |
| Justin Herbert | QB | 45 | 16 | 29 | SF QB1 floor 45; buy-low: volume > points |
