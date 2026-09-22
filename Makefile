TEST = pytest
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
COVERAGE = python -m pytest
ASSIGNMENT = ./assignments
A1 = $(ASSIGNMENT)/A1-OOD/convexpolygonarea

.PHONY: all check-type check-style run-test coverage clean

all: check-style check-type run-test
	@echo "All checks passed"

check-type:
	$(MAKE) -C $(A1) type

check-style:
	$(MAKE) -C $(A1) style

run-test:
	$(MAKE) -C $(A1) test

coverage:
	$(MAKE) -C $(A1) coverage

clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf `find . -type d -name .hypothesis`
	rm -rf `find . -name .coverage`