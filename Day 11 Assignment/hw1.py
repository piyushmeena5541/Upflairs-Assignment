import numpy as np

array = np.random.randint(0, 100, size=(12, 5))

array[-1] = [1, 2, 3, 4, 5]

print("Original array:")
print(array)
