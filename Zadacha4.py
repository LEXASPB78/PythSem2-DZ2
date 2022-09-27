# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Пример:
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Количество элементов: ', get_numbers(numbers))

x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Множество элементов: {numbers[x -1]} * {numbers[y -1]} =', mult)