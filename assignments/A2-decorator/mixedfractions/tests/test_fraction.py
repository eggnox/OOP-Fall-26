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


if __name__ == "__main__":
    unittest.main()