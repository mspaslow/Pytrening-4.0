sentence = input("Podaj zdanie: ")
sentence = sentence.lower()

vowels = ["a", "e", "i", "o", "u", "y"]
counter_a = 0
counter_e = 0
counter_i = 0
counter_o = 0
counter_u = 0
counter_y = 0


for char in sentence:
    if char in vowels:
        print(char)
        if char == "a":
            counter_a += 1
        elif char == "e":
            counter_e += 1
        elif char == "i":
            counter_i += 1
        elif char == "o":
            counter_o += 1
        elif char == "u":
            counter_u += 1
        elif char == "y":
            counter_y += 1

print("ilość liter a: ", counter_a)
print("ilość liter e: ", counter_e)
print("ilość liter i: ", counter_i)
print("ilość liter o: ", counter_o)
print("ilość liter u: ", counter_u)
print("ilość liter y: ", counter_y)


