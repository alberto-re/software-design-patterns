FLAKE8 = python -m flake8 --max-line-length=120
MYPY = python -m mypy

.PHONY: flake8 mypy

default: flake8 mypy

flake8:
	$(FLAKE8) .

mypy:
	find -mindepth 1 -maxdepth 1 -name "[!.]*" -type d -exec $(MYPY) {} \;