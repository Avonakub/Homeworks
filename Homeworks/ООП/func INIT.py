def show_menu():
    print("1 - Class ROBOT with limitations\n"
          "2 - Class MATH\n"
          "3 - Class CAR\n"
          "4 - Class SODA\n"
          "0 - Exit")
    print("➤➤➤")


# ====================== Class Robot ==============================
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = []


    def left(self):
        self.x -= 1
        print("Robot moved left ⬅️")
        self.history.append(self.x)


    def right(self):
        self.x += 1
        print("Robot moved right ➡️")
        self.history.append(self.x)


    def up(self):
        self.y += 1
        print("Robot moved up ⬆️")
        self.history.append(self.y)


    def down(self):
        self.y -= 1
        print("Robot moved down ⬇️")
        self.history.append(self.y)


    def position(self):
        print(f"Current robot position: x = {self.x}, y = {self.y}")


    def limiter(self):
        limiter_left, limiter_right, limiter_up, limiter_down = -9, 10, 8, -15
        moved = False  # Флаг для проверки, позодил ли робот

        if self.x > limiter_right:
            self.x = limiter_right
            print("🚫 Wall on the right! Can't go further.")
            moved = True
        elif self.x < limiter_left:
            self.x = limiter_left
            print("🚫 Wall on the left! Can't go further.")
            moved = True

        if self.y > limiter_up:
            self.y = limiter_up
            print("🚫 Wall above! Can't go further.")
            moved = True
        elif self.y < limiter_down:
            self.y = limiter_down
            print("🚫 Wall below! Can't go further.")
            moved = True

        if moved:
            self.history.append((self.x, self.y))


def robot_menu():
    print('=' * 50)
    print("CHOOSE ROBOT ACTION: \n"
          "1 - Move left\n"
          "2 - Move right\n"
          "3 - Move up\n"
          "4 - Move down\n"
          "5 - Robot history\n"
          "6 - Current position\n"
          "0 - Exit")


my_robot = Robot(0, 0)
# ====================== Class Math ==============================
class Math:
    def __init__(self):
        pass


    def get_numbers(self):

        while True:
            try:
                first_number = input("Enter first number: ")
                if first_number.startswith('0') and len(first_number) > 1 and first_number[1] != '.'\
                        or first_number.startswith('-0') and len(first_number) > 2 and first_number[2] != '.':
                    print("Error: Value cannot start with zero (except 0.86!)")
                    continue
                first_number = float(first_number)
                break
            except ValueError:
                print("❌ Error: Please enter a valid number.")

        while True:
            try:
                second_number = input("Enter second number: ")
                if second_number.startswith('0') and len(second_number) > 1 and second_number[1] != '.' \
                        or second_number.startswith('-0') and len(second_number) > 2 and second_number[2] != '.':
                    print("Error: Value cannot start with zero (except 0.86!)")
                second_number = float(second_number)
                return first_number, second_number
            except ValueError:
                print("❌ Error: Please enter a valid number.")


    def addition(self, first_number, second_number):
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")
        return result


    def subtraction(self, first_number, second_number):
        result = first_number - second_number
        print(f"{first_number} - {second_number} = {result}")
        return result


    def multiplication(self, first_number, second_number):
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")
        return result


    def division(self, first_number, second_number):
        if second_number == 0:
            print("❌ Error: Division by zero!")
            return None
        else:
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result:.2f}")
            return result


def math_menu():
    print('=' * 50)
    print("CHOOSE MATH OPERATION: \n"
          "1 - Addition\n"
          "2 - Subtraction\n"
          "3 - Multiplication\n"
          "4 - Division\n"
          "0 - Exit")


my_math = Math()
# ====================== Class Car ==============================
class Car:
    def __init__(self, color, type_car, year):
        self.color=color
        self.type_car=type_car
        self.year=year


    def started_car(self):
        print("✅ The car is started")


    def stoped_car(self):
        print("🛑 The car is stopped")

    def info_about_car(self):
        print("CAR INFORMATION")
        print("=" * 25)
        print(f"Color: {self.color}")
        print(f"Type: {self.type_car}")
        print(f"Year of release: {self.year}")


    def enter_value_car(self):
        while True:
            color = input("Enter color a car: ")
            if color !="":
                self.color = color
                break
            else:
                print("Information about the car color cannot be empty!")

        while True:
            type_car = input("Enter car type a car: ")
            if type_car !="":
                self.type_car = type_car
                break
            else:
                print("Information about the car type cannot be empty!")

        while True:
            try:
                year = input("Enter car year a car: ")
                if year == "":
                    print("Information about the car year cannot be empty!")
                    continue
                year = int(year)

                if year < 1950 or year > 2026:
                    print("❌ Error: Year must be between 1950 and 2026!")
                    continue
                self.year = year
                break
            except ValueError:
                print("❌ Error: Please enter a valid number.")


my_car = Car(None, None, None)


is_continue = True
while is_continue:
    show_menu()  # Вызвали функцию
    user_choice = input("Enter your choice HERE ➤ : ")

    if user_choice == "1":

        my_robot = Robot(0, 0)
        print("🟢 Robot created and launched!")
        my_robot.position()

        while True:
            robot_menu()  # Меню для отображения вариантов хода робота
            user_choice = input("Enter your choice HERE ➤ : ")
            if user_choice == '1':
                my_robot.left()
                my_robot.limiter()
            elif user_choice == '2':
                my_robot.right()
                my_robot.limiter()
            elif user_choice == '3':
                my_robot.up()
                my_robot.limiter()
            elif user_choice == '4':
                my_robot.down()
                my_robot.limiter()
            elif user_choice == '5':
                print("📜 Movement history:", my_robot.history)
            elif user_choice == '6':
                my_robot.position()
            elif user_choice == "0":
                print("↩️ Returning to main menu...")
                break
            else:
                print("❌ Invalid choice! Try again.")

    elif user_choice == "2":
        while True:
            math_menu()
            user_choice = input("Enter your choice HERE ➤ : ")
            if user_choice == '1':
                first, second = my_math.get_numbers()
                my_math.addition(first, second)
            elif user_choice == '2':
                first, second = my_math.get_numbers()
                my_math.subtraction(first, second)
            elif user_choice == '3':
                first, second = my_math.get_numbers()
                my_math.multiplication(first, second)
            elif user_choice == '4':
                first, second = my_math.get_numbers()
                my_math.division(first, second)
            elif user_choice == "0":
                print("↩️ Returning to main menu...")
                break
            else:
                print("❌ Invalid choice! Try again.")

    elif user_choice == "3":
        my_car.enter_value_car()
        my_car.info_about_car()
        print("-" * 25)
        while True:
            print("\nDRIVING CAR")
            print('=' * 25)
            print("1 - Start the car")
            print("2 - Turn off the car")
            print("0 - Exit")

            car_action = input("Enter action HERE ➤ : ")

            if car_action == "1":
                my_car.started_car()
            elif car_action == "2":
                my_car.stoped_car()
            elif car_action == "0":
                print("↩️ Returning to main menu...")
                break
            else:
                print("❌ Invalid choice! Try again.")








    elif user_choice == "0":
        print("👋 Goodbye!")
        is_continue = False
