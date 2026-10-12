students = ["Tulasi", "Rahul", "Priya", "Arun"]

present_count = 0
absent_count = 0

for student in students:
    status = input(f"Is {student} present? (yes/no): ").lower()

    if status == "yes":
        print(student, "- Present")
        present_count += 1
    else:
        print(student, "- Absent")
        absent_count += 1

print("\n--- Attendance Summary ---")
print("Total students:", len(students))
print("Present:", present_count)
print("Absent:", absent_count)
