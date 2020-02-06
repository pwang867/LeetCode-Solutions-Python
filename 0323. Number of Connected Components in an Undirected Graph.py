class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = [i for i in range(n)]
        size = [0]*n
        for u, v in edges:
            self.union(u, v, parent, size)
        map(lambda x: self.find(x, parent), range(n))   # important !!!
        return len(set(parent))
    
    def union(self, u, v, parent, size):
        parentu = self.find(u, parent)
        parentv = self.find(v, parent)
        if parentu != parentv:
            if size[parentu] <= size[parentv]:
                parentu, parentv = parentv, parentu
            parent[parentv] = parentu
            size[parentu] += size[parentv]
    
    def find(self, u, parent):
        if parent[u] != u:
            parent[u] = self.find(parent[u], parent)
        return parent[u]


class Solution1(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = [i for i in range(n)]
        size = [0]*n
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            p, q = find(u), find(v)
            if p != q:
                if size[p] < size[q]:
                    p, q = q, p
                parent[q] = p
                size[p] += size[q]
        for u, v in edges:
            union(u, v)
        map(find, range(n))
        return len(set(parent))
    


"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
