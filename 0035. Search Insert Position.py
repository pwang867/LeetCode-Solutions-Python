class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        
        if target <= nums[left]:
            return left
        elif target <= nums[right]:
            return right
        else:
            return right + 1
        
