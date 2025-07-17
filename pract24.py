def find(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return
    print(f"{key} not found in the list")

my_list = [10, 20, 30, 40]
find(my_list, 30)   # Output: 30 found at index 2
find(my_list, 50)   # Output: 50 not found in the list
