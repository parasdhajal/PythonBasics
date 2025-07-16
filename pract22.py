# List Comprehensions


#This is the noraml method of creating a new list by multiplying each element by 2# using a for loop
import random
prev_list = [1, 2, 3, 4, 5]
new_list = []
for i in prev_list:
    multiply_2 = i * 2
    new_list.append(multiply_2)
print(new_list)



#This is the list comprehension method to achieve the same result    

#List Comprehensions Primary structure :-   new_list1 = [new_item for item in prev_list] 
new_list1 = [i * 2 for i in prev_list]
print(new_list1)     
    
    
language = 'python'

new_list2 = [letter for letter in language]
print(new_list2)