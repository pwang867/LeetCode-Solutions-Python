from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = self.buildGraph(equations, values)
        return [self.dfs(query, graph) for query in queries]
    
    def buildGraph(self, equations, values):
        graph = defaultdict(list)
        for edge, value in zip(equations, values):
            u, v = edge
            graph[u].append((v, value))
            if value != 0:
                graph[v].append((u, 1/value))
        return graph
    
    def dfs(self, query, graph):
        start, end = query
        if start not in graph:
            return -1.0
        visited = set([start])
        stack = [(start, 1.0)]
        while stack:
            node, val = stack.pop()
            if node == end:
                return val
            for v, weight in graph[node]:
                if v in graph and v not in visited:
                    stack.append((v, val*weight))
                    visited.add(v)
        return -1



"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
