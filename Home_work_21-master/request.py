from typing import TypeVar

from abstract_class import Storage

T = TypeVar('T', bound=Storage)


class Request:
    def __init__(self, request: str, stock: dict[str, T]):
        self._request = request.lower().split(' ')
        self._stock = stock
        self._amount = int(self._request[self._request.index('доставить') + 1])
        self._product = self._request[self._request.index('доставить') + 2]
        self._from_name = self._request[self._request.index('из') + 1]
        self._to_name = self._request[self._request.index('в') + 1]

        if self._to_name not in self._stock or self._from_name not in self._stock:
            raise IndexError()

    @property
    def from_market(self) -> T:
        return self._stock[self._from_name]

    @property
    def to_market(self) -> T:
        return self._stock[self._to_name]

    @property
    def from_name(self) -> str:
        return self._from_name

    @property
    def to_name(self) -> str:
        return self._to_name

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def product(self) -> str:
        return self._product

    def __repr__(self):
        return f'Это запрос с {self.amount} {self.product} с {self.from_name} до {self.to_name}'
