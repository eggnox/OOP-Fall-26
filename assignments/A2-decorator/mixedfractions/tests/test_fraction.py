"""Unit tests for the Fraction class."""

import unittest

from fraction import Fraction
from hypothesis import given, strategies as st


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

    def test_numerator_property(self) -> None:
        """Test reading and updating the numerator."""
        fraction = Fraction(10, 3)

        self.assertEqual(fraction.numerator, 10)

        fraction.numerator = 20
        self.assertEqual(fraction.numerator, 20)

    def test_denominator_property(self) -> None:
        """Test reading and updating the denominator."""
        fraction = Fraction(10, 3)

        self.assertEqual(fraction.denominator, 3)

        fraction.denominator = 5
        self.assertEqual(fraction.denominator, 5)

    def test_invalid_denominator(self) -> None:
        """Test that invalid denominators raise exceptions."""
        with self.assertRaises(ValueError):
            Fraction(10, 0)

        with self.assertRaises(ValueError):
            Fraction(10, -3)

    def test_add_different_denominators(self) -> None:
        """Test adding fractions with different denominators."""
        result = Fraction(1, 2) + Fraction(1, 4)

        self.assertEqual(result.numerator, 6)
        self.assertEqual(result.denominator, 8)

    def test_add_same_denominators(self) -> None:
        """Test adding fractions with equal denominators."""
        result = Fraction(2, 3) + Fraction(1, 3)

        self.assertEqual(result.numerator, 9)
        self.assertEqual(result.denominator, 9)

    def test_add_zero_numerator(self) -> None:
        """Test adding a fraction with a zero numerator."""
        result = Fraction(0, 5) + Fraction(3, 7)

        self.assertEqual(result.numerator, 15)
        self.assertEqual(result.denominator, 35)

    @given(
        numerator=st.integers(min_value=1, max_value=100000),
        denominator=st.integers(min_value=1, max_value=100000)
    )
    def test_hypothesis_conversion(
        self, numerator: int, denominator: int
    ) -> None:
        """Test mixed fraction conversion with generated values."""
        fraction = Fraction(numerator, denominator)

        whole, remainder, bottom = fraction.to_mixed()

        self.assertEqual(whole * bottom + remainder, numerator)
        self.assertGreaterEqual(remainder, 0)
        self.assertLess(remainder, bottom)
        self.assertEqual(bottom, denominator)


if __name__ == "__main__":
    unittest.main()