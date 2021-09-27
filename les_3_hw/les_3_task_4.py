"""
4. Определить, какое число в массиве встречается чаще всего.
"""
"""
В цикле берем элементы массива и сравниваем их с элементами, стоящими уже после.
    в теле цикла присваиваем count = 1. 
    далее перебираем элементы стоящие после текущего элемента.
        если занчения совпадают, то count += 1.
    после того, как посчитано количество раз, какое встречается элемент, переменная сравнивается c count_max.
    Если count больше, то значения count_max и n перезаписываются 
"""

from random import randint

num = 15
my_arr = [randint(0, num - 5) for i in range(num)]
print(my_arr)

n = my_arr[0]  # самый встречаемый элемент
count_max = 1  # количество раз, которое он встречается
for i in range(num - 1):  # Последний элемент не с чем сравнивать, поэтому цикл идет до предпоследнего элемента.
    count = 1
    # print('i', i)
    for k in range(i + 1, num):  # Сравниваем i с последующими элементами
        # print('\tk',k)
        # print('my_arr[i]', my_arr[i], 'my_arr[k]', my_arr[k])
        if my_arr[i] == my_arr[k]:
            count += 1
    if count > count_max:
        count_max = count
        n = my_arr[i]

if count_max > 1:
    print(f'Число {n} встречается {count_max} раз(а).')
else:
    print('Повторов нет')

# # "2 Вариант"
#
# diction = {}
# for item in my_arr:
#     if item in diction.keys():
#         diction[item] += 1
#     else:
#         diction[item] = 1
# print(diction)

# "3 Вариант"
# import random
#
# array = [random.randint(0, 12) for _ in range(10)]
# print(f'Исходный массив {array}')
#
# # если без использования statistics.mode()
#
# max_count = 0
# for i in array:
#     if array.count(i) > max_count:
#         max_count = array.count(i)
#         max = i
# print(f'Число {max} встречается {max_count} раз')
