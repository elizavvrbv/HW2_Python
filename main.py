#Задание 14
# sum = 0
# for a in input():
#     if a.isdigit():
#         sum += int(a)
#
# print(sum)


#15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# lst, cum = [], 1
# N = int(input())
# for i in range (1, N+1):
#     cum = cum * i
#     lst.append(cum)
#
# print(*lst)

# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# n = int(input('Enter number: '))
# def sequence(n):
#     return [round((1 + 1 / x) ** x, 2) for x in range(1, n + 1)]
# 5
# print(sequence(n))
# print(round(sum(sequence(n))))


# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на введенных пользователем позициях.
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
print('Number of elements: ', get_numbers(numbers))

x = int(input('Enter  number of first element: '))
y = int(input('Enter number of second element: '))
x = int(input('Enter  position of first element: '))
y = int(input('Enter position of second element: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)

