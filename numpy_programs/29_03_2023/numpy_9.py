# Created by Srinivas Kadiyala at 29-03-2023
import numpy as np

# Passing the character to numerical array

array1 = np.array([1, 2, 3, 4, 'a'], dtype="i2")

print(array1)
print(array1.dtype)

# As data type is integer, it is invalidating the character 'a'

