# BFS, O(m^2*n), m = len(routes), n = len(routes[0])


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        routes = map(set, routes)
        graph = self.build_graph(routes)
        queue = collections.deque([i for i, route in enumerate(routes) if S in route])
        visited = set(queue)
        depth = 1
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if T in routes[i]:
                    return depth
                for nei in graph[i]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            depth += 1
        return -1

    def build_graph(self, routes):
        graph = collections.defaultdict(list)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if routes[i] & routes[j]:  # can transit from bus i to bus j
                    graph[i].append(j)
                    graph[j].append(i)
        return graph


"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. 
For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the 
sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. 
Travelling by buses only, what is the least number of buses we must take to reach our destination? 
Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.

"""

