def generate_bill():
    items = []
    total = 0

    count = int(input("How many items are you buying? "))

    for i in range(count):
        print("\nItem", i + 1)

        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))

        amount = price * quantity
        total += amount

        items.append([name, price, quantity, amount])

    if total >= 1000:
        discount = total * 0.10
    elif total >= 500:
        discount = total * 0.05
    else:
        discount = 0

    final_total = total - discount

    print("\n===== SHOPPING RECEIPT =====")

    for item in items:
        print(item[0], "-", item[2],
              "x Rs.", item[1],
              "= Rs.", item[3])

    print("----------------------------")
    print("Total: Rs.", round(total, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final Bill: Rs.", round(final_total, 2))
    print("============================")


generate_bill()
