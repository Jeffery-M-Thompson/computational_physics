#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

a = 1.0 
theta = np.arange(0, 2*np.pi, 0.001)
x = 2*a*np.cos(theta)+a*np.cos(2*theta)
y = 2*a*np.sin(theta)-a*np.sin(2*theta)
plt.plot(x, y)
plt.title("Deltoid")
plt.show()
