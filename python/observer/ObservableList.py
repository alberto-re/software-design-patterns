from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):

    @abstractmethod
    def update(self, **kwargs) -> None:
        pass


class Observable:

    def __init__(self):
        self._observers: List = []

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify_observers(self, **kwargs) -> None:
        for observer in self._observers:
            observer.update(state=self, **kwargs)


class ObservableList(Observable):

    _index: int

    def __init__(self, *args):
        super().__init__()
        self._list: list = []
        if args is not None:
            self._list.extend(*args)

    def __setitem__(self, key: int, value):
        self._list[key] = value
        self.notify_observers(event="set", key=key, value=value)

    def __getitem__(self, key: int):
        self.notify_observers(event="get", key=key)
        return self._list[key]

    def append(self, value):
        self._list.append(value)
        self.notify_observers(event="append", value=value)

    def __len__(self):
        self.notify_observers(event="len")
        return len(self._list)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self._list):
            raise StopIteration
        return self._list[self.index]

    def __str__(self):
        return str(self._list)


class PrintObserver(Observer):

    def update(self, **kwargs):
        state = kwargs.pop("state")
        print(kwargs, "->", state)


def main():
    observer = PrintObserver()

    observable_list = ObservableList([5, 6, 9])
    observable_list.register_observer(observer)

    observable_list.append(3)
    observable_list.append(8)
    observable_list[1] = 15
    observable_list[0]


if __name__ == "__main__":
    main()
