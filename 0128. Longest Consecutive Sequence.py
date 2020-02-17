# method 2, union find for index (not for nums[i])
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        self.parent = {i: i for i in range(n)}  # union find for index (not for nums[i])
        self.size = {i: 1 for i in range(n)}
        visited = {}
        for i, num in enumerate(nums):
            if num in visited:  # skip duplicates
                continue
            if num-1 in visited:
                self.union(i, visited[num-1])
            if num+1 in visited:
                self.union(i, visited[num+1])
            visited[num] = i
        return max(self.size.values())
    
    def union(self, i, j):
        p = self.find(i)
        q = self.find(j)
        if p != q:
            if self.size[p] > self.size[q]:
                p, q = q, p
            self.parent[p] = q
            self.size[q] += self.size[p]
    
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]


# method 1: hash set， time/space O(n)
class Solution1(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _set = set(nums) 
        ans = 0

        while _set:
            num = _set.pop()
            count = 1
            copy = num
            while num + 1 in _set:
                count += 1
                _set.remove(num + 1)
                num += 1
            while copy - 1 in _set:
                count += 1
                copy -= 1
                _set.remove(copy)
            ans = max(ans, count)
        
        return ans

    
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

from collections import Counter

