
# Assignment 2 — Mixed Fractions

## Overview

This project solves the Kattis Mixed Fractions problem using Python and object-oriented design.

The program converts improper fractions into mixed numbers. It demonstrates exception handling, operator overloading, the Singleton pattern, and the Decorator pattern.

**Kattis Problem:** https://open.kattis.com/problems/mixedfractions

**Kattis Verdict:** Accepted

## Program Structure

- `fraction.py` — Fraction class, properties, validation, and addition operator.
- `fraction_manager.py` — Singleton manager for converting fractions.
- `fraction_formatter.py` — Formatter classes implementing the Decorator pattern.
- `mixedfractions.py` — Main program that reads input and prints results.
- `tests/` — Unit tests, including Hypothesis-generated tests.
- `data/` — Kattis sample tests and additional test cases.
- `docs/uml/` — Class, sequence, and activity diagrams.
- `docs/html/` — Generated HTML documentation.

## OOP Features

### Exception Handling
The Fraction class raises a ValueError when the denominator is zero or negative.

### Operator Overloading
The Fraction class implements `__add__` to support adding two fractions.

### Singleton Pattern
FractionManager uses the Singleton pattern to maintain one manager instance.

### Decorator Pattern
SpacedFractionDecorator wraps BasicMixedFormatter to add spaces around the fraction slash without changing the original formatter.

## Running the Program

From the repository root:

```bash
python3 assignments/A2-decorator/mixedfractions/mixedfractions.py
```

Example input:

```text
27 12
0 0
```

Expected output:

```text
2 3 / 12
```

## Testing

From the repository root, start the Docker environment:

```bash
./run-docker.sh
```

Then run the following commands:

```bash
make a2-test
make a2-style
make a2-typecheck
make a2-coverage
make a2-security
make a2-docs
make a2-program-test
```

## Results

- 24 unit tests passed.
- 4 local Kattis tests passed.
- 100% code coverage.
- Flake8 and Mypy checks passed.
- Bandit security checks passed.
- GitHub Actions CI/CD passed.
- Official Kattis submission: Accepted.

## Evidence

Screenshots of testing, coverage, and Kattis submission results are located in the `screenshots/` directory.
