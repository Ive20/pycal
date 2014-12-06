'''
Created on 2014.05.17

@author: maxwell

'''
import Input


def merge(arr1, arr2):
    arr = []
    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            arr.append(arr2.pop(0))
        else:
            arr.append(arr1.pop(0))
    return arr+arr1+arr2


def mergesort(arr):
    if(len(arr) <= 1):
        return arr
    num = len(arr)//2
    left = mergesort(arr[:num])
    right = mergesort(arr[num:])
    return merge(left, right)

inputarr = Input.Input.getinputarr()
print(mergesort(inputarr))