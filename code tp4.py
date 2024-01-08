
"""
Created on Tue Oct 10 19:57:45 2023

@author: janna
"""
from time import perf_counter
import numpy as np
import random as rd
import matplotlib.pyplot as plt


# the insertion algorithm

def insertion_sort(arr):
    start = perf_counter()
    i=1
    n=len(arr)
    while i < n:
        x=arr[i]
        j=i
        while j>0 & arr[j-1] > x:
            arr[j] = arr[j-1]
            j=j-1
        
        arr[j]=x
        i=i+1
    end = perf_counter()
    return (arr, end-start)

#test on an example
random_arr= np.random.randint(15,size=2**4)
random_arr_sorted,execution_time_sort = insertion_sort(random_arr)
print('random_arr_sorted :',random_arr_sorted, 'execution_time:',execution_time_sort)


# the heapsort algorithm

def heapsort(arr):
    start=perf_counter()
    def heapify(arr):
        start=(len(arr)-1)/2
        start= start -1
        
        
    def siftdown(arr,start,end):
        root=start
        while root*2+1 <= end:
            child=2*root+1
            if child + 1 <= end and arr[child] < arr[child+1]:
                child= child+1
            if child <= end and arr[root] < arr[child]:
                arr[root],arr[child] = arr[child],arr[root]
                root = child 
            else:
                return 
            
    heapify(arr)
    end = len(arr) -1
    while end >0:
        arr[end], arr[0] = arr[0], arr[end]
        siftdown(arr, 0, end-1)
        end= end-1
    end= perf_counter() 
    return(arr,end-start)

random_arr= np.random.randint(15,size=2**4)
random_arr_heapsorted, execution_time_heap = heapsort(random_arr)
print('random_arr_heapsorted:',random_arr_heapsorted,'execution_time:',execution_time_heap)

#task 3 4

#sorted algo : execution_time: 3.31999999900745e-05
#heapsorted algo : execution_time: 6.479999998987296e-05
#sorted algo is more effecient because its time execution is lower than the heapsorted algo


#task 5 graphics

execution_time1 = []
execution_time2 = []
size = []

for l in range (3,30):
    random_arr1=np.random.randint(15,size=2**l)
    random_arr_sorted1=insertion_sort(random_arr1)
    random_arr_heapsorted1=heapsort(random_arr1)
    execution_time1.append(random_arr_sorted[1])
    execution_time2.append(random_arr_heapsorted1[1])
    size.append(2**l)
    
plt.figure()    
plt.plot(size,execution_time1,"blue",label='insertion_sort')
plt.plot(size,execution_time2,"red",label='heapsort')
plt.xlabel("size")
plt.ylabel("execution_time")
plt.show()


def sequentialsearch(arr,k):
    start = perf_counter()
    n=len(arr)
    i=0
    while i<n and arr[i] != k:
        i=i+1
    end= perf_counter()
    return (arr[i] == k, end-start)

print(sequentialsearch(random_arr_heapsorted,rd.choice(random_arr_heapsorted)))


#task 7 dichotomous search
  
def dichotomous_search(arr,element):
    start = perf_counter()
    low = 0
    high = len(arr)-1
    while (low <= high):
        mid = (low+high)//2
        if (arr[mid]== element):
            return mid
        elif (arr[mid]<element):
            low=mid+1
        else:
            high=mid-1
        mid= (low+high)//2
    end= perf_counter()
    return (mid,end-start)


print(dichotomous_search(random_arr_heapsorted,rd.choice(random_arr_heapsorted)))



execution_time3 = []
execution_time4 = []
size1 = []

for j in range (3,30):
    random_arr3=[np.random.randint(15,size=2**j)]
    A=rd.choice(random_arr3)
    B=heapsort(random_arr3)
    random_arr3=B[0]
    random_arr_sequentialsearch=sequentialsearch(random_arr3,A)
    random_arr_dichotomous_search=dichotomous_search(random_arr3,A)
    execution_time3.append(random_arr_sequentialsearch[1])
    execution_time4.append(random_arr_dichotomous_search[1])
    size.append(2**j)
    
plt.figure()    
plt.plot(size1,execution_time3,"blue",label='sequentialsearch')
plt.plot(size1,execution_time4,"red",label='dichotomous_search')
plt.xlabel("size")
plt.ylabel("execution_time")
plt.show()
        
        
    
    
    









    
    
        
    
 














































