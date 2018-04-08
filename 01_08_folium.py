#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def folium(b):
	theta = np.arange(0, 2*np.pi, 0.001)
	a = float(b * 0.5)
	r = (3*a*np.sin(theta)*np.cos(theta))/((np.sin(theta))**3+(np.cos(theta)**3))
	gc= colors[b]
	labels = 'a = '+str(a)
	ax.plot(theta, r, color = gc, label = labels)
	return

colors = ['purple', 'b', 'g', 'y', 'orange', 'r']
ax = plt.subplot(111, projection='polar')
for b in list(range(5)):
	folium(b)
ax.set_rmax(7)
ax.set_rticks([1,2,3,4,5,6,7])
ax.set_rlabel_position(-20)
ax.grid(True)
ax.set_title(
	r'Folum of Descarte $\frac{3a\sin{\theta}\cos{\theta}}{\sin^3{\theta}+\cos^3{\theta}}$')
legend = ax.legend(loc='lower left', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
for label in legend.get_texts():
	label.set_fontsize('large')
for label in legend.get_lines():
	label.set_linewidth(1.5)
plt.show()
