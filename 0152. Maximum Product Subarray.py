class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # _max means the max product ending in nums[i]
        # _min means the min product ending in nums[i]
        _max, _min = nums[0], nums[0]
        res = _max  # global maximum product
        for i in range(1, len(nums)):
            candidates = [nums[i], nums[i]*_max, nums[i]*_min]
            _max = max(candidates)  
            _min = min(candidates)
            res = max(res, _max)
        
        return res
    
