# Created by Srinivas Kadiyala at 28-03-2023

# Covered: Array Range, Array Shape, Array Dimension, Reshaping the Array


import numpy as np

# Exercise - 2

array1 = np.arange(12)
print(type(array1))
print(array1)
print("Shape of array1: ", array1.shape)
print("Dimesion of array1: ", array1.ndim)

# Reshaping the array of 1-D to 3-D

array1_reshape = array1.reshape(2, 2, 3)
print(type(array1_reshape))
print(array1_reshape)
print("Shape of Array1: ", array1_reshape.shape)
print("Shape of Array1: ", array1_reshape.ndim)

