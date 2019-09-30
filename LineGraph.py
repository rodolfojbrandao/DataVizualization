import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Num = 200
fx = []
gx = []
w = []
x = []
for i in range(Num):
    a = -2.5 + i / 100
    # print(a)
    x.append(a)
    if (((a + 1) >= 0) and (a != 0)):
        w.append(a)
        # print("terra")
        g = np.sqrt(a + 1) / abs(a)
    else:
        # print("ar")
        g = 0
    gx.append(g)
    if ((a + 2) >= 0 and a != 2):
        f = np.sqrt(a + 2) / abs(a - 2)
    else:
        f = 0
    fx.append(f)

plt.plot(x, fx)
plt.plot(x, gx)
plt.show()