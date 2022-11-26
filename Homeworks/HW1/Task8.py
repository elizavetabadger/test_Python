# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def find_coordinate_plane(x: int, y: int):
    if x == 0 and y == 0:
        return "Центр оси координат"
    if x == 0:
        return "x"
    if y == 0:
        return "y"
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3

x, y = map(int, input().split(" "))

print(find_coordinate_plane(x, y))