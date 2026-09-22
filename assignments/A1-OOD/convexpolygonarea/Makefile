PYTHON = python3
SOURCE_FILES = convexpolygonarea.py polygon.py area_calculator.py
TEST_FILES = tests/*.py

.PHONY: all style fix type test kattis coverage docs clean

all: style type test kattis

style:
	flake8 $(SOURCE_FILES) $(TEST_FILES)

fix:
	autopep8 --in-place $(SOURCE_FILES) $(TEST_FILES)

type:
	mypy $(SOURCE_FILES) $(TEST_FILES)

test:
	pytest tests -v

kattis:
	printf "n\n" | kattis test convexpolygonarea.py

coverage:
	pytest --cov=. --cov-report=term-missing tests

docs:
	rm -rf docs/*
	pdoc -o docs $(SOURCE_FILES)
	rm -f docs/.gitignore

clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -f .coverage
