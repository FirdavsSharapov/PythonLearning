def sort_array_by_parity(nums):
    # first we need to add condition where we we check if 
    # array has less than 0 elements
    if nums[0] == 0 & len(nums) == 1:
        return [0]
    
    # The optimal solution in here to use two way pointer 
    # first pointer would be i
    # second pointer would be j in loop
    for j in range(len(nums)):
        if nums[j] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


example_test = [0,2]
print(sort_array_by_parity(example_test))

