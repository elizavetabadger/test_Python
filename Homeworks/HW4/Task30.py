# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

from math import pi

d =  int(input('Укажите точность числа π (кол-во знаков после запятой): '))
print(f'Число π с заданной точностью {d} равно {round(pi, d)}')