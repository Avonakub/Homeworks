class Goods:
    def __init__(self, product_name, name_store, price):
        self.__product_name = product_name
        self.__name_store = name_store
        self.__price = price


    @property
    def product_name(self):
        return self.__product_name


    @property
    def name_store(self):
        return self.__name_store


    @property
    def price(self):
        return f"Цена товара: {self.__price}"

    @product_name.setter
    def product_name(self, product_name):
        if product_name is None:
            raise TypeError("Название продукта не может быть пустым")
        self.__product_name = product_name


    @name_store.setter
    def name_store(self, name_store):
        if name_store is None:
            raise TypeError("Название магазина не может быть пустым")
        self.__name_store = name_store


    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)):
            raise TypeError("Цена должна быть числом!")
        if new_price <= 0:
            raise ValueError("Цена не может быть отрицательной или отсутствовать")
        self.__price = new_price




class Warehouse:
    def __init__(self, product_name):
        self.__product_name = []
        pass







def show_menu():
    print("1 - Товары на складе\n"
          "2 - ПчёлоСлон\n"
          "3 - Посадка/высадка в автобусе\n"
          "4 - Генератор. Спецификатор\n"
          "5 - Генератор. Пачки повторов"
          "0 - Выход")
    print("➤➤➤")

