import os


def main():
    print(f"Operating system: {os.name}")
    print(f"Current directory: {os.getcwd()}")
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