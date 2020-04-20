# method 3: time O(n), space O(1) greedy, similar to BFS searching minimum depth
# try to get the furthest front for each jump

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        
        jump = 1
        pre = 1  # the farest index of jump-1 jumps plus 1
        front = cur = nums[0]  # the furthest index after jump jumps
        
        while cur < n - 1:
            jump += 1
            for i in range(pre, cur+1):
                front = max(i + nums[i], front)
            pre = cur + 1
            cur = front
        
        return jump
        
        
# method 2: dp, record the smallest jumps to reach each number
# O(sum(nums)), time limit exceeded

class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        jumps = [n for _ in range(n)]
        jumps[0] = 0  # don't forget !
        
        for i in range(1, n):
            for j in range(i):
                # save the smallest jump
                if j + nums[j] >= i:
                    jumps[i] = min(jumps[i], jumps[j] + 1)
        
        return jumps[-1]
        
        
# method 1: brute force, dfs
# time complexity: nums[0]*nums[1]*...*nums[n-1], time limit exceeded
class Solution1(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        ans = [len(nums)]
        self.helper(nums, 0, 0, ans)
        return ans[0]
        
        
    def helper(self, nums, cur, jumps, ans):
        # recursion
        
        # stop condition
        if cur == len(nums) - 1:
            # jump finished
            if jumps < ans[0]:
                ans[0] = jumps
            return
        if cur > len(nums) - 1:
            # jump out of bound
            return
        
        # try every possible jump in cur from large to small
        for i in range(nums[cur], 0, -1):
            if cur + i < len(nums):
                self.helper(nums, cur + i, jumps + 1, ans)



"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
