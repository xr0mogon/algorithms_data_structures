"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться,
больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
"""
from random import randint

x = randint(0, 100)
# print(x)
t = 1
while t <= 10:
    print(f'Попытка № {t} из 10!')
    y = int(input('Отгадай число: '))
    if y > x:
        print('Меньше.')
    elif y < x:
        print('Больше.')
    elif y == x:
        print(f'Ты отгадал число c {t} попытки!')
        break
    t += 1

else:
    print(f'Лимит попыток исчерпан! Было загадано {x}.')
