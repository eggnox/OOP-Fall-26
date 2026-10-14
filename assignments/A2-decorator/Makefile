
PYTHON = python3
PROJECT = mixedfractions

.PHONY: test program-test style typecheck

test:
	cd $(PROJECT) && $(PYTHON) -m unittest discover -s tests -v

program-test:
	cd $(PROJECT) && kattis test -p mixedfractions -l python3 -m mixedfractions.py mixedfractions.py fraction.py fraction_manager.py fraction_formatter.py


style:
	cd $(PROJECT) && $(PYTHON) -m flake8 fraction.py fraction_manager.py fraction_formatter.py mixedfractions.py tests


typecheck:
	cd $(PROJECT) && $(PYTHON) -m mypy fraction.py fraction_manager.py fraction_formatter.py mixedfractions.py tests/test_*.py
