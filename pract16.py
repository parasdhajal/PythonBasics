from array import *

arr= array('i', [1, 2, 3, 4, 5])

def linear_search(array, target):
    for i in range(len(array)):  # O(n) time complexity
        if array[i] == target:   # O(1) time complexity for comparison
            return i
    return -1  # If target is not found

print(linear_search(arr, 3))  

#space complexity is O(1) because it does not use any additional data structures that grow with the input size.


#Now deletion of element from array

arr.remove(3) 

print(arr)


