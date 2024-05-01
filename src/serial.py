# Quick Sorts (used GeeksforGeeks for reference)
def quicksort_list_comp(arr):
    # List comprehension way, this is probably faster, but could reach recursion limit
    if len(arr) <= 1:
        return arr
    
    pi = arr[0]
    left_arr = [x for x in arr[1:] if x < pi]
    right_arr = [x for x in arr[1:] if x >= pi]

    return quicksort_list_comp(left_arr) + [pi] + quicksort_list_comp(right_arr)

def quickSortIterative(arr,l = None, r = None):
    if not r and not l:
        l = 0
        r = len(arr) - 1
    size = r - l + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = r
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop h and l
        r = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, r)
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < r:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = r
    
    return arr


def partition(arr, l, r):
    pi = arr[r]
    i = l-1

    for j in range(l, r):
        if arr[j] <= pi:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    arr[r], arr[i + 1] = arr[i + 1], arr[r]

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


def insertionSort(arr):
    for i in range(1, len(arr)):
        val = arr[i]

        j = i-1
        while j >= 0 and val < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        
        arr[j+1] = val
    
    return arr
    
def countingSort(arr, exp1): 
   
    n = len(arr) 
    output = [0] * (n) 
    count = [0] * (10) 
   
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
   
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
   

    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
 
# Method to do Radix Sort
def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        countingSort(arr,exp)
        exp *= 10
    
    return arr


def heapify(arr, n, i):
    large = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        large = l

    if r < n and arr[large] < arr[r]:
        large = r

    if i != large:
        arr[i], arr[large] = arr[large], arr[i]
        heapify(arr, n, large)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1): # N//2 to 0 incrementing by 01
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)
    
    return arr

def shellSort(arr):
    n = len(arr)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2
    
    return arr

# NOTE THIS IS OPTIMIZED WITH BREAKING IF no swaps are made
def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break