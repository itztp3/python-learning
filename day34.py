print("===== SMART TRAVEL FARE ESTIMATOR =====")

print("\n1. Bus")
print("2. Metro")
print("3. Cab")

choice = int(input("\nChoose transport (1-3): "))

distance = float(input("Enter distance (KM): "))

student = input("Are you a student? (yes/no): ").lower()

if distance <= 0:
    print("Invalid distance!")

else:
    if choice == 1:
        transport = "Bus"
        rate = 10

    elif choice == 2:
        transport = "Metro"
        rate = 15

    elif choice == 3:
        transport = "Cab"
        rate = 25

    else:
        transport = None

    if transport is None:
        print("Invalid transport choice!")

    else:
        original_fare = distance * rate

        if student == "yes":
            discount = original_fare * 0.10
        else:
            discount = 0

        final_fare = original_fare - discount

        print("\n===== TRAVEL FARE RECEIPT =====")
        print("Transport:", transport)
        print("Distance:", distance, "KM")
        print("Original Fare: ₹", original_fare)
        print("Student Discount: ₹", discount)
        print("Final Fare: ₹", final_fare)

        print("\nThank you for travelling!")