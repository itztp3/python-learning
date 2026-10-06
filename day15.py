secret_number = 7
while True:
    guess =int(input("guess the number:"))

    if guess == secret_number:
        print("correct! you won!")
        break
    elif guess<secret_number:
        print("Too low!")
    else:
        print("Too high!")    