import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)


print("step 1")
#axis represents the dimension row or column for row 0 and column 1
#after twoDarray below there is 1 which represents the no of row or column to be added
# newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0) 
# print(newTwoDArray)

print(len(twoDArray))

print("step 2")

# Appending a new row to the 2D array
newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(len(newTwoDArray)) # Length of the new array
print(len(newTwoDArray[0])) # No of columns in the first row

print("step 3")

# Accessing elements in the 2D array
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

accessElements(newTwoDArray, 1, 2)



print("step 4")
# Traversing the 2D array
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseTDArray(twoDArray)

print("step 5")
# Searching for an element in the 2D array

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element no found'


print(searchTDArray(twoDArray, 444))

print("step 6")
# Deleting a column from the 2D array

newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)
