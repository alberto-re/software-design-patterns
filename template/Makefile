FLAKE8 = python -m flake8 --max-line-length=120
MYPY = python -m mypy

.PHONY: DocumentStorage.py

default: DocumentStorage.py

DocumentStorage.py:
	$(FLAKE8) DocumentStorage.py
	$(MYPY) DocumentStorage.py
