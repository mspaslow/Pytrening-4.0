moi_znajomi = ["Maciek Nowak", "Ania Kowalska", "Michu Bogacki", "Czarek Wieczorek", "Marta Kacprzak"]

licznik = 0
while licznik < 5:
    nazwisko = input("Podaj imię i nazwisko znajomego: ")
    moi_znajomi.append(nazwisko)
    licznik += 1
print(moi_znajomi)