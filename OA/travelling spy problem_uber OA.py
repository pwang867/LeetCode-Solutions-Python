# dp[i] means the total ways of travelling nodes 1-i starting from node i
# time O(N^2+M), space O(N)
from collections import defaultdict
class UberOA():
    def countSpy(self, N, M, edges):
        graph = self.buildGraph(edges)
        dp = [0]*(N+1)  
        dp[1] = 1
        for u in range(2, N+1):
            for v in graph[u]:
                dp[u] += dp[v]
            for j in range(1, u):
                dp[j] *= (u-1)
        return sum(dp)
    
    def buildGraph(self, edges):
        # build graph in a directed way: large node --> small node
        graph = defaultdict(list)
        for u, v in edges:
            u, v = max(u, v), min(u, v)
            graph[u].append(v)
        return graph

N = 4
M = 6
edges = [[1,2],[3,2],[1,3],[1,4],[3,4],[2,4]]
print(UberOA().countSpy(N, M, edges))

