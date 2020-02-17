# method 3, calculate the order in all four directions, 
# and then find the max
# time O(N^2), space O(N^2)
class Solution3(object):
    def orderOfLargestPlusSign(self, N, mines):
        mines = {tuple(mine) for mine in mines}
        order = [[float('inf')]*N for _ in range(N)]
        
        # left-arm order
        for i in range(N):
            cnt = 0
            for j in range(N):
                cnt = 0 if (i, j) in mines else cnt + 1
                order[i][j] = min(order[i][j], cnt)
        
        # right-arm order
        for i in range(N):
            cnt = 0
            for j in range(N-1, -1, -1):
                cnt = 0 if (i, j) in mines else cnt + 1
                order[i][j] = min(order[i][j], cnt)
        
        for j in range(N):
            cnt = 0
            for i in range(N):
                cnt = 0 if (i, j) in mines else cnt + 1
                order[i][j] = min(order[i][j], cnt)
        
        for j in range(N):
            cnt = 0
            for i in range(N-1, -1, -1):
                cnt = 0 if (i, j) in mines else cnt + 1
                order[i][j] = min(order[i][j], cnt)
                
        return max([max(row) for row in order])
    

# method 2, based on method 1, 
# but use a single traversal for horizontal and vertical
class Solution2(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mines = {tuple(mine) for mine in mines}
        order = [[float('inf')]*N for _ in range(N)]
        
        # Calculate horizontal order
        for i in range(N):
            start, end = -1, -1
            for j in range(N):
                if (i, j) not in mines:
                    end = j
                if (i, j) not in mines and (j==0 or (i,j-1) in mines):
                    start = j
                if (i, j) in mines:
                    order[i][j] = 0
                if ((i, j) in mines or j == N-1) and start != -1:
                    for k in range(start, end+1):
                        # min(k-start+1, end-k+1) is left-order and right-order
                        order[i][k] = min(order[i][k], min(k-start+1, end-k+1))
                    start, end = -1, -1
        
        # calculate vertical order
        for j in range(N):
            start, end = -1, -1
            for i in range(N):
                if (i, j) not in mines:
                    end = i
                if (i, j) not in mines and (i==0 or (i-1, j) in mines):
                    start = i
                if ((i, j) in mines or i == N-1) and start != -1:
                    for k in range(start, end+1):
                        order[k][j] = min(order[k][j], min(k-start+1, end-k+1))
                    start, end = -1, -1
        
        return max([max(row) for row in order])

    
# method 1, brute force, time O(N^3), space O(1), time limit exceeded
# for each point, calculate the order for all four directions
class Solution1(object):
    def orderOfLargestPlusSign(self, N, mines):
        max_order = 0
        mines = {tuple(mine) for mine in mines}
        
        for i in range(N):
            for j in range(N):
                if (i, j) not in mines:
                    cur_order = 1
                    while i - cur_order >= 0 and j - cur_order >= 0 \
                        and i + cur_order < N and j + cur_order < N \
                        and ((i, j-cur_order) not in mines) \
                        and ((i, j+cur_order) not in mines) \
                        and ((i-cur_order, j) not in mines) \
                        and ((i+cur_order, j) not in mines):
                        cur_order += 1
                    max_order = max(max_order, cur_order)
        return max_order
    
        

"""
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.
Note:

N will be an integer in the range [1, 500].
mines will have length at most 5000.
mines[i] will be length 2 and consist of integers in the range [0, N-1].
(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
"""
