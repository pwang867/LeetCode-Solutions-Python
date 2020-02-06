# BFS with memorization of states
# time/space O(2^n)

from collections import deque
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        if not graph:
            return 0
        n = len(graph)
        queue = deque([(1<<i, i) for i in range(n)])
        visited = set()  # visited state
        depth = 0
        while deque:
            for _ in range(len(queue)):
                path, cur = queue.popleft()
                if path == (1<<n) - 1:
                    return depth
                for nei in graph[cur]:
                    node = (path|(1<<nei), nei)
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)
            depth += 1
        return -1
    

"""
An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
 

Note:

1 <= graph.length <= 12
0 <= graph[i].length < graph.length
"""
