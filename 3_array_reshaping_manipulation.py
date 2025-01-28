import numpy as np

# Create an array
arr = np.arange(9)
print(arr)
# Reshape array
reshaped = arr.reshape(3, 3)
print("Reshaped array:\n", reshaped)

# Flatten array
flattened = reshaped.flatten()
print("Flattened array:", flattened)

# Concatenation
arr2 = np.array([10, 11, 12])
concat_arr = np.concatenate((arr, arr2))
print("Concatenated array:", concat_arr)
