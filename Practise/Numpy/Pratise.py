import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   # for data visualization

a = np.zeros(10)  # create an array of 10 zeros
print(a)

a_2d = np.zeros((5, 4))  # create a 2D array of 5x4 zeros
print(a_2d)

a_3d = np.zeros((5, 4, 3))  # create a 3D array of 5x4x3 zeros
print(a_3d)

b = np.random.random(10) # create an array of 10 random numbers
print(b)

b_2d = np.random.random((5, 4)) # create a 2D array of 5x4 random numbers
print(b_2d)

b_3d = np.random.random((5, 4, 3)) # create a 3D array of 5x4x3 random numbers
print(b_3d)

b_4d = np.random.random((5, 4, 3, 2)) # create a 4D array of 5x4x3x2 random numbers
print(b_4d)

plt.scatter (np.arange(10,23), np.arange(10,23)) # plot the random numbers
plt.show()

c = np.random.randint(0, 10, 10)
print(c)

d = np.arange(10)
print(d)

e = np.linspace(0, 10, 100)
print(e)

f = np.logspace(0, 10, 100) # create an array of 100 numbers from 0 to 10 in log scale
print(f)    # print the array       
plt.plot(f) # plot the array
plt.show()  # display the plot

g = np.random.randint(0, 10, 10)
print(g)
print(g[2]) # print the 3rd element of the array
print(g[2:5]) # print the 3rd to 5th elements of the array
print(g[:5]) # print the first 5 elements of the array


list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],      
]

array = np.array(list)  # convert the list to a numpy array
print(array)        # print the array
print(array.shape)  # print the shape of the array
print(array.size)   # print the size of the array
print(array.ndim)   # print the number of dimensions of the array   
print(np.flatten(array)) # flatten the array
print(array.flatten()) # flatten the array
print(array.T)      # transpose the array