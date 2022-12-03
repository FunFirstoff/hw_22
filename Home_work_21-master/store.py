from abstract_class import Storage
from exteption import ExceptionValueItem, ExceptionNotEnough


class Store(Storage):
    def __init__(self, items, capacity=100) -> None:
        super(Store, self).__init__(items, capacity)

    def add(self, name_item: str, add_count: int) -> None:
        """
        Проверка свободного места на складе и добавление новых товаров на склад
        """
        result_capacity = self.get_free_space - add_count
        if result_capacity >= 0:
            super(Store, self).add(name_item, add_count)
        else:
            raise ExceptionValueItem()

    def remove(self, name_item: str, remove_count: int) -> None:
        """
        Проверка количества товара на складе и удаление
        """
        count_items = self._items.get(name_item, 0) - remove_count
        if count_items >= 0:
            print('Нужное количество есть на складе')
            super(Store, self).remove(name_item, remove_count)
        else:
            raise ExceptionNotEnough()

    @property
    def get_free_space(self) -> int:
        """
        Получение количество свободного места на складе
        """
        return super(Store, self).get_free_space

    @property
    def get_items(self) -> dict:
        """
        Возвращение словаря с товарами на складе
        """
        return super(Store, self).get_items

    @property
    def get_unique_items_count(self) -> int:
        """
        Получение числа уникальных товаров на складе
        """
        return super(Store, self).get_unique_items_count

    def __repr__(self):
        return super(Store, self).__repr__()
