# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('text_RLE.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст: '))
with open('text_RLE.txt', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()

print(my_text)


def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''
    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding


text_compression = rle_encode(my_text)

with open('text_compression_RLE.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)

# def press(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             ind = 0
#             count = 1
#             while ind < len(inp_str) - 1:
#                 if inp_str[ind] == inp_str[ind + 1]:
#                     count += 1
#                 else:
#                     if count == 1:
#                         res.write(inp_str[ind])
#                     else:
#                         res.write(str(count) + inp_str[ind])
#                     count = 1
#                 ind += 1

# def depress(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             count = ''
#             for letter in inp_str:
#                 if letter.isdigit():
#                     count += letter
#                 else:
#                     if not count:
#                         res.write(int(count) * letter)
#                     else:
#                         res.write(letter)
#                     count = ''
