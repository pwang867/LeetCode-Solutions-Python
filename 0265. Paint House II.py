class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # dynamic programming, paint the house one by one
        # change costs in place
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])
        if k == 1:
            if n == 1:
                return costs[0][0]
            else:
                return -1
        
        # initialization (index, value)
        # to make sure that the first row of costs is unchanged
        min1 = (0, 0)  
        min2 = (0, 0)
            
        for i in range(n):
            # update current row using previous rows' two smallest numbers
            # at the same time, generate two smallest minimum for next row
            new_min1 = (0, float("inf"))
            new_min2 = (0, float("inf"))
            for j in range(k):  # using only one iteration
                # print i, j, costs
                if j == min1[0]:
                    costs[i][j] += min2[1]
                else:
                    costs[i][j] += min1[1]
                
                temp = costs[i][j]
                if temp <= new_min1[1]:
                    new_min1, new_min2 = (j, temp), new_min1
                elif new_min1[1] < temp < new_min2[1]:
                    new_min2 = (j, temp)
            min1, min2 = new_min1, new_min2
        
        return min(costs[-1])


"""
Share
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
"""
