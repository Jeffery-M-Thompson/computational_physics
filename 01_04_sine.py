#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4*np.pi, 0.001)
plt.plot(x, (np.sin(x)))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine Function")
plt.show()