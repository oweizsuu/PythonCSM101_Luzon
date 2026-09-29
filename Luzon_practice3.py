students = {
    "Ana": [90, 85, 82],
    "Kirk": [72, 73, 78],
    "Liza": [69, 71, 83]
}

highest = 0
namehighest = ""
tally = 0

for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average", average)

    if average > highest:
        highest = average
        namehighest = name

    for g in grade:
        if g < 75:
            tally = tally + 1

else:
    students = {"Ana": [90,85,82],
                "Kirk": [72,73,78],
                "Liza": [69,71,83],
}
lowest = 0
namelowest = ""
tally = 0

for name, grade in students.items():
    average = sum(grade)/ len(grade)
    print(name, *grade, "Average:", average)
    if average < lowest:
        lowest = average
        namelowest = name
    for g in grade:
        if g < 75:
            tally = tally + 1

print("")
print(f"Student {namehighest} got the highest average: {highest}")
print(f"There are {tally} grades which are below 75.")
print("")
print(f"Student {namelowest} got the lowest average: {lowest}")
print(f"There are {tally} grades which are below 75,")




