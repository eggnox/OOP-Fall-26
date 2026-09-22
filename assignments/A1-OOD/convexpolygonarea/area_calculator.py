"""Provides a singleton calculator for finding polygon areas."""

from typing import ClassVar, Optional

from polygon import Point, Polygon


class PolygonAreaCalculator:
    """Calculates polygon areas using a single shared instance."""

    __instance: ClassVar[Optional["PolygonAreaCalculator"]] = None

    def __new__(cls) -> "PolygonAreaCalculator":
        """Create or return the single calculator instance."""
        instance: Optional["PolygonAreaCalculator"] = cls.__instance

        if instance is None:
            instance = super().__new__(cls)
            cls.__instance = instance

        return instance

    @classmethod
    def get_instance(cls) -> "PolygonAreaCalculator":
        """Return the singleton calculator instance."""
        return cls()

    @staticmethod
    def shoelace_term(first: Point, second: Point) -> int:
        """Calculate one term of the shoelace formula."""
        return first[0] * second[1] - first[1] * second[0]

    def calculate_area(self, polygon: Polygon) -> float:
        """Calculate and return the area of a polygon."""
        vertex_total: int = len(polygon)

        if vertex_total < 3:
            return 0.0

        area_sum: int = 0
        index: int

        for index in range(vertex_total):
            first: Point = polygon.get_vertex(index)
            second: Point = polygon.get_vertex(
                (index + 1) % vertex_total
            )
            area_sum += self.shoelace_term(first, second)

        return abs(area_sum) / 2.0
