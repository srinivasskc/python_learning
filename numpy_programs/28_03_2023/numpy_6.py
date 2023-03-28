# Created by Srinivas Kadiyala at 28-03-2023
import numpy as np

# Numpy Arrays are classified as Homogeneous Data Structures because they store elements of the same type.

array1 = np.array([1, 2, 3, 4, 5, 6])
print("Print Type of Array: ", type(array1))

print("Print Type of Array List Data: ", array1.dtype)
print(array1)

array2 = array1*2
print("Array1 Multiply by 2: ", array2)
print("Print Type of Array List Data: ", array2.dtype)
