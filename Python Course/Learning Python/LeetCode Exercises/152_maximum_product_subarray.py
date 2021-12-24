def maxProduct(nums) -> int:
    result = 0
    if len(nums) == 1:
        result = nums[0]
        return result
    else:
        for i in range(len(nums)-1):
            x = nums[i] * nums[i+1]
            if result <= x:
                result = x
        return result

num_exam = [-2,0,-1]
#  [2,3,-2,4]
print(maxProduct(num_exam))