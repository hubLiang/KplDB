import numpy as np
#1.排序
#冒泡排序
def bubble_sort(arr: list, k: int, reverse: bool = False):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if reverse:
                if arr[j][k] < arr[j + 1][k]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:  # 如果reverse为False，则按照升序排列
                if arr[j][k] > arr[j + 1][k]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#选择排序
def select_sort(arr:list):
    l=len(arr)
    for i in range(l-1):
        min_index=i;
        for j in range(i+1,l):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

#快速排序
def quick_sort_2d(arr, k, reverse=False):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0][k]
        less_than_pivot = [x for x in arr[1:] if x[k] <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x[k] > pivot]
        if reverse:
            return quick_sort_2d(greater_than_pivot, k, reverse) + [arr[0]] + quick_sort_2d(less_than_pivot, k, reverse)
        else:
            return quick_sort_2d(less_than_pivot, k, reverse) + [arr[0]] + quick_sort_2d(greater_than_pivot, k, reverse)


#二分查找
def binary_search(arr:list,target:int,k:int)->int:
    left=1
    right=len(arr)
    while left+1!=right:
        middle=(left+right)//2
        if arr[middle][k]<target:
            left=middle
        elif arr[middle][k]>target:
            right=middle
        else:
            return middle

# data=np.random.randint(100,size=10)
# print(data)
# print(select_sort(data))
