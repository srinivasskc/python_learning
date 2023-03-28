# Created by Srinivas Kadiyala at 28-03-2023
import numpy as np

# Exercise - 1

# Range of Array
array_range = np.arange(24)
print(type(array_range))
print("Print Array_Range: ", array_range)
print("Shape of Array: ", array_range.shape)
print("Dimension of Array: ", array_range.ndim)

# Reshaping an Array from Single Dimesional Array to 3-D Array
array_shape = array_range.reshape(3, 2, 4)
print(type(array_shape))
print("Print Array after Reshape: ", array_shape)
print("Shape of Array: ", array_shape.shape)
print("Dimension of Array: ", array_shape.ndim)







