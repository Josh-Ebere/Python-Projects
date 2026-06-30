weight = int(input("Weight: "))
unit_weight = input("(L)bs or (K)gs: ")

if unit_weight.lower() == "k":
    conv_weight = weight // 0.45
    print(f"You are {conv_weight} pounds")
elif unit_weight.lower() == "l":
    conv_weight = round(weight * 0.45)
    print(f"You are {conv_weight} kilograms")
else:
    print(f"Wrong input")
