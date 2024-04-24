# Quick Sorts (used GeeksforGeeks for reference)
def quicksort_list_comp(arr):
    # List comprehension way, this is probably faster
    if len(arr) <= 1:
        return arr
    
    pi = arr[0]
    left_arr = [x for x in arr[1:] if x < pi]
    right_arr = [x for x in arr[1:] if x >= pi]

    return quicksort_list_comp(left_arr) + [pi] + quicksort_list_comp(right_arr)

def quicksort(array, l, r):
    # Recursive way, this is probably slower, and may reach recursive limit on large datasets
    if l < r:
        pi = quicksort(array, l, r)
        quicksort(array, l, pi - 1)
        quicksort(array, pi + 1, r)


def partition(arr, l, r):
    pi = arr[r]
    i = l-1

    for j in range(l, r):
        if arr[j] <= pi:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    temp = arr[r]
    arr[r] = arr[i + 1]
    arr[i + 1] = temp

    return i + 1
    
# Merge Sort (used GeeksforGeeks for reference)
# This is the top down approach of merge sort

def merge(arr1, arr2):
    i, j = 0, 0
    result=[]

    while (i < len(arr1) and j < len(arr2)):
        if arr2[j] > arr1[i]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
        
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result
    
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left,right)
