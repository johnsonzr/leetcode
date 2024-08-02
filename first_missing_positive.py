def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums = set(nums)
    nums = [x for x in nums if x > 0]
    if len(nums) > 1:
        nums = sorted(nums)
    elif nums == [1]: 
        return 2
    else:
        return 1

    for x in range(len(nums)):
        if x == len(nums)-1 and nums[x] > x and nums[x] - nums[x-1] == 1:
            return nums[x] + 1
        if nums[x] > x + 1:
            return x + 1

nums = [1,2,0]
# nums = [3,4,-1,1]
# nums = [0]
# nums = [1,1]
# nums = [1,1000]

print(firstMissingPositive(nums))


# Runtime: 384ms
# Beats: 60.7%

# Memory: 28.65MB
# Beats: 13%

# Difficulty: hard
