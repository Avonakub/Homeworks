is_continue = True

while is_continue:
    print("1 - Buying a phone\n"  # Покупка телефона
          "2 - Fibonacci number sequence\n"  # Последовательность чисел Фибоначчи
          "3 - Sum of numbers, maximum and minimum value\n"  # Сумма чисел, максимум и минимум
          "4 - Uniqueness of numbers\n"  # Проверка на уникальность числа
          "5 - Binary search for sorted numbers in ascending order\n"  # Бинарный поиск чисел по возрастанию
          "6 - Binary search on a shifted list of numbers\n"  # Бинарный поиск чисел по сдвинутому списку
          "7 - Random matrix\n"
          "8 - Vowels and consonants letters\n"
          "9 - Prime number N\n"
          "10 - Search for perfect numbers up to and including N\n"
          "11 - Finding the number of steps to N = 1")
    print("➤➤➤")
    user_choice = input("Enter your choice HERE ➤ : ")

    if user_choice == '1':
        price_phone = input("Enter a price phone: ")
        summ = input("How much does Masha save per day? ")

        # Проверка на числа (удаляем точку, удаляем минус, если остаются числа, выводим True)
        if (price_phone.replace('.', '', 1).replace('-', '', 1).isdigit()
                and summ.replace('.', '', 1).replace('-', '', 1).isdigit()):
            price_phone, summ = float(price_phone), float(summ)

        # Проверка на отрицательные числа
            if price_phone <= 0 or summ <= 0:
                print("Error: Price and savings must be greater than zero!")  # Ошибка, если число меньше 0
            else:
                current_money = 0  # Сколько накопила
                days_passed = 0  # Счетчик дней

                while current_money < price_phone:
                    days_passed += 1  # Пока сумма накоплений меньше стоимости телефона добавляем + 1 день
                    if days_passed % 7 != 0:
                        current_money += summ  # Если это не 7 день (вскр) добавляем сумму
                print(f"Masha will save up the required amount in {days_passed} days.")
        else:  # Если в строке были буквы, isdigit выдаст фолс и сработает этот блок
            print("Error: Please enter only numbers (letters are not allowed)!")

    elif user_choice == '2':
        value = input("Enter an integer for the Fibonacci number sequence: ")
        if value.isdigit():
            value = int(value)
            if value <= 0:  # Последовательность может быть только больше 0
                print("Please enter a number greater than 0.")
            else:
                fibonacci_sequence = []  # Создаем список, чтобы хранить последовательность
                a, b = 0, 1  # Задаем переменные, а - текущее, б - следующее
                for _ in range(value):
                    fibonacci_sequence.append(a)  # Добавляем в список каждое новое значение а
                    a, b = b, a + b  # а - первое число, б - это а плюс следующее (б)
            # Преобразуем в стр, потому что склейка только со строками. Склеиваем через запятую
            print(f"Sequence show is it: {', '.join(map(str, fibonacci_sequence))}.")
        else:
            print("Error: Please enter only numbers (letters are not allowed)!")

    elif user_choice == '3':
        numbers = []  # Создаем пустой список, чтобы складывать туда числа
        user_input = "start"  # Вводим любое значение, чтобы цикл мог начаться
        print("Enter the numbers one at a time. To finish, just press Enter ➤ ")

        while user_input != "":  # Цикл работает, пока пользователь не нажмет Enter на пустой строке
            user_input = input("Enter number: ")
            # Используем try для защиты от букв и неправильных символов и заменяем проверку методам строк с ифами
            try:
                # Проверка на корявые числа типа 076, -08765. Убираем с лишними нулями и -0
                # Но разрешаем корректные дроби (0.5, -0.2) через проверку точки
                if user_input.startswith('0') and len(user_input) > 1 and user_input[1] != '.'\
                        or user_input.startswith('-0') and len(user_input) > 2 and user_input[2] != '.':
                    print("Error: Number cannot start with zero (except 0.86 or -0.86)!")
                # Если ввод прошел проверку на нули, пробуем превратить его в число
                else:
                    numbers.append(float(user_input))  # float() сам поймет и минус, и точку, и целое число
            except ValueError:
                # Проверяем, что ошибка вызвана не простым нажатием Enter для выхода
                if user_input != "":
                    print("Error: Please enter a valid number!")
        if numbers:
            total_sum = 0  # Создаем сумматор для складывания

            # Начинаем поиск мин/макс с первого элемента списка нулевой индекс
            min_val = numbers[0]
            max_val = numbers[0]
            for number in numbers:
                total_sum += number
                if number < min_val:  # Если нашли число меньше текущего минимума, то пишем его в мин
                    min_val = number

                if number > max_val:  # Если нашли число больше текущего максимума, то пишем его в макс
                    max_val = number
            print(f"Sum of number: {total_sum:.2f}. Minimum number: {min_val}. Maximum number: {max_val}. ")
        else:  # Вывод, если ни одно значение в список не попало
            print("Error: List is empty!")





    # elif user_choice == '4':
    #     is_continue = False
    # else:
    #     print("No such action!")
    #
    # print("=" * 50)