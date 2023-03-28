# Created by Srinivas Kadiyala at 23-02-2023

import numpy as np
import sys

l = range(1000)
print(l)
print(type(l))

# Size of one element
print("Size of One Python Object/Item: ",sys.getsizeof(1))
print("length of range: ",len(l))
print(sys.getsizeof(5)*len(l))

# Size of numpy array
array = np.arange(1000)
print("Size of Array: ",array.size)
print("Size of numpy Object/Item: ",array.itemsize)
print(array.size * array.itemsize)


