budzet_brutto = float(input("Podaj budżet brutto: "))
podatek = budzet_brutto * 0.19
zus = 1172.56
budzet_netto = budzet_brutto - podatek - zus

wydatki = []
while True:
    wydatek = input("Podaj wydatek (jeżeli już skończyłeś podawać listę wydatków napisz stop): ")
    if wydatek == "stop":
        break
    wydatki.append(float(wydatek))

suma_wydatkow = sum(wydatki)

if suma_wydatkow <= budzet_netto:
    print("Spoko, mieścisz się w budżecie")
else:
    print("Nie dasz rady, dzieci nie dostaną prezentów")

print("ZUS:", zus)
print("Podatek:", podatek)
print("Budżet netto:", str)
print("Suma wydatków:", suma_wydatkow)
print("Stan konta po świętach:", budzet_netto - suma_wydatkow)
