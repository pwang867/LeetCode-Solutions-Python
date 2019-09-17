# method 1: undirected graph, dfs
# time O(n*n), space O(n)
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        
        n = len(M)
        visited = [False]*n
        
        cnt = 0
        for u in range(n):
            if not visited[u]:  # if M[i][i] could be 0, then add: and 1 in M[u]
                cnt += 1
                visited[u] = True
                self.dfs(u, visited, M)
        
        return cnt
    
    def dfs(self, u, visited, M):
        for v, w in enumerate(M[u]):
            if w == 1 and not visited[v]:
                visited[v] = True
                self.dfs(v, visited, M)
    
