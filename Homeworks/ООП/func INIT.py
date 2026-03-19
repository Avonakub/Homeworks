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


my_robot = Robot(0, 0)
print("🟢 Robot created and launched!")
my_robot.position()


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


is_continue = True
while is_continue:
    show_menu()  # Вызвали функцию
    user_choice = input("Enter your choice HERE ➤ : ")

    if user_choice == "1":

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
                print("↩️Returning to main menu...")
                break
            else:
                print("❌ Invalid choice! Try again.")

    elif user_choice == "0":
        print("👋 Goodbye!")
        is_continue = False
