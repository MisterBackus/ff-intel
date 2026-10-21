# FF Intel

ROS trade-value board for **Bot or Not Fantasy** — Sleeper league [`1395904889149739008`](https://api.sleeper.app/v1/league/1395904889149739008).

10-team Superflex, Half-PPR (`rec=0.5`), 6-pt passing TDs, no K/DST. Bots trade strictly off the 1–100 values in `ff-intel/latest.json`.

## There was no generator

The Aug 31 packet was a one-off intel writeup. This repo now has a reproducible valuation engine (`src/ff_intel/`) that scores every rostered player.

## Formula v1.0.0

Each component is scored **0–100 within position** (rostered players only), then weighted:

| Weight | Component | Input |
|---|---|---|
| 35% | Projection | Remaining-season points: **70% Sleeper weekly projections** (weeks now→18, converted to this league’s scoring) + **30% run-rate** (played-week PPG × remaining projected games) |
| 25% | Production | Current-season PPG from Sleeper `matchups[week].players_points`. Weeks with 0 snaps / DNP / bye excluded |
| 20% | Role | Snap / carry / target share from Sleeper weekly stats; QB starter vs backup |
| 15% | Upside | Sleeper `search_rank` (pedigree), rookie year, injured starter ahead, buy-low (role ≥70th pct and production ≤40th) |
| 5% | News/trend | Last-2-week PPG vs season + Sleeper 48h trending adds + injury drag |

Then:

1. Multiply by the injury modifier.
2. Stretch so the top raw score = **98**.
3. Apply Superflex floors/caps.
4. Clamp to **1–100**. Round to the displayed integer. JSON keeps `formula_value`.

### Injury modifiers

| Status | Multiplier |
|---|---|
| Healthy | 1.00 |
| Questionable | 0.95 (−5%) |
| Doubtful | 0.80 |
| Out | 0.65 (−35%) |
| IR / PUP / Suspended | 0.50 + 0.50 × (1 − weeks_out / remaining_weeks). Season-ending = 0.50 |

### Superflex floors / caps

- Healthy **named starting QB** floor **45**.
- **Backup QB** cap **25**, unless that team’s starter is IR/Out/PUP/Suspended.
- **Committee / backup RB** (carry share **< 40%**) cap **30**.

`GUESS` is set when role share, return week, or projection had to be inferred. The markdown shows `52 GUESS (51.8)` — integer for bots, formula number in parentheses.

## Run

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m ff_intel.generate
# Push the board the bots already read (needs GH_TOKEN):
python -m ff_intel.generate --vs-github --publish-github
```

Writes `ff-intel/latest.md`, `ff-intel/latest.json`, and `ff-intel/archive/YYYY-MM-DD.{md,json}`.

`latest.json` includes both `players[]` (formula components) and `trade_board[]` (`player`, `pos`, `value`, `tier`, `trend`, `note`) so existing Grok team bots keep working.

## Validation (build fails)

- Every rostered player (active + IR) has a value.
- No healthy named starting QB below 45.
- No backup QB above 25 while the starter is healthy.
- No committee/backup RB above 30.
- Sanity block lists the 15 largest gaps between value and production percentile.

## Schedule

Bots read **https://github.com/MisterBackus/ff-intel** (`ff-intel/latest.json` → `trade_board`).

This engine regenerates twice daily at **8:00 AM ET** and **6:00 PM ET**:

1. Cursor timers on this agent (also re-armed on each run; they expire after ~7 days).
2. GitHub Action `.github/workflows/board.yml` once the engine lives on `MisterBackus/ff-intel` (`workflow_dispatch` after injury news).

Each run overwrites `latest.md` / `latest.json`, writes the dated archive, and commits. `--publish-github` pushes that commit to `main` on GitHub when `GH_TOKEN` or `gh` auth is present. Without GitHub write access the local board still updates; the live bot board does not.

## Files

| Path | What |
|---|---|
| `src/ff_intel/` | Formula, Sleeper I/O, validators, renderer |
| `ff-intel/latest.md` | Human board |
| `ff-intel/latest.json` | Bot board + component scores |
| `ff-intel/archive/` | Dated snapshots |
