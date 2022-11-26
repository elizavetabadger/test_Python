# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [1, 0]:
    for y in [1, 0]:
        for z in [1, 0]:
            left_part = x or y or z
            right_part = not x and not y and not z

            result = not left_part == right_part
            res = {True: "истиной", False: "ложью"}    
            print(f"Для x = {bool(x)}, y = {bool(y)}, z = {bool(z)} выражение является {res[result]}")