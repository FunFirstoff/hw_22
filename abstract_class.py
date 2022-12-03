from abc import ABC, abstractmethod
from exception import ExceptionValueItem


class Storage(ABC):

    @abstractmethod
    def add(self, name_item: str, add_count: int) -> None:
        """
        Добавление новых товаров на склад

        :param name_item: Название товара
        :param add_count: Количество товара
        """
        raise NotImplemented

    @abstractmethod
    def remove(self, name_item: str, remove_count: int) -> None:
        """
        Удаление товара из склада

        :param name_item: Название товара
        :param add_count: Количество товара
        """
        raise NotImplemented

    @property
    @abstractmethod
    def get_free_space(self) -> int:
        """
        Получение количество свободного места на складе
        """
        raise NotImplemented

    @property
    @abstractmethod
    def get_items(self) -> dict:
        """
        Возвращение словаря с товарами на складе
        """
        raise NotImplemented

    @property
    @abstractmethod
    def get_unique_items_count(self) -> int:
        """
        Получение числа уникальных товаров на складе
        """
        raise NotImplemented
