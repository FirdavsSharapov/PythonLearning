def findMaxConsecutiveOnes(nums) -> int:
    final_result = 0
    result = 0
    for x in nums:
        if x == 1:
            result += 1
        else:
            if final_result < result:
                final_result = result
            result = 0

    return final_result


def duplicateZero(arr) -> None:
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            del arr[len(arr)-1]
            i += 2
        else:
            i += 1


##############
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
#     The number of elements initialized in nums1 and nums2 are m and n respectively.
#     You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
# Example:
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]


def merge(nums1, m, nums2, n) -> None:
    num_lenght = len(nums1)
    if num_lenght == m + n:
        for x in range(num_lenght - m):
            nums1.insert(m, nums2[x])
            del nums1[len(nums1)-1]
            x += 1
    nums1.sort()


def removeElement(nums, val) -> int:
    i = 0
    for x in range(len(nums)):
        if nums[x] != val:
            del nums[x-1]
    return i

# def removeDuplicate(nums) -> int:
#     # nums.sort() # will take extra space complexity and time complexity
#     # i = 0
#     for j in range(len(nums)):
#         for i in range(len(nums)-1):
#             if nums[j] != nums[i+1]:
#                 i += 1
#             else:
#                 del nums[j]

# nums = [0,1,5,1,2,5,3,3,4,3]
# print (removeDuplicate(nums))


def findLengthOfLCIS(nums) -> int:
    result = 1
    i = 1
    while i < len(nums):
        if nums[i-1] < nums[i]:
            result += 1
        elif nums[i-1] == nums[i]:
            break
        i += 1
    return result

# nums = [1,3,5,7]
# nums =[2,2,2,2,2]
# print (findLengthOfLCIS(nums))
# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2


# print(removeElement(nums, val))


# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

# print(merge(nums1, m, nums2, n))

# test = [1, 0, 2, 3, 0, 4, 5, 0]

# print(duplicateZero(test))

def removeDuplicatesOnce(nums):
    _i = 1
    for nums

    while _i < len(nums):
        if nums[_i] == nums[_i - 1]:
            nums.pop(_i)
            _i -= 1
            if len(nums) == 1 and :
                break
        else:
            _i += 1
    return nums

    # if len(nums) == 0:
    #     return 0
    # for i in range(1, len(nums)):
    #     if nums[i] != nums[i-1]:
    #         nums[_ctr] = nums[i]
    #         _ctr +=1
    # nums = nums[:_ctr]
    # return nums


sr = [0, 0, 0, 0, 0]
# [1,1]
print(removeDuplicatesOnce(sr))


def isPathCrossing(path) -> bool:
    d = {}
    x =0 
    y = 0
    d[(0, 0)] = 0
    for i in path:
        if i == 'N':
            y += 1
        elif i == 'S':
            y -= 1
        elif i == 'E':
            x += 1
        else:
            x -= 1
        if (x, y) in d:
            return True
        d[(x, y)] = 0
    return False
