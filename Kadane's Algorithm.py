def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]
    running_sum = nums[0]
    n = len(nums)
    for i in range(1,n):
        running_sum = max(nums[i],running_sum+nums[i])
        if running_sum > max_sum:
            max_sum = running_sum
    return max_sum
        