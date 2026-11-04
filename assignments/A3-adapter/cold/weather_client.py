
"""HTTP client for retrieving current weather data."""

import json
from typing import Any
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen

from weather_adapter import WeatherAdapter
from weather_reading import WeatherReading


class WeatherClient:
    """Retrieve weather data from the Open-Meteo API."""

    API_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self, timeout: float = 10.0) -> None:
        """Initialize the client with a request timeout."""
        if timeout <= 0:
            raise ValueError("Timeout must be positive")

        self._timeout = timeout

    @property
    def timeout(self) -> float:
        """Return the request timeout."""
        return self._timeout

    def fetch_current(
        self,
        city: str,
        latitude: float,
        longitude: float,
    ) -> WeatherReading:
        """Retrieve and adapt current weather for a location."""
        parameters: dict[str, str | float] = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,apparent_temperature,"
                "relative_humidity_2m,wind_speed_10m,"
                "weather_code"
            ),
            "temperature_unit": "celsius",
            "wind_speed_unit": "kmh",
        }

        url = f"{self.API_URL}?{urlencode(parameters)}"

        try:
            with urlopen(url, timeout=self._timeout) as response:
                data: dict[str, Any] = json.load(response)
        except (URLError, TimeoutError, json.JSONDecodeError) as error:
            raise RuntimeError(
                "Unable to retrieve weather data"
            ) from error

        return WeatherAdapter.adapt(data, city)
