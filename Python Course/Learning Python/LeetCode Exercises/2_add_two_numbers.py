"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Questions:
1) Does first list always bigger than secons? 
2) Is there max number of elements in the list?

"""

def helper_function (nums1, nums2, num):
    reminder = 0
    
    return helper_function(nums1, nums2, reminder)


def add_two_numbers(nums1, nums2):
    if len(nums1, nums2) <= 0:
        return [0]
    else:
        return helper_function (nums1, nums2, 0)

