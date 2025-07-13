#One Dimensional Array Practice
from array import *

#1. Create an array and traverse.
arr = array('i', [1, 2, 3, 4, 5])
for i in range(len(arr)):
    print(arr[i])

#2. Access individual elements through indexes

print("Step 2")
print("Element at index 2 :", arr[2])  

#3. Append any value to the array using append() method

print("Step 3")
arr.append(6)
print(arr)


#4. Insert value in an array using insert() method
print("Step 4")
arr.insert(0, 10) 
print(arr)

#5. Extend python array using extend() method
print("Step 5")
arr.extend([7, 8, 9])
print(arr)

#6. Add items from list into array using fromlist() method
print("Step 6")
templist = [11, 12, 13]
arr.fromlist(templist)
print(arr)

#7. Remove any array element using remove() method
print("Step 7")
arr.remove(10) 
print(arr)

#8. Remove last array element using pop() method

print("Step 8")
arr.pop() # Removes the last element
print(arr) 

#9. Fetch any element through its index using index() method

print("Step 9")
print("Element at index 2 :", arr.index(12))

#10. Reverse a python array using reverse() method

print("Step 10")
arr.reverse()
print(arr)

#11. Get array buffer information through buffer_info() method

print("Step 11")
print("Buffer info:", arr.buffer_info())

#12. Check for number of occurrences of an element using count() method

print("Step 12")
arr.append(1)
print(arr)
print("Count of 1 in array:", arr.count(1))

#13. Convert array to string using tostring() method

print("Step 13")
strtemp = arr.tobytes()
print("Array as string:", strtemp)
ints = array('i')
ints.frombytes(strtemp)
print("Converted back to array:", ints)

#14. Convert array to a python list with same elements using tolist() method
print("Step 14")
#print(arr.tolist())

#15. Slice Elements from an array
print("Step 15")
print(arr)
print(arr[1:4])