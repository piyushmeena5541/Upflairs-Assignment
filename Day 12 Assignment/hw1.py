import numpy as np

def array_stats(shape):
    
    rand_array = np.random.randint(0, 100, shape)
    print(rand_array)

    last_row = rand_array[-1]
    average = np.mean(last_row)
    minimum = np.min(last_row)
    maximum = np.max(last_row)
    evens_count = np.sum(last_row % 2 == 0)
    
    return {
        "Average": average,
        "Minimum": minimum,
        "Maximum": maximum,
        "No. of evens": evens_count
    }


shape = (12, 5)
stats = array_stats(shape)


for key, value in stats.items():
    print(f"{key} -> {value}")
