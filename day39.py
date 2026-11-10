# Day 35: Smart Inventory Management System

inventory = {}

def add_product():
    name = input("Enter product name: ").strip().lower()

    if not name:
        print("Product name cannot be empty!")
        return

    if name in inventory:
        print("Product already exists!")
        return

    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity < 0:
            print("Invalid price or quantity!")
            return

        inventory[name] = {
            "price": price,
            "quantity": quantity
        }

        print("Product added successfully!")

    except ValueError:
        print("Please enter valid numbers!")


def view_products():
    if not inventory:
        print("Inventory is empty!")
        return

    print("\n----- INVENTORY -----")

    for name, details in inventory.items():
        print(
            f"{name.title()} | "
            f"Price: Rs.{details['price']:.2f} | "
            f"Stock: {details['quantity']}"
        )


def search_product():
    name = input("Enter product name: ").strip().lower()

    if name in inventory:
        product = inventory[name]
        print("Product:", name.title())
        print("Price: Rs.", product["price"])
        print("Quantity:", product["quantity"])
    else:
        print("Product not found!")


def sell_product():
    name = input("Enter product name: ").strip().lower()

    if name not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            print("Enter a positive quantity!")
        elif quantity > inventory[name]["quantity"]:
            print("Insufficient stock!")
        else:
            inventory[name]["quantity"] -= quantity

            total = quantity * inventory[name]["price"]

            print("Sale successful!")
            print(f"Total amount: Rs.{total:.2f}")

    except ValueError:
        print("Enter a valid quantity!")


def restock_product():
    name = input("Enter product name: ").strip().lower()

    if name not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter quantity to add: "))

        if quantity <= 0:
            print("Enter a positive quantity!")
        else:
            inventory[name]["quantity"] += quantity
            print("Stock updated successfully!")

    except ValueError:
        print("Enter a valid quantity!")


def low_stock_alert():
    print("\n----- LOW STOCK ALERT -----")

    found = False

    for name, details in inventory.items():
        if details["quantity"] <= 5:
            print(name.title(), "- Only",
                  details["quantity"], "left!")
            found = True

    if not found:
        print("All products have sufficient stock!")


def inventory_value():
    total = 0

    for details in inventory.values():
        total += details["price"] * details["quantity"]

    print(f"Total inventory value: Rs.{total:.2f}")


# Main program

while True:

    print("\n===== SMART INVENTORY SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Sell Product")
    print("5. Restock Product")
    print("6. Low Stock Alert")
    print("7. Inventory Value")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_product()
        elif choice == 2:
            view_products()
        elif choice == 3:
            search_product()
        elif choice == 4:
            sell_product()
        elif choice == 5:
            restock_product()
        elif choice == 6:
            low_stock_alert()
        elif choice == 7:
            inventory_value()
        elif choice == 8:
            print("Thank you for using Inventory System!")
            break
        else:
            print("Invalid choice! Select 1-8.")

    except ValueError:
        print("Please enter a valid menu number!")