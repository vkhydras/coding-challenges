class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first_min = float('inf')
        second_min = float('inf')
        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True
        return False
            
        
            


"""
Has time complexity of O(n^2)
"""
# class Solution(object):
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         for i in range(1,len(nums)-1):
#             min_num = min(nums[:i])
#             max_num = max(nums[i+1:])
#             if min_num < nums[i] and nums[i] < max_num:
#                 return True
#         return False