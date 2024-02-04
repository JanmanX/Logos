from utils.math import round_up 

def test_round_to_nearest():
    assert round_up(3, 4) == 4
    assert round_up(5, 4) == 8
    assert round_up(0, 4) == 0
    assert round_up(1, 4) == 4
    assert round_up(2, 4) == 4