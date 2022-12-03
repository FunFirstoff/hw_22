from exteption import ExceptionValueItem, ExceptionUnique, ExceptionNotEnough
from request import Request
from shop import Shop
from store import Store

shop = Shop({})
store = Store({'печеньки': 20, 'коты': 20, 'собачки': 20, 'хлеб': 15, 'вода': 15, 'коробки': 10})

stock = {'магазин': shop,
         'склад': store}

while input_user := input('Введите запрос - '):

    if input_user.lower() in ['stop', 'exit', 'close']:
        break

    # проверка переданных аргументов в запрос
    try:
        request = Request(request=input_user, stock=stock)
    except (ValueError, IndexError):
        print("Неправильный запрос")
        continue

    # перемещение товаров со склада на склад
    try:
        request.from_market.remove(request.product, request.amount)
        request.to_market.add(request.product, request.amount)
        print(f'Курьер забрал {request.amount} {request.product} со {request.from_name}')
        print(f'Курьер везет {request.amount} {request.product} со {request.from_name} в {request.to_name}')
        print(f'Курьер доставил {request.amount} {request.product} в {request.to_name}')
    except ExceptionNotEnough:
        print(f"Не хватает в {request.from_name}, попробуйте заказать меньше")
        continue
    except ExceptionValueItem:
        request.from_market.add(request.product, request.amount)
        print(f"В {request.to_name} недостаточно места, попробуйте что то другое")
        continue
    except ExceptionUnique:
        request.from_market.add(request.product, request.amount)
        print(f"В {request.to_name} может быть не больше пяти разновидностей товаров")
        continue

    # вывод остатка на складах
    print('-' * 100)

    print(f'В {request.from_name} хранится:')
    for key, item in request.from_market.get_items.items():
        print(f"{key} - {item}")

    print('-' * 100)

    print(f'В {request.to_name} хранится:')
    for key, item in request.to_market.get_items.items():
        print(f"{key} - {item}")

    print('-' * 100)
