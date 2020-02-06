# method 1, calculate the order in all four directions, 
# and then find the max
# time O(N^2), space O(N^2)
class Solution1(object):
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

    
# method 3, brute force, time O(N^3), space O(1), time limit exceeded
# for each point, calculate the order for all four directions
class Solution(object):
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
    
        
