"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
"""
Задаём: num, min_el, max_el
Создаём случайный массив: my_arr
перебор (i) последовательности range(num). (перебираем по индексам)
    Поиск индексов максимума и минимума. 
Присвоить буферной переменной значение минимума.
Записать по индексу минимума максимум массива.
Записать по индексу максимума значение, хранимое в буферной переменной.
"""

from random import randint

num = 15
min_el = 0
max_el = 0
my_arr = [randint(0, 100) for i in range(num)]

print(my_arr)

for i in range(num):
    if my_arr[i] < my_arr[min_el]:
        min_el = i
    elif my_arr[i] > my_arr[max_el]:
        max_el = i

print('\n', f'min_el(index:{min_el}) = {my_arr[min_el]}, max_el(index:{max_el}) = {my_arr[max_el]}', '\n')

temp = my_arr[min_el]
my_arr[min_el] = my_arr[max_el]
my_arr[max_el] = temp

print(my_arr)

# import random
#
# array = [random.randint(0, 100) for _ in range(20)]
# print(f'Исходный массив {array}')
# min = array[0]
# max = array[0]
# for i in array:
#     if i < min:
#         min = i
#         pos_min = array.index(min)
#     if i > max:
#         max = i
#         pos_max = array.index(max)
# print(f'Минимальный элемент массива = {min}, максимальный = {max}')
# array[pos_min] = max
# array[pos_max] = min
# print(f'Массив с заменой {array}')

# import random
# new = [random.randint(-100, 100) for _ in range(20)]
# print(f'Исходный массив: {new}')
# max_ = {0 : new[0]}
# min_ = {0 : new[0]}
# for i, item in enumerate(new):
#     if item >= list(max_.values())[0]:
#         max_ = {i: item}
#     if item <= list(min_.values())[0]:
#         min_ = {i: item}
# print(f'Индекс и значение максимального элемента: {max_}')
# print(f'Индекс и значение минимального элемента: {min_}')
# new[list(max_.keys())[0]] = list(min_.values())[0]
# new[list(min_.keys())[0]] = list(max_.values())[0]
# print(f'Измененный массив: {new}')