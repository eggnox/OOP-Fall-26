"""Unit tests for the Polygon class."""

import unittest

from polygon import Point, Polygon


class TestPolygon(unittest.TestCase):
    """Test cases for Polygon."""

    def setUp(self) -> None:
        """Create a sample polygon before each test."""
        self.vertices: list[Point] = [(0, 0), (4, 0), (4, 3)]
        self.polygon: Polygon = Polygon(self.vertices)

    def test_vertices(self) -> None:
        """Test that vertices are returned correctly."""
        self.assertEqual(self.polygon.vertices, self.vertices)

    def test_vertex_count(self) -> None:
        """Test the number of vertices."""
        self.assertEqual(self.polygon.vertex_count, 3)

    def test_get_vertex(self) -> None:
        """Test retrieving a vertex by index."""
        self.assertEqual(self.polygon.get_vertex(1), (4, 0))

    def test_len(self) -> None:
        """Test the overloaded len operation."""
        self.assertEqual(len(self.polygon), 3)

    def test_vertices_setter(self) -> None:
        """Test changing the vertices using the property setter."""
        new_vertices: list[Point] = [(1, 1), (2, 1), (2, 2)]
        self.polygon.vertices = new_vertices

        self.assertEqual(self.polygon.vertices, new_vertices)


if __name__ == "__main__":
    unittest.main()