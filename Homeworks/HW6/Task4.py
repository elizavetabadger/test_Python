# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
new_list = list(map(int, input("Введите числа: ").split()))
print(new_list)
print(list([a * b for a, b in zip(new_list[0 : math.ceil(len(new_list) / 2)], new_list[::-1])]))