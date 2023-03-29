# Created by Srinivas Kadiyala at 29-03-2023
import numpy as np

# Convert Float Array to Integer array

array1_f = np.array([1.2, 2.2, 3.8])
print(array1_f)
print(array1_f.dtype)

array1_i = array1_f.astype('i')
print(array1_i)
print(array1_i.dtype)