"""
4. Найти сумму n элементов следующего
ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите количество элементов: '))
el = 1
sum = 0
for i in range(n):
    sum += el
    el /= (-2)
    print('Элемент последовательности: ', el)
print('Сумма элементов последовательности равна: ', sum)