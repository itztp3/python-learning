def check_password():
    password = input("Enter a password to check: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    print("\n--- PASSWORD REPORT ---")

    if score <= 2:
        print("Strength: Weak")
    elif score <= 4:
        print("Strength: Medium")
    else:
        print("Strength: Strong")

    print("Checks passed:", score, "/ 5")


check_password()
