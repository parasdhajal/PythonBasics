mylist = list()
while(True):
    inp = input("Enter the number: ")
    if inp == 'done': break
    value = float(inp)
    mylist.append(value)
average = sum(mylist) / len(mylist)

print('Average:', average)