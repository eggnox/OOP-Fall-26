
# Assignment 4 — Statistics / Template Method Pattern

PYTHON = python3
PROJECT = statistics

.PHONY: all test style typecheck coverage security \
        program-test manual-test docs fix

all: style typecheck test coverage security program-test
	@echo "All Assignment 4 checks passed!"

test:
	cd $(PROJECT) && $(PYTHON) -m pytest tests/ -v

style:
	cd $(PROJECT) && $(PYTHON) -m flake8 *.py tests/

typecheck:
	cd $(PROJECT) && $(PYTHON) -m mypy *.py tests/test_*.py

coverage:
	cd $(PROJECT) && $(PYTHON) -m pytest tests/ \
		--cov=kattis \
		--cov=statistics_values \
		--cov=statistics_template \
		--cov=statistics_solution \
		--cov=statistics_main \
		--cov-report=term-missing \
		--cov-fail-under=100

security:
	cd $(PROJECT) && $(PYTHON) -m bandit -q *.py

program-test:
	@cd $(PROJECT) && set -eu; \
	for file in data/*.in; do \
		[ -f "$$file" ] || { echo "No test inputs found"; exit 1; }; \
		echo "Testing $$file"; \
		$(PYTHON) statistics_main.py < "$$file" | \
			diff -u "$${file%.in}.ans" -; \
	done
	@echo "All whole-program tests passed!"

manual-test:
	cd $(PROJECT) && printf '4 4 7 10 6\n3 -10 0 5\n1 8\n' | \
		$(PYTHON) statistics_main.py

docs:
	cd $(PROJECT) && $(PYTHON) -m pdoc -o docs/html \
		kattis statistics_values statistics_template \
		statistics_solution statistics_main

fix:
	cd $(PROJECT) && $(PYTHON) -m autopep8 \
		--in-place *.py tests/test_*.py