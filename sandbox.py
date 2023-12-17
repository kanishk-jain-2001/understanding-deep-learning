'''

The purpose of this file is for testing and playing around with matplotlib, numpy, and ML principles

'''


# Libraries that are used often in Machine Learning 

# This first one is matplotlib, it is used for plotting functions
import matplotlib.pyplot as plt
# This one is a math library that allows us to do various mathematical tasks
import numpy as np

x1 = np.arange(0,10,.1)
x2= np.arange(0,10,.1)

x1,x2 = np.meshgrid(x1,x2)

print(x1)
print(x2)