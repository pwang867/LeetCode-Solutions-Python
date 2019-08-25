# two pointers, O(n)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        
        end = 2  # end is excluded in final answer, nums[:end]
        for i in range(2, len(nums)):
            # if not (nums[i] == nums[end-1] and nums[i] == nums[end-2]):
            if nums[i] != nums[end-2]:  # simplified from the sentence above
                nums[end] = nums[i]
                end += 1
        
        return end
    
