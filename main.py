from exception import ExceptionValueItem, ExceptionUnique, ExceptionNotEnough
from request import Request
from shop import Shop
from store import Store

shop = Shop({})
store = Store({'печеньки': 20, 'коты': 20, 'собачки': 20, 'хлеб': 15, 'вода': 15, 'коробки': 10})

STOCK = {'магазин': shop,
         'склад': store}


class StoreSimulator:

    def __init__(self, stock):
        self._stock = stock

    def get_user_str(self):
        user_str = input('Введите запрос - ')
        if user_str.lower() in ['stop', 'exit', 'close']:
            return 1

        try:
            req = Request(request=user_str, stock=self._stock)
            return req
        except (ValueError, IndexError):
            print("Неправильный запрос")

    # перемещение товаров со склада на склад
    def move_items(self, request):
        try:
            request.from_market.remove(request.product, request.amount)
            request.to_market.add(request.product, request.amount)
            print(f'Курьер забрал {request.amount} {request.product} со {request.from_name}')
            print(f'Курьер везет {request.amount} {request.product} со {request.from_name} в {request.to_name}')
            print(f'Курьер доставил {request.amount} {request.product} в {request.to_name}')
        except ExceptionNotEnough:
            print(f"Не хватает в {request.from_name}, попробуйте заказать меньше")
        except ExceptionValueItem:
            request.from_market.add(request.product, request.amount)
            print(f"В {request.to_name} недостаточно места, попробуйте что то другое")
        except ExceptionUnique:
            request.from_market.add(request.product, request.amount)
            print(f"В {request.to_name} может быть не больше пяти разновидностей товаров")
        else:
            return True

    # Вывод остатков
    def stock_remain(self, request):
        print('-' * 100)
        print(f'В {request.from_name} хранится:')
        for key, item in request.from_market.get_items.items():
            print(f"{key} - {item}")
        print('-' * 100)
        print(f'В {request.from_name} хранится:')
        for key, item in request.from_market.get_items.items():
            print(f"{key} - {item}")
        print('-' * 100)

    def start(self):
        req = self.get_user_str()
        if req == 1:
            exit()
        if req is not None:
            if self.move_items(req):
                self.stock_remain(req)


if __name__ == "__main__":
    while True:
        StoreSimulator(stock=STOCK).start()
