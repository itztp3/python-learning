tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks added yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n--- TO-DO LIST MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        print("Goodbye! Keep completing your tasks!")
        break

    else:
        print("Invalid choice. Try again.")
