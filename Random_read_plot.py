# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:16:02 2021

@author: David
"""

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

#x, the array of random numbers, will now be read from an exisitng .txt file instead of being generated
x = np.loadtxt("random_numbers.txt")
print(x)

# create histogram of our data
plt.figure()
n, bins, patches = plt.hist(x, 50, density=True, color='#17b9de', alpha=0.75)
# plot formating options
plt.xlabel('Numbers')
plt.ylabel('Probability')
plt.title('Uniform Random Number Distribution')
plt.grid(True)

plt.figure()
n, bins, patches = plt.hist(x, 50, density=False, color='#17de1b', alpha=0.75)
plt.xlabel('Numbers')
plt.ylabel('Counts')
plt.title('Uniform Random Number Distribution')
plt.grid(True)
