# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial (number, count = 1):
    for i in range(1, number + 1):
        count *= i
    return count

n = int(input("Введите число: "))
print(f"Факториал чисел от 1 до {n} = ", end = "")


for i in range(1, n + 1):
    if i == n: 
        print(f"{factorial(i)}")
    else:
        print(f"{factorial(i)}", end = ", ")






# n = int(input("Введите число: "))

# # f = 1
# # for i in range(N):
# #     i = i + 1
# #     f = i * f
    
# #     print(f, end=" ")