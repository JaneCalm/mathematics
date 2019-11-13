import matplotlib.pyplot as plt
import numpy as np
import itertools
import math

k, n = 0, 15
a = np.random.randint(0, 2 ,n)
b = np.random.randint(0, 2 ,n)
c = np.random.randint(0, 2 ,n)
d = np.random.randint(0, 2 ,n)
e = np.random.randint(0, 2 ,n)
x = a + b + c + d + e
k3 = 3
for i in range(0, n):
    if x[i] == k3:
        k += 1
#print(a, b, c, d)
#print(x)
print(k, n, k/n)


#ver = int(int(math.factorial(n))/(int(math.factorial(k))*(int(math.factorial(n-k))))*(1/(2*n)))
#print (ver)

def C(k2, n2):
    if k2 == 0 or k2 == n2:
        return 1
    else:
        return C(k2, n2 - 1) + C(k2 - 1, n2 - 1)
C2 = (C(k3,5))
print(C2)

P = C2*(1/(2**5))
print(P)
print("all")
