def search_insert(nums, target):
    begin_index = 0
    end_index = len(nums) -1

    while begin_index <= end_index:
        # we are getting middle index
        mid_point = (begin_index + end_index) // 2
        # check the the index
        if nums[mid_point] == target:
            return mid_point
            # left search
        if nums[mid_point] > target:
            end_index = mid_point - 1
            # right search
        else:
            begin_index = mid_point + 1
    
    return begin_index

    
            

    

if __name__ == '__main__':
    assert search_insert([1,3,5,6,7,8,9,11,23], 5) == 2
    assert search_insert([1,3,5,6,7,8,9,11,23,34], 2) == 1
    assert search_insert([1,3,5,6,8,9,12], 7) == 4
