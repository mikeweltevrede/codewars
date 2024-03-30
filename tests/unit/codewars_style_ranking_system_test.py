from codewars.codewars_style_ranking_system import User


class TestUser:
    def test_user_starts_at_rank_neg8(self):
        assert User().rank == -8

    def test_user_starts_at_0_progress(self):
        assert User().progress == 0
