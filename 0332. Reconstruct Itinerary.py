# time O(V+E)
# Eulerian graph: https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
# Hierholzer’s Algorithm for directed graph

from collections import defaultdict, deque
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # build map
        tickets.sort()
        targets = defaultdict(deque)
        for start, end in tickets:
            targets[start].append(end)
        # get route
        route = []
        self.travel(targets, route, "JFK")
        return route[::-1]   # due to backtracking
    
    def travel(self, targets, route, cur_stop):
        if cur_stop not in targets:
            route.append(cur_stop)
            return
        next_stops = targets[cur_stop]
        while next_stops:
            next_stop = next_stops.popleft()
            self.travel(targets, route, next_stop)
        route.append(cur_stop)


# StefanPochman's solutions: https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
def findItinerary(self, tickets):
    targets = defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack += targets[stack[-1]].pop(),
        route += stack.pop(),
    return route[::-1]



"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

