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

    