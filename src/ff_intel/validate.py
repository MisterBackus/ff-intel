"""Board validators. Fail the build if any rule is broken."""

from __future__ import annotations

from ff_intel.config import QB_BACKUP_CAP, QB_STARTER_FLOOR, RB_COMMITTEE_CAP, RB_COMMITTEE_CARRY_SHARE
from ff_intel.formula import HEALTHY_STATUSES, PlayerInput, PlayerValue, production_ppg
from ff_intel.render import BOT_TRADE_KEYS


class ValidationError(Exception):
    pass


def validate(
    values: list[PlayerValue],
    inputs: list[PlayerInput],
    rostered_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    by_id = {v.player_id: v for v in values}
    inp_by_id = {p.player_id: p for p in inputs}

    missing = sorted(rostered_ids - set(by_id))
    if missing:
        errors.append(f"missing values for {len(missing)} rostered players: {missing[:8]}")

    extra_blank = [v.player_id for v in values if v.value is None]
    if extra_blank:
        errors.append(f"blank values: {extra_blank}")

    for v in values:
        inp = inp_by_id.get(v.player_id)
        if not inp:
            continue
        healthy = inp.injury_status in HEALTHY_STATUSES
        if (
            inp.pos == "QB"
            and inp.is_named_starter_qb
            and healthy
            and v.value < QB_STARTER_FLOOR
        ):
            errors.append(
                f"healthy starting QB below {QB_STARTER_FLOOR}: {v.name}={v.value}"
            )
        if (
            inp.pos == "QB"
            and inp.is_backup_qb
            and not inp.starter_injured
            and v.value > QB_BACKUP_CAP
        ):
            errors.append(f"backup QB above {QB_BACKUP_CAP}: {v.name}={v.value}")
        if (
            inp.pos == "RB"
            and inp.carry_share is not None
            and inp.carry_share < RB_COMMITTEE_CARRY_SHARE
            and v.value > RB_COMMITTEE_CAP
        ):
            errors.append(
                f"committee/backup RB above {RB_COMMITTEE_CAP}: {v.name}={v.value} share={inp.carry_share:.2f}"
            )
        if not (1 <= v.value <= 100):
            errors.append(f"value out of 1-100: {v.name}={v.value}")

    if errors:
        raise ValidationError("\n".join(errors))
    return []


def validate_bot_contract(payload: dict) -> None:
    """Fail if trade_board is not the schema Grok bots already parse."""
    board = payload.get("trade_board")
    if not isinstance(board, list) or not board:
        raise ValidationError("trade_board missing or empty")
    errors: list[str] = []
    for i, row in enumerate(board):
        if set(row) != set(BOT_TRADE_KEYS):
            errors.append(f"trade_board[{i}] keys={sorted(row)} expected {list(BOT_TRADE_KEYS)}")
            continue
        if not isinstance(row["player"], str) or not row["player"].strip():
            errors.append(f"trade_board[{i}] blank player")
        if row["pos"] not in {"QB", "RB", "WR", "TE"}:
            errors.append(f"trade_board[{i}] bad pos {row['pos']}")
        if not isinstance(row["value"], int) or not (1 <= row["value"] <= 100):
            errors.append(f"trade_board[{i}] value {row.get('value')}")
        if row["trend"] not in {"up", "down", "flat"}:
            errors.append(f"trade_board[{i}] trend {row.get('trend')}")
        if not isinstance(row["note"], str):
            errors.append(f"trade_board[{i}] note not string")
    if errors:
        raise ValidationError("\n".join(errors[:12]))


def sanity_gaps(values: list[PlayerValue], n: int = 15) -> list[dict]:
    """Biggest |value - production percentile| with a one-line why."""
    rows = []
    for v in values:
        gap = abs(v.value - v.production)
        rows.append((gap, v))
    rows.sort(key=lambda x: x[0], reverse=True)
    out = []
    for gap, v in rows[:n]:
        out.append(
            {
                "player": v.name,
                "pos": v.pos,
                "value": v.value,
                "production": v.production,
                "gap": round(gap, 1),
                "why": v.why,
            }
        )
    return out
