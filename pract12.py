######  Quiz Questions ####### 


def f1(n):
    if n <= 0:
        return 1
    else:
        return 1 + f1(n-1)
#O(n) (Linear space complexity)
# This function has a linear space complexity because it uses the call stack to keep track of each recursive call, leading to O(n) space usage in the worst case.


def f2(n):
    
    if n <= 0:
        return 1
    else:
        return 1 + f2(n-5)
#O(n/5) = O(n)
# This function has a linear space complexity as well, but it reduces the input by 5 each time, which still results in O(n) space usage in terms of the number of recursive calls made.

def f3(n):
    if n <= 0:
        return 1
    else:
        return 1 + f3(n/5)
#O(log n)
# This function has logarithmic space complexity because it reduces the input size by a factor of 5 with each recursive call, leading to O(log n) space usage in the call stack.

def f4(n,m,o):
    if n<=0:
        print(n,m,o)
    else:
        f4(n-1,m+1,o)
        f4(n-1,m,o+1)
#O(2^n)
# This function has exponential space complexity because it makes two recursive calls for each value of n, leading to a total of 2^n calls in the worst case, which results in O(2^n) space usage.


def f5(n):
    for i in range(0,n,2):
        print(i)  
    if n<=0:
        return 1
    else:
        return 1 + f5(n-5)

#O(n/2) = O(n)
# This function has linear space complexity because it uses a loop that iterates through half of the input size, leading to O(n) space usage in terms of the number of recursive calls made.


print("f1(5):", f1(5))  

print("f2(20):", f2(20)) 

print("f3(125):", f3(125))  

print("f4(3,0,0):", f4(3,0,0))  

print("f5(20):", f5(20))  