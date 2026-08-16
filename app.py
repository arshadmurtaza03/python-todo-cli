TASKS_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def add_task(tasks):
    task = input("\nEnter a new task: ").strip()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- Python To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()