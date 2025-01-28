import numpy as np

# Dot product
v1 = np.array([1, 2])
v2 = np.array([3, 4])
dot_product = np.dot(v1, v2)
print("Dot product:", dot_product)

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_multiplication = np.dot(matrix1, matrix2)
print("Matrix multiplication:\n", matrix_multiplication)

# Transpose
transpose_matrix = matrix1.T
print("Transpose of matrix1:\n", transpose_matrix)
