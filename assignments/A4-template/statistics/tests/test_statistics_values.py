
"""Unit tests for the StatisticsValues class."""

import unittest

from statistics_values import StatisticsValues


class TestStatisticsValues(unittest.TestCase):
    """Test inheritance and statistical calculations."""

    def test_positive_numbers(self) -> None:
        """Calculate statistics for positive integers."""
        values = StatisticsValues([4, 7, 10, 6])

        self.assertEqual(values.minimum, 4)
        self.assertEqual(values.maximum, 10)
        self.assertEqual(values.spread, 6)

    def test_negative_numbers(self) -> None:
        """Calculate statistics for negative integers."""
        values = StatisticsValues([-10, -5, -3])

        self.assertEqual(values.minimum, -10)
        self.assertEqual(values.maximum, -3)
        self.assertEqual(values.spread, 7)

    def test_mixed_numbers(self) -> None:
        """Handle both positive and negative integers."""
        values = StatisticsValues([-8, 0, 12, 4])

        self.assertEqual(values.minimum, -8)
        self.assertEqual(values.maximum, 12)
        self.assertEqual(values.spread, 20)

    def test_single_number(self) -> None:
        """The range of one number is zero."""
        values = StatisticsValues([5])

        self.assertEqual(values.minimum, 5)
        self.assertEqual(values.maximum, 5)
        self.assertEqual(values.spread, 0)

    def test_duplicate_numbers(self) -> None:
        """Handle repeated integers correctly."""
        values = StatisticsValues([3, 3, 3])

        self.assertEqual(values.minimum, 3)
        self.assertEqual(values.maximum, 3)
        self.assertEqual(values.spread, 0)

    def test_empty_list(self) -> None:
        """Reject an empty collection."""
        with self.assertRaises(ValueError):
            StatisticsValues([])

    def test_list_inheritance(self) -> None:
        """Verify access to inherited list functionality."""
        values = StatisticsValues([1, 2, 3])

        self.assertIsInstance(values, list)

        values.append(10)

        self.assertEqual(values.maximum, 10)
        self.assertEqual(len(values), 4)


if __name__ == "__main__":
    unittest.main()
