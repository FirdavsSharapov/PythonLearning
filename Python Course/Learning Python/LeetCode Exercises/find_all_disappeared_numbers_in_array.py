def find_disappeared_numbers(nums):
    i = 1
    holder = []
    if len(nums) > 1:
        while i < len(nums):
            if i not in nums:
                holder.append(i)
            i += 1
        return holder
    return nums
    


if __name__ == '__main__':
    # assert find_disappeared_numbers([4,3,2,7,8,2,3,1]) == [5,6]
    assert find_disappeared_numbers([1,1]) == [2]