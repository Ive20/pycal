'''
Created on 2014.05.17

@author: maxwell

'''
import Sort.Input
def merge(arr1,arr2):
    arr=[];
    while arr1 and arr2:
        if arr1[0]>arr2[0]:
            arr.append(arr2.pop(0));
        else:
            arr.append(arr1.pop(0));       
    return arr+arr1+arr2;

arr=Sort.Input.Input.getinputarr();
while len(arr)>1:
    arr.append(merge(arr.pop(0),arr.pop(0)));
print(arr);