class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:  # easy to miss!!!
            return nums[0]
        
        # cut a circle into two 1DArrays without circles
        max1 = self.rob1DArray(nums[1:])
        max2 = self.rob1DArray(nums[:-1])
        return max(max1, max2)
    
    def rob1DArray(self, nums):
        # refer to LeetCode 198. House Robber
        if not nums:
            return 0
        pre1, pre2 = 0, 0
        for i in nums:
            pre1, pre2 = pre2, max(pre2, pre1 + i)
        return pre2
    
