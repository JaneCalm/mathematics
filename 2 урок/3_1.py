# 1. Задание (в программе)
# Нарисуйте график функции:
# y(x) = k∙cos(x – a) + b
# для некоторых (2-3 различных) значений параметров k, a, b


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20)


def f(k, a, b):
    y = k * np.cos(x - a) + b
    return y


plt.plot(x, f(3, 5, 7))
plt.plot(x, f(8, 10, 11))

plt.show()
