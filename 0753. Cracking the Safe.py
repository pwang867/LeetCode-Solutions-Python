class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        visited = {"0"*n}
        
        self.dfs("0"*n, k**n-1, visited, n, k, res)
        
        return res[0]
    
    def dfs(self, path, m, visited, n, k, res):
        if m == 0:
            res.append(path)
            return True
        
        for i in range(k-1, -1, -1):  
            # quicker if we start from large to small
            c = str(i)
            candidate = path[len(path)-n+1:] + c
            if candidate not in visited:
                visited.add(candidate)
                if self.dfs(path+c, m-1, visited, n, k, res):
                    return True
                visited.remove(candidate)
        
        return False
        
