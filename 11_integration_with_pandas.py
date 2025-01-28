import numpy as np
import pandas as pd

# Create a NumPy array
data = np.array([10, 20, 30, 40, 50])

# Convert to pandas DataFrame
df = pd.DataFrame(data, columns=['Values'])
print("Pandas DataFrame:\n", df)

# Perform NumPy operations on DataFrame columns
df['Squared'] = np.square(df['Values'])
print("\nDataFrame with squared values:\n", df)
