# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        n1, n2 = 1, -1
        for i in range(2, n):
            a = n1
            n1 = n2
            n2 = a - n2
        return n2

list = [0]
num = int(input("Введите число: "))
for i in range(1, num + 1):
    list.append(Fibonacci(i))
    list.insert(0, NegaFibonacci(i))
print(list)