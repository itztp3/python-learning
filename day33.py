tasks = []


def calculate_priority(task):
    days = task["days_left"]
    importance = task["importance"]

    if days < 0:
        return 1 # Overdue
    elif days == 0:
        return 1 # Due today
    elif days <= 2 and importance == "High":
        return 1
    elif days <= 2 or importance == "High":
        return 2
    elif importance == "Medium":
        return 3
    else:
        return 4


def add_task():
    name = input("Enter task name: ").strip()

    if not name:
        print("Task name cannot be empty.")
        return

    importance = input(
        "Importance (High/Medium/Low): "
    ).strip().capitalize()

    if importance not in ["High", "Medium", "Low"]:
        print("Invalid importance level.")
        return

    try:
        days = int(input("Days until deadline (negative if overdue): "))

        task = {
            "name": name,
            "importance": importance,
            "days_left": days
        }

        task["priority"] = calculate_priority(task)
        tasks.append(task)

        print("Task added successfully!")

    except ValueError:
        print("Please enter a valid whole number.")


def view_tasks():
    if not tasks:
        print("No tasks added yet.")
        return

    ordered_tasks = sorted(
        tasks,
        key=lambda task: task["priority"]
    )

    print("\n===== TASK PRIORITY REPORT =====")

    for task in ordered_tasks:
        priority = task["priority"]

        if priority == 1:
            label = "URGENT"
        elif priority == 2:
            label = "HIGH"
        elif priority == 3:
            label = "MEDIUM"
        else:
            label = "LOW"

        print(f"\nTask: {task['name']}")
        print(f"Importance: {task['importance']}")
        print(f"Days left: {task['days_left']}")
        print(f"Priority: {label}")


def main():
    while True:
        print("\n===== SMART TASK ANALYZER =====")
        print("1. Add task")
        print("2. View prioritized tasks")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Task analyzer closed.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
