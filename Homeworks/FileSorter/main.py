import os
import re

def show_menu():
    print("1 - OS. Creating folders, rename files\n"
          "2 - Change name\n"
          "3 - Reading text. The most frequently encountered word\n"
          "4 - Replace with *****\n"
          "5 - Grade less than 3 points\n"
          "6 - Sum of digits\n"
          "7 - Caesar cipher\n"
          "8 - \n"
          "0 - Exit")
    print("➤➤➤")


def main():
    print(f"Operating system: {os.name}")
    print(f"Current directory: {os.getcwd()}")

is_continue = True
while is_continue:
    show_menu()  # Вызвали функцию
    user_choice = input("Enter your choice HERE ➤ : ")

# ============================================
# TASK 1: OS. Creating folders, rename files
# ============================================
    if user_choice == "1":
        main()
        current_files = os.listdir()
        extentions = set()

        for item in current_files:
            if item.count(".") ==1:
                item_parts = item.split(".")
                if item_parts[0] != "" and item_parts[1] != "":
                    extentions.add(item_parts[1])

        print(f"Found extensions: {extentions}")

        for ext in extentions:
            if ext != 'py':
                new_folder_name = f"{ext}s"
                new_folder_path = os.path.join(os.getcwd(), new_folder_name)
                if not os.path.exists(new_folder_name):
                    os.mkdir(new_folder_name)

                files_to_move = []  # файлы
                total_size = 0  # размер

                for file in current_files:
                    if file.count(".") == 1:
                        file_parts = file.split(".")
                        if file_parts[0] != "" and file_parts[1] != "" and file_parts[1] == ext:
                            files_to_move.append(file)  # добавили в список файлов
                            total_size += os.path.getsize(file)  # размер в байтах

                for file in files_to_move:  # если попал в список файлов перемещаем
                    replaced_file_path = os.path.join(os.getcwd(), new_folder_name, file)
                    os.replace(file, replaced_file_path)

                first_file = files_to_move[0]
                old_path = os.path.join(new_folder_path, first_file)
                new_filename = f"renamed_{first_file}"
                new_path = os.path.join(new_folder_path, new_filename)

                # переименовываем
                os.rename(old_path, new_path)
                print(f"File {first_file} renamed {new_filename}")

                if files_to_move:
                    if total_size < 1024:
                        size_str = f"{total_size} bytes"
                    elif total_size < 1024 ** 2:
                        size_str = f"{total_size / 1024:.1f} KB"
                    elif total_size < 1024 ** 3:
                        size_str = f"{total_size / 1024 ** 2:.1f} MB"
                    else:
                        size_str = f"{total_size / 1024 ** 3:.1f} GB"

                    print(f"In the folder with {ext} files, {len(files_to_move)} files were moved, their total size - {size_str}")


        if os.path.exists('old_name.txt'):
            os.rename('old_name.txt', 'new_name.txt')
            print(f"Renamed old name to new_name.txt")
    print('-' * 50)

# ============================================
# TASK 2: Name change
# ============================================
    if user_choice == "2":

        filename = 'name_change.txt'
        if not os.path.exists(filename):
            print(f"File {filename} not found. Creating a test file...")  # если не найден, создаем файл
            test_text = (
                "Подсудимая Эверт-Колокольцева Елизавета Александровна\n"
                "в судебном заседании вину инкриминируемого правонарушения\n"
                "признала в полном объёме и суду показала, что\n"
                "14 сентября 1876 года, будучи в состоянии алкогольного опьянения\n"
                "от безысходности, в связи с состоянием здоровья позвонила\n"
                "со своего стационарного телефона в полицию, сообщив о том,\n"
                "что у неё в квартире якобы заложена бомба. После чего приехали\n"
                "сотрудники полиции, скорая и пожарные, которым она сообщила,\n"
                "что бомба — это она."
            )
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(test_text) # записали файл с нужным текстом
            print(f"✅ File {filename} created!")

        pattern = r"(?<=Подсудимая\s)[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?(?:\s[А-ЯЁ][а-яё]+){2}"  # регулярка для ФИО

        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.read()  # открываем и читаем созданный файл

        print(f"\nContent {filename}:")
        print("-" * 50)
        print(file_content)  # выводим содержимое файла
        print("-" * 50)

        if "Подсудимая N" in file_content:
            print(f"\n⚠️ File {filename} already contains replacements!")  # если в файле есть изменения
        else:
            target_content = re.sub(pattern, 'N', file_content)  # заменяем ФИО на N
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(target_content)  # записываем обратно

            print(f"✅ Replacement completed! File {filename} has been updated.")
            print("New content:")
            print(target_content)

# ==========================================================
# TASK 3: Reading text. The most frequently encountered word
# ==========================================================
    if user_choice == "3":
        filename = 'text.txt'
        lines = []
        while not lines:
            print("Enter lines in which there are at least 3 words one at a time. To finish, just press Enter ➤ ")
            while True:
                user_input = input("Enter line: ").strip()
                if user_input == "":
                    if len(lines) == 0:
                        print("❌ You must enter at least one line!")
                        continue
                    else:
                        break
                # находим все слова (последовательности букв) вместо сплита
                words = re.findall(r'[а-яА-ЯёЁa-zA-Z]+', user_input)
                if len(words) < 3:
                    print(f"❌ Line must contain at least 3 words! You entered {len(words)} word(s).")
                    continue
                lines.append(user_input)
                print(f"✅ Line accepted ({len(words)} words)")
            test_text = '\n'.join(lines)
            if not lines:
                print("Error: Text list cannot be empty!")

            with open(filename, 'w', encoding='utf-8') as file:
                file.write(test_text)  # записали файл с нужным текстом
            print(f"✅ File {filename} created!")

            with open(filename, 'r', encoding='utf-8') as file:
                results = []  # список результатов
                for line in file:
                    line = line.strip()
                    # находим все слова
                    words = re.findall(r'[а-яА-ЯёЁa-zA-Z]+', line.lower())

                    if words:
                        word_count = {}  # создаем словарь для слов
                        for word in words:
                            if word in word_count:
                                word_count[word] = word_count[word] + 1
                            else:
                                word_count[word] = 1

                        max_word = ""
                        max_count = 0

                        for word in word_count:  # слово должно встречаться больше 1 раза
                            if word_count[word] > 1 and word_count[word] > max_count:
                                max_count = word_count[word]
                                max_word = word

                        # проверяем, нашли ли слово с повторением
                        if max_count > 1:
                            results.append(f"{max_word}:{max_count}")
                            print(f"'{max_word}' - {max_count} times")
                        else:
                            results.append("no repeats:0")
                            print("No words repeated more than once")
                    else:
                        results.append("no words:0")
                        print("No words")

            # сохраняем в файл
            with open('freq.txt', 'w', encoding='utf-8') as file:
                for r in results:
                    file.write(r + '\n')

            print("\n✅ The results are saved in 'freq.txt'")
# ==========================================================
# TASK 4: Replace with *******
# ==========================================================
    if user_choice == "4":

        print("\nMake sure your file is in the same folder as this program!")
        print(f"Current directory: {os.getcwd()}")

        stop_words = None
        while stop_words is None:
            if os.path.exists('stop_words.txt'):
                with open('stop_words.txt', 'r', encoding='utf-8') as file:
                    raw_content = file.read().replace(',', ' ').split()
                    temp_words = [word.strip() for word in raw_content if word.strip()]
                if not temp_words:
                    print("\n⚠️ The file 'stop_words.txt' is EMPTY!")
                    print("Please add some forbidden words to it and save.")
                    user_input = input("Press Enter to try again or type 'q' to exit: ").strip().lower()
                    if user_input == 'q':
                        break
                    continue  # пробуем прочитать файл снова после паузы
                stop_words = temp_words
                print(f"✅ Stop-words loaded: {stop_words}")
            else:
                print("\n❌ File stop_words.txt not found!")
                print("Please create a file stop_words.txt in the current folder and add stop"
                      "words to it, separated by commas.")
                user_input = input("Press Enter to try again or type 'q' to exit: ").strip().lower()

                if user_input == 'q':
                    print("Exiting to main menu...")
                    break
        if stop_words is None:
            continue

        while True:
            filename = input("Enter the file name to be censored with extensions .txt (e.g., data.txt): ").strip()
            if os.path.exists(filename):
                print("✅ File found!")
                with open(filename, 'r', encoding='utf-8') as file:
                    file_content = file.read()  # открываем и читаем файл

                    print(f"\nOriginal text in {filename}:")
                    print("-" * 50)
                    print(file_content)  # выводим содержимое файла
                    print("-" * 50)
                    # очистка стоп-слов от мусора и пустых строк, стрип очистит, ловер приведет к одному регистру
                    stop_words_clean = [word.strip(' ,').lower() for word in stop_words if word.strip(' ,')]
                    # регулярное выражение для всех стоп-слов и внутри слов
                    pattern = '(' + '|'.join(map(re.escape, stop_words_clean)) + ')'


                    # функция для замены на звездочки той же длины
                    def replace_with_stars(match):
                        return '*' * len(match.group())


                    # применяем замену ко всему тексту
                    censored_text = re.sub(pattern, replace_with_stars,
                                           file_content, flags=re.IGNORECASE)
                    # собираем текст обратно
                    print(f"\nText after censorship:")
                    print("-" * 50)
                    print(censored_text)
                    print("-" * 50)

                    with open('censorship.txt', 'w', encoding='utf-8') as file:
                        file.write(censored_text)
                    print("✅ The result is saved in 'censorship.txt'")
                break
            else:
                print("❌ File not found! Please enter a valid file name to verify!")
                print("\nAvailable files in current folder:")
                found_files = False

                for file in os.listdir('.'):
                    if file.lower().endswith('.txt') and file not in ['stop_words.txt', 'censorship.txt']:
                        print(f"  - {file}")  # выводим название каждого найденного файла
                        found_files = True
                if not found_files:
                    print("\nPlease try again:")

# ==========================================================
# TASK 5: Grade less than 3 points
# ==========================================================
    if user_choice == "5":

        print("\nMake sure your file with grades is in the same folder as this program!")
        print(f"Current directory: {os.getcwd()}")

        grades_data = None  # переменная для хранения оценок
        while grades_data is None:  # бесконечный цикл пока не загрузится файл или не выйдут из цикла
            # имя файла и убираем пробелы
            filename = input("Enter the file name with grades (e.g., class_7a.txt) or 'q' to exit: ").strip()
            if filename.lower() == 'q':
                print("Returning to main menu...")
                break
            if os.path.exists(filename):  # проверяем есть ли файл
                with open(filename, 'r', encoding='utf-8') as file:
                    # читаем весь файл, заменяем запятые на пробелы и разбиваем на слова
                    raw_content = file.read().replace(',', ' ').split()
                    # оставляем только непустые слова и убираем лишние пробелы
                    temp_grades = [word.strip() for word in raw_content if word.strip()]

                    # проверка каждой строки
                    with open(filename, 'r', encoding='utf-8') as check_file:
                        lines = check_file.readlines()
                        valid = True  # флаг, что файл корректный
                        # перебираем все строки с номерами (начиная с 1)
                        for line_num, line in enumerate(lines, 1):
                            parts = line.strip().split()  # разбиваем строку на слова
                            if not parts:
                                continue
                            if len(parts) < 3: # проверяем, что есть фамилия, имя и оценка, иначе ошибка
                                print(f"\n⚠️ Error in line {line_num}: missing data (need surname, name, grade)")
                                valid = False
                                break
                            try:
                                int(parts[-1])  # последнее слово число, если не получилось, то ошибка
                            except ValueError:
                                print(f"\n⚠️ Error in line {line_num}: grade must be a number")
                                valid = False
                                break

                    if not valid:
                        input("Fix the file and press Enter to try again...")
                        continue  # предлагаем исправить файл и попробовать снова

                if not temp_grades: # проверяем, не пустой ли файл
                    print(f"\n⚠️ The file '{filename}' is EMPTY!")
                    user_input = input("Press Enter to try again or type 'q' to exit: ").strip().lower()
                    if user_input == 'q':
                        break
                    continue
                # проверяем, есть ли в файле цифры (оценки), если нет, ошибка
                has_digits = any(word.isdigit() for word in temp_grades)
                if not has_digits:
                    print(f"\n⚠️ The file '{filename}' contains text, but NO GRADES (numbers) found!")
                    user_input = input("Fix the file and press Enter to try again (or 'q' to exit): ").strip().lower()
                    if user_input == 'q':
                        break
                    continue
                grades_data = temp_grades  # если все ок, сохраняем данные и пишем, что сохранено
                print(f"✅ Grades loaded successfully!")

                # поиск оценок ниже 3
                with open(filename, 'r', encoding='utf-8') as file:
                    print("\nStudents with a grade below 3:")
                    print("-" * 50)
                    found = False  # флаг были ли найдены ученики
                    for line in file:
                        parts = line.split()
                        if len(parts) < 3:
                            continue
                        if not parts:
                            continue
                        try:
                            surname = parts[0]  # фамилия
                            name = parts[1]  # имя
                            grade = int(parts[-1])  # оценка
                            if grade < 3:  # если меньше 3, выводим данные ученика
                                print(f"{surname} {name}: {grade}")
                                found = True  # если нашли меняем флаг
                        except ValueError:
                            continue
                    if not found:  # если не нашли выводим
                        print("No students with grades below 3 found!")
                    print("-" * 50)
            else:
                print(f"\n❌ File '{filename}' not found!")  # выводим, если файл не найден
                print("Please add the student's last name, first name, and grade line by line.")
                user_input = input("Press Enter to try again or type 'q' to exit: ").strip().lower()
                if user_input == 'q':
                    print("Exiting to main menu...")
                    break
        if grades_data is None:  # если вышли из цикла через q возврат в меню
            continue

# ==========================================================
# TASK 6: Sum of digits
# ==========================================================
    if user_choice == "6":

        print("\nMake sure your file is in the same folder as this program!")
        print(f"Current directory: {os.getcwd()}")

        numbers = None
        while numbers is None:
            filename = input("Enter the file name with numbers or 'q' to exit: ").strip()
            if filename.lower() == 'q':
                print("Returning to main menu...")
                break
            if os.path.exists(filename):  # проверяем есть ли файл
                with open(filename, 'r', encoding='utf-8') as file:
                    file_content = file.read()

                    if not file_content.strip():  # проверяем, не пустой ли файл
                        print(f"\n⚠️ The file '{filename}' is EMPTY!")
                        user_input = input("Press Enter to try again or type 'q' to exit: ").strip().lower()
                        if user_input == 'q':
                            break
                        continue
                    # регулярка для поиска чисел в тексте
                    numbers_found = re.findall(r'\d+', file_content)

                    if not numbers_found:  # если чисел не найдено
                        print(f"\n⚠️ No numbers found in the file!")
                        user_input = input("Press Enter to try again or type 'q' to exit: ").strip().lower()
                        if user_input == 'q':
                            break
                        continue

                    # преобразуем строки в числа и суммируем
                    total_sum = 0
                    for num_str in numbers_found:
                        total_sum += int(num_str)
                    print(f"\nNumbers found: {numbers_found}")
                    print(f"Sum of all numbers: {total_sum}")
                    numbers = total_sum  # если все ок сохраняем
                    print(f"✅ File processed successfully!")

            else:
                print(f"\n❌ File '{filename}' not found!")
                print("Please add numbers to the file.")
                user_input = input("Press Enter to try again or type 'q' to exit: ").strip().lower()
                if user_input == 'q':
                    print("Exiting to main menu...")
                    break
        if numbers is None:
            continue

# ==========================================================
# TASK 7: Caesar cipher
# ==========================================================
    if user_choice == "7":

        print("\nMake sure your file is in the same folder as this program!")
        print(f"Current directory: {os.getcwd()}")

        cipher = None
        while cipher is None:
            filename = input("Enter the file name with an English strings for encryption or 'q' to exit: ").strip()
            if filename.lower() == 'q':
                print("Returning to main menu...")
                break
            if os.path.exists(filename):  # проверяем есть ли файл
                with open(filename, 'r', encoding='utf-8') as file:
                    lines = file.readlines()  # читаем файл построчно

                    # проверяем, не пустой ли файл
                    if not lines or not ''.join(lines).strip():
                        print(f"\n⚠️ The file '{filename}' is EMPTY!")
                        user_input = input("Press Enter to try again or type 'q' to exit: ").strip().lower()
                        if user_input == 'q':
                            break
                        continue
                    # проверяем наличие русских букв
                    has_russian = False
                    for char in lines:
                        if 'а' <= char.lower() <= 'я' or char.lower() == 'ё':
                            has_russian = True
                            break
                        if has_russian:
                            break
                    if has_russian:
                        print(f"\n⚠️ The file '{filename}' contains text with russian letters!")
                        user_input = input("Fix the file and press Enter to try again (or 'q' to exit): ").strip().lower()
                        if user_input == 'q':
                            break
                        continue

                    encrypted_lines = []
                    for line_num, line in enumerate(lines, 1):  # line_num начинается с 1
                        shift = line_num  # шаг = номер строки
                        encrypted_line = ""

                        for char in line:
                            if "a" <= char.lower() <= "z": # строчные буквы
                                start = ord("A") if char.isupper() else ord("a")
                                # (позиция буквы + шаг) % 26 + позиция 'a'
                                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                                encrypted_line += new_char
                            elif 'A' <= char <= 'Z':  # заглавные буквы
                                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                                encrypted_line += new_char
                            else:
                                encrypted_line += char  # не буквы оставляем без изменений
                        encrypted_lines.append(encrypted_line)
                        print(f"Line {line_num} (shift {shift}): {encrypted_line.strip()}")

                    encrypted_filename = f"encrypted_{filename}"
                    with open(encrypted_filename, 'w', encoding='utf-8') as out_file:
                        out_file.writelines(encrypted_lines)

                    print(f"\n✅ File encrypted successfully!")
                    print(f"Encrypted file saved as: {encrypted_filename}")
                    cipher = encrypted_lines  # чтобы выйти из цикла

            else:
                print(f"\n❌ File '{filename}' not found!")
                print("Please add numbers to the file.")
                user_input = input("Press Enter to try again or type 'q' to exit: ").strip().lower()
                if user_input == 'q':
                    print("Exiting to main menu...")
                    break
        if cipher is None:
            continue