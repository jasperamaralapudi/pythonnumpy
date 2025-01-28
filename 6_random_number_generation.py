import numpy as np

# Random numbers
random_array = np.random.rand(3, 3)
print("Random array (uniform distribution):\n", random_array)

# Random integers
random_integers = np.random.randint(1, 10, size=(3, 3))
print("\nRandom integers:\n", random_integers)

# Setting a seed for reproducibility
np.random.seed(42)
random_seeded = np.random.rand(3, 3)
print("\nRandom array with seed:\n", random_seeded)
