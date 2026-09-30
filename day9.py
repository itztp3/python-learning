name = input("enter your namer:")
marks = int(input("enter your marks:"))
if marks>=90:
    grade="A"
elif marks>=75:
    grade="B"
elif marks>=50:
    grade="C"
else:
    grade="fail"

print("name:",name)
print("grade:",grade)
