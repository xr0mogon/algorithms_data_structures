"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import randint

num = 15
my_arr = [randint(-100, 100) for i in range(num)]

print(my_arr)

max_min = 0  # максимальный отрицательный
index = -1  # индекс max_min

while max_min < num:
    if my_arr[max_min] < 0 and index == -1:
        index = max_min
    elif my_arr[max_min] < 0 and my_arr[max_min] > my_arr[index]:
        index = max_min
    max_min += 1
print('max_min (index:', index, ') =', my_arr[index])

# 2 Вариант

num = float('-inf')
index = -1
for i, item in enumerate(my_arr):
    if 0 > item > num:
        num = item
        index = i
print(f'Число {num} на позиции {index}')