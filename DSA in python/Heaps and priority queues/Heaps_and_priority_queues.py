#Build a MinHEAP (heapify)
#Time O(n), Space O(n)

A = [-4,3,1,0,2,5,10,8,12,9]

import heapq
heapq.heapify(A) #We heapify a tree

print(A)

#Heap push (Insert an element)
# Time: O(log n)

heapq.heappush(A,4) #we insert a new value into our heap (A)

#Heap pop (Extract the minimum element)
#Time: O(log n)

minn = heapq.heappop(A) # It restructures itself, so we mantain the property of a heap 

# Heap sort--- Basically we pop from the heap repeatedly
#Time: O(n log n), Space O(n)
#Note: O(1) is possible via swapping, but it is way more complex

def heaprsort(arr):
    heapq.heapify(arr) #Rearrange the array to make it a heap
    n = len(arr)
    new_list = [0]*n #This actually the one we are goign to return, to which we add the sorted elements

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return new_list


