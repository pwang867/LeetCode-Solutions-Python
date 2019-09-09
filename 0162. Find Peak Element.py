# method 2: binary search, O(log(n))
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid
        
        # at least one of left and right must be the boundary
        # edge case [1,2]
        if nums[left] < nums[right]:
            return right
        else:
            return left

        
# method 1: O(n), brute force, scan the whole array to find 
# the element that matches nums[i-1] <= nums[i] >= nums[i+1]
