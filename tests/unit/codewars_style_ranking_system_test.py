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
