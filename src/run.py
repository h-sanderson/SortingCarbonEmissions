from collections.abc import Iterable
from codecarbon import EmissionsTracker, OfflineEmissionsTracker
import cupy as cp
import numpy as np
import pandas as pd
from serial import quickSort, mergeSort, insertionSort, radixSort, heapSort, shellSort, bubbleSort, radix_sort_strings
from os import listdir
from os.path import isfile, join
import sys
from utils import check_sort
# from datagen import 
import time

TRACKER = OfflineEmissionsTracker(project_name="Sorting", measure_power_secs=15, country_iso_code="USA")


class RunSort:
    def __init__(self, sort_func: callable, project_name: str, is_gpu = 0):
        self.sort_func = sort_func
        self.project_name = project_name
        self.tracked = []
        self.is_gpu = is_gpu

    def run_sort(self, array: Iterable, data_name: str, sorted_arr: Iterable):
        project_name = f"{self.project_name}_{data_name}"
        length_arr = len(array)
        for i in range(1):
            arr = array.copy()
            if self.is_gpu:
                x_gpu = cp.asarray(arr)
                TRACKER.start_task(project_name)
                sorted_to_check = self.sort_func(x_gpu)
                amt = TRACKER.stop_task()
                sorted_to_check = cp.asnumpy(sorted_to_check)
                if not check_sort(sorted_to_check, sorted_arr):
                    print("FAILURE: NOT SORTED PROPERLY")
            else:
                TRACKER.start_task(project_name)
                sorted_to_check = self.sort_func(arr)
                amt = TRACKER.stop_task()
                if not check_sort(sorted_to_check, sorted_arr):
                    print("FAILURE: NOT SORTED PROPERLY")
            self.tracked.append([length_arr, amt.emissions, amt.duration, amt.energy_consumed, self.project_name, data_name])
            print(f"Emissions: {amt.energy_consumed}, Duration: {amt.duration}")
        
    
    def track_into_df(self):
        columns = ['SizeArray', "Emissions", "Duration", "Energy", "SortAlgo", "DataFile"]
        df=pd.DataFrame(self.tracked, columns=columns)
        return df


def run_all_sorts(data, data_name, sorts_list, sorted_data):
    for run in sorts_list:
        run.run_sort(data, data_name, sorted_data)
        print(f"Done with {run.project_name} with {data_name}\n")

def conglomorate_data(sorts_list):
    dfs = []
    for run in sorts_list:
        dfs.append(run.track_into_df())
    
    return pd.concat(dfs)


CPU_SORTS = {
    "RadixSort": radixSort, #d
    "MergeSort": mergeSort, #d
    "HeapSort": heapSort, #d
    "ShellSort": shellSort, #d
    "QuickSort": quickSort, #d
}

GPU_SORTS = {
    "RadixParallelSort": cp.sort,
}

def run_sorts(sorts, data_dir = 'data', is_gpu = 0):
    runSorts = []
    for key, func in sorts.items():
        runSorts.append(RunSort(func, key, is_gpu))

    onlyfiles = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]

    for file_name in onlyfiles:
        # read data and run
        data_name = file_name.replace('.csv', "")
        print(f"Starting {data_name}")
        data_df = pd.read_csv(f'{data_dir}/{file_name}')

        run_all_sorts(data_df['Random'].values.tolist(), f'Random_{data_name}', runSorts, data_df['Sorted'].values)
        run_all_sorts(data_df['ReverseSorted'].values.tolist(), f'ReversedSorted_{data_name}', runSorts, data_df['Sorted'].values)
        run_all_sorts(data_df['Sorted'].values.tolist(), f'Sorted_{data_name}', runSorts, data_df['Sorted'].values)
        print(f"Finished {data_name}")

    df = conglomorate_data(runSorts)
    return df



def main():
    is_gpu = False
    csv_extension = "generic"
    if len(sys.argv) > 1:
        if sys.argv[1] == 'gpu':
            is_gpu = True
        elif sys.argv[1] == 'cpu':
            is_gpu = False
        else:
            print("Using cpu as no proper argument was provided.\n")
            print("Run `python run.py cpu/gpu` to specify.\n")
        if len(sys.argv) > 2:
            csv_extension = sys.argv[2]
    if is_gpu:
        print("Running GPU Sorts")
        df = run_sorts(GPU_SORTS, 'data/quick', 1)
        df.to_csv(f"csvs/new/gpu_sorts_{csv_extension}.csv")
    else:
        print("Running CPU Sorts")
        df = run_sorts(CPU_SORTS, 'data/new')
        df.to_csv(f"csvs/all/cpu_sorts_{csv_extension}.csv")
    


if __name__ == "__main__":
    main()

