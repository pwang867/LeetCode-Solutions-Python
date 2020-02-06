# dfs with memo, O(N*2^N)
from collections import defaultdict
class Solution(object):
    def numSquarefulPerms(self, A):
        if not A or len(A) < 2:
            return 0
        n = len(A)
        A.sort()
        
        graph = defaultdict(list)  # graph saves the possible neighbors for each i
        for i in range(n):
            for j in range(i):
                if int((A[i]+A[j])**0.5)**2 == A[i]+A[j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        self.cnt = 0
        self.memo = {}
        for i, num in enumerate(A):
            if i > 0 and A[i]==A[i-1]:
                continue
            self.cnt += self.dfs(i, 1<<i, n, A, graph)
        return self.cnt
    
    def dfs(self, prev, state, n, A, graph):
        # dfs returns the number of ways to visit the remaining nodes 
        # when selected nodes are recorded in state 
        # and the last chosen element is A[prev]
        if (prev, state) in self.memo:
            return self.memo[(prev, state)]
        if state == 2**n-1:
            return 1
        
        res = 0
        for i, neighbor in enumerate(graph[prev]):
            if (state>>neighbor)&1 != 0:
                continue
            if i > 0 and A[graph[prev][i]] == A[graph[prev][i-1]] \
            and (state>>graph[prev][i-1])&1 == 0:  # skip duplicates
                continue
            res += self.dfs(neighbor, state|(1<<neighbor), n, A, graph)
        self.memo[(prev, state)] = res
        return res
        

# O(N!), but use (int((num + prev)**0.5))**2 == num + prev to prune
class Solution1(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 2:
            return 0
        
        A.sort()
        self.cnt = 0
        self.permute(A, None)
        return self.cnt
    
    def permute(self, nums, prev):
        if not nums:
            self.cnt += 1
            return 
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if prev is None or (int((num + prev)**0.5))**2 == num + prev:
                self.permute(nums[:i]+nums[i+1:], num)
        