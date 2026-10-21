"""Pure valuation formula. No I/O."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from ff_intel.config import (
    MAX_VALUE,
    MIN_VALUE,
    MOD_IR_BASE,
    MOD_OUT,
    MOD_QUESTIONABLE,
    QB_BACKUP_CAP,
    QB_STARTER_FLOOR,
    RB_COMMITTEE_CAP,
    RB_COMMITTEE_CARRY_SHARE,
    SEASON_END_WEEK,
    TOP_VALUE,
    WEIGHTS,
)

HEALTHY_STATUSES = {None, "", "Healthy"}
IR_STATUSES = {"IR", "PUP", "Sus", "SUS", "Suspended", "NA", "COV", "COVID", "DNR"}


@dataclass
class PlayerInput:
    player_id: str
    name: str
    pos: str
    team: str | None
    owner_id: str | None
    roster_id: int | None
    injury_status: str | None
    depth_chart_order: int | None
    years_exp: int | None
    search_rank: int | None
    rookie_year: str | None
    # League-scored points for weeks the player actually played (no DNP/bye/0).
    weekly_points: list[float] = field(default_factory=list)
    # Remaining-season Half-PPR (6pt pass TD) projection.
    ros_projection: float = 0.0
    projection_source: str = "sleeper_weekly"
    # Role
    snap_share: float | None = None
    carry_share: float | None = None
    target_share: float | None = None
    games_started: int = 0
    is_named_starter_qb: bool = False
    is_backup_qb: bool = False
    starter_injured: bool = False
    # Remaining weeks in fantasy season (including current).
    remaining_weeks: int = 12
    expected_return_week: int | None = None
    recent_ppg: float | None = None  # last 2 played weeks
    trending_adds: int = 0
    guess_role: bool = False
    guess_return: bool = False
    guess_projection: bool = False
    bye_this_week: bool = False
    previous_value: float | None = None


@dataclass
class PlayerValue:
    player_id: str
    name: str
    pos: str
    team: str | None
    owner_id: str | None
    roster_id: int | None
    value: int
    formula_value: float
    guess: bool
    projection: float
    production: float
    role: float
    upside: float
    news: float
    raw_weighted: float
    injury_mult: float
    ppg: float | None
    games: int
    ros_projection: float
    role_tag: str
    injury_tag: str
    bye_this_week: bool
    change: float | None
    why: str
    projection_source: str
    snap_share: float | None
    carry_share: float | None
    target_share: float | None

    def as_json(self) -> dict[str, Any]:
        return asdict(self)


def percentile_scores(values: list[float | None]) -> list[float]:
    """0-100 within the group. Higher raw value = higher score. None → 0."""
    present = [(i, v) for i, v in enumerate(values) if v is not None]
    out = [0.0] * len(values)
    if not present:
        return out
    if len(present) == 1:
        out[present[0][0]] = 50.0
        return out
    groups: dict[float, list[int]] = {}
    for i, v in present:
        groups.setdefault(v, []).append(i)
    n = len(present)
    rank_cursor = 0
    for raw in sorted(groups):
        idxs = groups[raw]
        k = len(idxs)
        avg_rank = rank_cursor + (k - 1) / 2
        score = 100.0 * avg_rank / (n - 1)
        for i in idxs:
            out[i] = score
        rank_cursor += k
    return out


def production_ppg(weekly_points: list[float]) -> float | None:
    played = [p for p in weekly_points if p is not None]
    if not played:
        return None
    return sum(played) / len(played)


def injury_multiplier(
    status: str | None,
    *,
    current_week: int,
    expected_return_week: int | None,
    remaining_weeks: int,
) -> float:
    if status in HEALTHY_STATUSES:
        return 1.0
    key = (status or "").strip()
    if key == "Questionable":
        return MOD_QUESTIONABLE
    if key == "Doubtful":
        return (MOD_OUT + MOD_QUESTIONABLE) / 2
    if key == "Out":
        return MOD_OUT
    if key in IR_STATUSES:
        rem = max(1, remaining_weeks)
        if expected_return_week is None or expected_return_week > SEASON_END_WEEK:
            return MOD_IR_BASE
        weeks_out = max(0, expected_return_week - current_week)
        # Full -50% if gone the rest of the year; fades toward 1.0 if back soon.
        return MOD_IR_BASE + (1.0 - MOD_IR_BASE) * max(0.0, 1.0 - weeks_out / rem)
    return 1.0


def apply_positional_bounds(
    value: float,
    *,
    pos: str,
    is_named_starter_qb: bool,
    is_backup_qb: bool,
    starter_injured: bool,
    healthy: bool,
    carry_share: float | None,
) -> float:
    if pos == "QB" and is_named_starter_qb and healthy:
        value = max(value, QB_STARTER_FLOOR)
    if pos == "QB" and is_backup_qb and not starter_injured:
        value = min(value, QB_BACKUP_CAP)
    if pos == "RB" and carry_share is not None and carry_share < RB_COMMITTEE_CARRY_SHARE:
        value = min(value, RB_COMMITTEE_CAP)
    return value


def clamp(value: float) -> float:
    return max(MIN_VALUE, min(MAX_VALUE, value))


def stretch_top(values: list[float], top: float = TOP_VALUE) -> list[float]:
    mx = max(values) if values else 0.0
    if mx <= 0:
        return values
    return [v * top / mx for v in values]


def role_tag(
    pos: str,
    *,
    is_named_starter_qb: bool,
    is_backup_qb: bool,
    carry_share: float | None,
    snap_share: float | None,
    depth_chart_order: int | None,
) -> str:
    if pos == "QB":
        if is_named_starter_qb:
            return "QB1"
        if is_backup_qb:
            return "QB2"
        return "QB"
    if pos == "RB":
        share = carry_share if carry_share is not None else snap_share
        if share is not None and share >= 0.55:
            return "RB1"
        if share is not None and share >= RB_COMMITTEE_CARRY_SHARE:
            return "RB1-split"
        if share is not None:
            return "committee"
        if depth_chart_order == 1:
            return "RB1-guess"
        return "backup"
    if depth_chart_order == 1:
        return f"{pos}1"
    if depth_chart_order == 2:
        return f"{pos}2"
    return pos


def injury_tag(status: str | None) -> str:
    if status in HEALTHY_STATUSES:
        return "Healthy"
    return status or "Healthy"


def news_score(inp: PlayerInput) -> float:
    """50 = flat. Recent form and waiver heat move it."""
    score = 50.0
    season = production_ppg(inp.weekly_points)
    if season and inp.recent_ppg is not None:
        delta = inp.recent_ppg - season
        score += max(-25.0, min(25.0, delta * 2.5))
    if inp.trending_adds >= 200_000:
        score += 15
    elif inp.trending_adds >= 50_000:
        score += 8
    if inp.injury_status in IR_STATUSES:
        score -= 10
    elif inp.injury_status == "Out":
        score -= 8
    elif inp.injury_status == "Questionable":
        score -= 3
    return clamp(score)


def upside_score(
    inp: PlayerInput,
    *,
    prod_pct: float,
    role_pct: float,
) -> float:
    """Pedigree + opportunity + buy-low (volume without points)."""
    score = 40.0
    rank = inp.search_rank
    if rank is not None:
        if rank <= 15:
            score += 35
        elif rank <= 40:
            score += 25
        elif rank <= 80:
            score += 15
        elif rank <= 150:
            score += 6
        else:
            score -= 5
    years = inp.years_exp if inp.years_exp is not None else 3
    if years <= 1:
        score += 8
    elif years <= 2:
        score += 4
    # Opportunity: injured starter ahead / depth doesn't match usage.
    if inp.starter_injured and inp.is_backup_qb:
        score += 20
    if inp.pos == "RB" and inp.carry_share and inp.carry_share >= 0.50:
        score += 8
    if inp.pos in {"WR", "TE"} and inp.target_share and inp.target_share >= 0.22:
        score += 8
    # Buy-low: role/volume high, production lagging.
    if role_pct >= 70 and prod_pct <= 40:
        score += 15
    elif role_pct >= 60 and prod_pct <= 35:
        score += 10
    return clamp(score)


def score_components(
    players: list[PlayerInput],
) -> list[tuple[PlayerInput, dict[str, float]]]:
    by_pos: dict[str, list[int]] = {}
    for i, p in enumerate(players):
        by_pos.setdefault(p.pos, []).append(i)

    proj = [0.0] * len(players)
    prod = [0.0] * len(players)
    role = [0.0] * len(players)
    for pos, idxs in by_pos.items():
        proj_raw = [players[i].ros_projection for i in idxs]
        prod_raw = [production_ppg(players[i].weekly_points) for i in idxs]
        role_raw = [_role_raw(players[i]) for i in idxs]
        for i, s in zip(idxs, percentile_scores(proj_raw)):
            proj[i] = s
        for i, s in zip(idxs, percentile_scores(prod_raw)):
            prod[i] = s
        for i, s in zip(idxs, percentile_scores(role_raw)):
            role[i] = s

    out = []
    for i, p in enumerate(players):
        ups = upside_score(p, prod_pct=prod[i], role_pct=role[i])
        news = news_score(p)
        out.append(
            (
                p,
                {
                    "projection": proj[i],
                    "production": prod[i],
                    "role": role[i],
                    "upside": ups,
                    "news": news,
                },
            )
        )
    return out


def _role_raw(p: PlayerInput) -> float:
    if p.pos == "QB":
        if p.is_named_starter_qb:
            return 90.0 + (5.0 if p.games_started >= 4 else 0.0)
        if p.is_backup_qb and p.starter_injured:
            return 70.0
        if p.is_backup_qb:
            return 20.0
        return 50.0
    share = None
    if p.pos == "RB":
        share = p.carry_share if p.carry_share is not None else p.snap_share
    elif p.pos in {"WR", "TE"}:
        share = p.target_share if p.target_share is not None else p.snap_share
    if share is not None:
        return 100.0 * max(0.0, min(1.0, share))
    if p.depth_chart_order == 1:
        return 70.0
    if p.depth_chart_order == 2:
        return 40.0
    if p.depth_chart_order and p.depth_chart_order >= 3:
        return 15.0
    return 25.0


def value_players(players: list[PlayerInput], *, current_week: int) -> list[PlayerValue]:
    scored = score_components(players)
    raws: list[float] = []
    metas: list[tuple[PlayerInput, dict[str, float], float, float]] = []
    for p, comps in scored:
        raw = sum(WEIGHTS[k] * comps[k] for k in WEIGHTS)
        rem = max(1, p.remaining_weeks)
        mult = injury_multiplier(
            p.injury_status,
            current_week=current_week,
            expected_return_week=p.expected_return_week,
            remaining_weeks=rem,
        )
        adjusted = raw * mult
        raws.append(adjusted)
        metas.append((p, comps, raw, mult))

    stretched = stretch_top(raws, TOP_VALUE)
    results: list[PlayerValue] = []
    for (p, comps, raw, mult), stretched_v in zip(metas, stretched):
        healthy = p.injury_status in HEALTHY_STATUSES
        bounded = apply_positional_bounds(
            stretched_v,
            pos=p.pos,
            is_named_starter_qb=p.is_named_starter_qb,
            is_backup_qb=p.is_backup_qb,
            starter_injured=p.starter_injured,
            healthy=healthy,
            carry_share=p.carry_share,
        )
        formula_v = round(clamp(bounded), 2)
        value = int(round(formula_v))
        value = max(MIN_VALUE, min(MAX_VALUE, value))
        guess = p.guess_role or p.guess_return or p.guess_projection
        ppg = production_ppg(p.weekly_points)
        change = None
        if p.previous_value is not None:
            change = round(value - p.previous_value, 1)
        why = _why(p, comps, change, guess, mult)
        results.append(
            PlayerValue(
                player_id=p.player_id,
                name=p.name,
                pos=p.pos,
                team=p.team,
                owner_id=p.owner_id,
                roster_id=p.roster_id,
                value=value,
                formula_value=formula_v,
                guess=guess,
                projection=round(comps["projection"], 2),
                production=round(comps["production"], 2),
                role=round(comps["role"], 2),
                upside=round(comps["upside"], 2),
                news=round(comps["news"], 2),
                raw_weighted=round(raw, 2),
                injury_mult=round(mult, 3),
                ppg=round(ppg, 2) if ppg is not None else None,
                games=len(p.weekly_points),
                ros_projection=round(p.ros_projection, 2),
                role_tag=role_tag(
                    p.pos,
                    is_named_starter_qb=p.is_named_starter_qb,
                    is_backup_qb=p.is_backup_qb,
                    carry_share=p.carry_share,
                    snap_share=p.snap_share,
                    depth_chart_order=p.depth_chart_order,
                ),
                injury_tag=injury_tag(p.injury_status),
                bye_this_week=p.bye_this_week,
                change=change,
                why=why,
                projection_source=p.projection_source,
                snap_share=p.snap_share,
                carry_share=p.carry_share,
                target_share=p.target_share,
            )
        )
    return results


def _why(
    p: PlayerInput,
    comps: dict[str, float],
    change: float | None,
    guess: bool,
    mult: float,
) -> str:
    bits = []
    if change is not None and abs(change) >= 8:
        bits.append(f"{change:+.0f} vs last board")
    if p.injury_status and p.injury_status not in HEALTHY_STATUSES:
        bits.append(f"{p.injury_status} x{mult:.2f}")
    if p.is_backup_qb and not p.starter_injured:
        bits.append("backup QB cap 25")
    if p.pos == "RB" and p.carry_share is not None and p.carry_share < RB_COMMITTEE_CARRY_SHARE:
        bits.append(f"committee RB {p.carry_share:.0%} cap 30")
    if p.is_named_starter_qb and p.injury_status in HEALTHY_STATUSES:
        bits.append("SF QB1 floor 45")
    if comps["production"] + 20 < comps["role"]:
        bits.append("buy-low: volume > points")
    if guess:
        bits.append("GUESS inputs")
    if not bits:
        bits.append(
            f"proj {comps['projection']:.0f} / prod {comps['production']:.0f} / role {comps['role']:.0f}"
        )
    return "; ".join(bits)
