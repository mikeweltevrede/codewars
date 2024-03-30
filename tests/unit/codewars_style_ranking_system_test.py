from codewars.codewars_style_ranking_system import User


def test_user_starts_at_rank_neg8():
    assert User().rank == -8
