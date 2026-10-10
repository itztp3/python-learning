contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact saved successfully!")

def view_contacts():
    if not contacts:
        print("No contacts saved yet.")
    else:
        print("\n--- Contact Book ---")
        for name, phone in contacts.items():
            print(name, ":", phone)

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
        