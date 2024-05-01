from collections.abc import Iterable
from codecarbon import EmissionsTracker
import numpy as np
from serial import quickSortIterative

class RunSort:
    def __init__(self, sort_func: callable, project_name: str):
        self.sort_func = sort_func
        self.project_name = project_name
        # self.tracker = EmissionsTracker(project_name=self.project_name, measure_power_secs=15)


    def run_sort(self, array: Iterable, data_name: str):
        tracker = EmissionsTracker(project_name=f"{self.project_name}_{data_name}", measure_power_secs=15)
        for i in range(5):
            tracker.start()
            self.sort_func(np.array(array))
            tracker.stop()

