# 5. Задание (в программе)
#     1. Нарисуйте трехмерный график двух параллельных плоскостей.
#     2. Нарисуйте трехмерный график двух любых поверхностей второго порядка.

import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X2, Y2 = np.meshgrid(X, Y)
Z = 2*X2 + 5*Y2
ax.plot_wireframe(X2, Y2, Z)

Z2 = 2*X2 + 5*Y2 + 16
ax.plot_wireframe(X2, Y2, Z2)

r = 1
u = np.linspace(-2, 2, 200)
v = np.linspace(0, 2 * np.pi, 60)
[u, v] = np.meshgrid(u, v)

a = 3
b = 3
c = 3

X3 = a * np.cosh(u) * np.cos(v)
Y3 = b * np.cosh(u) * np.sin(v)
Z3 = c * np.sinh(u)

ax.plot_surface(X3, Y3, Z3)

x4 = np.linspace(-5, 5, 100)
z4 = np.linspace(-6, 6, 100)
Xc, Zc = np.meshgrid(x4, z4)
Yc = np.sqrt(1-Xc**2)

ax.plot_surface(Xc, Yc, Zc)


plt.show()