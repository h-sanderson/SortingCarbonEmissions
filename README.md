# SortingCarbonEmissions

Algorithms to Implement (I = implemented)
- Serial:
  - Quick Sort (I)
  - Merge Sort (I)
  - Radix Sort (I)
  - Insertion Sort (I)
  - Heap Sort 
  - Shell Sort
  - Bubblesort
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

Research Process:
- Hypothesis: Unsure
- Method:
  - Create large diverse datasets. Some that are close to being sorted, some that are revered sorted, some that are completely random, some with only large numbers, some with small, and some with large standard deviations
  - Create the sorting algorithms.
  - Create a package to easily choose which sorting algorithm to use, which dataset, and on what device (CPU vs GPU), so when the time comes to run it, it is easily chosen
  - Run each algorithm 5 different times on each dataset (create script to do this). Collect results from each, average or take minimum the timings and C02 outputs as the main data point for that algorithm
  - Conglomorate all the different result datapoints
  - Do exploratory analysis
- Present Results
- Present conclusion

