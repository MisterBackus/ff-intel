from ff_intel.assemble import (
    _previous_value,
    bye_this_week,
    guess_return_week,
    norm_name,
    played_points,
    ros_projection,
    teams_playing,
)


def test_played_points_drops_zero_without_snaps():
    matchups = {
        1: [{"players_points": {"p": 12.0}}],
        2: [{"players_points": {"p": 0.0}}],
        3: [{"players_points": {"p": 8.0}}],
    }
    stats = {
        1: {"p": {"off_snp": 40, "gp": 1}},
        2: {"p": {"off_snp": 0}},
        3: {"p": {"off_snp": 30, "gp": 1}},
    }
    assert played_points(matchups, stats, "p") == [12.0, 8.0]


def test_played_points_keeps_true_zero_with_snaps():
    matchups = {1: [{"players_points": {"p": 0.0}}]}
    stats = {1: {"p": {"off_snp": 12, "gp": 1, "gms_active": 1}}}
    assert played_points(matchups, stats, "p") == [0.0]


def test_ros_blends_sleeper_and_run_rate():
    proj = {7: {"p": {"rec": 4, "rec_yd": 60, "rec_td": 0.4}}}
    # 4*0.5 + 60*0.1 + 0.4*6 = 2 + 6 + 2.4 = 10.4
    ros, src, guess = ros_projection("p", proj, [10.4], [7])
    assert src == "sleeper_weekly+run_rate"
    assert guess is False
    assert 10 < ros < 11


def test_ros_run_rate_only_is_guess():
    ros, src, guess = ros_projection("p", {}, [12, 12], [7, 8])
    assert guess is True
    assert src == "run_rate_only"
    assert ros == 24


def test_guess_return_week_ir_plus_four():
    wk, guess = guess_return_week("IR", 7)
    assert guess is True
    assert wk == 11


def test_bye_is_team_level_not_player_level():
    meta = {"p": {"team": "CHI"}, "q": {"team": "BUF"}, "r": {"team": "CHI"}}
    proj = {7: {"p": {"gp": 1, "rec": 3}}}
    playing = teams_playing(7, proj, meta)
    assert "CHI" in playing
    assert bye_this_week("CHI", playing) is False
    assert bye_this_week("BUF", playing) is True
    # Injured CHI player with no personal proj is not on bye.
    assert bye_this_week("CHI", playing) is False


def test_norm_name_strips_suffixes():
    assert norm_name("Kenneth Walker III") == norm_name("Kenneth Walker")
    assert norm_name("Michael Penix Jr.") == norm_name("Michael Penix")


def test_previous_value_falls_back_to_name():
    prev = {norm_name("Josh Allen"): 100.0}
    assert _previous_value(prev, "4984", "Josh Allen") == 100.0
    assert _previous_value({"4984": 88.0, norm_name("Josh Allen"): 100.0}, "4984", "Josh Allen") == 88.0
