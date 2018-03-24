#!/usr/bin/env python3

import numpy as np
import sys

sp = np.float32(1.0)
spunit = np.float32(0.000001)
dp = np.float64(1.0)
dpunit = np.float64(0.000001)

for i in range (0,1000000):
    sp = sp + spunit
    dp = dp + dpunit

print('Single Precision {0}  Double Precision {1}'.format(sp, dp))