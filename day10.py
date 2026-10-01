name = input("enter student name:")
marks = []
for i in range(3):
    mark = int(input("enter marks:"))
    marks.append(mark)

total = sum(marks)
average = total/3

print("\n---student result---")
print("Name:",name)
print("Marks:",marks)
print("Total:",total)
print("Average:",average)

if average>=40:
  print("result:pass")
else:
  print("result:fail")




