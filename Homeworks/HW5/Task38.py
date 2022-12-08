# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Всё арпб бтадвыа получилось выоажо абв опдавь'

text_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, text.split()))
print(text_list)
