woda = input("Czy woda jest w czajniku?\n")
if woda == "tak":
    print("Wspaniale, woda w czajniku")
else:
    print("Nalej wody")

gaz = input("Czy gaz jest włączony? \n")
if gaz == "tak":
    print("Wspaniale, gaz włączony")
else:
    print("Włącz gaz")

czajnik = input("Czy czajnik stoi na gazie? \n")
if czajnik == "tak":
    gwizdek = input("Czy czajnik gwiżdże? \n")
    if gwizdek == "tak":
        print("Wyłącz gaz")
    elif gwizdek == "nie":
        print("Czekaj z uśmiechem")
    else:
        print("Błędna wartość")
else:
    print("Postaw czajnik na gazie")