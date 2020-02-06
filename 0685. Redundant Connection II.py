"""
There are 3 kinds of duplicate edges:
  1. start from a node to the root
  2. start from a node to its parent or grandparent or ...
  3. start from a node to other nodes
"""


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges or not edges[0]:
            return []
        N = len(edges)
        # build graph and search nodes with indegree 2
        parent = {i:i for i in range(1,N+1)}
        first, second = [], []
        for u, v in edges:
            if parent[v] == v:
                parent[v] = u
            else:
                first = [parent[v], v]
                second = [u, v]
        
        def hasCircle(start, end):
            while parent[start] != start and parent[start] != end:
                start = parent[start]
            return parent[start] == end
        if first:   # if there is node with indegree 2
            if hasCircle(first[0], first[1]):
                return first
            return second
        # find circle and return the last edge
        return self.redundantConnectionI(edges)
    
    def redundantConnectionI(self, edges):
        N = len(edges)
        parent = {i:i for i in range(1, N+1)}
        size = {i:0 for i in range(1, N+1)}
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
        def union(u, v):
            p, q = parent[u], parent[v]
            if p != q:
                if size[p] < size[q]:
                    p, q = q, p
                parent[q] = p
                size[p] += size[q]
                return True
            else:
                False
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []  # when no circle


"""
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""
