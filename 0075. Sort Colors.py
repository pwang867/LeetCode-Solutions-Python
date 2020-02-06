# two pointers, pointing to the boundary of 0 and 2
# time O(n), in place, extra space O(1)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        start = 0
        end = len(nums) -1
        curr = 0
        while curr <= end:  # will be wrong is here is curr < end
            if nums[curr] == 0:
                nums[start], nums[curr] = nums[curr], nums[start]
                start += 1
                curr += 1
            elif nums[curr] == 2:
                nums[end], nums[curr] = nums[curr], nums[end]
                end -= 1
            else:
                curr += 1


"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""