from ff_intel.config import QB_BACKUP_CAP, QB_STARTER_FLOOR, RB_COMMITTEE_CAP
from ff_intel.formula import (
    PlayerInput,
    apply_positional_bounds,
    clamp,
    injury_multiplier,
    percentile_scores,
    production_ppg,
    stretch_top,
    value_players,
)


def _qb(**kwargs) -> PlayerInput:
    base = dict(
        player_id="1",
        name="Starter QB",
        pos="QB",
        team="BUF",
        owner_id="o",
        roster_id=1,
        injury_status=None,
        depth_chart_order=1,
        years_exp=6,
        search_rank=5,
        rookie_year=None,
        weekly_points=[22, 24, 20],
        ros_projection=280,
        is_named_starter_qb=True,
        remaining_weeks=12,
    )
    base.update(kwargs)
    return PlayerInput(**base)


def _rb(pid, name, proj, pts, share, **kwargs) -> PlayerInput:
    base = dict(
        player_id=pid,
        name=name,
        pos="RB",
        team="DET",
        owner_id="o",
        roster_id=1,
        injury_status=None,
        depth_chart_order=1,
        years_exp=3,
        search_rank=10,
        rookie_year=None,
        weekly_points=pts,
        ros_projection=proj,
        carry_share=share,
        remaining_weeks=12,
    )
    base.update(kwargs)
    return PlayerInput(**base)


def test_percentile_order():
    assert percentile_scores([1, 2, 3]) == [0.0, 50.0, 100.0]
    assert percentile_scores([None]) == [0.0]
    assert percentile_scores([7.0]) == [50.0]
    assert percentile_scores([250.0, 250.0]) == [50.0, 50.0]


def test_production_ppg_excludes_nothing_already_filtered():
    assert production_ppg([10, 20]) == 15
    assert production_ppg([]) is None


def test_injury_multipliers():
    assert injury_multiplier(None, current_week=7, expected_return_week=None, remaining_weeks=12) == 1.0
    assert injury_multiplier("Questionable", current_week=7, expected_return_week=None, remaining_weeks=12) == 0.95
    assert injury_multiplier("Out", current_week=7, expected_return_week=None, remaining_weeks=12) == 0.65
    ir_season = injury_multiplier("IR", current_week=7, expected_return_week=19, remaining_weeks=12)
    assert ir_season == 0.50
    ir_soon = injury_multiplier("IR", current_week=7, expected_return_week=8, remaining_weeks=12)
    assert 0.85 < ir_soon <= 1.0


def test_qb_floor_and_backup_cap():
    assert apply_positional_bounds(
        20,
        pos="QB",
        is_named_starter_qb=True,
        is_backup_qb=False,
        starter_injured=False,
        healthy=True,
        carry_share=None,
    ) == QB_STARTER_FLOOR
    assert apply_positional_bounds(
        80,
        pos="QB",
        is_named_starter_qb=False,
        is_backup_qb=True,
        starter_injured=False,
        healthy=True,
        carry_share=None,
    ) == QB_BACKUP_CAP
    # Cap lifts when the starter is hurt.
    assert apply_positional_bounds(
        80,
        pos="QB",
        is_named_starter_qb=False,
        is_backup_qb=True,
        starter_injured=True,
        healthy=True,
        carry_share=None,
    ) == 80


def test_committee_rb_cap():
    assert apply_positional_bounds(
        70,
        pos="RB",
        is_named_starter_qb=False,
        is_backup_qb=False,
        starter_injured=False,
        healthy=True,
        carry_share=0.25,
    ) == RB_COMMITTEE_CAP
    assert apply_positional_bounds(
        70,
        pos="RB",
        is_named_starter_qb=False,
        is_backup_qb=False,
        starter_injured=False,
        healthy=True,
        carry_share=0.55,
    ) == 70


def test_stretch_top_maps_max_to_98():
    out = stretch_top([10, 50, 100], 98)
    assert max(out) == 98
    assert out[0] == 9.8


def test_clamp():
    assert clamp(-4) == 1
    assert clamp(140) == 100


def test_value_players_top_near_98_and_qb_floor():
    players = [
        _qb(player_id="allen", name="Josh Allen", ros_projection=320, weekly_points=[28, 30, 26]),
        _qb(
            player_id="backup",
            name="Clip Backup",
            team="PHI",
            ros_projection=40,
            weekly_points=[2],
            search_rank=300,
            is_named_starter_qb=False,
            is_backup_qb=True,
            depth_chart_order=2,
        ),
        _rb("gibbs", "Jahmyr Gibbs", 260, [22, 24, 20], 0.70),
        _rb("cuff", "Handcuff", 40, [3, 2], 0.15, search_rank=250, depth_chart_order=3),
    ]
    vals = {v.player_id: v for v in value_players(players, current_week=7)}
    assert max(v.value for v in vals.values()) >= 90
    assert vals["allen"].value >= QB_STARTER_FLOOR
    assert vals["backup"].value <= QB_BACKUP_CAP
    assert vals["cuff"].value <= RB_COMMITTEE_CAP
    assert all(1 <= v.value <= 100 for v in vals.values())


def test_ir_hurts_value_vs_healthy_peer():
    healthy = _qb(player_id="h", name="Healthy QB", ros_projection=250)
    ir = _qb(
        player_id="ir",
        name="IR QB",
        ros_projection=250,
        injury_status="IR",
        expected_return_week=19,
        is_named_starter_qb=True,
    )
    vals = {v.player_id: v for v in value_players([healthy, ir], current_week=7)}
    assert vals["ir"].value < vals["h"].value
    assert vals["ir"].injury_mult == 0.5


def test_guess_flag_surfaces():
    p = _rb("x", "Guess Back", 80, [8], None, guess_role=True, carry_share=0.22)
    v = value_players([p], current_week=7)[0]
    assert v.guess is True
