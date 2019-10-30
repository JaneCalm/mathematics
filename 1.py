# 4. Задание (в программе):
# Постройте на одном графике две кривые y(x)
# для функции двух переменной y(k,x)=cos(k∙x),
# взяв для одной кривой значение k=1,
# а для другой – любое другое k, не равное 1.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20)
k = 1
plt.plot(x, np.cos(k*x))
k = 2
plt.plot(x, np.cos(k*x))
plt.show()
