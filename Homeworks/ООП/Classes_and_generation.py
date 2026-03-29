class Goods:
    def __init__(self, product_name, name_store, price):
        self.__product_name = product_name
        self.__name_store = name_store
        self.price = price


    @property
    def product_name(self):
        return self.__product_name


    @property
    def name_store(self):
        return self.__name_store


    @property
    def price(self):
        return f"{self.__price} BYN"


    @name_store.setter
    def name_store(self, name_store):
        if not name_store or name_store.strip() == "":
            raise TypeError("❌ Название магазина не может быть пустым!")
        self.__name_store = name_store


    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)):
            raise TypeError("❌ Цена должна быть числом!")
        if new_price <= 0:
            raise ValueError("Цена не может быть отрицательной или отсутствовать")
        self.__price = new_price


    def __add__(self, other):
        return self.__price + other.__price


    def __str__(self):
        return f"Название: {self.product_name}\nМагазин: {self.name_store}\nЦена: {self.__price} BYN"


class Warehouse:
    def __init__(self):
        self.__items = []


    def add_product(self, product):
        self.__items.append(product)


    def output_by_index(self, product_index):
        if product_index < 0 or product_index >= len(self.__items):
            raise ValueError(f"❌ Такого индекса нет. Введите корректный индекс. Количество индексов "
                             f"до {len(self.__items) - 1} включительно")
        product = self.__items[product_index]
        return f"Название: {product.product_name}\nМагазин: {product.name_store}\nЦена {product.price}"


    def output_by_name(self, name):
        for product in self.__items:
            if product.product_name.lower() == name.lower():
                return f"Название: {product.product_name}\nМагазин: {product.name_store}\nЦена {product.price}"
        raise ValueError("Товар не найден")


    def sort_by_name(self):
        self.__items.sort(key=lambda x: x.product_name)


    def sort_by_store(self):
        self.__items.sort(key=lambda x: x.name_store)


    def sort_by_price(self):
        self.__items.sort(key=lambda x: x.price)


    def get_all_items(self):
        return self.__items


class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part


    def fly(self):
        return self.bee_part >= self.elephant_part


    def trumpet(self):
        if self.elephant_part >= self.bee_part:
            return "ту-ту-ду-ду"
        return "взззз"


    def eat(self, meal, value ):
        if meal == "нектар":
            self.elephant_part -= value
            self.bee_part += value
        elif meal == "трава":
            self.bee_part -= value
            self.elephant_part += value
        else:
            raise ValueError("Кормить нужно только нектаром или травой")
        self.bee_part = max(0, min(100, self.bee_part))
        self.elephant_part = max(0, min(100, self.elephant_part))


    def __str__(self):
        return f"ПчёлоСлон с параметрами Пчела: {self.bee_part} / Слон: {self.elephant_part}"


def show_menu():
    print("1 - Товары на складе\n"
          "2 - ПчёлоСлон\n"
          "3 - Посадка/высадка в автобусе\n"
          "4 - Генератор. Спецификатор\n"
          "5 - Генератор. Пачки повторов\n"
          "0 - Выход")
    print("➤➤➤")


def show_menu_goods():
    print("=" * 40 + "\n"
          "1 - Показать все товары\n"
          "2 - Найти товар по индексу\n"
          "3 - Найти товар по названию\n"
          "4 - Сортировать по названию\n"
          "5 - Сортировать по магазину\n"
          "6 - Сортировать по цене\n"
          "7 - Добавить новый товар\n"
          "8 - Сложение товаров по цене\n"
          "0 - Выход")
    print("➤➤➤")


def create_default_warehouse():
    warehouse = Warehouse()
    warehouse.add_product(Goods("Iphone", "i-Store.by", 3000))
    warehouse.add_product(Goods("MacBook", "i-Store.by", 6200))
    warehouse.add_product(Goods("Холодильник", "5 Элемент", 2900))
    warehouse.add_product(Goods("Телевизор", "5 Элемент", 1600))
    return warehouse


def show_menu_bee_elephant():
    print("=" * 40 + "\n"
          "Нажмите:\n"
          "1 - Чтобы узнать не меньше ли часть пчелы части слона\n"
          "2 - Проверка звука в зависимости от соотношения частей\n"
          "3 - Можно покормить пчелу словом nectar или слона словом grass\n"
          "0 - Выход")
    print("➤➤➤")


is_continue = True
while is_continue:
    show_menu()  # Вызвали функцию показа общего меню
    user_choice = input("Введите свой выбор здесь ➤ : ")

    if user_choice == "1":
        warehouse = create_default_warehouse()
        while True:
            show_menu_goods() # Функция показа меню товаров
            user_choice = input("Введите свой выбор здесь ➤ : ")

            if user_choice == "1":
                print("Все товары на складе:")
                for i, product in enumerate(warehouse.get_all_items()):
                    print(f"{i}. {product}")
                    print()

            elif user_choice == "2":
                while True:
                    try:
                        index = int(input("Введите индекс товара: "))
                        print(warehouse.output_by_index(index))
                        break
                    except ValueError as e:
                        if "invalid literal" in str(e):
                            print("❌ Ошибка: нужно ввести число!")
                        else:
                            print(f"❌ Ошибка: {e}")

            elif user_choice == "3":
                name = input("Введите название товара: ").strip()
                try:
                    print(warehouse.output_by_name(name))
                except ValueError as e:
                    print(f"❌ Ошибка: {e}")

            elif user_choice == "4":
                warehouse.sort_by_name()
                print("Сортировка по названию выполнена!")
                print("\nОтсортированные товары:")
                for i, product in enumerate(warehouse.get_all_items()):
                    print(f"{i}. {product}")
                    print()

            elif user_choice == "5":
                warehouse.sort_by_store()
                print("Сортировка по магазину выполнена!")
                print("\nОтсортированные товары:")
                for i, product in enumerate(warehouse.get_all_items()):
                    print(f"{i}. {product}")
                    print()

            elif user_choice == "6":
                warehouse.sort_by_price()
                print("Сортировка по цене выполнена!")
                print("\nОтсортированные товары:")
                for i, product in enumerate(warehouse.get_all_items()):
                    print(f"{i}. {product}")
                    print()

            elif user_choice == "7":
                print("Добавление новых товаров. Для выхода оставьте строку с названием пустой")
                while True:
                    name = input("Введите название товара (или Enter для выхода): ")
                    if name == "":
                        print("↩️ Возврат в главное меню!")
                        break

                    while True:
                        store = input("Введите название магазина: ").strip()
                        try:
                            new_goods = Goods(name, "временный", 1)
                            new_goods.name_store = store
                            break
                        except TypeError as e:
                            print(f"{e}")
                            print("Попробуйте снова.")

                    while True:
                        try:
                            price = input("Введите цену товара: ")
                            if price == "":
                                print("❌ Ошибка: цена не может быть пустой!")
                                continue
                            price = float(price)
                            new_goods = Goods(name, store, price)
                            print(f"✅ Товар '{name}' успешно добавлен!")
                            break
                        except ValueError as e:
                            if "could not convert" in str(e):
                                print("❌ Ошибка: нужно ввести число, а не буквы!")
                            else:
                                print(f"❌ Ошибка: {e}")
                        except TypeError as e:
                            print(f"❌ Ошибка: {e}")

            elif user_choice == "8":
                print("Сложение цен двух товаров")
                items = warehouse.get_all_items()
                print("Доступные товары:")
                for i, product in enumerate(items):
                    print(f"{i}. {product.product_name} — {product.price}")
                    print()

                while True:
                    try:
                        index1 = int(input("Введите индекс первого товара: "))
                        if 0 <= index1 < len(items):
                            product1 = items[index1]
                        else:
                            print(f"❌ Ошибка: индекс должен быть от 0 до {len(items) - 1}")
                            continue
                        index2 = int(input("Введите индекс второго товара: "))
                        if 0 <= index2 < len(items):
                            product2 = items[index2]
                        else:
                            print(f"❌ Ошибка: индекс должен быть от 0 до {len(items) - 1}")
                            continue
                        total = product1 + product2
                        print(f"💰 Общая цена '{product1.product_name}' и '{product2.product_name}': {total} BYN")
                        break
                    except IndexError:
                        print("❌ Ошибка: неверный индекс товара!")
                    except ValueError:
                        print("❌ Ошибка: нужно ввести число!")
                    except TypeError as e:
                        print(f"Ошибка: {e}")

            elif user_choice == "0":
                print("↩️ Возврат в главное меню!")
                break
            else:
                print("❌ Неверный выбор! Попробуйте снова.")

    elif user_choice == "2":

        print("Создание ПчёлоСлона..")
        print("❗После ввода значения для пчелы, для слона рассчет будет произведен автоматически (100 - значение пчелы)")
        print("=" * 105)
        while True:
            try:
                bee_part = input("Введите значение для пчелы от 1 до 99: ")
                if bee_part == "":
                    print("❌ Ошибка: значение не может быть пустым!")
                    print("Попробуйте снова.")
                    continue
                bee_part = int(bee_part)
                if bee_part <= 0 or bee_part > 99:
                    print("❌ Значение не может быть отрицательным, больше 99 или равным нулю!")
                    continue
                print(f"✅ Значение пчелы: {bee_part} принято.")
                break
            except ValueError:
                print("❌ Ошибка: значение должно быть целым числом!")
                print("Попробуйте снова.")

        max_elephant = 100 - bee_part
        elephant_part = max_elephant
        print(f"Параметр слона: {max_elephant}")
        print("🟢 ПчёлоСлон создан")
        bee_elephant = BeeElephant(bee_part, elephant_part)
        print(bee_elephant)

        while True:
            show_menu_bee_elephant()
            user_choice = input("Введите свой выбор здесь ➤ : ")

            if user_choice == "1":
                print(bee_elephant.fly())

            elif user_choice == "2":
                print(bee_elephant.trumpet())

            elif user_choice == "3":

                print("Вам нужно ввести число от 1 до 10. Это шаг, который будет вычитаться\n"
                      "от части слона или пчелы в зависимости от того, чем вы покормите ПчёлоСлона;)")

                while True:
                    value_input = input("Введите значение от 1 до 10 (или Enter для выхода): ")
                    if value_input == "":
                        print("↩️ Возврат в главное меню!")
                        break
                    try:
                        value_input = int(value_input)
                        if 1 <= value_input <= 10:
                            while True:
                                meal_input = input("Введите еду для ПчёлоСлона (нектар или трава): ").strip()
                                if meal_input == "нектар":
                                    if value_input > bee_elephant.elephant_part:
                                        print("❌ Значение слона не может стать меньше 0!")
                                    else:
                                        bee_elephant.eat("нектар", value_input)
                                        print(
                                            f"✅ Покормили нектаром. Пчела: {bee_elephant.bee_part} / Слон: {bee_elephant.elephant_part}")
                                        break
                                elif meal_input == "трава":
                                    if value_input > bee_elephant.bee_part:
                                        print("❌ Значение пчелы не может стать меньше 0!")
                                    else:
                                        bee_elephant.eat("трава", value_input)
                                        print(
                                            f"✅ Покормили травой. Пчела: {bee_elephant.bee_part} / Слон: {bee_elephant.elephant_part}")
                                        break
                                else:
                                    print("❌ Некорректная еда. Введите только нектар или трава")
                        else:
                            print("❌ Ошибка: число должно быть от 1 до 10!")
                    except ValueError:
                        print("❌ Ошибка: введите целое число!")

            elif user_choice == "0":
                print("↩️ Возврат в главное меню!")
                break
            else:
                print("❌ Неверный выбор! Попробуйте снова.")








    elif user_choice == "0":
        print("👋 Пока!")
        is_continue = False








