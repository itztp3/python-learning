movies = {
    1: {"name": "Avengers", "price": 180, "seats": 30},
    2: {"name": "Interstellar", "price": 200, "seats": 25},
    3: {"name": "Inception", "price": 150, "seats": 20}
}

bookings = []


def display_movies():
    print("\n===== AVAILABLE MOVIES =====")

    for key, movie in movies.items():
        print(
            f"{key}. {movie['name']} | "
            f"Price: Rs.{movie['price']} | "
            f"Seats: {movie['seats']}"
        )


def book_ticket():
    display_movies()

    try:
        choice = int(input("\nSelect movie number: "))

        if choice not in movies:
            print("Invalid movie selection!")
            return

        quantity = int(input("Enter number of tickets: "))

        if quantity <= 0:
            print("Enter a valid ticket quantity!")
            return

        movie = movies[choice]

        if quantity > movie["seats"]:
            print("Sorry! Not enough seats available.")
            return

        student = input("Are you a student? (yes/no): ").lower()

        total = quantity * movie["price"]

        if student == "yes":
            discount = total * 0.10
        else:
            discount = 0

        final_amount = total - discount

        movie["seats"] -= quantity

        booking = {
            "movie": movie["name"],
            "tickets": quantity,
            "amount": final_amount
        }

        bookings.append(booking)

        print("\n===== BOOKING CONFIRMED =====")
        print("Movie:", movie["name"])
        print("Tickets:", quantity)
        print("Discount:", discount)
        print("Final Amount: Rs.", final_amount)

    except ValueError:
        print("Please enter valid numbers!")


def show_bookings():
    print("\n===== BOOKING HISTORY =====")

    if not bookings:
        print("No bookings found.")
        return

    for booking in bookings:
        print(booking)


while True:
    print("\n===== MOVIE BOOKING SYSTEM =====")
    print("1. View Movies")
    print("2. Book Tickets")
    print("3. View Bookings")
    print("4. Exit")

    try:
        option = int(input("Enter your choice: "))

        if option == 1:
            display_movies()

        elif option == 2:
            book_ticket()

        elif option == 3:
            show_bookings()

        elif option == 4:
            print("Thank you for using our system!")
            break

        else:
            print("Invalid option!")

    except ValueError:
        print("Please enter a valid menu number!")