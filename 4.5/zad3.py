for num in range(1, 27):
    if num % 2 == 0:
        print(num)

for i in range(1, 27, 2):
    print(i)


osoby = ["Monika", "Wojciech", "Jan", "Piotr", "Agata"]
for osoba in osoby:
    print("Wesołych Świąt " + osoba)

for char in "Ala ma 4 koty":
    if char.isdigit():
        print(char, "jest liczbą")
