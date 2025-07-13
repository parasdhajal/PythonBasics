from array import *

arr1 = array('i', [1, 2, 3, 4, 5])


def arrayindex(array,index):
    if index >len(array):
        return "Index out of range"
    else:
        print(array[index])


arrayindex(arr1, 2)
#time complexity is O(1) because it directly accesses the element at the specified index without iterating through the array.