"""
7. Написать программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""
num = int(input('Введите n: '))


def func_1():
    sum_num = 0
    for i in range(1, num + 1):
        sum_num += i
    print(f'n = {num}, 1+2+...+n = {sum_num}')


def func_2():
    sum_num2 = int(num * (num + 1) / 2)
    print(f'n = {num}, n(n+1)/2 = ', sum_num2)


if func_1() == func_2():
    print(f'Равенство верно')
else:
    print(f'Равенство не верно')
