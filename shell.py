# coding: utf-8

def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j>=gap and arr[j - gap] > temp:
                arr[j] = arr[j-gap]
                j -=gap
            arr[j] = temp

        gap = int(gap / 2)
    return arr

print(shellSort([3,2,1,0]))