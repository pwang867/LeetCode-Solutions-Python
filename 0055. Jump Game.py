# a BFS idea


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        front = 0
        for i in range(len(nums)-1):  # better than range(len(nums))
            front = max(front, i + nums[i])
            if front == i:
                return False
            if front >= len(nums) - 1:   # or this if clause and switch position with the if clause above
                return True
        
        return True
    


"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""