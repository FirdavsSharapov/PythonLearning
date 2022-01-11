"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""

def max_subarray(num):
    output = 0
    for i in range(len(num)):
        if num[i] >

if __name__ == '__main__':
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5,4,-1,7,8]) == 6

