def print_items(n):
    for i in range(n):
        print(i)
print_items(5)

# Simple big O - O(n) program to demonstrate a function that prints numbers from 0 to n-1 that is O(n) in complexity.

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(5)
# This prograam is for o(2n) complexity, which is equivalent to O(n) in big O notation.