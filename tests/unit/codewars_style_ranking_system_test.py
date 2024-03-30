import pytest

from codewars.codewars_style_ranking_system import User


class TestUser:
    def test_user_starts_at_rank_neg8(self):
        assert User().rank == -8

    def test_user_starts_at_0_progress(self):
        assert User().progress == 0

    def test_rank_cannot_be_0(self):
        with pytest.raises(ValueError, match="Rank must be between -8 and 8"):
            User().rank = 0

    def test_rank_cannot_be_lower_than_neg8(self):
        with pytest.raises(ValueError, match="Rank must be between -8 and 8"):
            User().rank = -9

    def test_rank_cannot_be_higher_than_8(self):
        with pytest.raises(ValueError, match="Rank must be between -8 and 8"):
            User().rank = 9

    def test_completing_activity_with_same_rank_as_user_adds_3_progress(self):
        user = User()

        user.inc_progress(rank_activity=-8)
        assert user.progress == 3

    def test_completing_activity_with_one_rank_lower_as_user_adds_1_progress(self):
        user = User()
        user.rank = -7

        user.inc_progress(rank_activity=-8)
        assert user.progress == 1

    def test_completing_activity_with_more_than_one_rank_lower_as_user_adds_no_progress(self):
        user = User()
        user.rank = -6

        user.inc_progress(rank_activity=-8)
        assert user.progress == 0
