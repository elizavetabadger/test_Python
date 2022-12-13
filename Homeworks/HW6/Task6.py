# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def convert(s: str):
  result = list
  last_sym = None
  count = 0
  for sym in (list(s) + [None]):
      if last_sym and sym != last_sym:
          if count == 1:
              result.append(last_sym)
          else:
              result.append(last_sym + str(count))
          count = 1
          last_sym = sym
      else:
          count += 1
  return ''.join(result)

n = input()
print(convert(n))