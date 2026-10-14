"""Unit tests for fraction formatting classes."""

import unittest

from fraction import Fraction
from fraction_formatter import BasicMixedFormatter, SpacedFractionDecorator

class TestBasicMixedFormatter(unittest.TestCase):
    """Test formatting fractions without extra spacing."""

    def test_improper_fraction(self) -> None:
        """Test formatting an improper fraction."""
        formatter = BasicMixedFormatter()
        fraction = Fraction(27, 12)

        self.assertEqual(formatter.format(fraction), "2 3/12")

    def test_proper_fraction(self) -> None:
        """Test formatting a proper fraction."""
        formatter = BasicMixedFormatter()
        fraction = Fraction(3, 4000)

        self.assertEqual(formatter.format(fraction), "0 3/4000")

    def test_whole_number(self) -> None:
        """Test formatting a fraction with no remainder."""
        formatter = BasicMixedFormatter()
        fraction = Fraction(10, 2)

        self.assertEqual(formatter.format(fraction), "5 0/2")

class TestSpacedFractionDecorator(unittest.TestCase):
    """Test the fraction formatting decorator."""

    def test_improper_fraction(self) -> None:
        """Test decorated formatting of an improper fraction."""
        formatter = SpacedFractionDecorator(BasicMixedFormatter())
        fraction = Fraction(27, 12)

        self.assertEqual(formatter.format(fraction), "2 3 / 12")

    def test_proper_fraction(self) -> None:
        """Test decorated formatting of a proper fraction."""
        formatter = SpacedFractionDecorator(BasicMixedFormatter())
        fraction = Fraction(3, 4000)

        self.assertEqual(formatter.format(fraction), "0 3 / 4000")

    def test_whole_number(self) -> None:
        """Test decorated formatting with no remainder."""
        formatter = SpacedFractionDecorator(BasicMixedFormatter())
        fraction = Fraction(10, 2)

        self.assertEqual(formatter.format(fraction), "5 0 / 2")


if __name__ == "__main__":
    unittest.main()