#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

plt.plot((0, 0), (-10, 10), 'k-')
plt.plot((-10, 10), (0, 0), 'k-')
plt.axis('scaled')
plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.title('Plus sign.')
plt.show()