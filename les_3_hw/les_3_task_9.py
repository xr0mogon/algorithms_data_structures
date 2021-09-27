"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint

row = 4  # строки
num = 5  # столбцы
matrix = []
for i in range(num):
    temp = []
    for j in range(row):
        n = randint(0, 100)
        temp.append(n)
    matrix.append(temp)

for i in matrix:
    print(i)

max_min_el = -1
for j in range(row):
    min_el = 100
    for i in range(num):
        if matrix[i][j] < min_el:
            min_el = matrix[i][j]
    if min_el > max_min_el:
        max_min_el = min_el

print(f'Максимальный элемент среди минимальных: {max_min_el}')
