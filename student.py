students = {
    "Asha": "Python",
    "Ravi": "Data Analytics",
    "Neha": "AI"
}
print("Student Names:")
for name in students.keys():
    print(name)
print("\nEnrolled Courses:")
for course in students.values():
    print(course)
check_name = input("\nEnter student name to check: ")
if check_name in students:
    print(check_name, "is enrolled in", students[check_name])
else:
    print("Student not found")