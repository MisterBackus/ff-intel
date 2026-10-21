"""Sleeper API I/O."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from ff_intel.config import LEAGUE_ID, SCORING_SETTINGS, SEASON_END_WEEK

BASE = "https://api.sleeper.app"
PROJ_BASE = "https://api.sleeper.app/projections/nfl"


def get_json(url: str, timeout: int = 60) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": "ff-intel/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def nfl_state() -> dict:
    return get_json(f"{BASE}/v1/state/nfl")


def league(league_id: str = LEAGUE_ID) -> dict:
    return get_json(f"{BASE}/v1/league/{league_id}")


def rosters(league_id: str = LEAGUE_ID) -> list[dict]:
    return get_json(f"{BASE}/v1/league/{league_id}/rosters")


def users(league_id: str = LEAGUE_ID) -> list[dict]:
    return get_json(f"{BASE}/v1/league/{league_id}/users")


def matchups(week: int, league_id: str = LEAGUE_ID) -> list[dict]:
    return get_json(f"{BASE}/v1/league/{league_id}/matchups/{week}")


def players() -> dict[str, dict]:
    return get_json(f"{BASE}/v1/players/nfl", timeout=120)


def trending_adds(lookback_hours: int = 48, limit: int = 50) -> dict[str, int]:
    rows = get_json(
        f"{BASE}/v1/players/nfl/trending/add?lookback_hours={lookback_hours}&limit={limit}"
    )
    return {str(r["player_id"]): int(r.get("count") or 0) for r in rows if r.get("player_id")}


def weekly_stats(season: int, week: int) -> dict[str, dict]:
    rows = get_json(f"{BASE}/stats/nfl/{season}/{week}?season_type=regular", timeout=90)
    out: dict[str, dict] = {}
    if isinstance(rows, list):
        for row in rows:
            pid = str(row.get("player_id") or "")
            if pid:
                out[pid] = row.get("stats") or {}
    elif isinstance(rows, dict):
        for pid, stats in rows.items():
            if isinstance(stats, dict) and "pts_half_ppr" in stats or "rush_att" in (stats or {}):
                out[str(pid)] = stats
            elif isinstance(stats, dict) and "stats" in stats:
                out[str(pid)] = stats["stats"]
    return out


def weekly_projections(season: int, week: int) -> dict[str, dict]:
    rows = get_json(f"{PROJ_BASE}/{season}/{week}?season_type=regular", timeout=90)
    out: dict[str, dict] = {}
    if isinstance(rows, list):
        for row in rows:
            pid = str(row.get("player_id") or "")
            if pid:
                out[pid] = row.get("stats") or {}
    return out


def fetch_weeks_stats(season: int, weeks: list[int]) -> dict[int, dict[str, dict]]:
    out: dict[int, dict[str, dict]] = {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        futs = {wk: pool.submit(weekly_stats, season, wk) for wk in weeks}
        for wk, fut in futs.items():
            try:
                out[wk] = fut.result()
            except urllib.error.URLError:
                out[wk] = {}
    return out


def fetch_weeks_projections(season: int, weeks: list[int]) -> dict[int, dict[str, dict]]:
    out: dict[int, dict[str, dict]] = {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        futs = {wk: pool.submit(weekly_projections, season, wk) for wk in weeks}
        for wk, fut in futs.items():
            try:
                out[wk] = fut.result()
            except urllib.error.URLError:
                out[wk] = {}
    return out


def project_points(stats: dict) -> float:
    pts = 0.0
    for key, weight in SCORING_SETTINGS.items():
        pts += float(stats.get(key) or 0) * weight
    return pts


def remaining_weeks(current_week: int) -> list[int]:
    return [w for w in range(current_week, SEASON_END_WEEK + 1)]
