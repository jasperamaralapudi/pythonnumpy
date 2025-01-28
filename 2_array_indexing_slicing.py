import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Basic indexing
print("Element at index 2:", arr[2])

# Slicing
print("Elements from index 1 to 4:", arr[1:4])

# Boolean Indexing
print("Elements greater than 20:", arr[arr > 20])

# Fancy Indexing
fancy_indices = np.array([1, 3])
print("Elements at indices 1 and 3:", arr[fancy_indices])
