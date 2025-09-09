class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i,n):
                if i == j:
                    continue
                if nums[i] == nums[j] and (i*j)%k == 0:
                    count+=1
        return count
        