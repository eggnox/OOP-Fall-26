
"""Unit tests for the WeatherReading class."""

import unittest

from hypothesis import given, settings
from hypothesis import strategies as st

from weather_reading import WeatherReading


class TestWeatherReading(unittest.TestCase):
    """Test weather reading attributes and properties."""

    def test_normal_weather(self) -> None:
        """Test a normal weather reading."""
        weather = WeatherReading(
            "Grand Junction", 20.5, 19.0, 45, 12.5, "Clear sky"
        )

        self.assertEqual(weather.city, "Grand Junction")
        self.assertEqual(weather.temperature_c, 20.5)
        self.assertEqual(weather.feels_like_c, 19.0)
        self.assertEqual(weather.humidity_percent, 45)
        self.assertEqual(weather.wind_speed_kmh, 12.5)
        self.assertEqual(weather.condition, "Clear sky")

    def test_boundary_weather(self) -> None:
        """Test freezing temperatures and zero wind."""
        weather = WeatherReading(
            "Denver", 0.0, -5.0, 100, 0.0, "Snow"
        )

        self.assertEqual(weather.city, "Denver")
        self.assertEqual(weather.temperature_c, 0.0)
        self.assertEqual(weather.feels_like_c, -5.0)
        self.assertEqual(weather.humidity_percent, 100)
        self.assertEqual(weather.wind_speed_kmh, 0.0)
        self.assertEqual(weather.condition, "Snow")

    @settings(max_examples=30)
    @given(
        temperature=st.floats(
            min_value=-80,
            max_value=60,
            allow_nan=False,
            allow_infinity=False,
        ),
        feels_like=st.floats(
            min_value=-100,
            max_value=70,
            allow_nan=False,
            allow_infinity=False,
        ),
        humidity=st.integers(min_value=0, max_value=100),
        wind=st.floats(
            min_value=0,
            max_value=300,
            allow_nan=False,
            allow_infinity=False,
        ),
    )
    def test_generated_weather(
        self,
        temperature: float,
        feels_like: float,
        humidity: int,
        wind: float,
    ) -> None:
        """Test weather properties with generated values."""
        weather = WeatherReading(
            "Test City",
            temperature,
            feels_like,
            humidity,
            wind,
            "Cloudy",
        )

        self.assertEqual(weather.city, "Test City")
        self.assertEqual(weather.temperature_c, temperature)
        self.assertEqual(weather.feels_like_c, feels_like)
        self.assertEqual(weather.humidity_percent, humidity)
        self.assertEqual(weather.wind_speed_kmh, wind)
        self.assertEqual(weather.condition, "Cloudy")


if __name__ == "__main__":
    unittest.main()
