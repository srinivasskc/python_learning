# Created by Srinivas Kadiyala at 10-03-2023
import time
import numpy as np
import sys

Size = 10

l1 = range(Size)
l2 = range(Size)

StartTime = time.time()
result = [(x+y) for x, y in zip(l1, l2)]
print("Python took time: ", (time.time() - StartTime)*1000)

arr1 = np.arange(Size)
arr2 = np.arange(Size)
StartTime = time.time()
result = [(x+y) for x, y in zip(arr1, arr2)]
print("Numpy took time: ", (time.time() - StartTime)*1000)
