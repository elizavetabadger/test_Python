# numbers = [0] * 5
# for index in range(5):
#     numbers [index] = int(input())
# print(max(numbers))

maxx = int(input())
for _ in range(4):
    n = int(input())
    if n > maxx:
        maxx = n
print(maxx)