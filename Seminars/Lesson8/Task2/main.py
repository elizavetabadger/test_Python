# Волшебник, сидящий справа, что-то пробормотал себе под нос и метнул заклинание вдоль столешницы. Оно проделало в лаковом покрытии дымящуюся борозду и примерно на полпути встретилось с серебряными змеями заклинания Эффективного Гадосейства, выпущенного волшебником слева.
# Волшебники обменялись долгими, медленными взглядами – такими взглядами можно спокойно жарить каштаны.

# Напишите программу, определяющую более сильные заклинания, то есть числа, большие первого в строке и имеющие четную сумму последних трех разрядов.
# Формат ввода
# Вводятся строки, в которых числа записаны через %%.
# Формат вывода
# Из каждой строки вывести подходящие числа через v в порядке ввода.
# 13250%%20190 - 20190
# 1632%%21031%%4391%%10053%%5553 - 21031v10053
# 23958%%24074%%25637%%25737 - 25637

file_6 = open('res.txt', 'r', encoding='utf-8')
res_list = []
while True:
    line = file_6.readline().strip()
    if not line:
        break
    line_list = list(map(int, line.split('%%')))
    temp_list = []
    for i in range(1, len(line_list)):
        if line_list[i] > line_list[0]:
            sum = 0
            a = line_list[i]
            for j in range(3):
                sum += a % 10
                a //= 10
            if not sum % 2:
                temp_list.append(line_list[i])
    res_list.append(temp_list)
for el in res_list:
    if len(el) != 0:
        print(*el, sep='v')
    else:
        print()

file_6.close()

