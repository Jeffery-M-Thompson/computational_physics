#!/usr/bin/env python3

import numpy as np
import sys



def instructions():
	print ('Enter the numbers to be averaged individually.')
	print ('When you are done enter the letter x.')

def get_data(data):
	cont = True
	while cont:
		In = input(' ')
		try:
			number = [float(In)]
			data = np.append(data, [In])
		except:
			try:
				if str(In) == 'x':
					cont = False
				else:
					print('Invalid input ignored!')
			except:
				print('Invalid Input')
	return data
		
def main():
	data = np.array([])
	instructions()
	data=get_data(data)
	average = np.mean(data)
	number = data.size
	print ('There are {0} values with an average of {1}.').format(number, average)
	
main()
