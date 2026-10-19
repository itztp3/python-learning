assignments = []

def add_assignment():
    subject = input("Enter subject: ")
    task = input("Enter assignment name: ")

    assignment = {
        "subject": subject,
        "task": task,
        "completed": False
    }

    assignments.append(assignment)
    print("Assignment added successfully!")

def view_assignments():
    if not assignments:
        print("No assignments added yet.")
        return

    for i, assignment in enumerate(assignments, start=1):
        status = "Completed" if assignment["completed"] else "Pending"

        print(f"{i}. {assignment['subject']} - "
              f"{assignment['task']} [{status}]")

def complete_assignment():
    view_assignments()

    if not assignments:
        return

    try:
        number = int(input("Enter assignment number: "))

        if 1 <= number <= len(assignments):
            assignments[number - 1]["completed"] = True
            print("Assignment marked as completed!")
        else:
            print("Invalid assignment number.")

    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n--- COLLEGE ASSIGNMENT TRACKER ---")
    print("1. Add assignment")
    print("2. View assignments")
    print("3. Complete assignment")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_assignment()
    elif choice == "2":
        view_assignments()
    elif choice == "3":
        complete_assignment()
    elif choice == "4":
        print("Goodbye! Keep learning Python.")
        break
    else:
        print("Invalid choice. Try again.")
