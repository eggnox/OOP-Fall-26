
# Assignment 3 - Weather App and Adapter Pattern

PYTHON = python3
PROJECT = cold

.PHONY: test style typecheck coverage fix program-test docs security

test:
	cd $(PROJECT) && $(PYTHON) -m pytest tests/ -v

style:
	cd $(PROJECT) && $(PYTHON) -m flake8 *.py tests/

typecheck:
	cd $(PROJECT) && $(PYTHON) -m mypy *.py tests/test_*.py

coverage:
	cd $(PROJECT) && $(PYTHON) -m pytest tests/ \
		--cov=weather_reading \
		--cov=weather_adapter \
		--cov=weather_client \
		--cov=weather_manager \
		--cov=weather_dashboard \
		--cov=weather_app \
		--cov=cold_counter \
		--cov=cold \
		--cov-report=term-missing \
		--cov-fail-under=100


fix:
	cd $(PROJECT) && $(PYTHON) -m autopep8 --in-place *.py tests/test_*.py

program-test:
	cd $(PROJECT) && kattis test -p cold -l python3 -m cold.py cold.py cold_counter.py

docs:
	cd $(PROJECT) && $(PYTHON) -m pdoc -o docs/html cold cold_counter weather_reading weather_adapter weather_client weather_manager weather_dashboard weather_app

security:
	cd $(PROJECT) && $(PYTHON) -m bandit -q *.py

