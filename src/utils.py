import numpy as np
from os import listdir
from os.path import isfile, join
import pandas as pd

def check_sort(arr1, arr2):
    return np.array_equal(arr1, arr2)

# onlyfiles = [f'data/{f}' for f in listdir('data') if isfile(join('data', f))]
# print(onlyfiles)

# df = pd.read_csv('data/Uniform0_0_10000_10k.csv')
# print(df['Random'].values)