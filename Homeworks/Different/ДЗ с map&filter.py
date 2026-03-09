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
        print(f"Your new list: {list(filter(lambda x: x[::-1].lower() == x.lower(), string_list))}")


    elif user_choice == "5":
        from functools import reduce

        rooms = []
        while not rooms:
            print("Enter the room details. To finish, just press Enter ➤ ")

            while True:
                name = input("Enter room name: ").strip()
                if name == "":
                    break
                try:
                    length_str = input("Enter a length room (m): ").strip()
                    width_str = input("Enter a width room (m): ").strip()

                    bad_length = (length_str.startswith('0') and len(length_str) > 1 and length_str[1] != '.') or \
                                 (length_str.startswith('-0') and len(length_str) > 2 and length_str[2] != '.')

                    bad_width = (width_str.startswith('0') and len(width_str) > 1 and width_str[1] != '.') or \
                                (width_str.startswith('-0') and len(width_str) > 2 and width_str[2] != '.')

                    if bad_length or bad_width:
                        print("Error: Number cannot start with zero (unless it's 0.something)!")
                        continue

                    length = float(length_str)
                    width = float(width_str)

                    if length <= 0 or width <= 0:
                        print("Error: Dimensions must be positive!")
                        continue
                    rooms.append({"name": name, "length": length, "width": width})
                    print(f"Added room: {name}")
                except ValueError:
                    print("Error: Please enter a valid float number!")
            if not rooms:
                print("Error: list rooms cannot be empty!")

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















    # elif user_choice == "0":
    #     print("Goodbye!")
    #     is_continue = False











