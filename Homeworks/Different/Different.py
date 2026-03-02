def show_menu():
    print("1 - Recursive binary search algorithm\n"
          "2 - From decimal to binary number system\n"
          "3 - Prime number\n"
          "4 - Greatest common divisor\n"
          "5 - Caesar cipher\n"
          "6 - Vigenère cipher\n"
          "7 - Run-Length Encoding\n"
          "8 - Spam\n"
          "9 - Genetic algorithm\n"
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


def compress_string():

        if not str_s: return ""
        result = []
        count = 1

        for i in range(len(str_s) -1):
            if str_s[i] == str_s[i + 1]:
                count += 1
            else:
                result.append(str_s[i] + str(count))
                count = 1
        result.append(str_s[-1] + str(count))
        return "".join(result)


def check_for_spam(text):
    cleaned_text = ""  # Корзина с чистыми буквами
    # Берем по символу, проверяем буква это или знак.
    # Если буква кидаем в корзину, и кидаем пробел
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char

    words = cleaned_text.split()  # Разбили текст на отд. слова в корзине по пробелу
    count = 0
    spam_list = ['бесплатно', 'акция', 'бонус', 'выигрыш', 'халява', 'казино', 'легкие деньги', 'последний шанс', 'гарантия']

    for word in words:
        if len(word) >= 3 and word.isupper():
            return True
        if word.lower() in spam_list:
            count += 1
    if count > 3:
        return True
    print(f"In message is {count} spam-words")
    return False


import random  # Рандомное число
import string  # Набор готовых строк "ABCD.."


def evolve_string(target):
    chars = string.ascii_uppercase

    current = ''.join(random.choice(chars) for _ in range(len(target)))
    generation = 0

    while current != target:
        generation += 1
        new_string_list = []  # Временный список для сборки новой строки
        for i in range(len(target)):
            if current[i] == target[i]:  # Если символ совпал, сохраняем
                new_string_list.append(current[i])
            else:
                new_string_list.append(random.choice(chars))

        current = ''.join(new_string_list)  # Превращаем обратно в строку
    return generation


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

    elif user_choice == "7":
        while True:
            str_s = input("Enter a string to compress: ")
            if not str_s:
                print("Error: There is nothing to compress!")
                continue
            string_s = compress_string()
            print(f"Compressed string is: {string_s}")
            break

    elif user_choice == "8":
        message = input("Enter a message: ")
        is_spam = check_for_spam(message)

        if is_spam:
            print("Warning: This message is SPAM!")
        else:
            print("OK: This message is safe.")

    elif user_choice == "9":
        while True:
            user_input = input("Enter the word in English letters : ")
            word = "".join(c for c in user_input if c.isalpha() and c.isascii()).upper()
            if not word:
                print("Error: Please enter at least one English letter!")
                continue
            else:
                result = evolve_string(word)
                print(f"String {word} was obtained over generations: {result}")
                break


    elif user_choice == "0":
        print("Goodbye!")
        is_continue = False