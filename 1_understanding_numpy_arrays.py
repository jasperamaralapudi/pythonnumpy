import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.zeros((3, 3))
arr3 = np.ones((2, 2))
arr4 = np.arange(10, 25, 2)

# Array attributes
print("Array 1:", arr1)
print("Shape of arr1:", arr1.shape)
print("Size of arr1:", arr1.size)
print("Data type of arr1:", arr1.dtype)

# Array created with ones
print("\nArray of ones:", arr3)
print("Shape of arr3:", arr3.shape)
print("Arange function",arr4)
print("Arrays of zeroes:",arr2)