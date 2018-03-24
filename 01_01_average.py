#!/usr/bin/env python3

import numpy as np
import sys

# Print out the instructions for the program.

def instructions():
    print ('Enter the numbers to be averaged individually.')
    print ('When you are done enter the letter x.')

# Input the data and check that it is good numeric data

def get_data():
    data=np.array([])
    cont = True
    while cont:
        In = input(' ')
        try:
            number = [np.float(In)]
            data = np.append(data, number)
        except:
            try:
                if str(In) == 'x':
                    cont = False
                else:
                    print('Invalid input ignored!')
            except:
                print('Invalid Input')
    return data

# Calculate the average and display the resutls.

def display_results(data):
    average = np.mean(data)
    number = data.size
    print('There are {0} values with an average of {1}.'.format(number, average))
    return

# The main program this calls the sub parts

def main():
    data=np.array([])
    instructions()
    data=get_data()
    display_results(data)

main()
