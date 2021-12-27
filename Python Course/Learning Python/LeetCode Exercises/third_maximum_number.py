def third_maximum_number(nums):
    # look for third distinct number from the array
    if len(nums) < 3:
        return max(nums)
    # Two pointer solution
    i = 0
    counter = 1
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            counter +=1
            if counter == 3:
                return nums[j]
        else:
            i + 1
    if counter < 3:
        return max(nums)



if __name__ == '__main__':
    assert third_maximum_number([3, 2, 1]) == 1
    # assert third_maximum_number([1, 2]) == 2
    # assert third_maximum_number([2, 2, 3, 1]) == 1
    # assert third_maximum_number([1,1,2]) == 2
    assert third_maximum_number([5,2,2]) == 5
