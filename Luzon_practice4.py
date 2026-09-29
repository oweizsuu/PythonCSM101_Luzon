students = {}
number = int(input("Enter number of students: "))
for i in range(number):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))

    students[name] = (grade1, grade2, grade3)

print("\n===== Student Records =====")


highest = 0
namehighest = ""
lowest = 100
namelowest = ""

tally = 0

for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average:" , round(average, 2))

    if average > highest:
        highest = average
        namehighest = name
    if average < lowest:
        lowest = average
        namelowest = name
    if average > 75:
        tally += 1

print(f"\nStudent {namehighest} got the highest average: {highest:.2f} ")
print(f"Student {namelowest} is lowest grade: {lowest:.2f}")
print(f"There are {tally} grades which are below 75.")
