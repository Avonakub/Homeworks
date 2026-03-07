def show_menu():
    print("1 - From number to string\n"
          "2 - Elements greater than 0\n"
          "3 - List of palindromes\n"
          "4 - Greatest common divisor\n"
          "5 - Decorator\n"
          "6 - Apartment area\n"
          "7 - IBM with Try Except\n"
          "8 - Calculate with Try Except\n"
          "9 - Pixelation\n"
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

    if user_choice == "2":
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

    if user_choice == "3":

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







