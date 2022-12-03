from exteption import ExceptionUnique
from store import Store


class Shop(Store):
    def __init__(self, items, capacity=20) -> None:
        super(Store, self).__init__(items, capacity)

    def add(self, name_item: str, add_count: int) -> None:
        """
        Проверка свободного места на складе, количества уникальных товаров и добавление новых товаров на склад
        """
        if name_item in self._items.keys() or self.get_unique_items_count < 5:
            super(Shop, self).add(name_item, add_count)
        else:
            raise ExceptionUnique()

    def remove(self, name_item: str, remove_count: int) -> None:
        """
        Проверка количества товара на складе и удаление
        """
        super(Shop, self).remove(name_item, remove_count)

    @property
    def get_free_space(self) -> int:
        """
        Получение количество свободного места на складе
        """
        return super(Shop, self).get_free_space

    @property
    def get_items(self) -> dict[str, int]:
        """
        Возвращение словаря с товарами на складе
        """
        return super(Shop, self).get_items

    @property
    def get_unique_items_count(self) -> int:
        """
        Получение числа уникальных товаров на складе
        """
        return super(Shop, self).get_unique_items_count

    def __repr__(self):
        return super(Shop, self).__repr__()
