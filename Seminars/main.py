import random

# n = int(input("введи число  "))
# mult = 1
# some_list =[random.randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('file_test123.txt', 'w+', encoding="utf-8") as file:
#     count = random.randint(1, n)
#     for _ in range(count):
#         file.writelines(f"{random.randint(0, n - 1)}" + "\n")
#     file.seek(0, 0)
#     list_index = file.read().splitlines()
#     for index in list_index:
#         mult = mult * some_list[int(index)]
# print(mult)

#1. ввести кол-во строк, потом строки. Строки должны записаться в текстовый файл.
# После вводим число, если есть число в файле, то написать ДА

# num = int(input("кол-во строк = "))
# with open('file.txt', 'w+', encoding='utf-8') as file:
#     for _ in range(num):
#         file.writelines(f'{input("введи стрoку  ")}' + '\n')
#     file.seek(0,0)
#     x = input("цифра которую ищем = ")
#     str_list = file.read().splitlines()
#     flag = False
#     count = 0
#     for row in str_list:
#         if x in row:
#             print(f'искомая цифра есть и находиться в строке №   {count}')
#             flag = True
#             break
#         count+=1
# print('end')

def fun(month, language):
    dict1 = {"ru": ['январь', 'февраль','март','апрель','май'],
             "en": ["1",'12','123']}
    
    return dict1[language][month]
print(fun(0, "en"))


