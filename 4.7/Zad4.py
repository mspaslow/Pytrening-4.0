def fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

n = 1

while n > 0:
    n = int(input("Podaj długość ciągu Fibonacciego: "))
    print(fib(n))

