'''
Created on 2014.4.24.

@author: maxwell

'''
import Sort.Input
arr=Sort.Input.Input.getinputarr();
for i in range(0,len(arr)):
    temp=arr[i];
    for j in range(0,i)[::-1]:
        if temp<arr[j]:
            arr[j+1]=arr[j];
            arr[j]=temp;
        else:
            break;
print(arr);         
            
            