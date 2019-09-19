# maintain a decreasing double-end queue, 
# store value and index, or only store index to save space
# time O(n), space O(k)

from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < k:
            return [max(nums)]
        
        queue = deque([])
        res = []
        for i in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            while queue[0] <= i-k:
                queue.popleft()
            if i >= k-1:
                res.append(nums[queue[0]])
        
        return res
    
