"""Turn Sleeper payloads into PlayerInput rows."""

from __future__ import annotations

from collections import defaultdict

from ff_intel.config import SEASON_END_WEEK
from ff_intel.formula import PlayerInput, production_ppg
from ff_intel.sleeper import project_points


def rostered_ids(rosters: list[dict]) -> dict[str, tuple[int, str | None]]:
    """player_id -> (roster_id, owner_id). Includes IR/reserve."""
    out: dict[str, tuple[int, str | None]] = {}
    for r in rosters:
        rid = int(r["roster_id"])
        owner = r.get("owner_id")
        for pid in (r.get("players") or []) + (r.get("reserve") or []):
            out[str(pid)] = (rid, owner)
    return out


def norm_name(name: str) -> str:
    """Collapse Jr/Sr/II suffixes so GitHub board names match Sleeper names."""
    n = " ".join((name or "").lower().split())
    for suf in (" jr.", " jr", " sr.", " sr", " iii", " ii", " iv"):
        if n.endswith(suf):
            n = n[: -len(suf)].rstrip()
    return n


def _previous_value(previous_values: dict[str, float], pid: str, name: str) -> float | None:
    if pid in previous_values:
        return previous_values[pid]
    key = norm_name(name)
    if key in previous_values:
        return previous_values[key]
    return None


def played_points(
    matchups_by_week: dict[int, list[dict]],
    stats_by_week: dict[int, dict[str, dict]],
    player_id: str,
) -> list[float]:
    """League points for weeks the player actually played. Drops DNP/bye/zero-snap."""
    pts: list[float] = []
    for week in sorted(matchups_by_week):
        scored = None
        for entry in matchups_by_week[week]:
            pp = entry.get("players_points") or {}
            if player_id in pp:
                scored = float(pp[player_id])
                break
        if scored is None:
            continue
        st = (stats_by_week.get(week) or {}).get(player_id) or {}
        snaps = st.get("off_snp")
        if snaps is not None and float(snaps) <= 0:
            continue
        if scored == 0.0 and (snaps is None or float(snaps) <= 0):
            continue
        if scored == 0.0 and not st.get("gp") and not st.get("gms_active"):
            continue
        pts.append(scored)
    return pts


def team_shares(
    stats_by_week: dict[int, dict[str, dict]],
    players_meta: dict[str, dict],
    player_ids: list[str],
) -> dict[str, dict[str, float | None]]:
    """Season snap / carry / target share from weeks with snaps."""
    team_rb_att: dict[str, float] = defaultdict(float)
    team_targets: dict[str, float] = defaultdict(float)
    team_snaps: dict[str, float] = defaultdict(float)
    player_att: dict[str, float] = defaultdict(float)
    player_tgt: dict[str, float] = defaultdict(float)
    player_snp: dict[str, float] = defaultdict(float)
    player_tm_snp: dict[str, float] = defaultdict(float)

    for _week, table in stats_by_week.items():
        for pid, st in table.items():
            meta = players_meta.get(pid) or {}
            team = meta.get("team")
            if not team:
                continue
            att = float(st.get("rush_att") or 0)
            tgt = float(st.get("rec_tgt") or st.get("tar") or 0)
            snp = float(st.get("off_snp") or 0)
            tm = float(st.get("tm_off_snp") or 0)
            pos = meta.get("position")
            if pos == "RB":
                team_rb_att[team] += att
            if pos in {"WR", "TE", "RB"}:
                team_targets[team] += tgt
            if snp:
                player_snp[pid] += snp
                if tm:
                    player_tm_snp[pid] += tm
            player_att[pid] += att
            player_tgt[pid] += tgt

    out: dict[str, dict[str, float | None]] = {}
    for pid in player_ids:
        meta = players_meta.get(pid) or {}
        team = meta.get("team")
        carry = None
        tgt_share = None
        snap = None
        if team and team_rb_att[team] > 0 and meta.get("position") == "RB":
            carry = player_att[pid] / team_rb_att[team]
        if team and team_targets[team] > 0 and meta.get("position") in {"WR", "TE", "RB"}:
            tgt_share = player_tgt[pid] / team_targets[team]
        if player_tm_snp[pid] > 0:
            snap = player_snp[pid] / player_tm_snp[pid]
        out[pid] = {"carry_share": carry, "target_share": tgt_share, "snap_share": snap}
    return out


def games_started(stats_by_week: dict[int, dict[str, dict]], player_id: str) -> int:
    n = 0
    for table in stats_by_week.values():
        st = table.get(player_id) or {}
        if float(st.get("off_snp") or 0) >= 20 or float(st.get("pass_att") or 0) >= 10:
            n += 1
    return n


def qb_roles(
    rostered: list[str],
    players_meta: dict[str, dict],
    stats_by_week: dict[int, dict[str, dict]],
    ros: dict[str, float],
) -> dict[str, dict[str, bool]]:
    """Named starter vs backup, and whether the team's starter is hurt."""
    by_team: dict[str, list[str]] = defaultdict(list)
    for pid in rostered:
        meta = players_meta.get(pid) or {}
        if meta.get("position") != "QB":
            continue
        team = meta.get("team")
        if team:
            by_team[team].append(pid)

    # Also consider non-rostered QBs on the same NFL team for "who is the starter".
    for pid, meta in players_meta.items():
        if meta.get("position") != "QB" or not meta.get("team"):
            continue
        if meta.get("status") not in {None, "Active", "Injured Reserve", "Inactive"}:
            continue
        by_team[meta["team"]].append(pid)
    for team in by_team:
        by_team[team] = list(dict.fromkeys(by_team[team]))

    out: dict[str, dict[str, bool]] = {}
    for pid in rostered:
        meta = players_meta.get(pid) or {}
        if meta.get("position") != "QB":
            continue
        team = meta.get("team")
        teammates = by_team.get(team or "", [pid])

        def starter_score(qid: str) -> tuple:
            m = players_meta.get(qid) or {}
            started = games_started(stats_by_week, qid)
            depth = m.get("depth_chart_order")
            depth_s = depth if isinstance(depth, int) else 99
            inj = m.get("injury_status")
            inj_pen = 50 if inj in {"IR", "PUP", "Out", "Suspended"} else 0
            return (-started, depth_s + inj_pen, -(ros.get(qid) or 0), int(m.get("search_rank") or 9999))

        ranked = sorted(teammates, key=starter_score)
        named = ranked[0] if ranked else pid
        # Established starters keep the label even if temporarily depth-charted behind.
        started = games_started(stats_by_week, pid)
        is_named = pid == named or started >= 2
        is_backup = not is_named
        starter_meta = players_meta.get(named) or {}
        starter_hurt = starter_meta.get("injury_status") in {"IR", "PUP", "Out", "Suspended", "Doubtful"}
        if pid == named:
            is_backup = False
            is_named = True
        out[pid] = {
            "is_named_starter_qb": is_named,
            "is_backup_qb": is_backup,
            "starter_injured": starter_hurt and is_backup,
        }
    return out


def guess_return_week(status: str | None, current_week: int) -> tuple[int | None, bool]:
    """IR/PUP default to +4 (minimum). Season-ending tags stay None. GUESS unless known."""
    if status in {None, "", "Healthy", "Questionable", "Doubtful", "Out"}:
        return None, False
    if status in {"IR", "PUP", "Suspended", "Sus"}:
        return min(SEASON_END_WEEK + 1, current_week + 4), True
    return None, False


def ros_projection(
    player_id: str,
    proj_by_week: dict[int, dict[str, dict]],
    weekly_points: list[float],
    remaining: list[int],
) -> tuple[float, str, bool]:
    """Consensus: 70% Sleeper remaining weekly proj + 30% run-rate * remaining games."""
    sleeper = 0.0
    games = 0
    for wk in remaining:
        st = (proj_by_week.get(wk) or {}).get(player_id)
        if not st:
            continue
        pts = project_points(st)
        if pts > 0:
            sleeper += pts
            games += 1
    ppg = production_ppg(weekly_points)
    games_left = games if games else len(remaining)
    run_rate = (ppg or 0.0) * games_left
    if sleeper <= 0 and (ppg or 0) <= 0:
        return 0.0, "sleeper_weekly+run_rate", True
    if sleeper <= 0:
        return run_rate, "run_rate_only", True
    if not ppg:
        return sleeper, "sleeper_weekly", False
    blended = 0.70 * sleeper + 0.30 * run_rate
    return blended, "sleeper_weekly+run_rate", False


def teams_playing(current_week: int, proj_by_week: dict[int, dict[str, dict]], players_meta: dict[str, dict]) -> set[str]:
    """NFL teams with a projected game this week (not on bye)."""
    playing: set[str] = set()
    table = proj_by_week.get(current_week) or {}
    for pid, st in table.items():
        if not (st.get("gp") or project_points(st) > 0):
            continue
        team = (players_meta.get(pid) or {}).get("team") or ""
        if team:
            playing.add(team)
    return playing


def bye_this_week(team: str | None, playing_teams: set[str]) -> bool:
    if not team:
        return False
    if not playing_teams:
        return False
    return team not in playing_teams


def build_inputs(
    *,
    roster_map: dict[str, tuple[int, str | None]],
    players_meta: dict[str, dict],
    matchups_by_week: dict[int, list[dict]],
    stats_by_week: dict[int, dict[str, dict]],
    proj_by_week: dict[int, dict[str, dict]],
    trending: dict[str, int],
    current_week: int,
    previous_values: dict[str, float],
) -> list[PlayerInput]:
    ids = list(roster_map)
    shares = team_shares(stats_by_week, players_meta, ids)
    remaining = list(range(current_week, SEASON_END_WEEK + 1))
    rem_n = len(remaining)
    ros_map = {}
    tmp_points = {}
    for pid in ids:
        tmp_points[pid] = played_points(matchups_by_week, stats_by_week, pid)
        ros, _, _ = ros_projection(pid, proj_by_week, tmp_points[pid], remaining)
        ros_map[pid] = ros
    roles = qb_roles(ids, players_meta, stats_by_week, ros_map)
    playing = teams_playing(current_week, proj_by_week, players_meta)

    inputs: list[PlayerInput] = []
    for pid in ids:
        meta = players_meta.get(pid) or {}
        pos = meta.get("position") or "WR"
        team = meta.get("team")
        weekly = tmp_points[pid]
        ros, src, guess_proj = ros_projection(pid, proj_by_week, weekly, remaining)
        sh = shares.get(pid) or {}
        carry = sh.get("carry_share")
        snap = sh.get("snap_share")
        tgt = sh.get("target_share")
        guess_role = False
        no_rb_usage = not weekly and (carry is None or carry == 0)
        if pos == "RB" and (carry is None or no_rb_usage):
            # No rush data yet (IR returners, new arrivals). Depth charts are stale.
            depth = meta.get("depth_chart_order")
            rank = meta.get("search_rank") or 999
            if isinstance(depth, int) and depth == 1:
                carry = 0.55
                guess_role = True
            elif isinstance(rank, int) and rank <= 40:
                # Elite name, unused so far — committee until touches prove otherwise.
                carry = 0.35
                guess_role = True
            else:
                carry = 0.20
                guess_role = True
        ret_wk, guess_ret = guess_return_week(meta.get("injury_status"), current_week)
        # Season-ending names we know from current 2026 reporting (still GUESS if notes missing).
        name = meta.get("full_name") or pid
        status = meta.get("injury_status")
        if status in {"IR", "PUP"} and _season_ending_name(name, meta):
            ret_wk = SEASON_END_WEEK + 1
            guess_ret = True
        recent = None
        if len(weekly) >= 1:
            recent = sum(weekly[-2:]) / min(2, len(weekly))
        qb = roles.get(pid) or {}
        rid, owner = roster_map[pid]
        rookie = None
        md = meta.get("metadata") or {}
        if isinstance(md, dict):
            rookie = md.get("rookie_year")
        inputs.append(
            PlayerInput(
                player_id=pid,
                name=name,
                pos=pos,
                team=team,
                owner_id=owner,
                roster_id=rid,
                injury_status=status,
                depth_chart_order=meta.get("depth_chart_order"),
                years_exp=meta.get("years_exp"),
                search_rank=meta.get("search_rank"),
                rookie_year=rookie,
                weekly_points=weekly,
                ros_projection=ros,
                projection_source=src,
                snap_share=round(snap, 3) if snap is not None else None,
                carry_share=round(carry, 3) if carry is not None else None,
                target_share=round(tgt, 3) if tgt is not None else None,
                games_started=games_started(stats_by_week, pid),
                is_named_starter_qb=bool(qb.get("is_named_starter_qb")),
                is_backup_qb=bool(qb.get("is_backup_qb")),
                starter_injured=bool(qb.get("starter_injured")),
                remaining_weeks=rem_n,
                expected_return_week=ret_wk,
                recent_ppg=recent,
                trending_adds=trending.get(pid, 0),
                guess_role=guess_role,
                guess_return=guess_ret,
                guess_projection=guess_proj,
                bye_this_week=bye_this_week(team, playing),
                previous_value=_previous_value(previous_values, pid, name),
            )
        )
    return inputs


def _season_ending_name(name: str, meta: dict) -> bool:
    notes = (meta.get("injury_notes") or "").lower()
    if "season" in notes or "year-ending" in notes or "out for the year" in notes:
        return True
    # Conservative known 2026 season-enders that bots must not overpay.
    return name in {
        "Jalen Hurts",
        "Jaxson Dart",
        "De'Von Achane",
        "Terry McLaurin",
        "Davante Adams",
        "Jayden Higgins",
        "Ricky Pearsall",
    }
