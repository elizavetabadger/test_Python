# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import random

n = int(input("Введите количество элементов списка "))
list = [random.randint(-n, n) for _ in range (n)]
new_list = []

for i in range(len(list)):
    while i < len(list)/2 and n > len(list)/2:
        n = n - 1
        k = list[i] * list[n]
        new_list.append(k)
        i += 1

print(list)
print(new_list)