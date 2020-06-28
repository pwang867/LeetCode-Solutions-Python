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


"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], 
find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
"""
