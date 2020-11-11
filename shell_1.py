# coding: utf-8

def shellSort(arr):
    gap = len(arr) // 2
    while gap >= 1:
        for j in range(gap, len(arr)):
            i = j
            while i > 0:
                if arr[i] < arr[i-gap]:
                    arr[i], arr[i-gap] = arr[i-gap],arr[i]
                    i -= gap
                else:
                    break
        gap = gap // 2
    return arr

print(shellSort([9, 8, 7, 6, 8, 4, 9, 2, 6]))