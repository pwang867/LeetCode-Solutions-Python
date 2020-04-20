# method 3: use binary search twice to search, time O(log(n))
# time O(log(n)) space O(1)

class Solution2(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.findLast(nums, target - 1)
        right = self.findLast(nums, target)
        if left + 1 > right:
            return [-1, -1]
        return [left + 1, right]

    def findLast(self, arr, target):
        # find the index of the last element <= target
        if not arr:
            return -1
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid
            else:
                right = mid
        if arr[right] <= target:
            return right
        elif arr[left] <= target:
            return left
        else:
            return -1


# method 2, use bisect package

import bisect


class Solution3(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = bisect.bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target)
        return [left, right - 1]


# method 1: use binary search only once to 
# find a number equal to target, then 
# linearly search its neighbors in two directions for duplicates
# time O(n) in worst case, generally O(log(n))
class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # edge cases
        if len(nums) == 0:
            return [-1, -1]
        
        # check the begin and end if they are target
        if nums[0] == target:
            return self.helper(nums, 0, target)
        else:
            left = 0
        if nums[-1] == target:
            return self.helper(nums, len(nums) - 1, target)
        else:
            right = len(nums) - 1
        
        # binary search
        while left + 1 < right:
            mid = (left + right)/2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return self.helper(nums, mid, target)
        
        return [-1, -1]
    
    
    def helper(self, nums, i, target):
        # this is linear search, tie O(n)
        left, right = i, i
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        return [left, right]
    
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
