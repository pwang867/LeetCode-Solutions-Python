# method 3, Dijkstra's algorithm, time < O(2^M), spaceO(2^M)
# this problem is actually to find the minimum 
import heapq
class Solution(object):
    def assignBikes(self, workers, bikes):
        # heap saves (total_distance, index of worker to assign bike, available bikes)
        M, N = len(bikes), len(workers)
        heap = [(0, 0, tuple(range(M)))]  
        dists = [[self.dist(bike, worker) for bike in bikes] for worker in workers]
        visited = set()
        
        while heap:
            dist, i, state = heapq.heappop(heap)  
            # i is actually also the counts of "1" in state
            if state in visited:    # no duplicate states, so time O(2^M)
                # this means same (i, state) with smaller dist has been seen
                continue
            visited.add(state)
            if i == len(workers):
                return dist
            for k, j in enumerate(state):
                new_state = tuple(state[:k] + state[k+1:])
                heapq.heappush(heap, (dists[i][j]+dist, i+1, new_state))
    
    def dist(self, pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


# method 2, many of the states is method 1 are useless, because the number of "1" in states 
# should be equal to the number of workers, we can reduce time from O(M*N*2^M) to O(M*2^M)
# and reduce space complexity to O(2^M)
class Solution2(object):
    def assignBikes(self, workers, bikes):
        M, N = len(bikes), len(workers)
        pre = {}
        for j in range(M):  # assign bikes[j] to workers[0]
            pre[1<<j] = self.dist(bikes[j], workers[0])
            
        for i in range(1, N):
            worker = workers[i]
            cur = {}
            for state in pre:
                for j in range(M):
                    if state&(1<<j) == 0:
                        new_state = state^(1<<j)
                        cur[new_state] = min(cur.get(new_state, float('inf')), 
                                             pre[state]+self.dist(worker, bikes[j]))
            pre = cur
        
        return min(pre.values())
        
    
    def dist(self, pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


# method 1, dp
# dp[i][state] means the minimum distance to assign bikes[:i] to reach the state
# time O(N*M*2^M), space O(N*2^M)
class Solution1(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        N, M = len(workers), len(bikes)
        dp = [[float('inf')]*(1<<M) for _ in range(N+1)]  # padding for workers
        dp[0][0] = 0
        
        for i in range(1, N+1):
            for state in range(1, 1<<M):
                for k in range(M):
                    if state&(1<<k) == (1<<k):
                        # if the k-th bit in state is "1", 
                        # it means we assign bikes[k] to workers[i-1]
                        pre_state = state ^ (1<<k)
                        dp[i][state] = min(dp[i][state], 
                                dp[i-1][pre_state]+self.dist(bikes[k], workers[i-1]))
        
        return min(dp[-1])
    
    def dist(self, bike, worker):
        return abs(bike[0]-worker[0]) + abs(bike[1]-worker[1])
    
    