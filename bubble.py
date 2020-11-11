# coding: utf-8

def BubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(BubbleSort([9, 8, 7, 6, 8, 4, 9, 2, 6]))
