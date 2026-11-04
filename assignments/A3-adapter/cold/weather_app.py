
"""Main application for displaying live Colorado weather."""

import argparse

from weather_dashboard import WeatherDashboard
from weather_manager import WeatherManager


CITY_COORDINATES: dict[str, tuple[str, float, float]] = {
    "grand-junction": ("Grand Junction", 39.0639, -108.5506),
    "denver": ("Denver", 39.7392, -104.9903),
    "colorado-springs": ("Colorado Springs", 38.8339, -104.8214),
    "fort-collins": ("Fort Collins", 40.5853, -105.0844),
}


def main(argv: list[str] | None = None) -> None:
    """Retrieve and display live weather for a selected city."""
    parser = argparse.ArgumentParser(
        description="Live Colorado Weather Dashboard"
    )

    parser.add_argument(
        "--city",
        choices=sorted(CITY_COORDINATES),
        default="grand-junction",
        help="Choose a Colorado city",
    )

    args = parser.parse_args(argv)

    city, latitude, longitude = CITY_COORDINATES[args.city]

    manager = WeatherManager()
    weather = manager.get_weather(
        city=city,
        latitude=latitude,
        longitude=longitude,
    )

    dashboard = WeatherDashboard()
    dashboard.show(weather)


if __name__ == "__main__":  # pragma: no cover
    main()
