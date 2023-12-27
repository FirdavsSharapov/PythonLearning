def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] =  i
    
    # If no solution is found, you can handle it as per your requirements.
    # For example, you can return an empty list or raise an exception.
    return []