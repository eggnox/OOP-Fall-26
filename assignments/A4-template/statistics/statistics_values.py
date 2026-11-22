
"""Integer statistics using inheritance from Python's list."""

from collections.abc import Iterable


class StatisticsValues(list[int]):
    """A list of integers with statistics properties."""

    def __init__(self, values: Iterable[int]) -> None:
        """Initialize a nonempty collection of integers."""
        super().__init__(values)

        if not self:
            raise ValueError("Statistics requires at least one integer.")

    @property
    def minimum(self) -> int:
        """Return the smallest integer."""
        return min(self)

    @property
    def maximum(self) -> int:
        """Return the largest integer."""
        return max(self)

    @property
    def spread(self) -> int:
        """Return the difference between maximum and minimum."""
        return self.maximum - self.minimum
