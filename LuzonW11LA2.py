print("Luzon Pizza Store")
print("Pizza Flavours (Pepperoni Pizza, Taco Pizza, BBQ Chicken Pizza)")

LuzonFlavor1 = [
    ("Pepperoni", 200, 350, 550),
    ("Taco", 250, 400, 650),
    ("BBQ", 370, 550, 750),
]

LuzonFlavor = input("Enter a Pizza Flavor: ").lower()
LuzonSize = input("Enter size (Small/Medium/Large): ").lower()

LuzonPrice = 0

print("\nReceipt Price")


for pizza in LuzonFlavor1:

    if pizza[0].lower() == LuzonFlavor:

        if LuzonSize == "small":
            LuzonPrice = pizza[1]

        elif LuzonSize == "medium":
            LuzonPrice = pizza[2]

        elif LuzonSize == "large":
            LuzonPrice = pizza[3]

        else:
            print("Invalid size")
            print("Please Try Again")

        break

else:
    print("Invalid Pizza Flavor")


if LuzonPrice > 0:
    print("\n----- RECEIPT -----")
    print(f"Pizza: {LuzonFlavor.title()}")
    print(f"Size: {LuzonSize.title()}")
    print(f"Price: {LuzonPrice}")
    print("Thank you for purchasing!")
