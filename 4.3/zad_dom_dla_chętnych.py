skrzaty = int(input("Ilość skrzatów: "))
hajs = float(input("Ile hajsu na h: "))
prezenty = int(input("Ilość prezentów: "))
dostawa = float(input("Koszt dostawy: "))


if skrzaty > 1000:
    hajs -= hajs * 0.3
    print("Rabat za skrzaty")

if prezenty % 2 == 0:
    dostawa = 0
    print("Dostawa za darmo")
elif prezenty > 10000:
    dostawa -= dostawa * 0.5
    print("Rabat za dostawę")

koszt = skrzaty * hajs + dostawa
koszt_brutto = koszt + koszt * 0.23

print("Koszt netto: ", koszt)
print("Koszt brutto: ", koszt_brutto)
