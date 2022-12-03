from abc import ABC, abstractmethod

from exteption import ExceptionValueItem


class Storage(ABC):
    @abstractmethod
    def __init__(self, items: dict[str, int], capacity: int) -> None:
        """
        Инициализация полей объекта из полей класса по умолчанию
        """
        if not sum(items.values()) > capacity:
            self._items = items
            self._capacity = capacity
        else:
            raise ExceptionValueItem('Количество товаров превышает вместимость')

    @abstractmethod
    def add(self, name_item: str, add_count: int) -> None:
        """
        Добавление новых товаров на склад

        :param name_item: Название товара
        :param add_count: Количество товара
        """
        if name_item not in self._items:
            self._items[name_item] = add_count
        else:
            self._items[name_item] = self._items[name_item] + add_count

    @abstractmethod
    def remove(self, name_item: str, add_count: int) -> None:
        """
        Удаление товара из склада

        :param name_item: Название товара
        :param add_count: Количество товара
        """
        self._items[name_item] = self._items[name_item] - add_count
        if self._items[name_item] == 0:
            del self._items[name_item]

    @property
    @abstractmethod
    def get_free_space(self) -> int:
        """
        Получение количество свободного места на складе
        """
        return self._capacity - sum(self._items.values())

    @property
    @abstractmethod
    def get_items(self) -> dict:
        """
        Возвращение словаря с товарами на складе
        """
        return self._items

    @property
    @abstractmethod
    def get_unique_items_count(self) -> int:
        """
        Получение числа уникальных товаров на складе
        """
        return len(set(self._items.keys()))

    @abstractmethod
    def __repr__(self):
        return f'Склад с товарами {self.get_items} и вместимостью {self._capacity}'
