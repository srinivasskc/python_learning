# Created by Srinivas Kadiyala at 29-03-2023
import numpy as np

# Convert Integer array to Float Array

array1_i = np.array([1, 3, 5])
print(array1_i)
print(array1_i.dtype)

array1_f = array1_i.astype('f')
print(array1_f)
print(array1_f.dtype)