def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i,i+1)
    return total
def pair_sum(a, b):
    return a + b

pair_sum_sequence(4)

# THis progrma is of big o space complexity O(1) because it uses a constant amount of space regardless of the input size.