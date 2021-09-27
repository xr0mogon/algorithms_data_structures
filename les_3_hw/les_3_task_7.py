"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
from random import randint

num = 10
my_arr = [randint(0, 100) for i in range(num)]
print('my_arr:', my_arr)

if my_arr[0] > my_arr[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, num):
    if my_arr[i] < my_arr[min1]:
        b = min1
        min1 = i
        if my_arr[b] < my_arr[min2]:
            min2 = b
    elif my_arr[i] < my_arr[min2]:
        min2 = i

print(f'min1(id:{min1+1}) = {my_arr[min1]}')
print(f'min2(id:{min2+1}) = {my_arr[min2]}')


# import random
#
# array = [random.randint(0, 100) for _ in range(30)]
# print(array)
# min = array[0]
# for i in array:
#     if i < min:
#         min = i
#         pos_min = array.index(min)
# min1 = min
# array.pop(pos_min)
# min2 = array[0]
# for i in array:
#     if i < min2:
#         min2 = i
# print(f'два наименьших элемента {min1}, {min2}')

# number_list = list(range(2, 100))
# small_list = list(range(2,10))
# for number in small_list:
#     result = []
#     for i, item in enumerate(number_list):
#         if item % number == 0:
#             result.append(number)
#     print(f'{len(result)} чисел из последовательности кратны цифре {number}')


# import random
#
# my_list = [random.randint(-10,10) for i in range(5)]
# print(my_list)
#
# my_min = my_list[0]
#
# for i in my_list:
#     if i < my_min:
#         my_min = i
# print(f"Первый наименьший элемент: {my_min}")
#
# my_list.remove(my_min)
# #print(my_list)
#
# my_min = my_list[0]
#
# for i in my_list:
#     if i < my_min:
#         my_min = i
# print(f"Второй наименьший элемент: {my_min}")
