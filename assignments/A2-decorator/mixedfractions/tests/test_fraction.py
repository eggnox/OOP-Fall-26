"""Unit tests for the Fraction class."""

import unittest

from fraction import Fraction


class TestFraction(unittest.TestCase):
    """Test fraction conversion functionality."""

    def test_improper_fraction(self) -> None:
        """Test conversion of an improper fraction."""
        fraction = Fraction(27, 12)
        self.assertEqual(fraction.to_mixed(), (2, 3, 12))

    def test_proper_fraction(self) -> None:
        """Test conversion of a proper fraction."""
        fraction = Fraction(3, 4000)
        self.assertEqual(fraction.to_mixed(), (0, 3, 4000))

    def test_whole_number_fraction(self) -> None:
        """Test conversion with no remainder."""
        fraction = Fraction(10, 2)
        self.assertEqual(fraction.to_mixed(), (5, 0, 2))


if __name__ == "__main__":
    unittest.main()