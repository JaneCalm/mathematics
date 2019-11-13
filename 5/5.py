import matplotlib.pyplot as plt
import numpy as np
import itertools
import math

#x = np.linspace(-2, 3, 21)
#plt.plot(x, x**2 -1, 'ro-')
#plt.ylim(-1,5)


n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
c = np.corrcoef(x, y)
print(c)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

def mean(x2):
    sumo = 0.0
    for i in x2:
         sumo += i
    return sumo / len(x2)

def sampleStandardDeviation(x3):
    suma = 0.0
    for i in x3:
         suma += (i - mean(x3))**2
    return math.sqrt(suma/(len(x3)-1))

def pearson(x4,y4):
    scorex = []
    scorey = []

    for i in x4:
        scorex.append((i - mean(x4))/sampleStandardDeviation(x4))

    for j in y4:
        scorey.append((j - mean(y4))/sampleStandardDeviation(y4))
    return (sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)
print (pearson(x,y))

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a,b)
print(a1, b1)
plt.grid(True)

plt.plot([0,1], [b, a+b])
plt.show()
