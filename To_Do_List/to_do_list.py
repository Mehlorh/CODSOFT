# To Do List by SM Mncwango
def add_task(task):
    with open('Tasks.txt', 'a') as file:
        file.write(task + '\n')


def view_tasks():
    try:
        with open('Tasks.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Your To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("Your to-do list is empty!")
    except FileNotFoundError:
        print("Your to-do list is empty!")


def update_task(task_number, new_task):
    try:
        with open('Tasks.txt', 'r+') as file:
            tasks = file.readlines()
            if 0 < task_number <= len(tasks):
                tasks[task_number - 1] = new_task + '\n'
                file.seek(0)
                file.writelines(tasks)
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
    except FileNotFoundError:
        print("Your to-do list is empty!")


def delete_task(task_number):
    try:
        with open('Tasks.txt', 'r+') as file:
            tasks = file.readlines()
            if 0 < task_number <= len(tasks):
                del tasks[task_number - 1]
                file.seek(0)
                file.writelines(tasks)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
    except FileNotFoundError:
        print("Your to-do list is empty!")


def To_Do_List():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")
            update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    To_Do_List()
# main.py

def add_task(task):
    with open('Tasks.txt', 'a') as file:
        file.write(task + '\n')


def view_tasks():
    try:
        with open('Tasks.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Your To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("Your to-do list is empty!")
    except FileNotFoundError:
        print("Your to-do list is empty!")


def update_task(task_number, new_task):
    try:
        with open('Tasks.txt', 'r+') as file:
            tasks = file.readlines()
            if 0 < task_number <= len(tasks):
                tasks[task_number - 1] = new_task + '\n'
                file.seek(0)
                file.writelines(tasks)
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
    except FileNotFoundError:
        print("Your to-do list is empty!")


def delete_task(task_number):
    try:
        with open('Tasks.txt', 'r+') as file:
            tasks = file.readlines()
            if 0 < task_number <= len(tasks):
                del tasks[task_number - 1]
                file.seek(0)
                file.writelines(tasks)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
    except FileNotFoundError:
        print("Your to-do list is empty!")


def To_Do_List():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")
            update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    To_Do_List()
