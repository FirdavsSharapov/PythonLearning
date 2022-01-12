def polindrome_array(nums):
    if nums[0] < 0:
        return False
    half_array = len(nums) % 2
    reversed_nums = nums[::-1]
    for i in range(half_array):
        if nums[i] != reversed_nums[i]:
            return False
    
    return True


def polindrome_number(nums):
    if nums <= 0:
        return False
    
    reversed_nums = 0
    
    while nums > reversed_nums:
        reversed_nums = reversed_nums * 10 + nums % 10
        nums = nums // 10
    
    return nums == True if(reversed_nums or nums == reversed_nums // 10) else False

# solution with converting to string which 
    # def isPalindrome(self, x: int) -> bool:
    #     if str(x) != str(x)[::-1]:
    #         return False
    #     return True


if __name__ == '__main__':
    # assert polindrome_array([1,2,1]) == True
    # assert polindrome_array([-1,1,1]) == False
    assert polindrome_number(11) == True
    assert polindrome_number(121) == True
    assert polindrome_number(-121) == False
    

    


