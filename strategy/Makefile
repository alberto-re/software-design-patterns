FLAKE8 = python -m flake8 --max-line-length=120
MYPY = python -m mypy

.PHONY: clean CacheableHttpRequest.py

default: CacheableHttpRequest.py

CacheableHttpRequest.py:
	$(FLAKE8) CacheableHttpRequest.py
	$(MYPY) CacheableHttpRequest.py