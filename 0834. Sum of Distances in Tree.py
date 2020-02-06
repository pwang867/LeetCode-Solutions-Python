# regard node 0 (chosen randomly) as the root of the whole tree
# traverse the tree like a directed tree even though it is undirected

# time/space O(N)

from collections import defaultdict
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = self.buildGraph(edges)
        self.counts = [0]*N      # self.counts[i] is the count of nodes in the subtree rooted at i
        self.dists = [0]*N       # self.dists[i] is the sum of distances for the subtree rooted at i
        self.countNodes(0, None, graph)   # find the counts for each subtree and find the dist for root 0
        self.calDists(0, None, graph)
        return self.dists
        
    def buildGraph(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)    # easy to forget
        return graph
    
    
    def countNodes(self, root, parent, graph):
        # postorder
        self.counts[root] = 1        # easy to miss
        for v in graph[root]:
            if v != parent:
                self.countNodes(v, root, graph)
                self.counts[root] += self.counts[v]
                self.dists[root] += self.dists[v] + self.counts[v]    # to get the total dist for root 0
    
    def calDists(self, root, parent, graph):
        # preorder
        if parent != None:
            self.dists[root] = self.dists[parent] + len(graph) - 2*self.counts[root]
        for v in graph[root]:
            if v != parent:
                self.calDists(v, root, graph)


"""
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
Note: 1 <= N <= 10000
"""
