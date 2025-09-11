class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        sums = {}

        totalOnes = nums.count(1)   
        zerosSoFar, onesSoFar = 0, 0

        for i in range(n+1):
            if i == n:
                sum = zerosSoFar 
                if sum not in sums:
                    sums[sum] = [i]
                else:
                    sums[sum].append(i)
                break
            sum = zerosSoFar + (totalOnes - onesSoFar)
            if sum not in sums:
                sums[sum] = [i]
            else:
                sums[sum].append(i)
            if nums[i] == 0:
                zerosSoFar += 1
            else:
                onesSoFar += 1
        return sums[max(sums.keys())]
