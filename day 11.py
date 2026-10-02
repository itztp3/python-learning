name = input("enter your name:")
marks = int(input("enter your name"))

if marks>=90:
    grade = "A"
elif marks>="75":
    grade = "B"
elif marks>="60":
    grade = "c"
elif marks>="40":
    grade = "D"
else:
    grade = "F"


print("\nstudent name:",name)
print("marks:",marks)
print("grade:",grade)
            