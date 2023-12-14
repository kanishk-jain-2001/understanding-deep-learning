import matplotlib.pyplot as plt
import numpy as np

# # Define a linear function with just one input, x
# def linear_function_1D(x,beta,omega):
#   y = omega*x+beta
#   return y


# # Plot the 1D linear function

# # Define an array of x values from 0 to 10 with increments of 0.01
# # https://numpy.org/doc/stable/reference/generated/numpy.arange.html

# x = np.arange(0.0,10.0, 0.01)
# x1 = np.arange (0.0,10.0, 0.01)

# # Compute y using the function you filled in above
# beta = 10.0; omega = -2.0
# y = linear_function_1D(x,beta,omega)

# beta1=0; omega1 = 2.0 
# y1 = linear_function_1D(x1, beta1, omega1)

# # Plot this function
# fig, ax = plt.subplots() 
# ax.plot(x,y,'r-')
# ax.plot(x1,y1,'b-')
# ax.set_ylim([0,10]); ax.set_xlim([0,10])
# ax.set_xlabel('x'); ax.set_ylabel('y')
# plt.show()

# Make 2D array of x and y points
x1 = np.arange(0.0, 10.0, 2)
x2 = np.arange(10.0, 20.0, 2)
x1,x2 = np.meshgrid(x1,x2) 


print(x1)
print(x2)