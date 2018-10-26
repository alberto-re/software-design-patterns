from typing import Optional
from datetime import datetime


class Logger:

    _FORMAT = "%s - %s"
    _instance: Optional["Logger"] = None

    def __new__(cls):
        if Logger._instance is None:
            Logger._instance = object.__new__(cls)
        return Logger._instance

    def log(self, msg: str) -> None:
        print(Logger._FORMAT % (datetime.now(), msg))


if __name__ == "__main__":
    logger = Logger()
    logger.log("Logger initialized")
    assert logger == Logger()
