import matplotlib.pyplot as plt
import numpy as np

for i in range(0, 5):
    a = input()
    x = int(np.random.uniform(0, 38))
    if x == 0:
        print("zero", x)
    elif x%2:
        print("black", x)
    else:
        print("red", x)