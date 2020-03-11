class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(range(n))
        num_extra_edges = 0
        for a, b in connections:
            if not uf.union(a, b):
                num_extra_edges += 1
        num_components = uf.get_num_components()
        if num_components - 1 <= num_extra_edges:
            return num_components - 1
        else:
            return -1


# standard Union Find
class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        p, q = self.find(u), self.find(v)
        if p != q:
            if self.size[p] < self.size[q]:
                p, q = q, p
            self.parent[q] = p
            self.size[p] += self.size[q]
            return True
        return False

    def get_num_components(self):
        map(self.find, self.parent)
        return len(set(self.parent.values()))


"""
There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 

 

Example 1:



Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:



Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
Example 4:

Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0
 

Constraints:

1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
There are no repeated connections.
No two computers are connected by more than one cable.
"""