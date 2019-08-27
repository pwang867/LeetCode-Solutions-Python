# basic dp
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 2:
            return 0
        
        cost.append(0)  # the top of the floor means the floor len(cost)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        
        return cost[-1]
    
