def show_menu():
    print("1 - From number to string\n"
          "2 - Elements greater than 0\n"
          "3 - List of palindromes\n"
          "4 - Decorator\n"
          "5 - Apartment area\n"
          "6 - IBM with Try Except\n"
          "7 - Calculate with Try Except\n"
          "8 - Pixelation\n"
          "0 - Exit")
    print("➤➤➤")


from PIL import Image

def pixelate_image(image_path, output_path, block_size):
    image = Image.open(image_path).convert("RGB")
    pixels = image.load()  # загрузит пиксели (это матрицы)
    width, height = image.size  # взять от картинки размер длина и ширина

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            # Определяем границы текущего блока
            block_x_end = min(x + block_size, width)
            block_y_end = min(y + block_size, height)

            # Собираем все пиксели в блоке
            block_pixels = []
            for block_y in range(y, block_y_end):
                for block_x in range(x, block_x_end):
                    block_pixels.append(pixels[block_x, block_y])

            # Вычисляем средний цвет для блока
            if block_pixels:
                avg_color = tuple(
                    int(sum(c[i] for c in block_pixels) / len(block_pixels))
                    for i in range(3)
                )

                # Закрашиваем весь блок средним цветом
                for block_y in range(y, block_y_end):
                    for block_x in range(x, block_x_end):
                        pixels[block_x, block_y] = avg_color

    image.save(output_path)

import time


def repeat_and_measure(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0

            print("\n" + "=" * 40)
            for i in range(times):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                exec_time = end - start
                total_time += exec_time

                if i < times - 1:
                    print("-" * 40)

            avg_time = total_time / times
            print(f"\nAverage time: {avg_time:.4f} seconds")
            print("=" * 40)

        return wrapper

    return decorator


def hello(name):
    text = f"Hello, {name}"
    border = "*" * (len(text) + 4)
    print(border)
    print(f"* {text} *")
    print(border)
    time.sleep(0.1)


is_continue = True
while is_continue:
    show_menu()  # Вызвали функцию
    user_choice = input("Enter your choice HERE ➤ : ")

    if user_choice == "1":
        number_list = []

        while not number_list:
            user_input = "start"
            print("Enter the numbers one at a time. To finish, just press Enter ➤ ")

            while True:
                user_input = input("Enter a number: ")
                if user_input == "":
                    break
                try:
                    number = int(user_input)
                    number_list.append(number)
                except ValueError:
                    print("Error: Please enter a valid number!")
            if not number_list:
                print("Error: Number list cannot be empty!")

        print(f"Your old list: {number_list}")
        print(f"Your new list: {list(map(str, number_list))}")

    elif user_choice == "2":
        number_list = []

        while not number_list:
            user_input = "start"
            print("Enter the numbers one at a time. To finish, just press Enter ➤ ")

            while True:
                user_input = input("Enter a number: ")
                if user_input == "":
                    break
                try:
                    number = int(user_input)
                    number_list.append(number)
                except ValueError:
                    print("Error: Please enter a valid number!")
            if not number_list:
                print("Error: Number list cannot be empty!")

        print(f"Your old list: {number_list}")
        print(f"Your new list: {list(filter(lambda x: x > 0, number_list))}")

    elif user_choice == "3":

        string_list = []

        while not string_list:
            user_input = "start"
            print("Enter the words or phrases one at a time longer than 3 characters. To finish, just press Enter ➤ ")

            while True:
                user_input = input("Enter a string: ").strip()
                if user_input == "":
                    break
                try:
                    if len(user_input) < 3:
                        print("Error: String cannot be shorter than 3 characters!")
                    else:
                        string_list.append(user_input)
                except ValueError:
                    print("Error: Please enter a valid string!")
            if not string_list:
                print("Error: list cannot be empty!")

        print(f"Your old list: {string_list}")
        print(f"Your new list: {list(filter(lambda x: x.replace(' ', '').lower() == x.replace(' ', '').lower()[::-1], 
                                            string_list))}")

    elif user_choice == "4":
        print("\n=== DECORATOR'S DEMONSTRATION ===")

        while True:
                name = input("Enter your name: ")
                if name == "":
                    print("Error: Name cannot be empty!")
                    continue
                break
        while True:
            try:
                times_str = input("How much repeat? ")
                if times_str == "":
                    print("Error: Number of repetitions cannot be empty!")
                    continue
                times = int(times_str)

                if times <= 1:
                    print("Error: Number of repetitions must be greater than 1!")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid number!")

        decorated_hello = repeat_and_measure(times)(hello)
        decorated_hello(name)

    elif user_choice == "5":
        from functools import reduce

        rooms = []
        print("Enter the room details. To finish, just press Enter ➤")
        while True:
            name = input("Enter room name: ").strip()
            if name == "":
                if not rooms:  # Если не ввели ни одной комнаты
                    print("Error: You must enter at least one room!")
                    continue
                else:
                    break  # Выходим из цикла ввода комнат
            while True:
                try:
                    length_str = input("Enter a length room (m): ").strip()

                    if length_str.startswith('0') and len(length_str) > 1 and length_str[1] != '.'\
                        or length_str.startswith('-0') and len(length_str) > 2 and length_str[2] != '.':
                        print("Error: Number cannot start with zero (unless it's 0.something)!")
                        continue

                    length = float(length_str)

                    if length <= 0:
                        print("Error: Dimensions must be positive!")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter valid value!")
                    continue
                finally:
                    print("-" * 40)

            while True:
                try:
                    width_str = input("Enter a width room (m): ").strip()

                    if width_str.startswith('0') and len(width_str) > 1 and width_str[1] != '.'\
                        or width_str.startswith('-0') and len(width_str) > 2 and width_str[2] != '.':
                        print("Error: Number cannot start with zero (unless it's 0.something)!")
                        continue

                    width = float(width_str)

                    if width <= 0:
                        print("Error: Dimensions must be positive!")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a valid float number!")
                finally:
                    print("-" * 40)

            rooms.append({"name": name, "length": length, "width": width})
            print(f"Added room: {name}")

        if rooms:
            areas = list(map(lambda r: r["length"] * r["width"], rooms))
            total_area = reduce(lambda x, y: x + y, areas)

            print("\n" + "-" * 40)
            print("ROOMS IN APARTMENT")
            print("-" * 40)
            for i, room in enumerate(rooms, 1):
                area = room['length'] * room['width']
                print(f"{i}. {room['name']}: {room['length']} m x {room['width']} m = {area} sq.m.")
            print("-" * 40)
            print(f"TOTAL AREA: {total_area} sq.m.")
            print("-" * 40)

    elif user_choice == "6":

        print("To determine your body mass index, enter your height between 0.6\n"
              "and 2.30 m and your weight between 30 and 320 kg.")

        while True:
            try:
                height_str = input("Enter your height in m: ").strip()
                if height_str.startswith('0') and len(height_str) > 1 and height_str[1] != '.'\
                        or height_str.startswith('-0') and len(height_str) > 2 and height_str[2] != '.':
                    print("Error: Value cannot start with zero (except 0.86!)")
                    continue
                height = float(height_str)
                if height < 0.6 or height > 2.3:
                    print("Error: Height must be between 0.6 and 2.3 meters!")
                    continue
                break
            except ValueError:
                print("Error: Please enter valid value!")
                continue
            finally:
                print("-" * 40)

        while True:
            try:
                weight_str = input("Enter your weight in kg: ").strip()

                weight = float(weight_str)
                if weight < 30 or weight > 320:
                    print("Error: Weight must be between 30 and 320 kilograms!")
                    continue

                bmi = weight / (height * height)

                print(f"Your height: {height} m. Your weight: {weight} kg.")

                if bmi < 16:
                    print(f"Your body mass index is {bmi:.2f}. Critical value!!!")
                elif 16 <= bmi < 18.5:
                    print(f"Your body mass index: {bmi:.2f}. Short.")
                elif 18.5 <= bmi <= 24.99:
                    print(f"Your body mass index is {bmi:.2f}. Normal value.")
                elif 25 <= bmi <= 29.99:
                    print(f"Your body mass index is {bmi:.2f}. Overweight.")
                elif 30 <= bmi <= 34.99:
                    print(f"Your body mass index is {bmi:.2f}. Obesity grade 1.")
                elif 35 <= bmi <= 39.99:
                    print(f"Your body mass index is {bmi:.2f}. Obesity grade 2.")
                elif bmi > 39.99:
                    print(f"Your body mass index is {bmi:.2f}. Obesity grade 3.")
                break
            except ValueError:
                print("Error: Please enter valid value!")
            finally:
                print("-" * 40)

    elif user_choice == "7":

        print("A simple calculator for operations with TWO numbers")

        while True:
            try:
                first_input = input("Enter first number: ").strip()

                if first_input.startswith('0') and len(first_input) > 1 and first_input[1] != '.' \
                        or first_input.startswith('-0') and len(first_input) > 2 and first_input[2] != '.':
                    print("Error: Number cannot start with zero (except 0.86!)")
                    continue
                a = float(first_input)
                break
            except ValueError:
                print("Error: Please enter valid number!")
                continue
            finally:
                    print("-" * 40)

        while True:
            try:
                operation = input('Enter operation ("*" , "/" , "+" or "-" ): ').strip()

                if operation != '*' and operation != '/' and operation != '+' and operation != '-':
                    print('Error: Operation must be one of: "*" , "/" , "+" or "-" ')
                    continue
                break
            finally:
                print("-" * 40)

        while True:
            try:
                second_input = input("Enter second number: ").strip()

                if second_input.startswith('0') and len(second_input) > 1 and second_input[1] != '.' \
                    or second_input.startswith('-0') and len(second_input) > 2 and second_input[2] != '.':
                    print("Error: Number cannot start with zero (except 0.86!)")
                    continue
                b = float(second_input)

                if operation == "+":
                    print(f"Result: {a} + {b} = {a + b}")
                elif operation == "-":
                    print(f"Result: {a} - {b} = {a - b}")
                elif operation == "/":
                    if b == 0:
                        print("Error: division by zero")
                        continue
                    else:
                        print(f"Result: {a} / {b} = {a / b}")
                elif operation == "*":
                    print(f"Result: {a} * {b} = {a * b}")
                break
            except ValueError:
                print("Error: Please enter valid number!")
                continue
            finally:
                print("-" * 40)

    elif user_choice == "8":
        import os

        print("\nMake sure your image is in the same folder as this program!")
        # Бесконечный ввод для имени файла, пока пользователь не введет существующий файл
        while True:
            image_path = input("Enter image filename (e.g., cat.jpg): ")
            # Проверяем существует ли файл, если да выходим из цикла
            if os.path.exists(image_path):
                break
            else:
                # Если файл не найден - показываем ошибку и список доступных изображений
                print(f"\nError: file '{image_path}' not found!")
                print("\nAvailable images in current folder:")
                found_images = False
                # Проходим по всем файлам в папке и проверяем расширения
                for file in os.listdir('.'):
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                        print(f"  - {file}")  # выводим название каждого найденного изображения
                        found_images = True
                if not found_images:
                    print("  No images found!")  # Если изображений нет вообще, просим повторно ввести
                print("\nPlease try again:")

        # Бесконечный ввод для размера блока
        while True:
            try:
                block = input("Enter pixel block size (integer number): ")
                block_size = int(block)
                if block_size < 1:
                    print("Error: Block size must be greater than 0!")
                    continue
                break
            # Если пользователь ввел не число (буквы, символы)
            except ValueError:
                print("Error: Please enter a valid number!")
            finally:
                print("-" * 40)

        # Если дошли сюда - значит оба ввода корректные
        output_path = "pixelated_" + image_path  # создаем имя для выходного файла
        pixelate_image(image_path, output_path, block_size) # применяем фильтр
        print(f"Done! Result saved as {output_path}")

    elif user_choice == "0":
        print("Goodbye!")
        is_continue = False











