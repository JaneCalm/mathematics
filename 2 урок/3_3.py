# 3. Задание (в программе)
#   1. Напишите код, который будет переводить полярные координаты в декартовы.
#  2. Напишите код, который будет рисовать график окружности в полярных координатах.
# 3. Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах.
#
import matplotlib.pyplot as plt
import numpy as np
import math
plt.subplot(111, polar=True)


def polar2cart(r, phi):
    x1 = r*math.cos(phi)
    y1 = r*math.sin(phi)
    return x1, y1


print(polar2cart(10, 20))


R2 = 6
x = np.linspace(-5.0, 5.0, 100)
y = np.linspace(-5.0, 5.0, 100)
X, Y = np.meshgrid(x, y)
F = X ** 2 + Y ** 2 - R2
plt.contour(X, Y, F, [0])

x2 = np.linspace(2, 5, 100)
y2 = x*2
plt.plot(x2, y2)

plt.xlabel('x')
plt.ylabel('y')
plt.show()