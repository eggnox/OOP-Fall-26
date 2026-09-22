"""Unit tests for the Polygon class."""

import unittest

from polygon import Point, Polygon


class TestPolygon(unittest.TestCase):
    """Test cases for Polygon."""

    def setUp(self) -> None:
        """Create a sample polygon before each test."""
        self.vertices: list[Point] = [(0, 0), (4, 0), (4, 3)]
        self.polygon: Polygon = Polygon(self.vertices)

    def test_vertices_returns_vertices(self) -> None:
        """Test returning all vertices."""
        self.assertEqual(self.polygon.vertices, self.vertices)

    def test_vertices_returns_copy(self) -> None:
        """Test that the vertices property returns a copy."""
        returned_vertices: list[Point] = self.polygon.vertices
        returned_vertices.append((10, 10))

        self.assertEqual(self.polygon.vertex_count, 3)

    def test_vertices_empty_polygon(self) -> None:
        """Test vertices for an empty polygon."""
        polygon: Polygon = Polygon([])

        self.assertEqual(polygon.vertices, [])

    def test_vertex_count_triangle(self) -> None:
        """Test vertex count for a triangle."""
        self.assertEqual(self.polygon.vertex_count, 3)

    def test_vertex_count_rectangle(self) -> None:
        """Test vertex count for a rectangle."""
        polygon: Polygon = Polygon(
            [(0, 0), (4, 0), (4, 3), (0, 3)]
        )

        self.assertEqual(polygon.vertex_count, 4)

    def test_vertex_count_empty(self) -> None:
        """Test vertex count for an empty polygon."""
        polygon: Polygon = Polygon([])

        self.assertEqual(polygon.vertex_count, 0)

    def test_get_vertex_first(self) -> None:
        """Test retrieving the first vertex."""
        self.assertEqual(self.polygon.get_vertex(0), (0, 0))

    def test_get_vertex_middle(self) -> None:
        """Test retrieving a middle vertex."""
        self.assertEqual(self.polygon.get_vertex(1), (4, 0))

    def test_get_vertex_last(self) -> None:
        """Test retrieving the last vertex."""
        self.assertEqual(self.polygon.get_vertex(2), (4, 3))

    def test_len_triangle(self) -> None:
        """Test len for a triangle."""
        self.assertEqual(len(self.polygon), 3)

    def test_len_rectangle(self) -> None:
        """Test len for a rectangle."""
        polygon: Polygon = Polygon(
            [(0, 0), (4, 0), (4, 3), (0, 3)]
        )

        self.assertEqual(len(polygon), 4)

    def test_len_empty(self) -> None:
        """Test len for an empty polygon."""
        polygon: Polygon = Polygon([])

        self.assertEqual(len(polygon), 0)

    def test_vertices_setter(self) -> None:
        """Test replacing the polygon vertices."""
        new_vertices: list[Point] = [(1, 1), (2, 1), (2, 2)]
        self.polygon.vertices = new_vertices

        self.assertEqual(self.polygon.vertices, new_vertices)

    def test_vertices_setter_empty(self) -> None:
        """Test setting the vertices to an empty list."""
        self.polygon.vertices = []

        self.assertEqual(self.polygon.vertex_count, 0)

    def test_vertices_setter_copies_input(self) -> None:
        """Test that the setter copies the supplied list."""
        new_vertices: list[Point] = [(1, 1), (2, 1), (2, 2)]
        self.polygon.vertices = new_vertices

        new_vertices.append((10, 10))

        self.assertEqual(self.polygon.vertex_count, 3)


if __name__ == "__main__":
    unittest.main()
