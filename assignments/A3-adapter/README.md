# Assignment 3 — Weather App: Adapter Pattern and Unit Testing

## Overview

This project implements a Python weather application that retrieves live weather information from the Open-Meteo API and displays it in a formatted terminal interface using Rich.

The application demonstrates object-oriented programming principles, the **Adapter design pattern**, and the **Singleton design pattern**.

The assignment also includes a separate solution to the Kattis problem **Cold-puter Science**, along with automated tests, code coverage, static analysis, UML diagrams, and generated API documentation.

**Links:**
- [GitHub Issue #6](https://github.com/eggnox/OOP-Fall-26/issues/6)
- [Kattis — Cold-puter Science](https://open.kattis.com/problems/cold)
- [Open-Meteo API](https://open-meteo.com/en/docs)

## Features

- Retrieves current weather information for four Colorado cities.
- Displays temperature, apparent temperature, humidity, wind speed, and weather conditions.
- Uses a Rich terminal dashboard for formatted output.
- Converts external API responses into internal weather objects using an Adapter.
- Uses a Singleton manager to coordinate weather requests.
- Supports command-line city selection.
- Includes a separate Kattis-compatible program.
- Uses unittest, Hypothesis, mocking, and patching.
- Includes automated style, type, coverage, and security checks.

## Project Structure

```text
A3-adapter/
├── Makefile
├── README.md
└── cold/
    ├── cold.py
    ├── cold_counter.py
    ├── cold.yaml
    ├── weather_app.py
    ├── weather_reading.py
    ├── weather_adapter.py
    ├── weather_client.py
    ├── weather_manager.py
    ├── weather_dashboard.py
    ├── data/
    ├── tests/
    └── docs/
        ├── html/
        └── uml/
```

## Installation

From the repository root, install the Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

The weather application uses the Rich library and Python's standard-library HTTP functionality.

No weather API key is required.

## Running the Weather Application

Navigate to the application directory:

```bash
cd assignments/A3-adapter/cold
```

Run the program with the default city, Grand Junction:

```bash
python3 weather_app.py
```

Select another supported city:

```bash
python3 weather_app.py --city denver
```

Other city options include:

```bash
python3 weather_app.py --city colorado-springs
python3 weather_app.py --city fort-collins
```

To display command-line help:

```bash
python3 weather_app.py --help
```

The dashboard displays the city's current temperature, feels-like temperature, humidity, wind speed, and weather conditions.

An internet connection is required to retrieve live weather information.

## Design Patterns

### Adapter Pattern

`WeatherAdapter` converts the JSON response returned by Open-Meteo into a `WeatherReading` object.

This separates external API formatting from the application's internal data representation.

The adapter allows the rest of the application to work with a consistent weather model rather than depending directly on third-party JSON fields.

### Singleton Pattern

`WeatherManager` implements the Singleton pattern.

Its `__new__` method ensures that only one manager instance exists. The manager contains a `WeatherClient` and provides a centralized method for requesting weather information.

### Object-Oriented Design

The application uses encapsulation, private attributes, read-only properties, typed methods, and separate classes with distinct responsibilities.

For example, `WeatherReading` stores weather values, `WeatherClient` handles HTTP requests, and `WeatherDashboard` handles presentation.

## Kattis Problem

The assignment includes a separate solution for the Kattis problem **Cold-puter Science**.

The program counts how many temperatures are below zero degrees Celsius.

Run the solution using standard input:

```bash
python3 cold.py
```

The Kattis solution uses `ColdCounter` and does not depend on Rich or the weather API.

Local Kattis tests can be executed from the `A3-adapter` directory using:

```bash
make program-test
```

The project includes the provided sample cases and three additional input/answer test pairs.

## Testing and Code Quality

Tests are located in the `cold/tests/` directory.

The test suite uses:

- **unittest:** Unit test organization and assertions.
- **Hypothesis:** Property-based testing with generated inputs.
- **unittest.mock:** Mocking and patching HTTP requests and application dependencies.
- **pytest:** Running the complete test suite.
- **pytest-cov:** Measuring statement coverage.
- **Mypy:** Static type checking.
- **Flake8:** Python style checking.
- **Bandit:** Security analysis.

The latest verified test results include **48 passing unit tests, 2 passing subtests, and 100% statement coverage across all eight production modules**.

### Makefile Commands

Run these commands from `assignments/A3-adapter/`:

| Command | Description |
|---|---|
| `make test` | Run unit tests |
| `make coverage` | Run tests with a 100% coverage requirement |
| `make style` | Run Flake8 |
| `make typecheck` | Run Mypy |
| `make fix` | Format Python files with autopep8 |
| `make security` | Run Bandit |
| `make program-test` | Run local Kattis tests |
| `make docs` | Generate pdoc HTML documentation |

To run all major quality checks:

```bash
make style
make typecheck
make test
make coverage
make security
```

## UML Diagrams

The project includes three UML diagrams documenting its architecture and behavior.

### Class Diagram

Shows the project's classes, attributes, methods, and relationships.

[View Class Diagram](cold/docs/uml/class-diagram.png)

### Sequence Diagram

Illustrates how the application retrieves weather data through the manager, client, API, adapter, and dashboard.

[View Sequence Diagram](cold/docs/uml/sequence-diagram.png)

### Activity Diagram

Shows the workflow from city selection through API retrieval, data conversion, and presentation.

[View Activity Diagram](cold/docs/uml/activity-diagram.png)

PlantUML source files are included alongside the exported images.

## API Documentation

HTML documentation is generated using pdoc and stored in:

`cold/docs/html/`

Open `cold/docs/html/index.html` in a browser to explore the generated module documentation.

Regenerate the documentation by running:

```bash
make docs
```

## External Services and Libraries

- **Open-Meteo:** Provides current weather information.
- **Rich:** Displays formatted weather information in the terminal.
- **Hypothesis:** Generates test cases for property-based testing.
- **Kattis:** Provides the separate programming challenge and testing interface.

The weather application does not require storing credentials or API keys.

## Assignment Status

The implementation, local unit tests, coverage checks, security analysis, documentation, and UML diagrams have been completed.

Final GitHub Actions verification, official Kattis submission, and repository release steps are handled separately.