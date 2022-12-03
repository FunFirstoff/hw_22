from abstract_class import Storage
from exception import ExceptionValueItem, ExceptionNotEnough


class Store(Storage):
    def __init__(self, items, capacity=100) -> None:
        if not items:
            self._items = {}
        else:
            self._items = items
        self._capacity = capacity

    def add(self, name_item: str, add_count: int) -> None:
        """
        Проверка свободного места на складе и добавление новых товаров на склад
        """
        result_capacity = self.get_free_space - add_count
        if result_capacity >= 0:
            self._items[name_item] = add_count
        else:
            self._items[name_item] = self._items[name_item] + add_count

    def remove(self, name_item: str, remove_count: int) -> None:
        """
        Проверка количества товара на складе и удаление
        """
        count_items = self._items.get(name_item, 0) - remove_count
        if count_items >= 0:
            if isinstance(self, Store):
                print('Нужное количество есть на складе')
            else:
                print('Нужное количество есть в магазине')
            self._items[name_item] = self._items[name_item] - remove_count
            if self._items[name_item] == 0:
                del self._items[name_item]
        else:
            raise ExceptionNotEnough('Недостаточно товара на складе')

    @property
    def get_free_space(self) -> int:
        """
        Получение количество свободного места на складе
        """
        return self._capacity - sum(self._items.values())

    @property
    def get_items(self) -> dict:
        """
        Возвращение словаря с товарами на складе
        """
        return self._items

    @property
    def get_unique_items_count(self) -> int:
        """
        Получение числа уникальных товаров на складе
        """
        return len(set(self._items.keys()))

    def __repr__(self):
        return f'Склад с товарами {self.get_items} и вместимостью {self._capacity}'
