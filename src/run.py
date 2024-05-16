from collections.abc import Iterable
from codecarbon import EmissionsTracker
import cupy as cp
import numpy as np
import pandas as pd
import time
from serial import quickSortIterative, mergeSort, insertionSort, radixSort, heapSort, shellSort, bubbleSort
from utils import generate_ints
from os import listdir
from os.path import isfile, join



class RunSort:
    def __init__(self, sort_func: callable, project_name: str, is_gpu = 0):
        self.sort_func = sort_func
        self.project_name = project_name
        self.track_energy = {}
        self.track_time = {}
        self.is_gpu = is_gpu

    def run_sort(self, array: Iterable, data_name: str):
        tracker = EmissionsTracker(project_name=f"{self.project_name}_{data_name}", measure_power_secs=15)
        measure_energy = []
        measure_time = []

        for i in range(1):
            if self.is_gpu:
                x_gpu = cp.asarray(array)
                tracker.start()
                t0 = time.time()
                self.sort_func(x_gpu)
                lapsedTime = time.time()-t0
                amt = tracker.stop()
            else:
                tracker.start()
                t0 = time.time()
                self.sort_func(np.array(array))
                lapsedTime = time.time()-t0
                amt = tracker.stop()
            measure_energy.append(amt)
            measure_time.append(lapsedTime)
            print(lapsedTime, amt)
        
        self.track_energy[data_name] = measure_energy
        self.track_time[f"{data_name}_Time"] = measure_time
    
    def track_into_df(self):
        dfCarbon = pd.DataFrame.from_dict(self.track_energy)
        dfTime = pd.DataFrame.from_dict(self.track_time)
        df = pd.concat([dfCarbon, dfTime], axis=1)
        df['SortAlgo'] = self.project_name
        return df


def run_all_sorts(data, data_name, sorts_list):
    for run in sorts_list:
        run.run_sort(data, data_name)

def conglomorate_data(sorts_list):
    dfs = []
    for run in sorts_list:
        dfs.append(run.track_into_df())
    
    return pd.concat(dfs)


CPU_SORTS = {
    "QuickSort": quickSortIterative,
    "RadixSort": radixSort,
    "MergeSort": mergeSort,
    "NumpySort": np.sort,
    "InsertionSort": insertionSort, 
}

GPU_SORTS = {
    "RadixParallelSort": cp.sort,
}

def run_sorts(sorts, data_dir = 'data'):
    runSorts = []
    for key, func in sorts.items():
        runSorts.append(RunSort(func, key))

    onlyfiles = [f for f in listdir('data') if isfile(join('data', f))]

    for file_name in onlyfiles:
        # read data and run
        dataDF = pd.read_csv(f'{data_dir}/{file_name}')
        # randArr = read_file
        run_all_sorts(dataDF['Random'].values, f'Random_{file_name}', runSorts)
        run_all_sorts(dataDF['ReverseSorted'].values, f'ReversedSorted_{file_name}', runSorts)
        run_all_sorts(dataDF['Sorted'].values, f'Sorted{file_name}', runSorts)

    df = conglomorate_data(runSorts)
    return df

def main(gpu = False):
    if gpu:
        print("Running GPU Sorts")
        df = run_sorts(GPU_SORTS)
        df.to_csv(f"gpu_sorts.csv")
    else:
        print("Running CPU Sorts")
        df = run_sorts(CPU_SORTS)
        df.to_csv(f"cpu_sorts.csv")


if __name__ == "__main__":
    main()

