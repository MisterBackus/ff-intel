"""Build the trade board from live Sleeper data."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ff_intel.assemble import build_inputs, norm_name, rostered_ids
from ff_intel.config import FORMULA_VERSION, GITHUB_LATEST_URL, GITHUB_REPO, LEAGUE_ID
from ff_intel.formula import value_players
from ff_intel.render import et_now, merge_live_packet, render_json, render_md, stamp, write_outputs
from ff_intel.sleeper import (
    fetch_weeks_projections,
    fetch_weeks_stats,
    league,
    matchups,
    nfl_state,
    players,
    remaining_weeks,
    rosters,
    trending_adds,
)
from ff_intel.validate import ValidationError, sanity_gaps, validate, validate_bot_contract


SOURCES = [
    "Sleeper weekly projections (remaining regular-season weeks), converted to this league's Half-PPR / 6-pt pass TD scoring",
    "Sleeper league matchup players_points for production (played weeks only)",
    "Sleeper weekly player stats for snap / carry / target share",
    "Sleeper player directory for injury status, depth chart, search_rank",
    "Sleeper trending adds (48h) for the news/trend component",
]


def _ingest_board(data: dict, out: dict[str, float]) -> None:
    for row in data.get("players") or []:
        pid = str(row.get("player_id") or "")
        name = str(row.get("name") or row.get("player") or "")
        if row.get("value") is None:
            continue
        val = float(row["value"])
        if pid:
            out[pid] = val
        if name:
            out[norm_name(name)] = val
    for row in data.get("trade_board") or []:
        name = str(row.get("player") or "")
        if name and row.get("value") is not None:
            out.setdefault(norm_name(name), float(row["value"]))


def load_previous(path: Path) -> dict[str, float]:
    out: dict[str, float] = {}
    if path.exists():
        try:
            _ingest_board(json.loads(path.read_text()), out)
        except json.JSONDecodeError:
            pass
    return out


def load_github_packet(url: str = GITHUB_LATEST_URL) -> dict:
    """Full live GitHub latest.json (injuries/faab/start_sit + trade_board)."""
    import urllib.error
    import urllib.request

    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read().decode())
            return data if isinstance(data, dict) else {}
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError):
        return {}


def load_github_previous(url: str = GITHUB_LATEST_URL) -> dict[str, float]:
    """Live GitHub board the bots already read. Used for deltas on first publish."""
    out: dict[str, float] = {}
    _ingest_board(load_github_packet(url), out)
    return out


def run(
    league_id: str = LEAGUE_ID,
    root: str = "ff-intel",
    *,
    vs_github: bool = False,
    merge_live: bool = False,
) -> dict:
    state = nfl_state()
    current_week = int(state.get("display_week") or state.get("week") or 1)
    season = int(state.get("season") or 2026)
    last_scored = int(state.get("leg") or current_week) - 1
    if last_scored < 1:
        last_scored = 0

    lg = league(league_id)
    roster_rows = rosters(league_id)
    rmap = rostered_ids(roster_rows)
    if not rmap:
        raise SystemExit("no rostered players")

    played_weeks = list(range(1, last_scored + 1))
    rem = remaining_weeks(current_week)

    matchups_by_week = {wk: matchups(wk, league_id) for wk in played_weeks} if played_weeks else {}
    stats_by_week = fetch_weeks_stats(season, played_weeks) if played_weeks else {}
    proj_by_week = fetch_weeks_projections(season, rem)
    meta = players()
    trend = trending_adds()
    if vs_github:
        prev = load_github_previous()
    else:
        prev = load_previous(Path(root) / "latest.json")

    inputs = build_inputs(
        roster_map=rmap,
        players_meta=meta,
        matchups_by_week=matchups_by_week,
        stats_by_week=stats_by_week,
        proj_by_week=proj_by_week,
        trending=trend,
        current_week=current_week,
        previous_values=prev,
    )
    values = value_players(inputs, current_week=current_week)
    validate(values, inputs, set(rmap))
    sanity = sanity_gaps(values, 15)

    now = et_now()
    generated = stamp(now)
    commit_message = f"intel: {now.strftime('%Y-%m-%d')} week {current_week} values {FORMULA_VERSION}"
    payload = render_json(
        values,
        generated_at_et=generated,
        nfl_week=current_week,
        sanity=sanity,
        sources=SOURCES,
        commit_message=commit_message,
    )
    payload["league"]["sleeper_name"] = lg.get("name")
    validate_bot_contract(payload)
    if merge_live or vs_github:
        # Keep injuries/FAAB/start-sit from the live GitHub packet. Never let
        # that packet's trade_board replace formula 1.0.0 values.
        payload = merge_live_packet(load_github_packet(), payload)
        validate_bot_contract(payload)
    md = render_md(
        values,
        generated_at_et=generated,
        nfl_week=current_week,
        sanity=sanity,
        sources=SOURCES,
        commit_message=commit_message,
    )
    write_outputs(md, payload, now.strftime("%Y-%m-%d"), root=root)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate the ff-intel trade value board")
    parser.add_argument("--league-id", default=LEAGUE_ID)
    parser.add_argument("--root", default="ff-intel")
    parser.add_argument(
        "--vs-github",
        action="store_true",
        help="Compute Δ against github.com/MisterBackus/ff-intel latest.json",
    )
    parser.add_argument(
        "--publish-github",
        action="store_true",
        help="Push latest.md/json + engine to github.com/MisterBackus/ff-intel",
    )
    args = parser.parse_args(argv)
    try:
        payload = run(
            league_id=args.league_id,
            root=args.root,
            vs_github=args.vs_github,
            merge_live=args.publish_github or args.vs_github,
        )
    except ValidationError as exc:
        print("VALIDATION FAILED\n", exc, file=sys.stderr)
        return 1
    n = len(payload.get("players") or [])
    print(f"wrote {n} players week {payload.get('nfl_week')} formula {payload.get('formula_version')}")
    if args.publish_github:
        from ff_intel.publish import publish_github

        try:
            publish_github(root=args.root, commit_message=str(payload.get("commit_message") or "intel: update"))
        except Exception as exc:
            print(f"GITHUB NOT UPDATED (github.com/{GITHUB_REPO}): {exc}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
