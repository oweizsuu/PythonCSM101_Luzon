flavor = input("enter pizza flavor (Pepperoni Pizza/Taco Pizza/BBQ Chicken Pizza): ").lower()

LuzonFlavor1 = [
    ("Pepperoni Pizza" , 200, 350, 550),
    ("Taco Pizza" , 250, 400, 650),
    ("BBQ Chicken Pizza" , 370, 550, 750),

]

LuzonFlavor = input("enter a Pizza Flavor: ").lower()
LuzonSize = input("enter size (Small/Medium/Large): ").lower

LuzonPrice = 0

print("Receipt Price")
for pizza in LuzonFlavor1:
    if pizza[0] == LuzonFlavor:
        if LuzonSize == "Small":
            LuzonPrice = pizza[1]
        elif LuzonSize == "Medium":
            LuzonPrice = pizza[2]
        elif LuzonSize == "Large":
            LuzonPrice = pizza[3]
        else:
            print("Invalid size")
            print("Please Try Again")
        break

else:
    print("Invalid Pizza Flavor")

if LuzonPrice > 0:
    print(f"{LuzonFlavor.capitalize()} Pizza")