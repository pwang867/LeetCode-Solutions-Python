# Dijkstra, time K*(V+E)*log(E), space O(n*K)
import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = {i: [] for i in range(n)}
        for flight in flights:
            u, v, price = flight
            graph[u].append([v, price])
        heap = [(0, src, K + 1)]            # input K doesn't include the src and dst
        costs = [[float('inf')] * (K + 2) for _ in range(n)]  # 2D cost matrix
        costs[src] = [0] * (K + 2)
        while heap:
            cost, node, k = heapq.heappop(heap)
            if dst == node:
                return cost
            for v, price in graph[node]:
                if k - 1 >= 0 and cost + price < costs[v][k - 1]:
                    costs[v][k - 1] = cost + price
                    heapq.heappush(heap, (cost + price, v, k - 1))
        return -1


"""
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
Accepted
"""
