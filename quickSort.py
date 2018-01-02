#Author: Rishabh Dalal
#Description: Quick sort with various timings

import random
import time
import sys

# always implementing last element as pivot
def partition(lyst,low,high):
    i = low
    pivotIndex = high-1
    pivot = lyst[pivotIndex]     
    lyst[pivotIndex], lyst[low] = lyst[low], lyst[pivotIndex]
    
    for j in range(low , high+1):
        if lyst[j] < pivot:
            i = i+1
            lyst[i], lyst[j] = lyst[j], lyst[i]
 
    lyst[low], lyst[i] = lyst[i], lyst[low]
    return i
 
def quickSort(lyst,low,high):
    if low < high:
        p = partition(lyst,low,high)
        quickSort(lyst, low, p-1)
        quickSort(lyst, p+1, high)

# initializing the arrays and timing each rum
def main():
    lyst = []
    SIZE = 3000 ##Can change the size here
    
    print("Using last element as pivot\n")
    print("Size of array:", SIZE)
    sys.setrecursionlimit(SIZE*SIZE)  #changing recursion depth
    
    for i in range(SIZE):
        lyst.append(i)
    
    start = time.time()
    quickSort(lyst, 0, SIZE-1)
    end = time.time()
    print("Time taken to sort array sorted in ascending order:", end-start, "seconds")
    
    count = 0
    for i in range(SIZE-1, -1, -1):
        lyst[count] = i
        count += 1
    
    start = time.time()
    quickSort(lyst, 0, SIZE-1)
    end = time.time()
    print("Time taken to sort array sorted in descending order:", end-start, "seconds")
    
    lyst = random.sample(range(1, SIZE*SIZE), SIZE)
    
    start = time.time()
    quickSort(lyst, 0, SIZE-1)
    end = time.time()
    print("Time taken to sort randomly generated array:", end-start, "seconds")
    
