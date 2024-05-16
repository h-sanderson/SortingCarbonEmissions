import numpy as np
import cupy as cp
import time
from utils import generate_ints
from codecarbon import EmissionsTracker



# length = 100000
def run_gpu(x_cpu, data_name):
    x_gpu = cp.asarray(x_cpu)
    tracker = EmissionsTracker(project_name=f"Parallel_{data_name}", measure_power_secs=15)
    measure_energy = []
    measure_time = []
    for i in range(1):
        tracker.start()
        t0 = time.time()
        x_sorted_gpu = cp.sort(x_gpu)
        t1 = time.time()
        energy = tracker.stop()
        measure_energy.append(energy)
        measure_time.append(t1-t0)b
        x_sorted_cpu = cp.asnumpy(x_sorted_gpu)
    
    return x_sorted_cpu

def main():
    x_cpu = generate_ints(10000000, 1, 1000) # READ IN DATA TO KEEP CONSISTENT WITH OTHER
    arr, energy_usage, time_lapsed = run_gpu(x_cpu)