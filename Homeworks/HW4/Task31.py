#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))
if n == 1:
    print(1)
list = []
for i in range(1, n + 1):
    if n % i == 0:
        for k in range(2, i // 2 + 1):
            if i % k == 0:
                break
        else:
            list.append(i)
print(f"Список простых множителей {list}")