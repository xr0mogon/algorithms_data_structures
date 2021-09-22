# 2. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

# x1 = 4.3
# y1 = -1.2
# x2 = -8.5
# y2 = 4

print('Введите координаты точки A(x1;y1)')
x1 = float(input('\tx1 = '))
y1 = float(input('\ty1 = '))
print('Введите координаты точки B(x2;y2)')
x2 = float(input('\tx2 = '))
y2 = float(input('\ty2 = '))
print(f'Уравнение прямой, проходящей через точки A({x1};{y1}) B({x2};{y2}):')
# Вычислить значение k по формуле:
k = (y1 - y2) / (x1 - x2)
# Вычислить значение b по формуле:
b = y2 - k * x2
print(f'y = {k:.2f}x + {b:.2f}')
