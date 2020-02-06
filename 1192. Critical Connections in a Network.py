# method 2: use Tarjan's Algorithm, time O(V+E), space O(V+E)
# ref: edges in graph, https://www.geeksforgeeks.org/bridge-in-a-graph/
# ref: strongly connected components, https://www.youtube.com/watch?v=TyWtx7q2D7Y
from collections import defaultdict
class Solution(object):
    def criticalConnections(self, n, connections):
        graph = self.buildGraph(connections)
        visited = [False]*n
        self.time = 0
        disc = [-1]*n  # the discovered time when a node is first visited
        low = [-1]*n
        parent = [-1]*n
        res = []
        self.dfs(0, disc, low, graph, visited, parent, res)
        return res
    
    
    def dfs(self, u, disc, low, graph, visited, parent, res):
        # u is not processed yet before entering dfs()
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                self.dfs(v, disc, low, graph, visited, parent, res)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    res.append([u, v])
            else:
                if v != parent[u]:
                    low[u] = min(low[u], disc[v])  
                    # also OK for this problem: low[u] = min(low[u], low[v])
    
    
    def buildGraph(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
        



# method 1: trival method, remove edges sequentially 
# and then check if the graph is still connected
# time O(E*(V+E)), space O(V+E)
# Time Limit Exceeded

from collections import defaultdict, deque
class Solution1(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        d = self.buildMap(connections)
        
        res = []
        for start, end in connections:
            d[start].remove(end)
            d[end].remove(start)
            if not self.checkPath(d, start, end, n):
                res.append([start, end])
            d[start].add(end)
            d[end].add(start)
        
        return res
    
    def buildMap(self, connections):
        d = defaultdict(set)
        for start, end in connections:
            d[start].add(end)
            d[end].add(start)
        return d
    
    def checkPath(self, d, start, end, n):
        used = [False]*n
        used[start] = True
        stack = deque([start])
        while stack:
            server = stack.popleft()
            if server == end:
                return True
            for neighbor in d[server]:
                if not used[neighbor]:
                    used[neighbor] = True
                    stack.append(neighbor)
        
        return False
    
    
