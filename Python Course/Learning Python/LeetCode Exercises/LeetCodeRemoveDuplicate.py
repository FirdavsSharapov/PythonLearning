# Problem Description

'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

# Code


# def removeDuplicates(nums: list):
#     _i = 1
#     while _i < len(nums):
#         if nums[_i] == nums[_i - 1]:
#             nums.pop(_i)
#             _i -= 1
#             if len(nums) == 1:
#                 break
#         else:
#             _i += 1
#     return len(nums)

def removeDuplicates(nums: list):
    i = 1
    while i < len(nums):
        for y in range(len(nums)-1):
            if nums[i] == nums[y]:
                nums.pop(y)
    return len(nums)


# _____TEST_____
if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert removeDuplicates([1, 1, 2]) == 2
    assert removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert removeDuplicates([0, 0, 0, 0, 0]) == 1

    print("Coding complete? Click 'Check' to earn cool rewards!")
