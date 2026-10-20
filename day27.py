def calculate_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    else:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5

    return bill


units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units!")
else:
    bill = calculate_bill(units)
    print("Units consumed:", units)
    print("Total electricity bill: Rs.", bill)
