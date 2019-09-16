# method 2: Dijkstra's Algorithm
# use a heap, for every step, 
# choose the shortest time path to travel
from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        earliest = [float('inf')]*(N+1)
        heap = [(0, K)]
        earlist[K] = 0
        earlist[0] = 0
        while heap:
            time, u = heapq.heappop(heap)
            for w, v in graph[u]:
                if time + w < earliest[v]:
                    earlist[v] = time + w
                    heapq.heappush((time+w, v))
        
        max_time = max(earlist)
        return max_time if max_time != float('inf') else -1



# method 1: use BFS to go through every path, 
# visit the nearest child first
# if the node has been visited at an earlier time, then terminate early
from collections import defaultdict, deque
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = self.buildGraph(times)
        visit_time = [float('inf')]*(N+1)  # earlist time to arrive at a node
        queue = deque([(K, 0)])  # (node, arrive_time_at_node)
        
        while queue:  # 
            u, time = queue.popleft()
            visit_time[u] = min(visit_time[u], time)
            if u not in graph:  # when no children
                continue
            else:
                for v, dist in graph[u]:
                    if time + dist < visit_time[v]:
                        queue.append((v, time + dist))
        
        max_time = -1
        for t in visit_time[1:]:
            if t == float('inf'):
                return -1
            else:
                max_time = max(max_time, t)
        
        return max_time
    
    def buildGraph(self, times):
        graph = defaultdict(list)
        
        for start, end, time in times:
            graph[start].append((end, time))
        
        return graph
    
        
