"""Main module for the Kattis Convex Polygon Area problem."""

from area_calculator import PolygonAreaCalculator
from polygon import Point, Polygon


def solve() -> None:
    """Read input, calculate polygon areas, and print the results."""
    polygon_total: int = int(input())

    calculator: PolygonAreaCalculator = (
        PolygonAreaCalculator.get_instance()
    )

