#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def conchoid(b):
	theta = np.arange(-np.pi, np.pi, 0.001)
	a = float(b * 0.5)
	r1 = 1.0/np.sin(theta)+a
	r2 = 1.0/np.sin(theta)-a
	gc= colors[b]
	labels = str(a)
	ax.plot(theta, r1, color = gc, label = labels)
	ax.plot(theta, r2, color = gc)
	return

colors = ['purple', 'b', 'g', 'y', 'orange', 'r']
ax = plt.subplot(111, projection='polar')
for b in list(range(6)):
	conchoid(b)
ax.set_rmax(3)
ax.set_rticks([0.5,1,1.5,2,2.5,3])
ax.set_rlabel_position(-20)
ax.grid(True)
ax.set_title("Conchoid of Nicomedes")
legend = ax.legend(loc='lower left', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
for label in legend.get_texts():
	label.set_fontsize('large')
for label in legend.get_lines():
	label.set_linewidth(1.5)
plt.show()
