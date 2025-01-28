import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[11], [20], [30]])

# Broadcasting arr2 to match arr1's shape
result = arr1 + arr2
print("Result after broadcasting:\n", result)