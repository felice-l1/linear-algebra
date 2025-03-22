# 2D_Data_Starter
# Basic plotting of 2D data.

# Import the matplotlib package and alias the pyplot module 
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np

# Create the plot object
fig, ax = plt.subplots()

# Set the viewing window in the plot from -50 to 50  in both directions
ax.set_xlim(-50,50)
ax.set_ylim(-50,50)

# Read in the data
# Data format: x,y,

xdata = []
ydata = []

f = open("2D_data.txt")
data = f.readlines()
f.close()

# Parse the data into lists of x's and y's

for i in range(len(data)):
  datapoint = data[i].split(',')
  xdata.append(float(datapoint[0]))
  ydata.append(float(datapoint[1]))
  

# Here we define the set of x- and y-coordinates beforehand
# The 'ro' option yields red unconnected dots

plt.plot(xdata,ydata, 'ro')

# linear regression line using linear algebra
ones_array = np.ones(len(xdata))
xnumpy = np.asarray(xdata)
ynumpy = np.asarray(ydata)
M = np.stack((ones_array, xnumpy), axis = 1)
# print(M)
# print(M.transpose())
x = np.linalg.inv(M.transpose()@M)@M.transpose()@ynumpy
plt.axline((x[0], 0), slope=x[1], c="blue")

# linear regression line using matplotlib
m, b = np.polyfit(xdata, ydata, 1)
line1 = plt.axline((b, 0), slope=m, dashes=[2, 2], c = "red")


# This plots the line from (0,5) to (20,1), i.e. the line y = -0.2x + 5 
# plt.plot([-25,25], [-50,50],'b')

# This shows the object (Must ctrl-c out of this in the console)
# Commented out because this does not work in Github Codespaces
plt.show() 

# Save plot to output.png
# plt.savefig('2D_Data_output.png')
