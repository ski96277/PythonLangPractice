weight = float(input("Weight? "))

kg_or_lbs = input("(K)g OR (L)bs: ")

if kg_or_lbs.lower() == "l":

    converted = weight / 0.45
    print("Wight in lbs : ", converted)
else:
    converted = weight * 0.45
    print("Wight in (k)g : ", converted)
