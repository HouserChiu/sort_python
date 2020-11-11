# coding: utf-8

def mergeSort(alist):
    n = len(alist)
    mid = n // 2
    if n <= 1:
        return alist
    left_li = mergeSort(alist[:mid])
    right_li = mergeSort(alist[mid:])
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] > right_li[right_pointer]:
            result.append(right_li[right_pointer])
            right_pointer += 1
        else:
            result.append(left_li[left_pointer])
            left_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result
print(mergeSort([9, 8, 7, 6, 8, 4, 9, 2, 6]))


# def mergeSort(alist):
#     n = len(alist)
#     if n <= 1:
#         return alist
#     mid = n // 2
#
#     left_li = mergeSort(alist[:mid])
#     right_li = mergeSort(alist[mid:])
#     # 将两个有序子序列合并为整体
#     left_pointer, right_pointer = 0, 0
#     result = []
#     while left_pointer < len(left_li) and right_pointer < len(right_li):
#         if left_li[left_pointer] < right_li[right_pointer]:
#             result.append(left_li[left_pointer])
#             left_pointer += 1
#         else:
#             result.append(right_li[right_pointer])
#             right_pointer += 1
#     result += left_li[left_pointer:]
#     result += right_li[right_pointer:]
#     return result
# print(mergeSort([9, 8, 7, 6, 8, 4, 9, 2, 6]))
