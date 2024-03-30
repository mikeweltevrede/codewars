from unittest import mock

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

    def test_completing_activity_with_higher_rank_as_user_adds_accelerated_progress(self):
        user = User()
        user.rank = 2
        user._progress_increase_with_rank_acceleration = mock.Mock(return_value=42)

        user.inc_progress(rank_activity=4)
        assert user.progress == 42

    def test_inc_rank_when_progress_is_lower_than_max_progress_does_not_increase_rank(self):
        user = User()
        user.rank = 3
        user.progress = 42

        user.inc_rank()
        assert user.rank == 3

    def test_inc_rank_when_progress_is_equal_to_max_progress_increase_rank_by_1_if_rank_not_maxed(self):
        user = User()
        user.rank = 3
        user.progress = 100

        user.inc_rank()
        assert user.rank == 4

    def test_inc_rank_does_not_change_rank_and_progress_if_rank_is_maxed(self):
        user = User()
        user.rank = 8
        user.progress = 100

        user.inc_rank()
        assert user.rank == 8
        assert user.progress == 100

    def test_inc_rank_when_progress_is_equal_to_max_progress_resets_progress_to_0(self):
        user = User()
        user.rank = 3
        user.progress = 100

        user.inc_rank()
        assert user.progress == 0

    def test_inc_rank_when_progress_is_equal_to_max_progress_plus_n_resets_progress_to_n(self):
        user = User()
        user.rank = 3
        user.progress = 142

        user.inc_rank()
        assert user.progress == 42

    def test_inc_rank_when_progress_exceeds_multiple_of_max_progress_raises_rank_by_multiple_levels_if_it_does_not_make_the_user_reach_max_rank(
        self,
    ):  # noqa: E401
        user = User()
        user.rank = 3
        user.progress = 242

        user.inc_rank()
        assert user.rank == 5

    def test_inc_rank_when_progress_exceeds_multiple_of_max_progress_sets_progress_to_remainder_if_it_does_not_make_the_user_reach_max_rank(
        self,
    ):  # noqa: E401
        user = User()
        user.rank = 3
        user.progress = 242

        user.inc_rank()
        assert user.progress == 42

    def test_inc_rank_when_progress_exceeds_multiple_of_max_progress_raises_rank_till_at_most_max_rank(self):
        user = User()
        user.rank = user.max_rank - 2
        user.progress = 342

        user.inc_rank()
        assert user.rank == user.max_rank

    def test_inc_rank_when_progress_exceeds_multiple_of_max_progress_which_raises_rank_till_max_rank_keeps_remaining_progress_after_increase(
        self,
    ):  # noqa: E401
        user = User()
        user.rank = user.max_rank - 2
        user.progress = 342

        user.inc_rank()
        assert user.progress == 142

    @pytest.mark.parametrize(
        ("rank_user", "rank_activity", "expected"),
        [
            (-8, -7, 10),
            (-8, -6, 40),
            (-8, -5, 90),
            (-8, -4, 160),
            (-1, 1, 10),
            (-2, 2, 90),
        ],
    )
    def test__progress_increase_with_rank_acceleration_returns_10_times_difference_squared(
        self, rank_user: int, rank_activity: int, expected: int
    ):
        """Requirements as provided in the kata description.

        - If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
        - If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
        - If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
        - If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user
          being upgraded to rank -7 and having earned 60 progress towards their next rank
        - If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is
          ignored)
        """
        user = User()
        user.rank = rank_user

        actual = user._progress_increase_with_rank_acceleration(rank_activity=rank_activity)

        assert actual == expected

    def test__progress_increase_with_rank_acceleration_raises_value_error_if_rank_of_user_is_above_rank_activity(self):
        user = User()
        user.rank = 5

        with pytest.raises(
            ValueError, match="Progress acceleration only possible for activities ranked higher than user's rank."
        ):
            user._progress_increase_with_rank_acceleration(rank_activity=4)
