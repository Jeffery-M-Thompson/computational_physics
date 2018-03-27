#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4*np.pi, 0.001)
plt.plot(x, (np.sin(x)), label="Sine")
plt.plot(x, (np.cos(x)), label="Cosine")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine and Cosine Functions")
# Place a legend to the right of this smaller subplot.
plt.legend()
plt.show()