class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # method 2: dictionary, O(n)
        d = {}
        
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            else:
                d[target-num] = i
        
        return []
    
        
        
        # method1: brute force, O(n^2)
#     def twoSum(self, nums, target):
#         n = len(nums)
#         if n < 2:
#             return []
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return res
    
