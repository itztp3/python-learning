units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 3
    print("Electricity bill: ₹", bill)
elif units <= 200:
    bill = units * 5
    print("Electricity bill: ₹", bill)
else:
    bill = units * 7
    print("Electricity bill: ₹", bill)
