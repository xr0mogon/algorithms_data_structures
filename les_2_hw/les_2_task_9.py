"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

num = int(input('Введи число: '))
max_1 = 0
max_2 = 0
while num != 0:
    n = num
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    if sum > max_1:
        max_1 = sum
        max_2 = n
    print('\tНоль(0) для выхода')
    num = int(input('Введи число: '))
print(f'Число {max_2} имеет наибольшую сумму цифр: {max_1}')
