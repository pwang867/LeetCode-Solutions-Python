class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.found = False
        self.dfs(nums)
        return self.found
    
    def dfs(self, nums):
        if self.found:
            return
        if len(nums) == 1:
            if abs(nums[0] - 24) < 0.001:   # epsilon resolution
                self.found = True
            return
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                x, y = nums[i], nums[j]
                new_nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                self.dfs(new_nums + [x+y])
                self.dfs(new_nums + [x-y])
                if x != y:
                    self.dfs(new_nums + [y-x])
                self.dfs(new_nums + [x*y])
                if y != 0:
                    self.dfs(new_nums + [x*1.0/y])
                if x != 0:
                    self.dfs(new_nums + [y*1.0/x])


"""
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""
