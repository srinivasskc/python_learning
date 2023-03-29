# Created by Srinivas Kadiyala at 29-03-2023
import numpy as np

# Feature: Defining the Data Type

array1 = np.array([1, 2, 3, 4, 5], dtype="i2")
# i2 = Integer data type of 2 Bytes.

print(array1)
print(type(array1))
print(array1.dtype)


array1 = np.array([1, 2, 3, 4, 5], dtype="i4")
print(array1)
print(type(array1))
print(array1.dtype)
