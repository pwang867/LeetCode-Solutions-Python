# time O(result)
# let arrays in results be sorted, in this way we can avoid duplicate results
# there is no duplicate in this problem
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k <= 0 or k > n or n < 1:
            return []
        res = []
        self.dfs(n, 1, k, [], res)
        return res
    
    def dfs(self, n, start, k, path, res):
        if len(path) == k:
            res.append(path[:])
            return  # do not forget !!
        for num in range(start, n-(k-len(path))+2):  # mistake: n-(k-len(path))+1,  num is the number, not index of the number so 
            path.append(num)
            self.dfs(n, num+1, k, path, res)
            path.pop()



"""
Given two integers n and k, return all possible combinations of k numbers 
out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

