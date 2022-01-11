def find_max_pair(nums):
    sum_of_two_max = 0

# O(n^2)
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if (nums[i] + nums[j]) > sum_of_two_max:
    #             sum_of_two_max = nums[i] + nums[j]
    
    # return sum_of_two_max

    # declare the pointer
    pointer = 0
    i = 1
    while i < len(nums):
        if (nums[pointer]+nums[i]) > sum_of_two_max:
            



if __name__ == '__main__':
    assert (find_max_pair([1,2,3,4,5,6,6,11,23,44,6])) == 67  


