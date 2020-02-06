class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        visited = [False]*9
        
        visited[0] = True
        res += self.dfs(0, visited, 1, m, n)*4
        visited[0] = False
        
        visited[1] = True
        res += self.dfs(1, visited, 1, m, n)*4
        visited[1] = False
        
        visited[4] = True
        res += self.dfs(4, visited, 1, m, n)
        visited[4] = False
        
        return res
    
    def dfs(self, cur, visited, cnt, m, n):
        if cnt == n:
            return 1
        if cnt > n:
            return 0
        res = 0
        if m <= cnt < n:
            res += 1
        for target in range(9):
            if self.possible(cur, target, visited):
                visited[target] = True
                res += self.dfs(target, visited, cnt+1, m, n)
                visited[target] = False
        return res
    
    def possible(self, cur, target, visited):
        if visited[target]:
            return False
        dist = (target//3 - cur//3)**2 + (target%3 - cur%3)**2
        if dist in {1, 2, 5}:
            return True
        return visited[(cur + target)//2]
    
    

"""
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

 

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
"""
