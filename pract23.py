pre_list = [-1,10,15,-20,26,99,-75,-25]

new_list = [number*number for number in pre_list if number < 0]
print(new_list)



# List Comprehensions with Conditional Logic
# This function returns the number if it is negative, otherwise returns 'negative number'
def get_number(number):
    return number if number <0 else 'negative number'

new_list1 = [get_number(number) for number in pre_list]

print(new_list1)