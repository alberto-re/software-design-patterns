JAVAC = javac
FLAKE8 = python -m flake8 --max-line-length=120
MYPY = python -m mypy

.PHONY: clean Logger.py

default: Logger.class Logger.py

Logger.class: Logger.java
	$(JAVAC) Logger.java

Logger.py:
	$(FLAKE8) Logger.py
	$(MYPY) Logger.py

clean:
	- rm *.class