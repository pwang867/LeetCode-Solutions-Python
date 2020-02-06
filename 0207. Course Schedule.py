# method 2, Kahn's algorithm, BFS
# this is more commonly used
# time/space O(E+V)
from collections import defaultdict, deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        
        # build graph and compute indegrees
        graph = self.buildGraph(prerequisites)
        degrees = self.computeIndegrees(graph, numCourses)
        
        # initialize queue with nodes with indegrees of 0
        queue = deque()
        for u in range(numCourses):
            if degrees[u] == 0:
                queue.append(u)
        
        res = []   # save topologically sorted list of courses
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in graph[u]:  # u might not be in graph, but thanks to defaultdict
                degrees[v] -= 1
                if degrees[v] == 0:
                    queue.append(v)  # mistake: queue.append(u)
        return len(res) == numCourses
    
    def buildGraph(self, prerequisites):
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        return graph
    
    def computeIndegrees(self, graph, numCourses):
        degrees = [0]*numCourses   # nodes are from 0 to n-1, indegrees
        for u in graph:
            for v in graph[u]:
                degrees[v] += 1
        return degrees
    

# method 1, Using DFS. ref: https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
# main idea: if we meet a visiting node again, it means there is a circle
# time O(E+V), recursion depth O(depth), depth <= V
from collections import defaultdict
class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        NOTVISITED = 0
        VISITED = 1
        VISITING = -1
        # initiation
        mark = [NOTVISITED]*numCourses  # initiate marks
        graph = defaultdict(list)
        for i, j in prerequisites:
            graph[i].append(j)  # directed graph, no graph[j].append(i)
        
        # DFS method
        def visit(u):
            # return True is there is no circle, else return False
            if mark[u] == VISITING:
                return False
            if mark[u] == VISITED:
                return True
            mark[u] = VISITING
            for v in graph[u]:
                if not visit(v):
                    return False
            mark[u] = VISITED  # vertex will be marked permanantly if it has no child any more
            return True
        
        for u in range(numCourses):
            if mark[u] == NOTVISITED:
                if not visit(u):  # if there is circle
                    return False
        return True


"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
