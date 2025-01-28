import numpy as np

# Create array with NaN values
arr = np.array([1, 2, np.nan, 4, 5])

# Check for NaN
print("Is NaN at index 2:", np.isnan(arr[2]))

# Handle NaN: Replace NaN with mean
arr[np.isnan(arr)] = np.nanmean(arr)
print("Array after replacing NaN:", arr)
