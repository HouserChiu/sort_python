# coding: utf-8

def selectionSort(arr):
    for j in range(0, len(arr) - 1):
        minIndex = j
        for i in range(j + 1, len(arr)):
            if arr[minIndex] > arr[i]:
                minIndex = i
        arr[j],arr[minIndex] = arr[minIndex],arr[j]
    return arr
print(selectionSort([9, 8, 7, 6, 8, 4, 9, 2, 6]))



def selectionSort(arr):
    for j in range(0, len(arr) - 1):
        minIndex = j
        for i in range(j + 1, len(arr)):
            if arr[minIndex] > arr[i]:
                minIndex = i
        arr[j], arr[minIndex] = arr[minIndex], arr[j]
    return arr
