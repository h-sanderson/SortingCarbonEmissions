# SortingCarbonEmissions

Algorithms to Implement (I = implemented)
- Serial:
  - Quick Sort (I)
  - Merge Sort (I)
  - Radix Sort (I)
  - Insertion Sort (I)
  - Heap Sort (I)
  - Shell Sort (I)
  - Bubblesort (I)
  - Timsort (python sorted() function)
- Parallel: Quick Sort, Merge Sort, Radix Sort, Insertion Sort, Bitonic Sort

Big Os:
| Algorithm      | Time Complexity |             |             | Space Complexity |
|----------------|-----------------|-------------|-------------|------------------|
|                |   Best          | Average     | Worst       |       Worst      |
| Bubble Sort    | O(n)            | O(n^2)      | O(n^2)      | O(1)             |
| Insertion Sort | O(n)            | O(n^2)      | O(n^2)      | O(1)             |
| Heap Sort      | O(n log(n))     | O(n log(n)) | O(n log(n)) | O(1)             |
| Quick Sort     | O(n log(n))     | O(n log(n)) | O(n^2)      | O(n)             |
| Merge Sort     | O(n log(n))     | O(n log(n)) | O(n log(n)) | O(n)             |
| Radix Sort     | O(nk)           | O(nk)       | O(nk)       | O(n + k)         |
| Shell Sort     | O(n log(n))     | O(n log(n)) | O(n^2)      | O(1)             |

- Tracking Carbon Using: https://github.com/mlco2/codecarbon?tab=readme-ov-file
- Parallel Sorting Psuedocode: https://www.cs.cmu.edu/~scandal/nesl/algorithms.html

ISSUES:
- How to best run and measure CUDA CODE?
  - Run Script using subprocesses
  - Numba
  - CUDA Python: https://github.com/NVIDIA/cuda-python
  - PyCUDA: https://pypi.org/project/pycuda/
  - CuPy: https://cupy.dev/
- Should I just test parallel sorting using CPU (Multiprocessing)?

Research Process:
- Hypothesis:
  - Serial: Algorithms with smaller time complexities and smaller space complexities should have smaller carbon output. Based on this Heap Sort being O(n log(n) with a space complexity of O(1) should be the most energy and carbon efficient program. Quick Sort and Merge Sort being close seconds. I imagine Radix sort to also be near the top given the number of digits in the largest number is small (this represents k). I see Bubble and Insertion sort to be the least carbon efficient.
  - Serial CPU vs Parallel GPU: Generally GPUs have higher energy usage than CPUs. However, if the GPU sorts more than x times faster than the x times more carbon it outputs, then the GPU will be more carbon efficient. My hypothesis is that the parallelized sorting on GPUs will be LESS carbon efficient than sorting on CPUs as their speedups will not make up for the amount of carbon they output.
- Method:
  - Create the serial sorting algorithms.
  - Create large diverse datasets. Some that are close to being sorted, some that are revered sorted, some that are completely random, some with only large numbers, some with small, and some with large standard deviations. Essential can take ints randomly from different distributions and ranges.
  - Create a package to easily choose which sorting algorithm to use, which dataset, and on what device (CPU vs GPU), so when the time comes to run it, it is easily chosen
  - Run each algorithm 5 different times on each dataset (create script to do this). Collect results from each, average or take minimum the timings and C02 outputs as the main data point for that algorithm
  - Conglomorate all the different result datapoints
  - Do exploratory analysis
- Present Results
- Present conclusion

