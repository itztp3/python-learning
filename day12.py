import random
number = random.randint(1,10)

while True:
     guess = int(input("guess a number between 1 and 10:"))
     if guess == number:
          print("correct!")
          break
     else:
         print("wrong! try again/,")






