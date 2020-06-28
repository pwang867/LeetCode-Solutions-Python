# both critical connections and critical routers can be solved by Tarjan's Algorithm



# method 3, optimized from method 2


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = self.build_graph(connections)
        res = []
        disc = [-1] * n    # will also be used as visited
        low = [n] * n
        parent = [-1] * n
        self.time = 0
        for i in range(n):   # can handle edge cases where there are multiple components in the graph
            if disc[i] == -1:
                self.tarjan(i, graph, disc, low, parent, res)
        return res

    def tarjan(self, u, graph, disc, low, parent, res):
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        for v in graph[u]:
            if v == parent[u]:
                continue
            elif disc[v] != -1:
                low[u] = min(low[u], low[v])
            else:
                parent[v] = u
                self.tarjan(v, graph, disc, low, parent, res)
                if low[v] > disc[u]:
                    res.append([u, v])
                low[u] = min(low[u], low[v])

    def build_graph(self, connections):
        # build undirected graph, graph = {parent: [children]}
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        return graph


# method 2: use Tarjan's Algorithm, time O(V+E), space O(V+E)
# ref: edges in graph, https://www.geeksforgeeks.org/bridge-in-a-graph/
# ref: strongly connected components, https://www.youtube.com/watch?v=TyWtx7q2D7Y


from collections import defaultdict
class Solution1(object):
    def criticalConnections(self, n, connections):
        graph = self.buildGraph(connections)
        visited = [False]*n    # can be deleted, can use disc as visited
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
                    low[u] = min(low[u], disc[v])     # edge case: [[0,1], [1,2],[2,0],[2,3],[3,0]]
                    # also OK for this problem: low[u] = min(low[u], low[v])
    
    def buildGraph(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph


# critical Routers, Tarjan


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
        children = 0   # number of child component connected to u, like a "8" shape
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
                if parent[u] != -1 and low[v] >= disc[u]:  # wrong: low[v] > disc[u]:
                    res.add(u)
            else:
                low[u] = min(low[u], disc[v])
                # also OK for this problem: low[u] = min(low[u], low[v])

# method 1: brute force, remove edges one by one
# and then check if the graph is still a single component
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
        # check if start and end are connected
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
    
    
"""
There are n servers numbered from 0 to n-1 connected by 
undirected server-to-server connections forming a network where 
connections[i] = [a, b] represents a connection between servers a and b. 
Any server can reach any other server directly or indirectly through the network.

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
    connections = [[1,2],[1,3],[3,4],[1,4],[4,5]]
    print(SolutionX().criticalRouters(n, connections))
    
    