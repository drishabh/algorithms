##Author: Rishabh Dalal

def main():
    lyst = []
    SIZE = 10000
    for i in range(SIZE, -1, -1):
        lyst.append(i)
        
    print("Sorting...")
    
    insertionSort(lyst)
    #selectionSort(lyst, len(lyst))
    #bubbleSort(lyst)
    #mergeSort(lyst)

    print("Sorting complete")

##Selection sort 
def selectionSort(arr, size):
    for i in range(size-1):
        minm = i
        for j in range(i+1, size):
            if arr[j] < arr[minm]:
                minm = j
        arr[minm], arr[i] = arr[i], arr[minm]

##Bubble sort
def bubbleSort(arr):
    for lastUnsorted in range(len(arr)-1, -1, -1):
        swap = 0
        for test in range(0, lastUnsorted):
            if arr[test] > arr[test+1]:
                arr[test], arr[test+1] = arr[test+1], arr[test]
                swap = 1
        if not swap:
            return
        
##Insertion sort
def insertionSort(arr):
    for firstUnsorted in range(1, len(arr)):
        toInsert = arr[firstUnsorted]
        test = firstUnsorted-1
        while test >= 0 and arr[test] > toInsert:
            arr[test+1] = arr[test]
            test -= 1
        arr[test+1] = toInsert

## Merge sort
def merge(alist, lefthalf, righthalf):
    i=j=k=0
    while i<len(lefthalf) and j<len(righthalf):
        if lefthalf[i]<righthalf[j]:
            alist[k]=lefthalf[i]
            i=i+1
        else:
            alist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i<len(lefthalf):
        alist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j<len(righthalf):
        alist[k]=righthalf[j]
        j=j+1
        k=k+1

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(alist, lefthalf, righthalf)

main()
