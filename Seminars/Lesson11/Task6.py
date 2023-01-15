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
    
    def odd(self):
        res_list = []
        for item in self.list_obg:
            if item % 2:
                res_list.append(item)
        return res_list

x = Separator()
x.add_num(1)
x.add_num(2)
x.add_num(3)
x.add_num(4)
print(x.even())
print(x.odd())

# Напишите класс MinMaxWordFinder. Класс должен уметь анализировать текст и находить в нём слова наименьшей и наибольшей длины. Текст состоит из предложений, которые добавляются в обработку методом add_sentence. Метод shortest_words возвращает список самых коротких на данный момент слов, метод longest_words — самых длинных. Слова, возвращаемые методами shortest_words и longest_words, должны быть отсортированы по алфавиту.
# Если одно из самых коротких слов встретилось в исходных предложениях несколько раз, оно должно столько же раз повториться в списке самых коротких слов. Самые длинные слова наоборот должны входить в список без повторов.
