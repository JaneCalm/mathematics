# 3. Задание (в программе)
# Напишите код на Python, реализующий построение графиков:
#    1. окружности,
#    2. эллипса,
#   3. гиперболы.

import matplotlib.pyplot as plt
import numpy as np
import math

R2 = 3
x = np.linspace(-2.0, 2.0, 100)
y = np.linspace(-2.0, 2.0, 100)
X, Y = np.meshgrid(x, y)
F = X ** 2 + Y ** 2 - R2
plt.contour(X, Y, F, [0])

a = 0.5
b = 1
F2 = (X ** 2 / a ** 2) + (Y ** 2 / b ** 2) - 1
plt.contour(X, Y, F2, [0])
plt.axis('equal')

F3 = (X ** 2 / a ** 2) - (Y ** 2 / b ** 2) - 1
plt.contour(X, Y, F3, [0])

plt.show()
