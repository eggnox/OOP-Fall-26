
"""Property-based tests for StatisticsValues using Hypothesis."""

import unittest

from hypothesis import given, strategies as st

from statistics_values import StatisticsValues


class TestStatisticsProperties(unittest.TestCase):
    """Verify statistical properties with generated inputs."""

    @given(
        st.lists(
            st.integers(min_value=-100000, max_value=100000),
            min_size=1,
            max_size=30,
        )
    )
    def test_matches_python(self, numbers: list[int]) -> None:
        """Statistics should agree with Python's built-in functions."""
        values = StatisticsValues(numbers)

        self.assertEqual(values.minimum, min(numbers))
        self.assertEqual(values.maximum, max(numbers))
        self.assertEqual(
            values.spread,
            max(numbers) - min(numbers),
        )

    @given(
        st.lists(st.integers(-10000, 10000), min_size=1),
        st.integers(-1000, 1000),
    )
    def test_translation_invariance(
        self, numbers: list[int], offset: int
    ) -> None:
        """Adding a constant should not change the range."""
        original = StatisticsValues(numbers)
        shifted = StatisticsValues(
            [number + offset for number in numbers]
        )

        self.assertEqual(original.spread, shifted.spread)

    @given(
        st.lists(st.integers(-10000, 10000), min_size=1)
    )
    def test_order_independence(
        self, numbers: list[int]
    ) -> None:
        """Reversing the list should not change the statistics."""
        original = StatisticsValues(numbers)
        reversed_values = StatisticsValues(reversed(numbers))

        self.assertEqual(original.minimum, reversed_values.minimum)
        self.assertEqual(original.maximum, reversed_values.maximum)
        self.assertEqual(original.spread, reversed_values.spread)


if __name__ == "__main__":
    unittest.main()
