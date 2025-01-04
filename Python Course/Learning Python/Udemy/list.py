# list comprehension
prev_list = [1,2,3]
new_list = [i*2 for i in prev_list]
print(new_list)

#conditional list comprehension
# version 1
prev_list2 = [1,2,3,4,5,6]
new_list2 = [new_item for new_item in prev_list2 if new_item > 3]
print(new_list2)

# version 2
new_list3 = [number1 if number1 > 2 else nfor number1 in prev_list2]
print(new_list3)