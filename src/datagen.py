import numpy as np
import pandas as pd
import math

def uniform_dist(low, high, size):
    return np.random.randint(low=low, high=high, size=size)

def binomial_dist(n, probability, size):
    return np.random.binomial(n=1000, p=probability, size=size)

def generate_uniform_data(low, high, size, file_dir = 'generic', file_prefix = 'generic'):
    for i in range(1):
        data = uniform_dist(low, high, size)
        sorted = np.sort(data)
        reverse_sorted = np.flip(sorted)
        df = pd.DataFrame({
            'Random': data,
            'Sorted': sorted,
            'ReverseSorted': reverse_sorted
        })
        thousands = int(size/1000)
        print(f"data/{file_dir}/{file_prefix}_{high}_{thousands}k.csv")
        df.to_csv(f"data/{file_dir}/{file_prefix}_{high}_{thousands}k.csv")

def generate_radix_tests():
    ns = [25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    for n in ns:
        generate_uniform_data(0, 10, n, 'radix', 'RadixO')

    for n in ns:
        generate_uniform_data(0, 1000000, n, 'radix', 'RadixO')

def generate_quick_sort():
    # ns = [25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000]
    # for n in ns:
    #     generate_uniform_data(0, 10000, n, 'quick', 'Quick0')
    
    ns = [15, 16, 17, 18, 19, 20]
    for n in ns:
        generate_uniform_data(0, 10000, 2**n, 'evenpartition', 'evenpartition')


def worstMergeSort(n):
    if n == 1:
        return [1]
    else:
        top = worstMergeSort(int(math.floor(float(n) / 2)))
        bottom = worstMergeSort(int(math.ceil(float(n) / 2)))
        return list(map(lambda x: x * 2, top)) + list(map(lambda x: x * 2 - 1, bottom))

def generate_merge_sort():
    ns = [25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    for n in ns:
        data = worstMergeSort(n)
        save_data(data, file_dir = 'worstmerge', file_prefix = 'worstmerge')

def generate_heap_shell():
    ns = [25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    for n in ns:
        generate_uniform_data(0, 10000, n, 'heapshell', 'heapshell')

def save_data(data, file_dir = 'generic', file_prefix = 'generic'):
    sorted = np.sort(data)
    reverse_sorted = np.flip(sorted)
    df = pd.DataFrame({
        'Random': data,
        'Sorted': sorted,
        'ReverseSorted': reverse_sorted
    })
    thousands = int(len(data)/1000)
    print(f"data/{file_dir}/{file_prefix}_{thousands}k.csv")
    df.to_csv(f"data/{file_dir}/{file_prefix}_{thousands}k.csv")

def main():
    generate_quick_sort()
    # return

# main()