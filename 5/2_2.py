import matplotlib.pyplot as plt
import numpy as np

z = []
for i in range(10):
    x = np.random.rand(9)
    print(x)
    y = 0
    for k in x:
        y = y + int(k*10)
    z.append(y)
print (z)
num_bins = 10
n, bins, patches = plt.hist(z, num_bins)
plt.show()