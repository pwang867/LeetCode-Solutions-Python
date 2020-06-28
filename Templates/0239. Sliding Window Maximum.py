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
            while queue and nums[queue[-1]] <= nums[i]:  # make queue decreasing
                queue.pop()
            queue.append(i)
            if queue[0] <= i-k:  # remove index not in window anymore
                queue.popleft()
            if i >= k-1:
                res.append(nums[queue[0]])
        
        return res
    

"""

Given an array nums, there is a sliding window of size k which is moving from the very left of 
the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
 """
 