# due to symmetry, we will only allow the knight to move in the first quarant to greatly reduce time
# time complexity O(x*y)
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = abs(x), abs(y)   # use symmetry
        
        level = [(0,0)]
        depth = 0
        visited = {(0, 0)}
        while True:
            n = len(level)
            new_level = []
            for i, j in level:
                if i == x and j == y:
                    return depth
                for v in [(2, 1), (2, -1), (1, 2), (-1, 2), 
                          (-2, 1), (-2, -1), (1, -2), (-1, -2)]:
                    p, q = i + v[0], j + v[1]
                    if (p, q) not in visited and p >= 0 and q >= 0:
                        visited.add((p, q))
                        new_level.append((p, q))
            level = new_level
            depth += 1
            
