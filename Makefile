PYTHON := python3
VENV := flyinenv
VENV_PYTHON := $(VENV)/bin/python3

MAIN := src/flyin.py
CONFIG ?= maps/easy/01_linear_path.txt
REQUIREMENTS := requirements.txt

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PYTHON) -m pip install -r $(REQUIREMENTS)

run: 
	$(VENV_PYTHON) $(MAIN) $(CONFIG)

debug:
	$(VENV_PYTHON) -m pdb $(MAIN) $(CONFIG)

clean: clean-venv
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -prune -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -prune -exec rm -rf {} +
	find . -type f \( -name "*.pyc" -o -name "*.pyo" \) -delete

clean-venv:
	test -n "$(VENV)" && test "$(VENV)" != "/" && rm -rf "$(VENV)"

lint:
	$(VENV_PYTHON) -m flake8 . --exclude=$(VENV)
	$(VENV_PYTHON) -m mypy . --exclude '^$(VENV)/' \
							--warn-return-any \
							--warn-unused-ignores \
							--ignore-missing-imports \
							--disallow-untyped-defs \
							--check-untyped-defs

lint-strict:
	$(VENV_PYTHON) -m flake8 . --exclude=$(VENV)
	$(VENV_PYTHON) -m mypy . --exclude '^$(VENV)/' --strict


.PHONY: install run debug lint lint-strict clean clean-venv