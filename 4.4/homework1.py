liczba_widzow = [50, 43, 20, 80, 130]
wczoraj = liczba_widzow[4]
dzis = int(input("ile osób bylo w kinie dzisiaj? "))
liczba_widzow.append(dzis)
if dzis < wczoraj:
    print("Dzisiaj było mniej ludzi niż wczoraj")
elif dzis == wczoraj:
    print("Dzisiaj było tyle samo ludzi co wczoraj")
else:
    print("Dzisiaj było więcej ludzi niz wczoraj")

suma_widzow = sum(liczba_widzow)
print("Suma widzów: ", suma_widzow)
srednia_widzow = suma_widzow / len(liczba_widzow)
print("Średnia widzów: ", srednia_widzow)
