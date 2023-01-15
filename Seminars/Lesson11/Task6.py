# Напишите класс OddEvenSeparator, в который можно добавлять числа, получая потом отдельно чётные и нечётные. 
# Числа добавляются в объект с помощью метода add_number. Методы even и odd должны возвращать списки чётных и нечётных чисел соответственно. 
# Числа в списке должны идти в том же порядке, что и при добавлении в объект.

class Separator:

    def __init__(self):
        self.list_obg = []

    def add_num(self, num: int):
        self.list_obg.append(num)

    def even(self):
        res_list = []
        for item in self.list_obg:
            if not item % 2:
                res_list.append(item)
        return res_list
    # return list(filter(lambda x: x % 2, self.list_obg)) # x принимает выражение     
    
    def odd(self):
        # res_list = []
        # for item in self.list_obg:
        #     if item % 2:
        #         res_list.append(item)
        # return res_list
        return list(filter(lambda x: x % 2, self.list_obg))

x = Separator()
x.add_num(1)
x.add_num(2)
x.add_num(3)
x.add_num(4)
print(x.even())
print(x.odd())