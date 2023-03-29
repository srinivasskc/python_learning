# Created by Srinivas Kadiyala at 28-03-2023

# Feature: Unicode String - array with numbers and characters

import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, "a"])
print(array1)
print(type(array1))
print(array1.dtype)
# <U11 means Unicode and 11 -  number of elements that it can hold


array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "a", "b"])
print(array2)
print(type(array2))
print(array2.dtype)
# <U11 means Unicode and 11 -  number of elements that it can hold

"""
We cannot multiply the unicode string.
"""
# print(array2*2)

