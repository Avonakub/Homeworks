def show_menu():
    print("1 - Recursive binary search algorithm\n"
          "2 - From decimal to binary number system\n"
          "3 - Prime number\n"
          "4 - Greatest common divisor\n"
          "5 - Caesar cipher\n"
          "6 - Vigenère cipher\n"
          "0 - Exit")
    print("➤➤➤")


def get_positive_integer(text, min_value=1):
    while True:
        user_input = input(text)
        try:
            number = int(user_input)
            if number >= min_value:
                return number
            else:
                print(f"Please enter a number greater than {min_value - 1}.")
        except ValueError:
            print("Error: Please enter only numbers!")


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


is_continue = True
while is_continue:
    show_menu()  # Вызвали функцию
    user_choice = input("Enter your choice HERE ➤ : ")

    if user_choice == "3":
        number = get_positive_integer("Enter a number greater than 1 to check if it's prime: ", 2)
        prime_number(number)

    elif user_choice == "4":
        num1 = get_positive_integer("Enter first number: ")
        num2 = get_positive_integer("Enter second number: ")
        result = greatest_common_divisor(num1,num2)
        print(f"The greatest common divisor of {num1} and {num2} is {result}")

    elif user_choice == "0":
        print("Goodbye!")
        is_continue = False