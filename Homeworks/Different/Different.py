def show_menu():
    print("1 - Recursive binary search algorithm\n"
          "2 - From decimal to binary number system\n"
          "3 - Prime number\n"
          "4 - Greatest common divisor\n"
          "5 - Caesar cipher\n"
          "6 - Vigenère cipher\n"
          "0 - Exit")
    print("➤➤➤")


def get_validated_integer(text, min_value=None):
    while True:
        user_input = input(text)
        try:
            number = int(user_input)
            if min_value is not None and number < min_value:
                print(f"Please enter a number greater than or equal to {min_value}.")
                continue
            return number
        except ValueError:
            print("Error: Please enter only numbers!")


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return "- 1 or element not found"

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def get_validated_binary(text):
    while True:
        user_input = input(text)

        if not user_input:
            print("Error: Input cannot be empty!")
            continue

        if all(char in "01" for char in user_input):
            return user_input

        print("Error: Please enter only 0 and 1!")


def from_binary_to_decimal(binary_number):
    binary_str = str(binary_number)
    decimal_number = 0
    for digit in binary_str:
        decimal_number = decimal_number * 2 + int(digit)
    return decimal_number


def prime_number(number):
    div = 2
    while number % div != 0:
        div += 1
    if div == number:
        print(f"{number} a prime number.")
    else:
        print(f"{number} is not a prime number.")


def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def caesar_cipher(text, step):
    result = ""

    for letters in text:
        if "a" <= letters.lower() <= "z":
            start = ord("A") if letters.isupper() else ord("a")  # Если А, то один код, если а, то начальный другой

            new_pos = (ord(letters) - start + step) % 26
            result += chr(start + new_pos)
        else:
            result += letters  # Пробелы и знаки как есть
    return result


def vigenre_cipher(text, key_chipher):
    result = ""
    key_index = 0

    for letters in text:
        if "a" <= letters.lower() <= "z":
           start = ord("A") if letters.isupper() else ord("a")
           # Берем тек. букву и считаем сдвиг (код буквы минус код начала)
           current_key_letter = key_chipher[key_index % len(key_chipher)]
           step_start = ord("A") if current_key_letter.isupper() else ord("a")
           step = ord(current_key_letter) - step_start

           new_pos = (ord(letters) - start + step) % 26
           result += chr(start + new_pos)

           key_index += 1  # Перешли к след. букве ключа
        else:
             result += letters  # Пробелы и знаки как есть
    return result


is_continue = True
while is_continue:
    show_menu()  # Вызвали функцию
    user_choice = input("Enter your choice HERE ➤ : ")

    if user_choice == "1":
        number_list = []

        user_input = "start"
        print("Enter the numbers one at a time. To finish, just press Enter ➤ ")
        while user_input != "":
            user_input = input("Enter number: ")
            if user_input != "":
                try:
                    if (user_input.startswith('0') and len(user_input) > 1 and user_input[1] != '.') or \
                            (user_input.startswith('-0') and len(user_input) > 2 and user_input[2] != '.'):
                        print("Error: Number cannot start with zero!")
                    else:
                        number_list.append(float(user_input))
                except ValueError:
                    print("Error: Please enter a valid number!")

        number_list.sort()
        print(f"Sorted numbers: {number_list}")

        target = get_validated_integer("What number to find? ")
        pos = binary_search_recursive(number_list, target, 0, len(number_list) - 1)
        print(f"Found number index: {pos}")

    elif user_choice == "2":
        binary_number = get_validated_binary("Enter the binary number: ")
        decim_num = from_binary_to_decimal(binary_number)
        print(f"Number {binary_number} to decimal {decim_num}")

    elif user_choice == "3":
        number = get_validated_integer("Enter a number greater than 1 to check if it's prime: ", 2)
        prime_number(number)

    elif user_choice == "4":
        num1 = get_validated_integer("Enter first number: ")
        num2 = get_validated_integer("Enter second number: ")
        result = greatest_common_divisor(num1,num2)
        print(f"The greatest common divisor of {num1} and {num2} is {result}")

    elif user_choice == "5":
        while True:
            text_to_encrypt = input("Enter an English string for encryption or decryption: ")

            has_russian = False
            for letters in text_to_encrypt:
                if 'а' <= letters.lower() <= 'я' or letters.lower() == 'ё':
                    has_russian = True
                    break
            if has_russian:
                print("Error: Russian letters are not supported!")
            else:
                break

        print("- for encryption select a positive step\n"
              "- for decryption - a negative step")
        user_step = get_validated_integer("Enter the shift step: ")
        encrypted_text = caesar_cipher(text_to_encrypt, user_step)
        print(f"New string is: {encrypted_text}")

    elif user_choice == "6":
        while True:
            text_to_encrypt = input("Enter an English string for encryption or decryption: ")

            has_russian = False
            for letters in text_to_encrypt:
                if 'а' <= letters.lower() <= 'я' or letters.lower() == 'ё':
                    has_russian = True
                    break
            if has_russian:
                print("Error: Russian letters are not supported!")
            else:
                break
        input_key = input("Enter a keyword (letters only): ")
        encrypted_text = vigenre_cipher(text_to_encrypt, input_key)
        print(f"New string is: {encrypted_text}")

    elif user_choice == "0":
        print("Goodbye!")
        is_continue = False