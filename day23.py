budget = float(input("Enter your monthly budget: ₹"))

expenses = []

while True:
    print("\n--- PERSONAL EXPENSE TRACKER ---")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. Check remaining budget")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        if amount > 0:
            expenses.append([name, amount])
            print("Expense added successfully!")
        else:
            print("Amount must be greater than zero.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print(expense[0], "- ₹", expense[1])

    elif choice == "3":
        total = sum(expense[1] for expense in expenses)
        print("Total spent: ₹", total)

    elif choice == "4":
        total = sum(expense[1] for expense in expenses)
        remaining = budget - total
        print("Remaining budget: ₹", remaining)

        if remaining < 0:
            print("Warning: You exceeded your budget!")

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")


