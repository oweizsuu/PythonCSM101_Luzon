Luzon_patients = {"Ana": [70, 80, 100, 150, 160, 170, 180], "Ben": [190, 180, 167, 162, 99, 82, 77], "Alan":[130, 159, 120, 89, 90, 110, 120]}
for pn, bs in Luzon_patients.items():
    print(pn)

    print("Blood sugar summary - ")
    for value in bs:

        if value>120:
            print(value, "high")

        else:
            print(value, "normal")
    highestbs = max(bs)
    lowestbs = min(bs)
    averagebs = sum(bs) / len(bs)
    diffbs = max(bs) - min(bs)

    print("max blood sugar: ", highestbs)
    print("min blood sugar: ", lowestbs)
    print(f"average blood sugar: {averagebs: .2f}")
    print("diff blood sugar: ", diffbs)
