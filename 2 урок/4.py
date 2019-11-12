# 4. Задание (в программе)
#    1. Решите систему уравнений:
# y = x2 – 1
# exp(x) + x∙(1 – y) = 1
#
from scipy.optimize import fsolve
import math


def func2(x):
    out = [x[1] - x[0] ** 2 + 1, math.exp(x[0]) + x[0] * (1 - x[1]) - 1]
    return out


print(fsolve(func2, [-1.5, 1.5]))

