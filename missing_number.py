def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #return [x for x in range(len(nums)+1) if x not in nums][0]

    return len(nums) * (len(nums)+1)/2 - sum(nums)


nums = [9,6,4,2,3,5,7,0,1]

print(missingNumber(nums))


# Runtime: 93ms
# Beats: 70%

# Memory: 12.78MB
# Beats: 88.%
