import pytest
from gameplay import lag_compensation as mod

CASES = [
    ("sample", 'm.sample_hitbox([(0, "a"), (1, "b"), (2, "c")], 1.5) == "b"'),
    ("align", 'm.align_snapshot(100, 50) == 50'),
    ("authority", 'm.prediction_authority(True) is False'),
    ("interval", 'm.fire_interval(60, 1) == approx(0.016667)'),
    ("recoil", 'm.recoil_authoritative((1, 2), (3, 4)) == (3, 4)'),
    ("seed", 'm.pellet_seed(42) == 42'),
    ("damage", 'm.resolve_damage(10, 15) == (0, 5)'),
    ("swept", 'm.swept_hit((0, 0), (10, 0), (5, 3), 4) is True'),
    ("dedupe", 'm.dedupe_hits([1, 1, 2]) == 2'),
    ("window", 'm.rollback_window(300, 50) == 50'),
    ("tick", 'm.tick_for_time(1.5, 60) == 90'),
    ("interp", 'm.interpolate(2, 4, 0.5) == approx(3.0)'),
    ("box", 'm.hitbox_scale(2, (1, 2)) == (2, 4)'),
    ("position", 'm.authoritative_position((1, 1), (2, 2)) == (2, 2)'),
    ("id", 'm.lag_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
