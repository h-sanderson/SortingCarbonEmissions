import numpy as np
import pandas as pd

def uniform_dist(low, high, size):
    return np.random.randint(low=low, high=high, size=size)


def binomial_dist(n, probability, size):
    return np.random.binomial(n=1000, p=probability, size=size)


def poisson_dist(lam, size):
    return np.random.poisson(lam=lam, size=size)

def generate_uniform_data(low, high, size):
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
        print(f"data/Uniform{i}_{low}_{high}_{thousands}k.csv")
        df.to_csv(f"data/Uniform{i}_{low}_{high}_{thousands}k.csv")
    

generate_uniform_data(0, 10000, 10000)
generate_uniform_data(0, 10000, 100000)
generate_uniform_data(0, 10000, 1000000)
generate_uniform_data(0, 10000, 10000000)
generate_uniform_data(0, 10000, 100000000)