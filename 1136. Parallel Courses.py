# topological sort with BFS
from collections import defaultdict, deque
class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        graph = self.buildGraph(relations)
        indegrees = self.computeIndegrees(graph, N)
        queue = deque([])
        for u in range(1, N+1):   # mistake: for u in range(N)
            if indegrees[u] == 0:
                queue.append(u)
        num_semesters = 0
        num_courses = 0
        while queue:
            num_semesters += 1
            for _ in range(len(queue)):
                u = queue.popleft()
                num_courses += 1
                for v in graph[u]:
                    indegrees[v] -= 1
                    if indegrees[v] == 0:
                        queue.append(v)
        if num_courses != N:
            return -1
        else:
            return num_semesters
        
    def buildGraph(self, relations):
        graph = defaultdict(list)
        for u, v in relations:
            graph[u].append(v)
        return graph
    
    def computeIndegrees(self, graph, N):
        indegrees = [0]*(N+1)   # mistake: indegrees = [0]*N
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1
        return indegrees
    

"""
There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.

 

Example 1:



Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
Example 2:



Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.
 

Note:

1 <= N <= 5000
1 <= relations.length <= 5000
relations[i][0] != relations[i][1]
There are no repeated relations in the input.
Accepted
"""
