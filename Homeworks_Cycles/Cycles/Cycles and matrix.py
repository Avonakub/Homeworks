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








    #
    # elif user_choice == '2':
    #     first_value = int(input("First value:"))
    #     second_value = int(input("Second value:"))
    #     print(f"Sum is: {first_value + second_value}")
    # elif user_choice == '3':
    #     number = int(input("Enter a value: "))
    #     result = 1
    #     for i in range(2, number + 1):
    #         result *= i
    #     print(f"{number}! = {result}")
    # elif user_choice == '4':
    #     is_continue = False
    # else:
    #     print("No such action!")
    #
    # print("=" * 50)