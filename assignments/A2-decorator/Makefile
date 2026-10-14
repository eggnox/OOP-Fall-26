
PYTHON = python3
PROJECT = mixedfractions

.PHONY: test program-test style typecheck coverage docs security

test:
	cd $(PROJECT) && $(PYTHON) -m unittest discover -s tests -v

program-test:
	cd $(PROJECT) && kattis test -p mixedfractions -l python3 -m mixedfractions.py mixedfractions.py fraction.py fraction_manager.py fraction_formatter.py


style:
	cd $(PROJECT) && $(PYTHON) -m flake8 fraction.py fraction_manager.py fraction_formatter.py mixedfractions.py tests


typecheck:
	cd $(PROJECT) && $(PYTHON) -m mypy fraction.py fraction_manager.py fraction_formatter.py mixedfractions.py tests/test_*.py


coverage:
	cd $(PROJECT) && $(PYTHON) -m coverage run --source=fraction,fraction_manager,fraction_formatter,mixedfractions -m unittest discover -s tests
	cd $(PROJECT) && $(PYTHON) -m coverage report -m


docs:
	cd $(PROJECT) && $(PYTHON) -m pdoc -o docs/html fraction fraction_manager fraction_formatter mixedfractions


security:
	cd $(PROJECT) && $(PYTHON) -m bandit -q fraction.py fraction_manager.py fraction_formatter.py mixedfractions.py

