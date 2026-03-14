import os
import re

def show_menu():
    print("1 - OS. Creating folders, rename files\n"
          "2 - Change name\n"
          "3 - Prime number\n"
          "4 - Greatest common divisor\n"
          "5 - Caesar cipher\n"
          "6 - Vigenère cipher\n"
          "7 - Run-Length Encoding\n"
          "8 - Spam\n"
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
            with open(filename, 'w') as file:
                file.write(test_text) # записали файл с нужным текстом
            print(f"✅ File {filename} created!")

        pattern = r"(?<=Подсудимая\s)[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?(?:\s[А-ЯЁ][а-яё]+){2}"  # регулярка для ФИО

        with open(filename, 'r') as file:
            file_content = file.read()  # открываем и читаем созданный файл

        print(f"\nContent {filename}:")
        print("-" * 50)
        print(file_content)  # выводим содержимое файла
        print("-" * 50)

        if "Подсудимая N" in file_content:
            print(f"\n⚠️ File {filename} already contains replacements!")  # если в файле есть изменения
        else:
            target_content = re.sub(pattern, 'N', file_content)  # заменяем ФИО на N
            with open(filename, 'w') as file:
                file.write(target_content)  # записываем обратно

            print(f"✅ Replacement completed! File {filename} has been updated.")
            print("New content:")
            print(target_content)
