three_musketeers = ('Atos', 'Portos', 'Aramis')
name = input("Jak masz na imię?: ").capitalize()

if name in three_musketeers:
    print("Witaj muszkieterze")
else:
    print("Chyba nie jesteś muszkieterem")