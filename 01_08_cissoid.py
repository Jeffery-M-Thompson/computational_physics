#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(-np.pi, np.pi, 0.001)
r = np.sin(theta)*np.tan(theta)
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(10)
ax.set_rticks([0.5,1,1.5,2])
ax.set_rlabel_position(-22.5)
ax.grid(True)
ax.set_title("Cissoid of Diocles")
plt.show()