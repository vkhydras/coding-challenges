class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hash:
                return [hash[compliment],i]
            hash[nums[i]] = i
       
        