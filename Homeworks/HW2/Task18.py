# Реализуйте алгоритм перемешивания списка.

import random
list = [random.randint(0,10) for i in range(random.randint(0,15))]
print(f"Наш список: {list}")
random.shuffle(list)
print(f"Перемешанный список: {list}")
