from math import ceil

kms = float(input("how many kilometers you walk today : "))

miles = (kms / 1.609).__round__(2)
print("You walk {} miles today".format(miles))

