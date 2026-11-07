complaints = []
complaint_id = 1001


def register_complaint():
    global complaint_id

    title = input("Enter complaint title: ")
    category = input("Enter category: ")
    priority = input("Enter priority (Low/Medium/High): ")

    if not title.strip():
        print("Complaint title cannot be empty!")
        return

    if priority.lower() not in ["low", "medium", "high"]:
        print("Invalid priority!")
        return

    complaint = {
        "id": complaint_id,
        "title": title,
        "category": category,
        "priority": priority.capitalize(),
        "status": "Pending"
    }

    complaints.append(complaint)

    print("Complaint registered successfully!")
    print("Complaint ID:", complaint_id)

    complaint_id += 1


def view_complaints():
    if not complaints:
        print("No complaints available.")
        return

    for item in complaints:
        print("\nComplaint ID:", item["id"])
        print("Title:", item["title"])
        print("Category:", item["category"])
        print("Priority:", item["priority"])
        print("Status:", item["status"])


def update_status():
    search_id = int(input("Enter complaint ID: "))

    for item in complaints:
        if item["id"] == search_id:
            new_status = input(
                "Enter status (Pending/In Progress/Resolved): "
            )

            if new_status.lower() not in [
                "pending", "in progress", "resolved"
            ]:
                print("Invalid status!")
                return

            item["status"] = new_status.title()
            print("Status updated successfully!")
            return

    print("Complaint not found!")


def dashboard():
    total = len(complaints)

    pending = sum(
        1 for item in complaints
        if item["status"] == "Pending"
    )

    resolved = sum(
        1 for item in complaints
        if item["status"] == "Resolved"
    )

    print("\n--- CAMPUS DASHBOARD ---")
    print("Total complaints:", total)
    print("Pending:", pending)
    print("Resolved:", resolved)


while True:
    print("\n===== CAMPUS MAINTENANCE TRACKER =====")
    print("1. Register Complaint")
    print("2. View Complaints")
    print("3. Update Status")
    print("4. Dashboard")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_complaint()
    elif choice == "2":
        view_complaints()
    elif choice == "3":
        update_status()
    elif choice == "4":
        dashboard()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")


        