import pytest

from ff_intel.formula import PlayerInput, PlayerValue, value_players
from ff_intel.validate import ValidationError, sanity_gaps, validate


def _val(pid, name, pos, value, **kwargs) -> PlayerValue:
    base = dict(
        player_id=pid,
        name=name,
        pos=pos,
        team="X",
        owner_id="o",
        roster_id=1,
        value=value,
        formula_value=float(value),
        guess=False,
        projection=50,
        production=50,
        role=50,
        upside=50,
        news=50,
        raw_weighted=50,
        injury_mult=1.0,
        ppg=12.0,
        games=6,
        ros_projection=100,
        role_tag="RB1",
        injury_tag="Healthy",
        bye_this_week=False,
        change=None,
        why="ok",
        projection_source="test",
        snap_share=0.6,
        carry_share=0.6,
        target_share=None,
    )
    base.update(kwargs)
    return PlayerValue(**base)


def _inp(pid, pos, **kwargs) -> PlayerInput:
    base = dict(
        player_id=pid,
        name=pid,
        pos=pos,
        team="X",
        owner_id="o",
        roster_id=1,
        injury_status=None,
        depth_chart_order=1,
        years_exp=4,
        search_rank=20,
        rookie_year=None,
        weekly_points=[12],
        ros_projection=100,
        remaining_weeks=12,
    )
    base.update(kwargs)
    return PlayerInput(**base)


def test_missing_rostered_player_fails():
    values = [_val("a", "A", "QB", 70)]
    inputs = [_inp("a", "QB", is_named_starter_qb=True)]
    with pytest.raises(ValidationError, match="missing"):
        validate(values, inputs, {"a", "b"})


def test_healthy_starter_qb_below_floor_fails():
    values = [_val("a", "QB A", "QB", 30)]
    inputs = [_inp("a", "QB", is_named_starter_qb=True)]
    with pytest.raises(ValidationError, match="starting QB"):
        validate(values, inputs, {"a"})


def test_backup_qb_over_cap_fails():
    values = [_val("a", "Backup", "QB", 40)]
    inputs = [_inp("a", "QB", is_named_starter_qb=False, is_backup_qb=True, starter_injured=False)]
    with pytest.raises(ValidationError, match="backup QB"):
        validate(values, inputs, {"a"})


def test_committee_rb_over_cap_fails():
    values = [_val("a", "Cuff", "RB", 55, carry_share=0.2)]
    inputs = [_inp("a", "RB", carry_share=0.2)]
    with pytest.raises(ValidationError, match="committee"):
        validate(values, inputs, {"a"})


def test_valid_board_passes():
    qb = _inp("q", "QB", is_named_starter_qb=True, ros_projection=300, weekly_points=[25, 24])
    rb = _inp("r", "RB", carry_share=0.6, ros_projection=200, weekly_points=[18, 20])
    cuff = _inp("c", "RB", carry_share=0.15, ros_projection=20, weekly_points=[2], search_rank=400)
    values = value_players([qb, rb, cuff], current_week=7)
    validate(values, [qb, rb, cuff], {"q", "r", "c"})


def test_sanity_gaps_sorted():
    values = [
        _val("a", "A", "WR", 90, production=10, why="proj"),
        _val("b", "B", "WR", 50, production=48, why="flat"),
        _val("c", "C", "WR", 20, production=80, why="injury"),
    ]
    gaps = sanity_gaps(values, n=2)
    assert len(gaps) == 2
    assert gaps[0]["player"] == "A"
    assert gaps[0]["gap"] == 80
