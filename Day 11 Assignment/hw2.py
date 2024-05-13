import numpy as np

def min_max_per_row(array):
    min_max_array = np.empty((array.shape[0], 2), dtype=int)
    for i, row in enumerate(array):
        min_max_array[i] = [np.min(row), np.max(row)]
    return min_max_array

array = np.random.randint(0, 100, size=(12, 5))

result = min_max_per_row(array)

print("Minimum and Maximum elements in each row:")
print(result)
