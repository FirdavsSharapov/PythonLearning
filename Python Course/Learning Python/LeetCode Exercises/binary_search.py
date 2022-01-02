def binary_search(nums, item):
    # first got the len of the array
    begin_index = 0
    end_index = len(nums)-1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        mid_value = nums[midpoint]
        if mid_value == item:
            return midpoint
            #looking to the left side if target number is less the middle value
        elif item < mid_value:
            end_index = midpoint - 1
            #otherwise looking to the right side if target number 
        else:
            begin_index = midpoint + 1
    
    return -1

if __name__ == '__main__':
    assert binary_search ([-1,0,3,5,9,12,13],9) == 4
    assert binary_search ([-1,0,3,5,9,12,41], 2) == -1