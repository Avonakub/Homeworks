def show_menu():
    print("1 - Recursive binary search algorithm\n"
          "2 - From decimal to binary number system\n"
          "3 - Prime number\n"
          "4 - Greatest common divisor\n"
          "5 - Caesar cipher\n"
          "6 - Vigenère cipher\n"
          "0 - Exit")
    print("➤➤➤")


def prime_number(text):
    while True:
        user_input = input(text)
        if user_input == "0":
            print("Returning to Menu")
            return
        try:
            number = int(user_input)
            if number <= 1:
                print("Please enter a number greater than 1.")
                continue

            div = 2
            while number % div != 0:
                div += 1
            if div == number:
                print(f"{number}  a prime number.")
            else:
                print(f"{number} is not a prime number.")

        except ValueError:
            print("Error: Please enter only numbers!")


is_continue = True
while is_continue:
    show_menu()  # Вызвали функцию
    user_choice = input("Enter your choice HERE ➤ : ")

    if user_choice == "3":
        num = prime_number("Enter a positive integer (or '0' to back to menu): ")

    elif user_choice == "0":
        print("Goodbye!")
        is_continue = False