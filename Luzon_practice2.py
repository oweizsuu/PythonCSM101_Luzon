studentsL={"Ana": [90,85,82],
            "Kirk": [72,73,78]}

studentsT={"Ana": (90,85,82),
            "Kirk": (72,73,78)}
print("Dictionary L")
for name, grade in studentsL.items():
    print(name, *grade)
print("")
print("Dictionary T")
for name, grade in studentsT.items():
    print(name,*grade)