# union find
# two requirement to be a tree: 1. no loop, 2. only a single component


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        self.parent = {i:i for i in range(n)}
        self.size   = {i:0 for i in range(n)}
        cnt = 0
        for u, v in edges:
            parentu = self.find(u)
            parentv = self.find(v)
            if parentu == parentv:    # no loop
                return False    
            if self.size[parentu] <= self.size[parentv]:  # union the two nodes
                self.parent[parentu] = parentv
            else:
                self.parent[parentv] = parentu
            cnt += 1
        return cnt == n-1    # only one component
    
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    


"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to check whether these edges 
make up a valid tree.

Example 1:
 
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""
