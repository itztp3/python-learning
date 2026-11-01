import json
import os

FILE_NAME = "event_data.json"
MAX_SEATS = 50


def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read saved data.")
    return []


def save_data(participants):
    with open(FILE_NAME, "w") as file:
        json.dump(participants, file, indent=4)


def register_participant(participants):
    if len(participants) >= MAX_SEATS:
        print("Sorry! All seats are booked.")
        return

    name = input("Enter participant name: ").strip()
    email = input("Enter email: ").strip()

    if not name or not email or "@" not in email:
        print("Please enter valid details.")
        return

    registration_id = max(
        [p["id"] for p in participants], default=1000
    ) + 1

    participant = {
        "id": registration_id,
        "name": name,
        "email": email
    }

    participants.append(participant)
    save_data(participants)

    print("\nRegistration successful!")
    print("Registration ID:", registration_id)


def view_participants(participants):
    if not participants:
        print("No registrations found.")
        return

    print("\n--- REGISTERED PARTICIPANTS ---")

    for person in participants:
        print(
            f"ID: {person['id']} | "
            f"Name: {person['name']} | "
            f"Email: {person['email']}"
        )


def search_participant(participants):
    name = input("Enter name to search: ").strip().lower()

    found = [
        person for person in participants
        if name in person["name"].lower()
    ]

    if found:
        for person in found:
            print(person)
    else:
        print("Participant not found.")


def cancel_registration(participants):
    try:
        reg_id = int(input("Enter registration ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for person in participants:
        if person["id"] == reg_id:
            participants.remove(person)
            save_data(participants)
            print("Registration cancelled successfully.")
            return

    print("Registration ID not found.")


def show_seats(participants):
    available = MAX_SEATS - len(participants)

    print("Total seats:", MAX_SEATS)
    print("Booked seats:", len(participants))
    print("Available seats:", available)


def main():
    participants = load_data()

    while True:
        print("\n===== EVENT MANAGEMENT SYSTEM =====")
        print("1. Register Participant")
        print("2. View Participants")
        print("3. Search Participant")
        print("4. Cancel Registration")
        print("5. Check Seat Availability")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_participant(participants)

        elif choice == "2":
            view_participants(participants)

        elif choice == "3":
            search_participant(participants)

        elif choice == "4":
            cancel_registration(participants)

        elif choice == "5":
            show_seats(participants)

        elif choice == "6":
            print("Thank you for using Event Manager!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()