
"""Weather data model for the weather application."""


class WeatherReading:
    """Represent weather information for a city."""

    def __init__(
        self,
        city: str,
        temperature_c: float,
        feels_like_c: float,
        humidity_percent: int,
        wind_speed_kmh: float,
        condition: str,
    ) -> None:
        """Initialize a weather reading."""
        self._city = city
        self._temperature_c = temperature_c
        self._feels_like_c = feels_like_c
        self._humidity_percent = humidity_percent
        self._wind_speed_kmh = wind_speed_kmh
        self._condition = condition

    @property
    def city(self) -> str:
        """Return the city name."""
        return self._city

    @property
    def temperature_c(self) -> float:
        """Return the temperature in Celsius."""
        return self._temperature_c

    @property
    def feels_like_c(self) -> float:
        """Return the apparent temperature."""
        return self._feels_like_c

    @property
    def humidity_percent(self) -> int:
        """Return the relative humidity percentage."""
        return self._humidity_percent

    @property
    def wind_speed_kmh(self) -> float:
        """Return the wind speed in kilometers per hour."""
        return self._wind_speed_kmh

    @property
    def condition(self) -> str:
        """Return the weather condition description."""
        return self._condition
