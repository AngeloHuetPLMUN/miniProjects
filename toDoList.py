tasks = []


def add_task():
    add = input("Add a task: ")
    tasks.append(add)
    print(f"Task added!: {add}")


def view_task():
    if not tasks:
        print("No tasks yet!")
    else:
        for index, task in enumerate(tasks, start=1):
            print("\nYour To-Do List!")
            print(f"{index}. {task}")


def delete_task():
    if not tasks:
        print("No tasks to delete!")
    else:
        for index, task in enumerate(tasks, start=1):
            print("\nYour To-Do List!")
            print(f"{index}. {task}")

    task_number = int(input("\nEnter the number to delete: "))
    index = task_number - 1

    try:
        tasks.pop(index)
        print("Task deleted Successfully!")
    except IndexError:
        print("Invalid task number!")


def quit_program():
    pass


def main():
    is_running = True
    while is_running:
        print("--------------------------------")
        print("TO-DO LIST APP")
        print("1. Add a task")
        print("2. View Task")
        print("3. Delete a Task")
        print("4. Exit")
        print("--------------------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            is_running = False
        else:
            print("Invalid input!")
    print("\nThank You, I hope you can add more To-do list today!")


main()
