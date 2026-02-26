from random import randint


def generate_random_matrix(rows_count, cols_count):
    matrix = []
    for row in range(0, rows_count):
        matrix.append([])
        for col in range(0, cols_count):
            matrix[row].append(randint(0, 50))

    return matrix


def show_beautiful_matrix(matrix):
    for row in matrix:
        print(row)


def show_menu():
    print("1 - Matrix M x N\n"
          "2 - Min % max in matrix M x N\n"
          "3 - Sum of elements in matrix M x N\n"
          "4 - Multiplies of elements in matrix M x N\n"
          "5 - Sum of elements every rows in matrix M x N\n"
           "0 - Exit")
    print("➤➤➤")


def get_positive_integer(text):  # Функция проверки положительных целых чисел
    user_input = input(text)
    if user_input.isdigit():
        number = int(user_input)

        if number > 0:
            return number
        else:
            print("Please enter a number greater than 0.")
    else:
        print("Error: Please enter only numbers (letters are not allowed)!")


is_continue = True
while is_continue:
    show_menu()  # Вызвали функцию
    user_choice = input("Enter your choice HERE ➤ : ")

    if user_choice == "1":
        rows = get_positive_integer("Enter rows (M): ")
        cols = get_positive_integer("Enter columns (N): ")
        my_matrix = generate_random_matrix(rows, cols)
        print("Generated Matrix: ")
        show_beautiful_matrix(matrix=my_matrix)