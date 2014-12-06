__author__ = 'maxwell'

import  Input

def getmaxcrossmidarray(arr):
    n = len(arr)//2
    numleft=0
    numright=0
    sumleft=0
    sumright=0
    for  i in  range(n-1, -1, -1):
         numleft = arr[i]+numleft
         if sumleft < numleft:
            sumleft = numleft
    for  j in arr[n:]:
        numright = j+numright
        if sumright < numright:
            sumright = numright
    return sumleft+sumright

def getmaxarray(arr):
    n = len(arr)//2
    if len(arr)==1:
        return max(arr[0],0)
    summid=getmaxcrossmidarray(arr)
    sumleft=getmaxarray(arr[n:])
    sumright=getmaxarray(arr[:n])
    return max(summid, sumleft, sumright)
arr = Input.Input.getinputarr('bigestarrinput.txt')
print(getmaxarray(arr))