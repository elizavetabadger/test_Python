# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

def compress(numbers) -> str:
    if not numbers:
        return ''
        
    numbers_ = sorted(numbers)
    groups = []
    last_group_start = None
    last_group_end = None

    for n in numbers_:
        if last_group_end is None:
            last_group_start = n
            last_group_end = n
        elif last_group_end == n-1:
            last_group_end = n
        else:
            groups.append(repr(last_group_start, last_group_end))
            last_group_start = n
            last_group_end = n
    else:
        groups.append(repr(last_group_start, last_group_end))
    return ','.join(groups)

def repr(group_start, group_end) -> str:
    if last_group_start == last_group_end:
        return str(last_group_end)

    return f'{last_group_start}-{last_group_end}'


# list = list(map(int, input("Введите числа через пробел: ").split()))
list = [1,4,5,2,3,9,8,11,0]
print(repr(list))
print(compress(list))