"""
Given an integer array nums sorted in non-decreasing order, return an array 
of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, 
could you find an O(n) solution using a different approach?
"""
from quick_sort import quickSort
def sorted_squares(nums):
    result = []
    for i in range(len(nums)):
        sqr = nums[i]**2
        if 


    i = 0
    for i in range(len(result)):
        if i = 0

    array_len = len(result)
    # result = quickSort(result,0, array_len-1)
    return quickSort(result,0, array_len-1)
    



if __name__ == '__main__':
    assert sorted_squares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert sorted_squares([-7,-3,2,3,11]) == [4,9,9,49,121]