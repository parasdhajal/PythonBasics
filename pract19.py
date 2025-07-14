my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list.append(8)
print(my_list)

del my_list[2]
print(my_list)

#print(my_list[2:5])

#List Operators
a =[0,1]
a = a* 3
print(a)

#List Functions
b = [1, 2, 3, 4, 5]
print(len(b))
print(sum(b))
print(max(b))
print(min(b))



mylist = list()
while(true):
    inp = input("Enter the number: ")
    value = float(inp)
    if value == 0: break
    mylist.append(value)
average = sum(mylist) / len(mylist)

print('Average:', average)