
"""Adapter for converting Open-Meteo API data."""

from typing import Any, ClassVar

from weather_reading import WeatherReading


class WeatherAdapter:
    """Convert third-party weather data into WeatherReading."""

    CONDITIONS: ClassVar[dict[int, str]] = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Freezing fog",
        51: "Light drizzle",
        61: "Light rain",
        63: "Rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Snow",
        75: "Heavy snow",
        95: "Thunderstorm",
    }

    @staticmethod
    def adapt(data: dict[str, Any], city: str) -> WeatherReading:
        """Convert an Open-Meteo response into a weather reading."""
        current: dict[str, Any] = data["current"]
        code: int = int(current["weather_code"])

        return WeatherReading(
            city=city,
            temperature_c=float(current["temperature_2m"]),
            feels_like_c=float(current["apparent_temperature"]),
            humidity_percent=int(current["relative_humidity_2m"]),
            wind_speed_kmh=float(current["wind_speed_10m"]),
            condition=WeatherAdapter.CONDITIONS.get(
                code, "Unknown"
            ),
        )
