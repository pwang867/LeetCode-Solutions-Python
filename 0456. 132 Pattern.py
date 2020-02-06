class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        middle = -float('inf')  # the "2" in "132"
        stack = []  # maintain a decreasing sequence
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < middle:
                return True
            while stack and stack[-1] < nums[i]:
                middle = stack.pop()  # middle will always increase
            stack.append(nums[i])
        
        return False



"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
"""

