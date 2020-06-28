# minimum spanning tree, time O(N + m*log(m)), space O(N)
# use UnionFind class


class Solution(object):
    def minimumCost(self, N, connections):
        uf = UnionFind(range(1, N + 1))
        connections.sort(key=lambda x: x[-1])
        total_cost = 0
        num_components = N
        for u, v, cost in connections:
            if uf.union(u, v):
                total_cost += cost
                num_components -= 1
        if num_components == 1:
            return total_cost
        else:
            return -1


class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        p, q = self.find(u), self.find(v)
        if p != q:
            if self.size[p] < self.size[q]:
                p, q = q, p
            self.parent[q] = p
            self.size[p] += self.size[q]
            return True
        return False


# use a single function
# minimum spanning tree, time O(N + m*log(m)), space O(N)
class Solution1(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        parent = {i: i for i in range(1, N + 1)}
        size = {i: 0 for i in range(1, N + 1)}

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            # return True when a new connection is added
            p, q = find(u), find(v)
            if p != q:
                if size[p] < size[q]:
                    p, q = q, p
                parent[q] = p
                size[p] += size[q]
                return True
            return False

        connections.sort(key=lambda x: x[-1])
        total_cost = 0
        for u, v, cost in connections:
            if union(u, v):
                total_cost += cost
        map(find, parent)
        num_components = len(set(parent.values()))   # or use a counter to find it
        if num_components == 1:
            return total_cost
        else:
            return -1


"""
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] 
represents the cost to connect city1 and city2 together.  (A connection is bidirectional: 
connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections 
(possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. 
If the task is impossible, return -1.



Example 1:



Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:



Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.
 

Note:

1 <= N <= 10000
1 <= connections.length <= 10000
1 <= connections[i][0], connections[i][1] <= N
0 <= connections[i][2] <= 10^5
connections[i][0] != connections[i][1]
"""
