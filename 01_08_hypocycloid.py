#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def hypocycloid(b):
	theta = np.arange(0, 2*np.pi, 0.001)
	a = float(b * 0.5 + 0.5)
	
	gc= colors[b]
	labels = 'a = '+str(a)
	x = a * (np.cos(theta))**3
	y = a * (np.sin(theta))**3
	ax.plot(x, y, color = gc, label = labels)
	return

colors = ['purple', 'b', 'g', 'y', 'orange', 'r']
ax = plt.subplot(111)
for b in list(range(5)):
	hypocycloid(b)
ax.set_title(
	r'Hypocycloid $x^{2/3}+y^{2/3}=a^{2/3}$')
legend = ax.legend(loc='lower left', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
for label in legend.get_texts():
	label.set_fontsize('large')
for label in legend.get_lines():
	label.set_linewidth(1.5)
plt.show()
