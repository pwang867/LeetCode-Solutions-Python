class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if nums[0] < nums[-1]:  # not rotated
            return nums[0]
        
        left, right = 0, len(nums)-1
        
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] > nums[mid+1]:  # pivot found
                return nums[mid+1]
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        
        return min(nums[left], nums[right])
    
