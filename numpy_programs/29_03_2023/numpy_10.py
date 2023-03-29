# Created by Srinivas Kadiyala at 29-03-2023
import numpy as np

# Passing character to numerical data type with data type - unicode "<U11"

array1 = np.array([1, 2, 3, 4, 'a'], dtype="<U11")

print(array1)

print(array1.dtype)
