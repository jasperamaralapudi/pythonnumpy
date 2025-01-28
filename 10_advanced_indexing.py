import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Fancy indexing: Selecting specific indices
indices = np.array([0, 2, 4])
print("Selected elements:", arr[indices])

# Conditional fancy indexing
even_numbers = arr[arr % 2 == 0]
print("Even numbers:", even_numbers)
