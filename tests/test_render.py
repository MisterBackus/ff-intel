from ff_intel.assemble import norm_name
from ff_intel.formula import PlayerValue
from ff_intel.generate import _ingest_board
from ff_intel.render import BOT_TRADE_KEYS, merge_live_packet, render_json, trade_board_row
from ff_intel.validate import validate_bot_contract


def _val(**kwargs) -> PlayerValue:
    base = dict(
        player_id="1",
        name="Josh Allen",
        pos="QB",
        team="BUF",
        owner_id="o",
        roster_id=1,
        value=88,
        formula_value=88.2,
        guess=False,
        projection=90,
        production=95,
        role=100,
        upside=80,
        news=40,
        raw_weighted=85,
        injury_mult=1.0,
        ppg=30.5,
        games=6,
        ros_projection=300,
        role_tag="QB1",
        injury_tag="Healthy",
        bye_this_week=True,
        change=10,
        why="+10 vs last board",
        projection_source="sleeper_weekly+run_rate",
        snap_share=1.0,
        carry_share=None,
        target_share=None,
    )
    base.update(kwargs)
    return PlayerValue(**base)


def test_trade_board_row_matches_bot_contract():
    row = trade_board_row(_val())
    assert row["player"] == "Josh Allen"
    assert row["pos"] == "QB"
    assert row["value"] == 88
    assert row["tier"] == "QB1"
    assert row["trend"] == "up"
    assert "GUESS" not in row["note"]
    assert "bye this week" in row["note"]
    assert set(row) == set(BOT_TRADE_KEYS)


def test_trade_board_marks_guess():
    row = trade_board_row(_val(guess=True, why="IR x0.50", change=0, bye_this_week=False))
    assert row["trend"] == "flat"
    assert "GUESS" in row["note"]


def test_render_json_includes_trade_board_and_players():
    payload = render_json(
        [_val()],
        generated_at_et="now",
        nfl_week=7,
        sanity=[],
        sources=["sleeper"],
        commit_message="intel: test",
    )
    assert payload["trade_board"][0]["player"] == "Josh Allen"
    assert payload["players"][0]["player_id"] == "1"
    assert payload["league"]["faab"] == 100
    assert payload["league"]["platform"] == "sleeper"


def test_ingest_github_trade_board_by_name():
    out: dict[str, float] = {}
    _ingest_board(
        {
            "trade_board": [
                {"player": "Kenneth Walker III", "value": 82},
                {"player": "Ollie Gordon II", "value": 32},
            ]
        },
        out,
    )
    assert out[norm_name("Kenneth Walker")] == 82
    assert out[norm_name("Ollie Gordon II")] == 32


def test_merge_keeps_live_sections_and_strict_trade_board():
    live = {
        "injuries": [{"player": "X"}],
        "faab": [{"player": "Y"}],
        "start_sit": [{"player": "Z", "call": "Start"}],
        "trade_board": [{"player": "Old", "pos": "QB", "value": 1, "tier": "QB5", "trend": "flat", "note": "old"}],
    }
    payload = render_json(
        [_val()],
        generated_at_et="now",
        nfl_week=7,
        sanity=[],
        sources=["sleeper"],
        commit_message="intel: test",
    )
    merged = merge_live_packet(live, payload)
    validate_bot_contract(merged)
    assert merged["injuries"] == live["injuries"]
    assert merged["faab"] == live["faab"]
    assert merged["start_sit"] == live["start_sit"]
    assert merged["trade_board"][0]["player"] == "Josh Allen"
    assert merged["nfl_week"] == "7"
    assert merged["players"][0]["player_id"] == "1"
