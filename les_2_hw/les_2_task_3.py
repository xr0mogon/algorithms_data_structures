"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

n = int(input('Ведите число: '))
i = 0
while n > 0:
    i = i * 10 + n % 10
    n = n // 10
print(i)
