
"""Utilities for counting below-freezing temperatures."""


class ColdCounter:
    """Count temperatures below zero degrees Celsius."""

    @staticmethod
    def count(temperatures: list[int]) -> int:
        """Return the number of temperatures below zero."""
        return sum(1 for temp in temperatures if temp < 0)
