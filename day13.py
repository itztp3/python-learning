password = input("enter your password:")

if len(password)<6:
    print("Weak password")
elif len(password)<10:
    print("Medium password")
else:
    print("Strong password")


