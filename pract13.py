import array

myarray = array.array('i', [1, 2, 3, 4, 5])
print(myarray)

myarray.insert(0,10) #insert 10 at the beginning also we can specify the index no then insert the element at that index
print(myarray)

#time complexity and space complexity is O(n) and O(1) respectively because we are inserting an element at the beginning of the array, which requires shifting all other elements by one position. This operation takes linear time in terms of the number of elements in the array, while the space complexity remains constant as we are not using any additional data structures.