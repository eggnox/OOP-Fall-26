"""Defines the Polygon class used for the Convex Polygon Area problem."""

from typing import List, Tuple


Point = Tuple[int, int]


class Polygon:
    """Represents a polygon using a collection of coordinate points."""

    def __init__(self, vertices: List[Point]) -> None:
        """Initialize a polygon with a list of vertices."""
        self.__vertices: List[Point] = vertices

    @property
    def vertices(self) -> List[Point]:
        """Return a copy of the polygon's vertices."""
        return self.__vertices.copy()

    @vertices.setter
    def vertices(self, vertices: List[Point]) -> None:
        """Set the polygon's vertices."""
        self.__vertices = vertices

    @property
    def vertex_count(self) -> int:
        """Return the number of vertices in the polygon."""
        return len(self.__vertices)

    def get_vertex(self, index: int) -> Point:
        """Return the vertex at the specified index."""
        return self.__vertices[index]

    def __len__(self) -> int:
        """Return the number of vertices in the polygon."""
        return len(self.__vertices)