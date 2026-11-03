# Assignment 3 — Weather App

## Overview
Build an Open-Meteo weather client with a Rich terminal interface using an Adapter pattern and Singleton manager. The weather dashboard is separate from the Kattis-compatible `cold.py` mode.

- **GitHub issue:** [#6](https://github.com/eggnox/OOP-Fall-26/issues/6)
- **Kattis:** [Cold-puter Science](https://open.kattis.com/problems/cold)
- **Weather API:** [Open-Meteo](https://open-meteo.com/en/docs)
- **Status:** In progress

## Goals
- OOP with private attributes, properties and typed public APIs
- Singleton manager and API-to-domain adapter
- Rich CLI weather interface and exact-output Kattis entry point
- `unittest`, Hypothesis, mocked network responses, and 100% pytest-cov
- Three UML diagrams, pdoc HTML, Makefile, CI, and submission evidence

> Do not embed secrets or commit API keys.
