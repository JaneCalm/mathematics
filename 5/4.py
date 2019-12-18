import matplotlib.pyplot as plt
import numpy as np
import itertools
import math

#for p in itertools.product("0234",repeat=5):
#    print(''.join(p))

#for p in itertools.permutations("012378",5):
 #  print(''.join(str(x)  for x in p))

for p in itertools.combinations("1236",3):
    print(''.join(p))