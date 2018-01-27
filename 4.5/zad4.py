rok = []
for num in range(0, 12):
    miesiac = int(input("podaj miesięczne wynagrodzenie: "))
    rok.append(miesiac)

srednia = sum(rok) / len(rok)

print(srednia)


rok = []
i = 0
while i < 12:
    miesiac = int(input("podaj miesięczne wynagrodzenie: "))
    rok.append(miesiac)
    i += 1
srednia = sum(rok) / len(rok)

print(srednia)

suma = 0
miesiac = 1
while miesiac < 13:
    wynagrodzenie = int(input("podaj miesieczne wynagrodzenie :"))
    suma += wynagrodzenie
    miesiac += 1
print("Średnia:", suma/12)