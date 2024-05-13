import numpy as np
import random

def check_sort(check_arr, sorted_arr):
    check_arr = np.sort(randArr)
    # sorted_arr = np.array(sorted_arr)
    return np.array_equal(check_arr, sorted_arr)

# def generate_ints(distr, keysize, n, repeated_elements, low, high):
def generate_ints(n, low, high):
    arr = np.random.randint(low, high+1, n)

    return arr

def main():
    randArr = generate_ints(5, 10, 20)
    sortedArr = np.sort(randArr)
    reversedArr = np.flip(sortedArr)

if __name__ == "__main__":
    main()