from collections.abc import Iterable
from codecarbon import EmissionsTracker
import numpy as np
from serial import quickSortIterative, mergeSort, insertionSort, radixSort, heapSort, shellSort, bubbleSort
from utils import generate_ints
import pandas as pd
import time

SORTS = {
    # "QuickSort": quickSortIterative,
    "RadixSort": radixSort,
    "MergeSort": mergeSort,
    # "InsertionSort": insertionSort, 
}

class RunSort:
    def __init__(self, sort_func: callable, project_name: str):
        self.sort_func = sort_func
        self.project_name = project_name
        # self.tracker = EmissionsTracker(project_name=self.project_name, measure_power_secs=15)
        self.track_energy = {}
        self.track_time = {}

    def run_sort(self, array: Iterable, data_name: str):
        tracker = EmissionsTracker(project_name=f"{self.project_name}_{data_name}", measure_power_secs=15)
        measure_energy = []
        measure_time = []

        for i in range(1):
            tracker.start()
            t0 = time.time()
            self.sort_func(np.array(array))
            lapsedTime = time.time()-t0
            amt = tracker.stop()
            measure_energy.append(amt)
            measure_time.append(lapsedTime)
            print(lapsedTime)
        
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


def main():
    runSorts = []
    for key, func in SORTS.items():
        runSorts.append(RunSort(func, key))
    
    # randArr = generate_ints(100000, 10, 20)
    # dataName = "UniformRandom100k"
    # run_all_sorts(randArr, dataName, runSorts)

    randArr = generate_ints(1000000, 1, 10000)
    dataName = "UniformRandom1M"
    run_all_sorts(randArr, dataName, runSorts)

    # randArr = generate_ints(10000000, 10, 20)
    # dataName = "UniformRandom10M"
    df = conglomorate_data(runSorts)
    df.to_csv("TEST.csv")


if __name__ == "__main__":
    main()


