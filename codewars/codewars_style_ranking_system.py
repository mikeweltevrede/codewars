"""Codewars style ranking system

Write a class called User that is used to calculate the amount that a user will progress through a ranking system
similar to the one Codewars uses.

Business Rules:
- A user starts at rank -8 and can progress all the way to 8.
- There is no 0 (zero) rank. The next rank after -1 is 1.
- Users will complete activities. These activities also have ranks.
- Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
- The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of
  the activity
- A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next
  level
- Any remaining progress earned while in the previous rank will be applied towards the next rank's progress (we don't
  throw any progress away). The exception is if there is no other rank left to progress towards (Once you reach rank 8
  there is no more progression).
- A user cannot progress beyond rank 8.
- The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an
  error.

The progress is scored like so:
- Completing an activity that is ranked the same as that of the user's will be worth 3 points
- Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
- Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
- Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater
  the difference between rankings the more the progression will be increased. The formula is 10 * d * d where d equals
  the difference in ranking between the activity and the user.

Logic Examples:
- If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
- If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
- If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
- If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being
  upgraded to rank -7 and having earned 60 progress towards their next rank
- If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)

Code Usage Examples:
    user = User()
    user.rank # => -8
    user.progress # => 0
    user.inc_progress(-7)
    user.progress # => 10
    user.inc_progress(-5) # will add 90 progress
    user.progress # => 0 # progress is now zero
    user.rank # => -7 # rank was upgraded to -7

Note: Codewars no longer uses this algorithm for its own ranking system. It uses a pure Math based solution that gives
consistent results no matter what order a set of ranked activities are completed at.
"""


class User:
    min_rank = -8
    max_rank = 8
    max_progress = 100

    def __init__(self) -> None:
        """User in a ranking system similar to the one Codewars uses."""
        self._rank = self.min_rank
        self._progress = 0

    @property
    def rank(self) -> int:
        """The user's rank in the system."""
        return self._rank

    @rank.setter
    def rank(self, value: int) -> None:
        if value not in range(self.min_rank, self.max_rank + 1) or value == 0:
            raise ValueError(f"Rank must be between {self.min_rank} and {self.max_rank} (0 excluded) but was {value}")

        self._rank = value

    @property
    def progress(self) -> int:
        """The user's progress within their rank."""
        return self._progress

    @progress.setter
    def progress(self, value: int) -> None:
        self._progress = value

    @property
    def max_rank_increases(self) -> int:
        """Number of ranks that the user can still increase."""
        return self.max_rank - self.rank

    def inc_progress(self, rank_activity: int) -> None:
        """Increase the progress based on the rank of the activity compared to the user's rank.

        :param rank_activity: Rank of the completed activity.
        """
        if rank_activity <= self.rank - 2:
            return

        if rank_activity == self.rank - 1:
            self.progress += 1
        elif rank_activity == self.rank:
            self.progress += 3
        else:  # rank_activity > self.rank - not sure if it is best practice to put else or the conditional
            self.progress += self._progress_increase_with_rank_acceleration(rank_activity=rank_activity)

        self.inc_rank()

    def inc_rank(self) -> None:
        """Increase the rank based on the collected progress."""
        if self.progress < self.max_progress or self.rank == self.max_rank:
            # Note that the if-statement about progress can be considered obsolete because the calculations below with
            # modulus would lead to the same result. However, it is better to exit early.
            return

        rank_increases, remainder_progress = divmod(self.progress, self.max_progress)

        if rank_increases > self.max_rank_increases:
            self.progress = remainder_progress + self.max_progress * (rank_increases - self.max_rank_increases)
            self.rank = self.max_rank
            return

        self.progress = remainder_progress

        if self.rank + rank_increases == 0:
            self.rank += rank_increases + 1
        else:
            self.rank += rank_increases

    def _progress_increase_with_rank_acceleration(self, rank_activity: int) -> int:
        """Formula to compute rank increase for completion of tasks higher than the user's current rank.

        Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The
        greater the difference between rankings the more the progression will be increased. The formula is 10 * d * d
        where d equals the difference in ranking between the activity and the user.

        :param rank_activity: Rank of the completed activity.
        :return: How much the progress increases.
        """
        if self.rank >= rank_activity:
            raise ValueError("Progress acceleration only possible for activities ranked higher than user's rank.")

        difference = rank_activity - self.rank

        if self.rank < 0 < rank_activity:
            # 0 is not a valid rank. As such, if the sign changes, we have to subtract it.
            # TODO: Perhaps this can be done better... E.g. maintaining valid ranks somewhere else
            difference -= 1

        return 10 * difference**2
