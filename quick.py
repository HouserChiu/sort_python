# coding: utf-8

def quickSort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    quickSort(alist, first, low - 1)
    quickSort(alist, low + 1, last)


li = [9, 8, 7, 6, 8, 4, 9, 2, 6]
quickSort(li, 0, len(li) - 1)
print(li)
