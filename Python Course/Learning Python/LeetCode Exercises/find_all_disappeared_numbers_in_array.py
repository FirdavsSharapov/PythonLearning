def find_disappeared_numbers(nums):
    holder = []
        # mark existing numbers 
    for i in nums:
        position = abs(i) - 1
        if nums[position] > 0:
            nums[position] *= -1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                holder.append(i+1)
        
        
    return holder
    # i = 1
    # holder = []
    # if len(nums) > 1:
    #     while i <= len(nums):
    #         if i not in nums:
    #             holder.append(i)
    #         i += 1
    #     return holder
    # return nums
    
if __name__ == '__main__':
    # assert find_disappeared_numbers([4,3,2,7,8,2,3,1]) == [5,6]
    assert find_disappeared_numbers([1,1]) == [2]


