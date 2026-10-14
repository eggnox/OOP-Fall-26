"""Unit tests for FractionManager."""

import unittest

from fraction_manager import FractionManager


class TestFractionManager(unittest.TestCase):
    """Test the Singleton manager and fraction conversion."""

    def test_singleton(self) -> None:
        """Verify that the manager uses one shared instance."""
        manager1 = FractionManager()
        manager2 = FractionManager()

        self.assertIs(manager1, manager2)

    def test_improper_fraction(self) -> None:
        """Test converting an improper fraction."""
        manager = FractionManager()

        self.assertEqual(manager.convert(27, 12), "2 3 / 12")

    def test_proper_fraction(self) -> None:
        """Test converting a proper fraction."""
        manager = FractionManager()

        self.assertEqual(manager.convert(3, 4000), "0 3 / 4000")

    def test_whole_number(self) -> None:
        """Test converting a fraction with no remainder."""
        manager = FractionManager()

        self.assertEqual(manager.convert(10, 2), "5 0 / 2")


if __name__ == "__main__":
    unittest.main()