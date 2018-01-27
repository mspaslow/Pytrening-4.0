bok_1 = float(input("podaj dlugość boku 1: "))
bok_2 = float(input("podaj dlugość boku 2: "))
bok_3 = float(input("podaj dlugość boku 3: "))
waga = float(input("podaj wagę prezentu: "))
koszt_dostawy = float(input("podaj koszt dostawy: "))
rabat = 0.25
pole = 2 * bok_1 + 2 * bok_2 + 2 * bok_3
wyliczony_koszt = pole + koszt_dostawy
print("Koszt bez rabatu: ", wyliczony_koszt)

if bok_1 == bok_2 == bok_3 or waga > 120:
    wyliczony_koszt -= wyliczony_koszt * rabat
    print("Koszt z rabatem: ", wyliczony_koszt)
else:
    print("Prezent nie kwalifikuje się do rabatu")
