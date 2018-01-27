bok_1 = float(input("Podaj długość boku nr 1: "))
bok_2 = float(input("Podaj długość boku nr 2: "))
bok_3 = float(input("Podaj długość boku nr 3: "))

objętość = bok_1 * bok_2 * bok_3
print("Objętość wynosi " + str(objętość) + " m3")

if bok_1 == bok_2 == bok_3:
    print("Bryła jest sześcianem")
else:
    print("Bryła nie jest sześcianem")

pole = 2 * bok_1 * bok_2 + 2 * bok_2 * bok_3 + 2 * bok_1 * bok_3
if pole > 100:
    print("Pole jest większe niż 100")