def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]

    ans = []

    for i in range(len(nums)):
        print(nums[:i])
        print(nums[i+1:])
        print(nums[:i]+nums[i+1:])
        temp = permute(nums[:i]+nums[i+1:])

        for j in temp:
            ans.append([nums[i]]+j)

    return ans


if __name__ == '__main__':
    assert permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
