# time/space O(m*n)
# create all_pos in a sorted manner, so we don't need to sort all_pos again
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # all_pos will be already sorted, no need to sort again
        all_pos = [i for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]==1]  
        res = self.getDistance1D(all_pos)
        all_pos = [j for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j]==1]
        return res + self.getDistance1D(all_pos)
    
    def getDistance1D(self, nums):
        res = 0
        left, right = 0, len(nums)-1
        while left < right:
            res += nums[right] - nums[left]
            left += 1
            right -= 1
        return res



# time O(mn*log(mn)), space O(mn)
class Solution1(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        all_pos = [i for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]==1]
        all_pos.sort()
        res = self.getDistance1D(all_pos)
        all_pos = [j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]==1]
        all_pos.sort()
        return res + self.getDistance1D(all_pos)
    
    def getDistance1D(self, nums):
        res = 0
        left, right = 0, len(nums)-1
        while left < right:
            res += nums[right] - nums[left]
            left += 1
            right -= 1
        return res



"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.
"""

