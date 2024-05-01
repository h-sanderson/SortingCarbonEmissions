import numpy as np

def check_sort(arr, sorted_arr):
    arr = np.array(arr)
    arr = np.sort(arr)
    # sorted_arr = np.array(sorted_arr)
    return np.array_equal(arr, sorted_arr)