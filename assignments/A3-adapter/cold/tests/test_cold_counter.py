
"""Unit tests for the ColdCounter class."""

import unittest

from hypothesis import given, settings
from hypothesis import strategies as st

from cold_counter import ColdCounter


class TestColdCounter(unittest.TestCase):
    """Test counting temperatures below zero Celsius."""

    def test_mixed_temperatures(self) -> None:
        """Count negative values in a mixed list."""
        temperatures = [-10, 0, 5, -3, 12]

        self.assertEqual(ColdCounter.count(temperatures), 2)

    def test_no_negative_temperatures(self) -> None:
        """Return zero when nothing is below freezing."""
        temperatures = [0, 1, 5, 20, 100]

        self.assertEqual(ColdCounter.count(temperatures), 0)

    def test_all_negative_temperatures(self) -> None:
        """Count every temperature when all are negative."""
        temperatures = [-1, -5, -10, -100]

        self.assertEqual(ColdCounter.count(temperatures), 4)

    def test_empty_list(self) -> None:
        """Return zero for an empty temperature list."""
        self.assertEqual(ColdCounter.count([]), 0)

    @settings(max_examples=50)
    @given(
        temperatures=st.lists(
            st.integers(min_value=-100, max_value=100),
            max_size=100,
        )
    )
    def test_generated_temperatures(
        self, temperatures: list[int]
    ) -> None:
        """Verify counting properties with generated data."""
        count = ColdCounter.count(temperatures)

        self.assertGreaterEqual(count, 0)
        self.assertLessEqual(count, len(temperatures))

        self.assertEqual(
            ColdCounter.count(temperatures + [0]),
            count,
        )

        self.assertEqual(
            ColdCounter.count(temperatures + [-1]),
            count + 1,
        )


if __name__ == "__main__":
    unittest.main()
