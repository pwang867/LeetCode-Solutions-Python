# pancake, time O(n), in place
# similar to #186. Reverse Words in a String II
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        k = k%len(nums)
        nums = self.reverse(nums, 0, len(nums) - 1)
        nums = self.reverse(nums, 0, k - 1)
        nums = self.reverse(nums, k, len(nums) - 1)
    
    def reverse(self, nums, left, right):
        # reverse nums between index left and right
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
