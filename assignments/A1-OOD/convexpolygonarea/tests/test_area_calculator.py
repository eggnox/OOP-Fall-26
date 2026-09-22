"""Unit tests for the PolygonAreaCalculator class."""

import unittest

from area_calculator import PolygonAreaCalculator
from polygon import Polygon


class TestPolygonAreaCalculator(unittest.TestCase):
    """Test cases for PolygonAreaCalculator."""

    def setUp(self) -> None:
        """Get the shared calculator before each test."""
        self.calculator: PolygonAreaCalculator = (
            PolygonAreaCalculator.get_instance()
        )

    def test_singleton_same_instance(self) -> None:
        """Test that get_instance returns the same object."""
        first = PolygonAreaCalculator.get_instance()
        second = PolygonAreaCalculator.get_instance()

        self.assertIs(first, second)

    def test_singleton_constructor_same_instance(self) -> None:
        """Test that direct construction still returns one instance."""
        first = PolygonAreaCalculator()
        second = PolygonAreaCalculator()

        self.assertIs(first, second)

    def test_singleton_mixed_creation(self) -> None:
        """Test direct construction and get_instance match."""
        first = PolygonAreaCalculator()
        second = PolygonAreaCalculator.get_instance()

        self.assertIs(first, second)

    def test_shoelace_term_zero(self) -> None:
        """Test a shoelace term that equals zero."""
        result = self.calculator.shoelace_term((0, 0), (4, 0))

        self.assertEqual(result, 0)

    def test_shoelace_term_negative(self) -> None:
        """Test a negative shoelace term."""
        result = self.calculator.shoelace_term((2, 3), (4, 5))

        self.assertEqual(result, -2)

    def test_shoelace_term_positive(self) -> None:
        """Test a positive shoelace term."""
        result = self.calculator.shoelace_term((4, 5), (2, 3))

        self.assertEqual(result, 2)

    def test_triangle_area(self) -> None:
        """Test the area of a triangle."""
        polygon = Polygon([(0, 0), (4, 0), (0, 3)])

        self.assertEqual(
            self.calculator.calculate_area(polygon),
            6.0,
        )

    def test_rectangle_area(self) -> None:
        """Test the area of a rectangle."""
        polygon = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])

        self.assertEqual(
            self.calculator.calculate_area(polygon),
            12.0,
        )

    def test_reversed_polygon_area(self) -> None:
        """Test that clockwise vertices still give positive area."""
        polygon = Polygon([(0, 3), (4, 3), (4, 0), (0, 0)])

        self.assertEqual(
            self.calculator.calculate_area(polygon),
            12.0,
        )


if __name__ == "__main__":
    unittest.main()
