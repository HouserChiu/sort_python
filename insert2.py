# coding: utf-8

def insertSort(arr):
    for j in range(1, len(arr)):
        i = j
        while i > 0:
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                i -= 1
            else:
                break
    return arr