# Operations on list
list1 = [1,2,3,4,5,6,7,8,9,10,11]

# [] -> indicate index to get elemnent from the list 0 is a default
assert(list1[2] == 3)
# if I indicate negative number than the list will start from the end
assert(list1[-1] == 11) # note that index of elements start from -1 


# [:] -> slicing. indicates the start index and end index
# [start:end:steps]
assert(list1[2:]==[3,4,5,6,7,8,9,10,11])
assert(list1[3:8]==[4,5,6,7,8])

# list.extend method that will allow you to concat the list with new values
list1.extend([12,13,14])
assert(list1 == [1,2,3,4,5,6,7,8,9,10,11,12,13,14])