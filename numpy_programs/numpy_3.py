# Created by Srinivas Kadiyala at 27-03-2023

import numpy as np

# One Dimensional Array.
#numpy.ndarray = numpy n-dimensional array.

array1d_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(array1d_1))
print(array1d_1)
print("Array Shape: ", array1d_1.shape)
print("Dimensional: ", array1d_1.ndim)

array1d_2 = np.array(['Rama', 'Seetha', 'Anjaneya'])
print(type(array1d_2))
print(array1d_2)

array1d_3 = np.array(['Rama', 1])
print(type(array1d_3))
print(type(array1d_3[0]))
print(type(array1d_3[1]))
print(array1d_3)

# Two Dimensional Array
# Example: Rows and Columns - 2 rows, 5 columns

array2d_1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(type(array2d_1))
print(array2d_1)
print("Dimensional: ", array2d_1.ndim)


# 3 rows, 3 columns.
array2d_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(array2d_2))
print(array2d_2)
print("Array Shape: ", array2d_2.shape)
print("Dimensional: ", array2d_2.ndim)

# Three Dimensional Array.
array3d_1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(type(array3d_1))
print(array3d_1)
print("Array Shape: ", array3d_1.shape)
print("Array Dimensional: ", array3d_1.ndim)
# 1,2,3 - 1st row
# 4,5,6 - 2nd row
# Columns - 3
# Layers - 2
# Expected result: 2,2,3 - 2 layers, 2 rows , 3 columns

array3d_1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print(type(array3d_1))
print(array3d_1)
print("Array Shape: ", array3d_1.shape)
print("Array Dimensional: ", array3d_1.ndim)

# as the number of arrays increases, first value increases.
