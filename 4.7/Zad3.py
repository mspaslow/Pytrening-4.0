n = int(input("Podaj długość ciągu Fibonacciego: "))
n_list = [0, 1]
sum_of_evens = 0

for x in range(3, n + 1):
    num = n_list[-2] + n_list[-1]
    n_list.append(num)
    if num % 2 == 0:
        sum_of_evens += num

print(n_list)
print("Suma: ", sum(n_list))
print("Suma wyrazów parzystych: ", sum_of_evens)