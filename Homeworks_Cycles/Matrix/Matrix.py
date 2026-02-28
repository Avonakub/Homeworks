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


def find_min_max(matrix):
    minimum = matrix[0][0]
    maximum = matrix[0][0]

    min_idx = [0, 0]
    max_idx = [0, 0]
    for i in range(len(matrix)):  # Перебираем строки
        for j in range(len(matrix[i])):  # Перебираем столбцы

            current_val = matrix[i][j]  # Начальная точка индексов

            if current_val < minimum:
                minimum = current_val
                min_idx = [i, j]  # Запоминаем новые координаты

            if current_val > maximum:
                maximum = current_val
                max_idx = [i, j]  # Запоминаем новые координаты

    print(f"Min value: {minimum} at index [{min_idx[0]}][{min_idx[1]}]")
    print(f"Max value: {maximum} at index [{max_idx[0]}][{max_idx[1]}]")


def summ_elements(matrix):

    total = 0

    for row in matrix:
        for item in row:
            total += item
    print(f"Sum of elements of matrix: {total}")

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for j in range(num_cols):
        col_sum = 0
        for i in range(num_rows):
            col_sum += matrix[i][j]

        percentage = (col_sum / total) * 100
        print(f"Column {j}: sum of elements = {col_sum}, proportion of the total sum of matrix elements: "
              f"{percentage:.2f} %")


def input_K_columns(text, cols):
    while True:
        user_input = input(text)
        try:
            k = int(user_input)  # Пытаемся превратить в число
            if 0 <= k < cols:
                return k
            else:
                print(f"Error: k is out of range! Enter a number from 0 to {cols - 1}.")
        except ValueError:
            print("Error: Please enter only numbers!")


def multiply_columns_by_K(matrix, k):
    rows = len(matrix)  # Получаем количество строк матрицы
    cols = len(matrix[0])  # Количество столбцов

    if k < 0 or k >= cols:
        print("Error: k is out of range!")
        return None

    result = []  # Копия матрицы
    for row in matrix:
        result.append(list(row))

    for i in range(rows):
        k_value = matrix[i][k]
        for j in range(cols):
            result[i][j] *= k_value
    return result


def show_menu():
    print("1 - Matrix M x N\n"
          "2 - Min & max in matrix M x N\n"
          "3 - The sum of the elements of the matrix M x N and the proportion of the "
          "sum of the columns from the total sum of the matrix elements.\n"
          "4 - Multiplication of the elements of each column of the matrix M x N"
          "by the corresponding elements of the K-th column\n"
          "5 - Sum of the elements of each row of the matrix with the elements of the L-th row in matrix M x N\n"
          "6 - Finding matches in a matrix M x N\n"
          "7 - Sum of elements on the main and secondary diagonals\n"
          "8 - Transformation to even elements\n"
          "0 - Exit")
    print("➤➤➤")


def get_positive_integer(text):  # Функция проверки положительных целых чисел
    while True:  # Бесконечный цикл ввода при ошибках
        user_input = input(text)
        try:
            number = int(user_input)  # Пытаемся превратить в число
            if number > 0:
                return number
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Error: Please enter only numbers!")


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

    elif user_choice == "2":
        rows = get_positive_integer("Enter rows (M): ")
        cols = get_positive_integer("Enter columns (N): ")
        my_matrix = generate_random_matrix(rows, cols)
        print("Generated Matrix: ")
        show_beautiful_matrix(matrix=my_matrix)

        find_min_max(my_matrix)

    elif user_choice == "3":
        rows = get_positive_integer("Enter rows (M): ")
        cols = get_positive_integer("Enter columns (N): ")
        my_matrix = generate_random_matrix(rows, cols)
        print("Generated Matrix: ")
        show_beautiful_matrix(matrix=my_matrix)

        summ_elements(my_matrix)

    elif user_choice == "4":
        rows = get_positive_integer("Enter rows (M): ")
        cols = get_positive_integer("Enter columns (N): ")
        my_matrix = generate_random_matrix(rows, cols)
        print("Generated Matrix: ")
        show_beautiful_matrix(matrix=my_matrix)
        k = input_K_columns(f"Enter index of column K (0 to {cols-1}): ",cols)

        result_matrix = multiply_columns_by_K(my_matrix, k)
        if result_matrix:
            print("Result Matrix after multiplication:")
            show_beautiful_matrix(result_matrix)
