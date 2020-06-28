# Amazon OA


from collections import defaultdict


class SolutionX(object):
    def criticalRouters(self, n, connections):
        graph = self.buildGraph(connections)
        visited = [False]*n    # can be deleted, can use disc as visited
        self.time = 0
        disc = [-1]*n  # the discovered time when a node is first visited
        low = [-1]*n
        parent = [-1]*n
        res = set()
        self.dfs(1, disc, low, graph, visited, parent, res)
        return res

    def buildGraph(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def dfs(self, u, disc, low, graph, visited, parent, res):
        # res: a set
        # u is not processed yet before entering dfs()
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        children = 0   # number of child component connected to u
        for v in graph[u]:
            if v == parent[u]:
                continue
            if not visited[v]:
                children += 1
                parent[v] = u
                self.dfs(v, disc, low, graph, visited, parent, res)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children == 2:
                    res.add(u)
                if parent[u] != -1 and low[v] >= disc[u]:
                    res.add(u)
            else:
                low[u] = min(low[u], disc[v])
                # also OK for this problem: low[u] = min(low[u], low[v])
    
"""
There are n servers numbered from 0 to n-1 connected by 
undirected server-to-server connections forming a network where 
connections[i] = [a, b] represents a connection between servers a and b. 
Any server can reach any other server directly or indirectly 
through the network.

A critical connection is a connection that, if removed, will make some server 
unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""


if __name__ == "__main__":
    n = 6
    connections = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
    print(SolutionX().criticalRouters(n, connections))
