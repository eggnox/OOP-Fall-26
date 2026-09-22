"""Main module for the Kattis Convex Polygon Area problem."""

from area_calculator import PolygonAreaCalculator
from polygon import Point, Polygon


def solve() -> None:
    """Read input, calculate polygon areas, and print the results."""
    polygon_total: int = int(input())

    calculator: PolygonAreaCalculator = (
        PolygonAreaCalculator.get_instance()
    )
    for _ in range(polygon_total):
        values: list[int] = list(map(int, input().split()))
        vertex_total: int = values[0]
        vertices: list[Point] = []

        for index in range(vertex_total):
            x_coordinate: int = values[1 + index * 2]
            y_coordinate: int = values[2 + index * 2]

            vertices.append((x_coordinate, y_coordinate))

        polygon: Polygon = Polygon(vertices)
        area: float = calculator.calculate_area(polygon)

        print(f"{area:g}")


if __name__ == "__main__":
    solve()
