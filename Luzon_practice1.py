students = {
    "Ana": 85,
    "Ben": 98,
    "Carlo": 78,
    "Diana": 95,
}
print("Students Grade")
print("-----------------")
print("Ana:" , students["Ana"])
print("Ben:" , students["Ben"])
#add a new student
students["Ella"] = 88
#update a students grade
students["Carlo"] = 82
students["Diana"] = 91
name1 = input("Enter student name: ")
grade1 = input("Enter grade: ")
students[name1] = grade1

print(students)
print("\nUpdated Students Grades")
print("------------------")

for name, grade in students.items():
    print(name,capitalize(), ":", grade)
search = input("enter student name to: ")
if search in students:
    print(search, ":", students[search])
else:
    print("Student not found")