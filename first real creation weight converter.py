w = int(input("Weight: "))
u = input("(K)g or (L)bs: ")
if u.upper() == "K":
    converted = w / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = w * 0.45
    print("Weight in Kgs: " + str(converted))

# variable u = unit, KG or LBs, variable w = weight input
