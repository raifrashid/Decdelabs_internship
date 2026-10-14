import json
from pathlib import Path


class Todo:

    database = "data.json"

    def __init__(self):
        self.my_task = []

        if Path(self.database).exists():
            with open(self.database, "r") as fs:
                self.my_task = json.load(fs)
        else:
            print("No such file exist")

    def save_tasks(self):
        with open(self.database, "w") as fs:
            json.dump(self.my_task, fs)

    def add_task(self):
        user_inp = input("Enter Your Task: ")
        self.my_task.append(user_inp)
        self.save_tasks()
        print("Task Added Successfully")

    def view_task(self):
        if len(self.my_task) == 0:
            print("No Task Available")
        else:
            for i, task in enumerate(self.my_task, start=1):
                print(f"{i}. {task}")

            print("Task Viewed Successfully")

    def remove_task(self):
        if len(self.my_task) == 0:
            print("No tasks to delete")

        else:
            self.view_task()

            task_num = int(input("Enter task number which you want to delete: "))

            if 1 <= task_num <= len(self.my_task):
                deleted = self.my_task.pop(task_num - 1)
                self.save_tasks()
                print(f"{deleted} deleted successfully")

            else:
                print("Invalid task number")


user = Todo()

while True:

    print("""
    === To Do App ===
    === 1. Add Task ===
    === 2. View Task ===
    === 3. Delete Task ===
    === 4. Exit ===
    """)

    user_choice = int(input("Enter Your Choice: "))

    if user_choice == 1:
        user.add_task()

    elif user_choice == 2:
        user.view_task()

    elif user_choice == 3:
        user.remove_task()

    elif user_choice == 4:
        print("Thank you for using To Do App!")
        break

    else:
        print("Invalid choice!")