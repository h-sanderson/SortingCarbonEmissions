import pandas as pd
import random

def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
 
    for j in range(l , h):
        if arr[j] <= x:
 
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1

def partition_r(arr, l, h):
    n = random.randint(l,h)
    arr[h],arr[n] = arr[n],arr[h]
    return partition(arr, l, h)

 
def quickSort(arr, l = None, h = None):
    if not l and not h:
        l = 0
        h = len(arr) - 1
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # Set pivot element at its correct position in
        # sorted array
        p = partition_r( arr, l, h )
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
    return arr
    
# Merge Sort (used GeeksforGeeks for reference)
# This is the top down approach of merge sort

def merge(arr1, arr2):
    i, j = 0, 0
    result = []

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
    if len(arr) < 2:
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



from utils import check_sort
import numpy as np
import time

def main():
    # df = pd.read_csv(f'data/worstmerge/worstmerge_300k.csv')
    df = pd.read_csv(f'data/radix/BigK_100000_100k.csv')
    # print("start")
    t0 = time.time()
    # vals = [1 if i%2==0 else 2 for i in range(0,1000*1000)]
    vals = df['Random'].values.tolist()
    print(len(str(max(vals))))
    print(len(vals))
    sortattempt1 = bubbleSort(vals)
    t1 = time.time()
    # print(f"Time: {t1-t0}")
    # t0 = time.time()
    # sortattempt2 = heapSort(df['Random'].values.tolist())
    sortattempt2 = np.sort(vals)
    # t1 = time.time()
    print(check_sort(sortattempt2, sortattempt1))
    print(f"Time: {t1-t0}")

if __name__ == "__main__":
    main()

# main()
# import sys
# sys.setrecursionlimit(1000)
# print(sys.getrecursionlimit())
# main()

