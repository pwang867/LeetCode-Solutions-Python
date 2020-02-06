# time/space O(n!*n)
class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        self.dfs(nums, 0, res)
        return res
    
    def dfs(self, nums, start, res):
        if start == len(nums):
            res.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.dfs(nums, start+1, res)
            nums[start], nums[i] = nums[i], nums[start]
        



# backtracking, o(n!*(n+2.71828))
class Solution1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # use recursion
        n = len(nums)
        if n == 0:
            return []
        
        ans = []
        self.helper(nums, [], ans, n)
        return ans
    
    def helper(self, nums, path, ans, n):
        if len(path) == n:  # or len(nums) == 0
            ans.append(path)
            return
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:], path + [nums[i]], ans, n)

"""
dfs(nums = [1, 2, 3] , path = [] , result = [] )
|____ dfs(nums = [2, 3] , path = [1] , result = [] )
|      |___dfs(nums = [3] , path = [1, 2] , result = [] )
|      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
|           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
|____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
|      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
|      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
|           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
|____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
       |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
            |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result
"""





"""
Given a collection of distinct integers, 
return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from time import time

nums = list(range(9))
s2 = Solution2()
s1 = Solution1()

time1 = time()
s1.permute(nums)
time2 = time()
print(time2-time1)

s2.permute(nums)
print(time()-time2)


