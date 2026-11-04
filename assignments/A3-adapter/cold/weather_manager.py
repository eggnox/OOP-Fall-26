
"""Singleton manager for weather information."""

from __future__ import annotations

from typing import ClassVar

from weather_client import WeatherClient
from weather_reading import WeatherReading


class WeatherManager:
    """Manage weather requests using the Singleton pattern."""

    _instance: ClassVar[WeatherManager | None] = None

    def __new__(
    cls, client: WeatherClient | None = None
) -> WeatherManager:
        """Create only one manager instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, client: WeatherClient | None = None) -> None:
        """Initialize the weather client only once."""
        if not hasattr(self, "_client"):
            self._client = client if client is not None else WeatherClient()

    @property
    def client(self) -> WeatherClient:
        """Return the weather client."""
        return self._client

    def get_weather(
        self,
        city: str,
        latitude: float,
        longitude: float,
    ) -> WeatherReading:
        """Retrieve current weather for a city."""
        return self._client.fetch_current(
            city=city,
            latitude=latitude,
            longitude=longitude,
        )
