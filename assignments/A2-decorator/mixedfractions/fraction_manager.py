"""Singleton manager for processing fractions."""

from fraction import Fraction


class FractionManager:
    """Manage fraction operations using a single instance."""

    _instance: "FractionManager | None" = None

    def __new__(cls) -> "FractionManager":
        """Return the same manager instance each time."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance