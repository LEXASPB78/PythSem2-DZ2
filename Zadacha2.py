# 2. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# Пример:
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

N = int(input('Введите число '))

f = 1
for i in range(N):
    i = i + 1
    f = i * f
    
    print(f, end=" ")

