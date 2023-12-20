'''

The purpose of this file is for testing and playing around with matplotlib, numpy, and ML principles

'''

# Libraries that are used often in Machine Learning 

# This first one is matplotlib, it is used for plotting functions
import matplotlib.pyplot as plt
# This one is a math library that allows us to do various mathematical tasks
import numpy as np

# Create some input / output data
x = np.array([0.03, 0.19, 0.34, 0.46, 0.78, 0.81, 1.08, 1.18, 1.39, 1.60, 1.65, 1.90])
y = np.array([0.67, 0.85, 1.05, 1.0, 1.40, 1.5, 1.3, 1.54, 1.55, 1.68, 1.73, 1.6 ])

# Function to calculate the loss
def compute_loss(x,y,phi0,phi1):
  predicted_y = f(x, phi0, phi1)
  loss = np.sum(np.square(predicted_y-y))
  return loss

# Define 1D linear regression model
def f(x, phi0, phi1):
  y = phi0+x*phi1
  return y 

# Make a 2D grid of possible phi0 and phi1 values
phi0_mesh, phi1_mesh = np.meshgrid(np.arange(0.0,2.0,0.02), np.arange(-1.0,1.0,0.02))

# Make a 2D array for the losses
all_losses = np.zeros_like(phi1_mesh)

# Run throught each 2D combination of phi0, phi1 and compute loss
for indices,temp in np.ndenumerate(phi1_mesh):
    all_losses[indices] = compute_loss(x,y, phi0_mesh[indices], phi1_mesh[indices])

