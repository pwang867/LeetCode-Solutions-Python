"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

# method 2, combine node creation and relationship copy
# make sure that: 1. a node is only copied once, 2. a node's relationship is only processed once
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        d = {node: Node(node.val, [])}
        visited = set()  # visited means the nodes whose copies' neighbors has been copied
        stack = [node]
        while stack:
            p = stack.pop()
            if p in visited:
                continue
            visited.add(p)
            for nei in p.neighbors:
                if nei not in d:
                    d[nei] = Node(nei.val, [])
                d[p].neighbors.append(d[nei])
                stack.append(nei)
        
        return d[node]
    


# method 1: separate creating node and copying relation
class Solution1(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        d = {}
        stack = [node]
        while stack:
            p = stack.pop()
            if p in d:
                continue
            else:
                d[p] = Node(p.val, [])
            for nei in p.neighbors:
                stack.append(nei)
        
        stack = [node]
        visited = set()  # save nodes whose neighbor relationship has been cloned
        while stack:
            p = stack.pop()
            if p in visited:
                continue
            else:
                visited.add(p)
            for nei in p.neighbors:
                d[p].neighbors.append(d[nei])
                stack.append(nei)
        
        return d[node]

"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
"""
