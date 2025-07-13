from array import *

arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('b', [6, 7, 8, 9, 10])


def myarray(array):
    for i in array:
        print(i)

myarray(arr1)


print("",arr1[2])
#time complexity is O(n) because it iterates through the array once, where n is the number of elements in the array.
#space complexity is O(1) because it does not use any additional data structures that grow.