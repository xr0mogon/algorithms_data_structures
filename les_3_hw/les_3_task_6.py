"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

num = 10
my_arr = [randint(0, 100) for i in range(num)]
print('my_arr:', my_arr)

min_id = 0
max_id = 0
for i in range(1, num):
    if my_arr[i] < my_arr[min_id]:
        min_id = i
    elif my_arr[i] > my_arr[max_id]:
        max_id = i
print(f'min(id:{min_id}) = {my_arr[min_id]}, max(id:{max_id}) = {my_arr[max_id]}')

if min_id > max_id:
    min_id, max_id = max_id, min_id

summ = 0
for i in range(min_id+1, max_id):
    summ += my_arr[i]

print(my_arr[min_id+1:max_id])
print(f'summa = {summ}')

# "_____________2 вариант_____________"
# from random import randint
#
# num = 15
# my_arr = [randint(0, 100) for i in range(num)]
#
# max_num = max(my_arr)
# ind_max_num = my_arr.index(max_num)
# min_num = min(my_arr)
# ind_min_num = my_arr.index(min_num)
#
# print('my_arr:', my_arr)
# print(f'max_num: {max_num}, index({my_arr.index(max_num)})')
# print(f'min_num: {min_num}, index({my_arr.index(min_num)})')
#
# if ind_max_num > ind_min_num:
#     summa = sum(my_arr[my_arr.index(min_num)+1:my_arr.index(max_num)])
#     print(f'summa {(my_arr[my_arr.index(min_num)+1:my_arr.index(max_num)])} = {summa}')
# else:
#     summa = sum(my_arr[my_arr.index(max_num)+1:my_arr.index(min_num)])
#     print(f'summa {(my_arr[my_arr.index(max_num)+1:my_arr.index(min_num)])} = {summa}')


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
#
# sum_ = 0
# if list(max_.keys())[0] < list(min_.keys())[0]:
#     for i in range (list(max_.keys())[0] + 1, list(min_.keys())[0]):
#         sum_ += new[i]
# else:
#     for i in range(list(min_.keys())[0] + 1, list(max_.keys())[0]):
#         sum_ += new[i]
# print(f'Сумма элементов между максимальным и минимальным значением в массиве равна: {sum_}')
