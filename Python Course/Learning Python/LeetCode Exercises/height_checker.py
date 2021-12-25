def hight_checker(heights):
        # I have solution in my mind where we can sort one of the arrays and 
        # and compare it against original array and count inconsistancy
        # first I think we can sort the array and assign into the new array
        # then compare 
    count = 0
    for i, j in zip(heights, sorted(heights)):
        if i != j:
            count += 1
    return count


# another way to solve that
# i = 0
#         new_sorted_array = sorted(heights)

#         for j in range(len(heights)):
#             if heights[j] != new_sorted_array[j]:
#                 i += 1
#         return i

if __name__ == '__main__':
    assert hight_checker([1,1,4,2,1,3]) == 3
