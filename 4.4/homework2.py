tydzien_1 = [234, 356, 260, 287, 298, 387, 245]
tydzien_2 = [245, 234, 265, 134, 345, 390, 367]

suma_1 = sum(tydzien_1)
suma_2 = sum(tydzien_2)
if suma_1 > suma_2:
    print("więcej w 1 tygodniu")
elif suma_1 < suma_2:
    print("więcej w 2 tygodniu")
else:
    print("tyle samo")

srednia_1 = suma_1 / len(tydzien_1)
srednia_2 = suma_2 / len(tydzien_2)
if srednia_1 > srednia_2:
    print("większa średnia w 1 tygodniu")
elif srednia_1 < srednia_2:
    print("większa średnia w 2 tygodniu")
else:
    print("taka sama średnia")