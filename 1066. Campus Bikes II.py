# many of the states is method 1 are useless, because the number of "1" in states 
# should be equal to the number of workers, we can reduce time from O(M*N*2^M) to O(M*2^M)
# and reduce space complexity to O(2^M)
class Solution(object):
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
    
    
