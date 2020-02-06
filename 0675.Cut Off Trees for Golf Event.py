class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest or not forest[0]:
            return 0
        m, n = len(forest), len(forest[0])
        
        # get all trees and sort trees by height
        trees = [(0,0,-1)]  # to make (0, 0) always as a start point
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 0:
                    trees.append((i, j, forest[i][j]))
        trees = sorted(trees, key=lambda x: x[-1])
        
        # cut trees
        cnt = 0
        for i in range(len(trees)-1):
            start = trees[i]
            end = trees[i+1]
            visited = [[False for j in range(n)] for i in range(m)]
            visited[start[0]][start[1]] = True
            steps = self.bfs(forest, visited, start[:2], end[:2])
            if steps == -1:
                return -1
            cnt += steps
        
        return cnt
    
    def bfs(self, forest, visited, start, end):
        # level order traversal
        # find number of moves needed to move from start to end
        if end == start:
            return 0
        
        stack = [start]
        level = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while stack:
            level += 1
            new_stack = []
            for i, j in stack:
                for d in dirs:
                    p, q = i + d[0], j + d[1]
                    if (p, q) == end:
                        return level
                    if p >= 0 and p < len(forest) and q >= 0 \
                    and q < len(forest[0]) and not visited[p][q] and \
                    forest[p][q] > 0:
                        visited[p][q] = True
                        new_stack.append((p, q))
            stack = new_stack
        
        return -1
        
        
        
        
        
        
