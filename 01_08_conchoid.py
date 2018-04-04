#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(-np.pi, np.pi, 0.001)
r1 = 1.0/np.sin(theta)+2.5
r2 = 1.0/np.sin(theta)-2.5
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r1)
ax.plot(theta, r2)
ax.set_rmax(5)
ax.set_rticks([0.5,1,1.5,2,2.5,3, 3.5, 4, 4.5, 5])
ax.set_rlabel_position(10)
ax.grid(True)
ax.set_title("Conchoid of Nicomedes")
plt.show()
