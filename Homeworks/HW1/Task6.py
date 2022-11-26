# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

#is_weekend = {
#    1: "no", 
#    2: "no",
#    3: "no",
#    4: "no",
#    5: "no",
#    6: "yes",
#    7: "yes"}

#print(is_weekend.get(int(input()), "Нет такого дня в неделе"))

def is_it_weekend(day: int) -> str:
    if day < 1 or day > 7:
        return "введен неправильный день недели"

    if day >= 6:
        return "да"
    else:
        return "нет"

print(is_it_weekend(int(input())))