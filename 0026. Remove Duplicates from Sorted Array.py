class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        end = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[end-1]:
                nums[end] = nums[i]
                end += 1
        
        return end
    
