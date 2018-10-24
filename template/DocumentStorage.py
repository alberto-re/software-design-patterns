import json
import yaml
from abc import ABC, abstractmethod
from typing import IO


class DocumentStorage(ABC):

    _file: IO

    def store(self, filename: str, document: dict) -> None:
        """This is the template method, and is supposed to not being overridden"""
        self._open(filename)
        self._write(document)
        self._close()

    @abstractmethod
    def _write(self, document: dict) -> None:
        pass

    def _open(self, filename: str) -> None:
        self._file = open(filename, 'w')

    def _close(self) -> None:
        self._file.close()


class JsonDocumentStorage(DocumentStorage):

    def __init__(self) -> None:
        super().__init__()

    def _write(self, document: dict) -> None:
        self._file.write(json.dumps(document))


class YamlDocumentStorage(DocumentStorage):

    def __init__(self) -> None:
        super().__init__()

    def _write(self, document: dict) -> None:
        self._file.write(yaml.dump(document, default_flow_style=False))


def main() -> None:

    content = {"name": "Bob", "age": 28, "sex": "male"}

    storage: DocumentStorage = JsonDocumentStorage()
    storage.store("file.json", content)

    storage = YamlDocumentStorage()
    storage.store("file.yaml", content)


if __name__ == "__main__":
    main()
