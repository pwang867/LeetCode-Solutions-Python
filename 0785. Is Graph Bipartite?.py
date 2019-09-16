# method 2: BFS, label the node with color
# time O(n), space O(n)
from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        if not graph:
            return True
        
        color = [0]*len(graph)
        for node in range(len(graph)):
            # use a for loop because the graph may have multiple components
            if color[node] == 0:
                # use BFS to assign color with node as the root
                color[node] = 1
                if not self.bfs(node, graph, color):
                    return False
        return True
    
    def bfs(self, root, graph, color):
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if color[v] == 0:
                    color[v] = -color[u]
                    queue.append(v)
                elif color[v] != -color[u]:
                    return False
        return True


# create two sets, initialize with graph[0]
# and then check if all the other edges can fit into those two sets
# time O(2**n), space O(n) 
class Solution1(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return True
        set1 = {0}
        set2 = set(graph[0])
        return self.helper(set1, set2, graph, 1)
        
    def helper(self, set1, set2, graph, i):
        if i == len(graph):
            return True
        part2 = [x for x in graph[i] if x > i]  # graph is undirected
        if not part2:
            return self.helper(set1, set2, graph, i+1)
        
        part1 = {i}
        part2 = set(part2)
        
        if not part1.intersection(set1) and not part2.intersection(set2):
            if self.helper(set1.union(part2), set2.union(part1), graph, i+1):
                return True
        if not part1.intersection(set2) and not part2.intersection(set1):
            if self.helper(set1.union(part1), set2.union(part2), graph, i+1):
                return True
        
        return False
    
