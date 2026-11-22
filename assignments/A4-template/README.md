# Assignment 4 — Statistics: Template Method Pattern

## Overview

This assignment solves the Kattis Statistics problem using object-oriented programming, inheritance, abstract base classes, and the Template Method design pattern.

The program reads multiple test cases until the end of input and calculates the minimum, maximum, and range for each case.

**Kattis Problem:** https://open.kattis.com/problems/statistics

**GitHub Issue:** https://github.com/eggnox/OOP-Fall-26/issues/8

## Design Patterns and OOP Concepts

### Template Method Pattern

The `StatisticsTemplate` class inherits from the professor-provided `Kattis` abstract base class.

Its `run()` method defines the sequence of operations:

1. `read_input()` — Read and validate test cases.
2. `solve()` — Calculate the statistics.
3. `print_answer()` — Display the results.

The `StatisticsSolution` subclass provides the implementations of these operations.

This demonstrates how the Template Method pattern separates the overall algorithm from its individual steps.

### Inheritance

The `StatisticsValues` class inherits from Python's built-in `list[int]` class.

It adds three read-only properties:

- `minimum` — Returns the smallest integer.
- `maximum` — Returns the largest integer.
- `spread` — Returns the difference between the maximum and minimum.

### Abstract Base Class

The project uses the instructor-provided `Kattis` abstract base class from:

https://github.com/rambasnet/Object-Oriented-Programming-Design-Patterns/blob/main/demo-assignments/A2-ABC/egypt/src/kattis.py

The class requires implementations of `read_input()`, `data`, `answer`, `solve()`, and `print_answer()`.

## Project Structure

The `statistics/` directory contains the following Python modules:

| File | Purpose |
|---|---|
| `kattis.py` | Professor-provided abstract base class |
| `statistics_values.py` | List inheritance and statistics calculations |
| `statistics_template.py` | Template Method implementation |
| `statistics_solution.py` | Kattis input parsing and problem solution |
| `statistics_main.py` | Command-line entry point |

Additional directories include `tests/` for automated tests, `data/` for whole-program test cases, and `docs/uml/` for diagrams.

## Running the Program

From the `A4-template` directory, run:

`make manual-test`

To provide custom input, navigate to `statistics/` and run:

`python3 statistics_main.py`

For example, input:

```text
4 4 7 10 6
3 -10 0 5
1 8
```

Produces:

```text
Case 1: 4 10 6
Case 2: -10 5 15
Case 3: 8 8 0
```

The program supports multiple cases and handles negative integers and repeated values.

## Testing and Code Quality

The project uses `unittest`, `pytest`, Hypothesis, and mocking/patching to test its functionality.

**Verified local results:**

- 22 passing automated tests
- 100% statement coverage across five production modules
- 3 passing whole-program test cases
- Successful Flake8 style checking
- Successful Mypy type checking
- Successful Bandit security analysis
- Successful GitHub Actions CI/CD

Run all checks from the assignment directory using:

`make all`

Individual commands include `make test`, `make style`, `make typecheck`, `make coverage`, `make security`, and `make program-test`.

## UML Diagrams

Three UML diagrams document the system's design and execution.

### Class Diagram

Shows inheritance from `Kattis` and `list`, including the relationship between the Template Method and the Statistics solution.

[View Class Diagram](statistics/docs/uml/class-diagram.png)

### Sequence Diagram

Illustrates how the program reads input, creates statistics objects, calculates results, and prints answers.

[View Sequence Diagram](statistics/docs/uml/sequence-diagram.png)

### Activity Diagram

Shows the execution flow, input validation, test-case loops, and output process.

[View Activity Diagram](statistics/docs/uml/activity-diagram.png)

PlantUML source files are provided alongside the PNG diagrams.

## Documentation and Evidence

API documentation can be generated using:

`make docs`

This generates HTML documentation under `statistics/docs/html/`.

Testing screenshots will be saved in the `screenshots/` directory.

## Assignment Status

The object-oriented implementation, unit testing, coverage, UML diagrams, and CI/CD integration are complete.

The Statistics solution was officially Accepted by Kattis, passing all 51 test cases with a runtime of 0.06 seconds. All local tests, UML diagrams, and CI/CD checks are complete. Final GitHub merge, tag, and release are pending.