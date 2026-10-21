"""Markdown + JSON board output."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

from ff_intel.config import (
    FORMULA_VERSION,
    FORMAT,
    LEAGUE_ID,
    LEAGUE_NAME,
    SCORING,
    TEAMS,
    WEIGHTS,
)
from ff_intel.formula import PlayerValue


def et_now() -> datetime:
    return datetime.now(ZoneInfo("America/New_York"))


def stamp(now: datetime | None = None) -> str:
    now = now or et_now()
    return now.strftime("%Y-%m-%d %I:%M %p %Z")


def _trend(change: float | None) -> str:
    if change is None or change == 0:
        return "flat"
    return "up" if change > 0 else "down"


BOT_TRADE_KEYS = ("player", "pos", "value", "tier", "trend", "note")


def trade_board_row(v: PlayerValue) -> dict:
    """Exact contract Grok team bots already parse from GitHub latest.json."""
    bits: list[str] = []
    if v.why:
        bits.append(v.why)
    if v.guess and "GUESS" not in (v.why or ""):
        bits.append("GUESS")
    if v.bye_this_week and "bye" not in (v.why or "").lower():
        bits.append("bye this week")
    return {
        "player": v.name,
        "pos": v.pos,
        "value": int(v.value),
        "tier": v.role_tag or v.pos,
        "trend": _trend(v.change),
        "note": "; ".join(bits) or v.injury_tag,
    }


def merge_live_packet(live: dict | None, payload: dict) -> dict:
    """Keep injuries/faab/start_sit/etc. Overlay formula trade_board the bots read."""
    out = dict(live or {})
    league = dict(out.get("league") or {})
    league.update(payload.get("league") or {})
    out.update(
        {
            "generated_at_et": payload["generated_at_et"],
            "nfl_week": str(payload["nfl_week"]),
            "formula_version": payload.get("formula_version"),
            "league": league,
            "weights": payload.get("weights"),
            "sources": payload.get("sources"),
            "commit_message": payload.get("commit_message"),
            "sanity_gaps": payload.get("sanity_gaps"),
            "trade_board": [ {k: row[k] for k in BOT_TRADE_KEYS} for row in payload.get("trade_board") or [] ],
            "players": payload.get("players"),
        }
    )
    return out


def render_json(
    values: list[PlayerValue],
    *,
    generated_at_et: str,
    nfl_week: int,
    sanity: list[dict],
    sources: list[str],
    commit_message: str,
) -> dict:
    ranked = sorted(values, key=lambda x: (-x.value, x.name))
    return {
        "formula_version": FORMULA_VERSION,
        "generated_at_et": generated_at_et,
        "nfl_week": nfl_week,
        "league": {
            "id": LEAGUE_ID,
            "name": LEAGUE_NAME,
            "teams": TEAMS,
            "format": FORMAT,
            "scoring": SCORING,
            "faab": 100,
            "no_k": True,
            "no_dst": True,
            "platform": "sleeper",
            "season": 2026,
        },
        "weights": WEIGHTS,
        "sources": sources,
        "commit_message": commit_message,
        "sanity_gaps": sanity,
        "trade_board": [trade_board_row(v) for v in ranked],
        "players": [v.as_json() for v in ranked],
    }


def render_md(
    values: list[PlayerValue],
    *,
    generated_at_et: str,
    nfl_week: int,
    sanity: list[dict],
    sources: list[str],
    commit_message: str,
) -> str:
    by_pos: dict[str, list[PlayerValue]] = defaultdict(list)
    for v in values:
        by_pos[v.pos].append(v)
    lines = [
        f"# FF Intel trade board — {LEAGUE_NAME}",
        "",
        f"Generated {generated_at_et}",
        "",
        f"- **NFL week:** {nfl_week}",
        f"- **League:** {TEAMS}-team Superflex Half-PPR (Sleeper `{LEAGUE_ID}`)",
        f"- **Formula:** {FORMULA_VERSION} — 35% ROS proj / 25% ppg / 20% role / 15% upside / 5% news",
        f"- **Commit:** `{commit_message}`",
        f"- **Sources:** {'; '.join(sources)}",
        "- Values are 1–100 ROS trade prices for bots. `GUESS` = inferred role, return week, or projection.",
        "",
        "## How to read a value",
        "",
        "Value = stretch-to-98 of (weighted components × injury modifier), then Superflex floors/caps.",
        "Healthy named QB1 floor **45**. Backup QB cap **25** (unless the starter is hurt). "
        "Committee/backup RB (<40% carry share) cap **30**. Out −35%. IR/PUP/SUS −50% scaled by return week. Q −5%.",
        "",
    ]
    order = ["QB", "RB", "WR", "TE"]
    for pos in order:
        rows = sorted(by_pos.get(pos, []), key=lambda x: (-x.value, x.name))
        if not rows:
            continue
        lines.append(f"## {pos}")
        lines.append("")
        lines.append("| Val | Δ | Player | Team | PPG | Role | Inj | Bye | Why (moves ≥8) |")
        lines.append("|---:|---:|---|---|---:|---|---|---|---|")
        for v in rows:
            val = f"{v.value}"
            if v.guess:
                val = f"{v.value} GUESS ({v.formula_value:g})"
            delta = "—" if v.change is None or v.change == 0 else f"{v.change:+.0f}"
            ppg = "—" if v.ppg is None else f"{v.ppg:.1f}"
            bye = "BYE" if v.bye_this_week else ""
            why = v.why if (v.change is not None and abs(v.change) >= 8) or v.guess else ""
            lines.append(
                f"| {val} | {delta} | {v.name} | {v.team or '—'} | {ppg} | {v.role_tag} | {v.injury_tag} | {bye} | {why} |"
            )
        lines.append("")
    lines.append("## Sanity: 15 biggest value vs production-percentile gaps")
    lines.append("")
    lines.append("| Player | Pos | Value | Prod % | Gap | Why |")
    lines.append("|---|---|---:|---:|---:|---|")
    for g in sanity:
        lines.append(
            f"| {g['player']} | {g['pos']} | {g['value']} | {g['production']:.0f} | {g['gap']:.0f} | {g['why']} |"
        )
    lines.append("")
    return "\n".join(lines)


def write_outputs(md: str, payload: dict, archive_date: str, root: str = "ff-intel") -> None:
    from pathlib import Path

    dest = Path(root)
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "archive").mkdir(exist_ok=True)
    (dest / "latest.md").write_text(md, encoding="utf-8")
    (dest / "latest.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    (dest / "archive" / f"{archive_date}.md").write_text(md, encoding="utf-8")
    (dest / "archive" / f"{archive_date}.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
