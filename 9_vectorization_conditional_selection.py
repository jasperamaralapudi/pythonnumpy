import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Vectorized operation: Adding 5 to each element
arr = arr + 5
print("After vectorized addition:", arr)

# Conditional selection
print("Elements greater than 6:", arr[arr > 6])
