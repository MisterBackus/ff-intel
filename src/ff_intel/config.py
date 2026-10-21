"""League + formula constants."""

from __future__ import annotations

LEAGUE_ID = "1395904889149739008"
LEAGUE_NAME = "Bot or Not Fantasy"
GITHUB_REPO = "MisterBackus/ff-intel"
GITHUB_LATEST_URL = (
    "https://raw.githubusercontent.com/MisterBackus/ff-intel/main/ff-intel/latest.json"
)
TEAMS = 10
SCORING = "half-ppr"
FORMAT = "superflex"
FORMULA_VERSION = "1.0.0"

WEIGHTS = {
    "projection": 0.35,
    "production": 0.25,
    "role": 0.20,
    "upside": 0.15,
    "news": 0.05,
}

TOP_VALUE = 98
MIN_VALUE = 1
MAX_VALUE = 100

QB_STARTER_FLOOR = 45
QB_BACKUP_CAP = 25
RB_COMMITTEE_CAP = 30
RB_COMMITTEE_CARRY_SHARE = 0.40

MOD_QUESTIONABLE = 0.95
MOD_OUT = 0.65
MOD_IR_BASE = 0.50  # -50% when out the rest of the year

SEASON_END_WEEK = 18
REGULAR_WEEKS = range(1, SEASON_END_WEEK + 1)

# League scoring (Sleeper league settings).
SCORING_SETTINGS = {
    "pass_yd": 0.04,
    "pass_td": 6.0,
    "pass_int": -1.0,
    "pass_2pt": 2.0,
    "rush_yd": 0.1,
    "rush_td": 6.0,
    "rush_2pt": 2.0,
    "rec": 0.5,
    "rec_yd": 0.1,
    "rec_td": 6.0,
    "rec_2pt": 2.0,
    "fum_lost": -2.0,
}

SKILL_POS = ("QB", "RB", "WR", "TE")
